#!/usr/bin/env python3
"""Exercise the real Follow2 bundle, exports, callables, and integrity failures."""

import asyncio
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import follow2


class Follow2Tests(unittest.TestCase):
    def test_all_originals_match_pinned_blobs(self):
        result = follow2.verify()
        self.assertTrue(result['ok'])
        self.assertEqual(result['files'], 15)
        self.assertEqual(result['source_bytes'], 654818)
        self.assertEqual(result['source']['commit'],
                         'afa62719754bd32a4e3e0673ce173ccf45b410f0')

    def test_complete_export_preserves_every_original_byte(self):
        export = follow2.context().encode('utf-8')
        cursor = 0
        for name in follow2.SOURCE_PATHS:
            original = (follow2.ROOT / name).read_bytes()
            position = export.find(original, cursor)
            self.assertGreaterEqual(position, cursor, name)
            cursor = position + len(original)

    def test_ranges_reconstruct_all_files_and_unicode(self):
        for source in follow2.catalog()['files']:
            pieces, start = [], 0
            while True:
                part = follow2.handle_function(json.dumps({
                    'operation': 'read', 'path': source['path'],
                    'start': start, 'length': 4093,
                }))
                self.assertEqual(part['start'], start)
                pieces.append(part['content'])
                if part['complete']:
                    self.assertIsNone(part['next_start'])
                    break
                self.assertGreater(part['next_start'], start)
                start = part['next_start']
            data = ''.join(pieces).encode('utf-8')
            self.assertEqual(data, (follow2.ROOT / source['path']).read_bytes())
            self.assertEqual(hashlib.sha256(data).hexdigest(), source['sha256'])

    def test_range_end_and_invalid_offsets(self):
        item = follow2.catalog()['files'][0]
        end = follow2.read_source(item['path'], start=item['characters'])
        self.assertEqual(end['content'], '')
        self.assertTrue(end['complete'])
        for options in ({'start': -1}, {'start': True}, {'start': 1.5},
                        {'start': item['characters'] + 1}, {'length': 0},
                        {'length': 65537}, {'length': False}):
            with self.subTest(options=options), self.assertRaises(follow2.Follow2Error):
                follow2.read_source(item['path'], **options)

    def test_function_rejects_unexpected_or_invalid_arguments(self):
        for arguments in (None, [], '[]', '{', {}, {'operation': 'run'},
                          {'operation': 'read'}, {'operation': 'read', 'path': '../AGENTS.md'},
                          {'operation': 'read', 'path': '/etc/passwd'},
                          {'operation': 'read', 'path': False},
                          {'operation': 'verify', 'start': 0},
                          {'operation': 'catalog', 'root': '/tmp'}):
            with self.subTest(arguments=arguments), self.assertRaises(follow2.Follow2Error):
                follow2.handle_function(arguments)
        self.assertEqual(len(follow2.handle_function({'operation': 'catalog'})['files']), 15)
        self.assertTrue(follow2.handle_function({'operation': 'verify'})['ok'])

    def test_budget_boundary_and_no_callable_invocation_on_failure(self):
        text = follow2.context()
        size = len(text.encode('utf-8'))
        self.assertEqual(follow2.context(max_bytes=size), text)
        for limit in (size - 1, 0, -1, True, '100'):
            with self.subTest(limit=limit), self.assertRaises(follow2.Follow2Error):
                follow2.context(max_bytes=limit)
        called = []
        with self.assertRaises(follow2.Follow2Error):
            follow2.invoke(lambda text: called.append(text), 'task', max_bytes=10)
        self.assertEqual(called, [])

    def test_message_roles_and_serialized_budget(self):
        for role in ('system', 'developer', 'user'):
            records = follow2.messages('Task with Unicode: café µm.', instruction_role=role)
            self.assertEqual([r['role'] for r in records], [role, 'user'])
            self.assertEqual(records[0]['content'], follow2.context())
            size = len(json.dumps(records, ensure_ascii=False).encode('utf-8'))
            self.assertEqual(follow2.messages(records[1]['content'], instruction_role=role,
                                             max_bytes=size), records)
            with self.assertRaises(follow2.Follow2Error):
                follow2.messages(records[1]['content'], instruction_role=role, max_bytes=size-1)
        with self.assertRaises(follow2.Follow2Error):
            follow2.messages('Task', instruction_role='assistant')

    def test_sync_and_async_preserve_result_and_exceptions(self):
        output = object()
        seen = []
        def send(text):
            seen.append(text)
            return output
        self.assertIs(follow2.invoke(send, 'Current task'), output)
        self.assertEqual(seen, [follow2.prompt('Current task')])
        async def async_send(text):
            return send(text)
        self.assertIs(asyncio.run(follow2.ainvoke(async_send, 'Async task')), output)
        self.assertEqual(seen[-1], follow2.prompt('Async task'))
        def fail(text):
            raise RuntimeError('host failure')
        with self.assertRaisesRegex(RuntimeError, 'host failure'):
            follow2.invoke(fail, 'Task')

    def test_invalid_tasks(self):
        for value in ('', '  ', None, 17):
            for builder in (follow2.prompt, follow2.messages):
                with self.subTest(value=value, builder=builder), self.assertRaises(follow2.Follow2Error):
                    builder(value)

    def test_cli_from_an_unrelated_directory_and_failed_export_is_empty(self):
        script = str(follow2.ROOT / 'scripts/follow2.py')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONIOENCODING='utf-8')
        with tempfile.TemporaryDirectory() as cwd:
            def run(*args):
                return subprocess.run([sys.executable, script, *args], cwd=cwd, env=env,
                                      capture_output=True, check=False)
            checked = run('verify')
            self.assertEqual(checked.returncode, 0, checked.stderr)
            self.assertTrue(json.loads(checked.stdout)['ok'])
            failed = run('context', '--max-bytes', '10')
            self.assertEqual(failed.returncode, 1)
            self.assertEqual(failed.stdout, b'')
            self.assertIn(b'Nothing was truncated', failed.stderr)
            exported = run('context')
            self.assertEqual(exported.returncode, 0, exported.stderr)
            self.assertEqual(exported.stdout, follow2.context().encode('utf-8'))
            self.assertEqual(run('messages', '--task', 'task').returncode, 0)
            self.assertEqual(run('prompt', '--task', 'task').stdout,
                             follow2.prompt('task').encode('utf-8'))
            schema = json.loads(run('schema').stdout)
            self.assertEqual(schema['name'], 'follow2_source')
            self.assertEqual(len(json.loads(run('catalog').stdout)['files']), 15)
            first = json.loads(run('read', 'AGENTS.md', '--length', '5').stdout)
            self.assertEqual(first['content'], '# Fol')

    def test_integrity_failures_and_manifest_inventory(self):
        # These fixtures contain sources only, not an initialized installable skill.
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for name in (*follow2.SOURCE_PATHS, 'follow2.manifest.json'):
                shutil.copyfile(follow2.ROOT / name, root / name)
            original = (root / 'AGENTS.md').read_bytes()
            (root / 'AGENTS.md').write_bytes(original + b' ')
            with self.assertRaisesRegex(follow2.Follow2Error, 'integrity failed'):
                follow2.verify(root=root)
            (root / 'AGENTS.md').write_bytes(original)
            raw = (root / 'follow2.manifest.json').read_bytes()
            for mutation in ('remove', 'reorder', 'metadata', 'schema'):
                manifest = json.loads(raw)
                if mutation == 'remove':
                    manifest['files'].pop()
                elif mutation == 'reorder':
                    manifest['files'].reverse()
                elif mutation == 'metadata':
                    manifest['source'].pop('commit')
                else:
                    manifest['schema_version'] = True
                (root / 'follow2.manifest.json').write_text(json.dumps(manifest), encoding='utf-8')
                with self.subTest(mutation=mutation), self.assertRaises(follow2.Follow2Error):
                    follow2.verify(root=root)
            (root / 'follow2.manifest.json').write_bytes(raw)
            (root / 'AGENTS.md').unlink()
            with self.assertRaises(follow2.Follow2Error):
                follow2.verify(root=root)
            try:
                (root / 'AGENTS.md').symlink_to(follow2.ROOT / 'AGENTS.md')
            except OSError:
                if os.name == 'nt':
                    self.skipTest('Symlink creation needs Windows developer mode or privileges')
                raise
            with self.assertRaisesRegex(follow2.Follow2Error, 'Invalid original source path'):
                follow2.verify(root=root)


if __name__ == '__main__':
    unittest.main(verbosity=2)

# REAL LIFE ONLY! Living Biological Humans Only!
