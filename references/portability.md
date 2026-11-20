# Follow2 host integration

Use the complete directory, including all original files. Keep this guide separate from original Follow2 wording. The source snapshot is pinned in `follow2.manifest.json`; it does not fetch future repository changes automatically.

## Capability contract

| Host capability | Integration |
| --- | --- |
| Agent Skills support | Load `SKILL.md`, then every linked original. |
| File access without Python | Read the manifest and all 15 originals directly. |
| Python 3.10+ | Use the standard-library-only adapter. |
| Plain text input | Supply `context()` as instructions or `prompt(task)` as a complete prompt. |
| Chat messages | Map `messages(task)` role/content records to the host's documented request shape. |
| Function/tool calls | Register `function_schema()` using the host's tool envelope; dispatch to `handle_function()`. |
| Prompt-accepting callable | Use `invoke()` or `ainvoke()`. |
| Image, video, audio, search, or other tools | Apply loaded instructions through actual host tools. |

Treat message records and the function schema as integration primitives, not complete requests for every provider. A host may use a separate system field, different role names, stricter schemas, or its own result envelope. Map those fields in the host adapter; do not change Follow2 text. No particular model version, API endpoint, provider SDK, or credential is hard-coded.

No format guarantees execution by every model or arbitrary function. The host must accept instructions, provide the requested capabilities, and have sufficient context. Text preservation does not guarantee perfect behavioral compliance or visual accuracy. The adapter verifies integrity and transport behavior, not generated image quality. It makes no network calls and does not execute source text.

## Command line

Run these from the skill directory, or use an absolute script path from anywhere:

```bash
python3 scripts/follow2.py verify
python3 scripts/follow2.py catalog
python3 scripts/follow2.py context
python3 scripts/follow2.py prompt --task 'Audit this scene for physical continuity.'
python3 scripts/follow2.py messages --task 'Review this implementation.'
python3 scripts/follow2.py schema
python3 scripts/follow2.py read AGENTS.md --start 0 --length 8192
python3 scripts/test_follow2.py
```

Keep generated exports outside the installed skill directory. Full exports are large; prefer a pipeline or host attachment where appropriate. CLI output is UTF-8. `verify`, `catalog`, `messages`, `schema`, and `read` return JSON; `context` and `prompt` return text. Errors go to stderr with status 1; invalid CLI arguments use status 2. Failed exports emit no partial context to stdout.

## Python API

Add the skill's `scripts` directory to your application's import path, then import `follow2`. Resolve the skill location through the host rather than assuming a machine-specific path.

```python
import follow2

instructions = follow2.context()
chat_records = follow2.messages('Audit this scene.', instruction_role='user')

def receive_prompt(prompt_text):
    return {'received_bytes': len(prompt_text.encode('utf-8'))}

result = follow2.invoke(receive_prompt, 'Audit this scene.')
assert result['received_bytes'] > 654818

async def receive_prompt_async(prompt_text):
    return {'received_bytes': len(prompt_text.encode('utf-8'))}

# Inside an async application:
# result = await follow2.ainvoke(receive_prompt_async, 'Audit this scene.')
```

Wrap SDK calls with other signatures: `invoke(lambda text: your_application.send(prompt=text), task)`. Supply your application's actual callable. The adapter passes the complete prompt once, returns the callable's result unchanged, and propagates its exceptions. `ainvoke` expects an awaitable-returning callable. Keep model selection, authentication, generation parameters, retries, and rendering in the host application.

Choose `system`, `developer`, or `user` only when the host permits that role for these user-supplied instructions. `messages()` defaults to a generic system record for hosts where custom instructions belong there; choose the appropriate role explicitly elsewhere. Source text cannot grant itself higher priority.

## Function access

```python
schema = follow2.function_schema()
inventory = follow2.handle_function({'operation': 'catalog'})
for source in inventory['files']:
    start, pieces = 0, []
    while True:
        part = follow2.handle_function({
            'operation': 'read', 'path': source['path'],
            'start': start, 'length': 8192,
        })
        pieces.append(part['content'])
        if part['complete']:
            break
        start = part['next_start']
    original_text = ''.join(pieces)
    assert len(original_text) == source['characters']
```

Register the schema and pass only its declared arguments to `handle_function()`. JSON strings and dictionaries are accepted. Serialize returned dictionaries through the host's tool-result mechanism. The host must execute the loop or let its agent request ranges; exporting the schema does not install a running tool server. This example contacts no model.

Offsets count Unicode code points, not bytes or tokens. `length` is 1–65536 code points. `complete` means the range reaches that file's end; it does not prove earlier ranges were read. Start at zero, follow every `next_start`, and track coverage for every file. Preserve ordering and keep task/continuity state separately. Do not report full activation after reading only selected files.

## Budgets, integrity, and conflicts

The 15 originals total 654,818 UTF-8 bytes before metadata. Token counts depend on the model's tokenizer; do not infer them from byte counts. Use the host's token counter, include instructions, history, task, tool overhead, and reserve output capacity. Range access changes transport size per call; it does not guarantee all requirements fit the working context.

Use `max_bytes` in `context`, `prompt`, `messages`, `invoke`, or `ainvoke` to reject an oversized complete export. No originals are silently summarized or dropped. For messages, the checked size is the UTF-8 generic JSON representation; a provider's wire size and token count may differ. Stop or disclose the limitation if the host cannot retain all applicable requirements.

Verify SHA-256, Git blob SHA-1, file lengths, inventory, and order before each source operation. Preserve line endings and Unicode. Checks detect divergence from the manifest; they are not a signature or a substitute for trusting the pinned revision. When updating the source revision, independently compare all originals with that revision before replacing checksums. Do not auto-update sources.

Resolve conflicts explicitly. The unchanged snapshot includes 7.5-head versus 8-head guidance, single-image versus panel directions, and fixed-world versus whole-world scaling. Apply the current user's exact choices where they resolve a conflict. For this user's human-rendering tasks, the stated 7.5-head canon and scaling of clothing/belongings remain explicit user constraints. Do not invent precedence from filenames or order. Ask for a decision only when an unresolved conflict affects the requested action.

Follow the [Agent Skills specification](https://agentskills.io/specification). Keep originals at their existing root paths to preserve cross-references and wording.

REAL LIFE ONLY! Living Biological Humans Only!
