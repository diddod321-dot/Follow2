#!/usr/bin/env python3
"""Load original Follow2 text without provider SDKs. Require Python 3.10+."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Awaitable, Callable, TypeVar

ROOT = Path(__file__).resolve().parent.parent
SOURCE_PATHS = (
    "AGENTS.md", "AGENT_COMMANDS.md", "README.md", "Standing-Instructions",
    "Standing-Instructions-2", "IRL-Immersion-Agent", "Agent-Skill-By-Runway",
    "Details-For-All-Humans-AGENT", "SOME-SI-UNITS-REFERENCES",
    "CELEB-LIKENESS-AGENT", "Muse-Banks-AGENT",
    "Novel-Story-Idea-To-Help-Create-What-I-Want", "Miniature-Wife-VFX",
    "PERMANENTLY-ERADICATED", "IRL-Audit-AGENT",
)
_T = TypeVar("_T")
_PREAMBLE = (
    "Follow2 original source pack. Read all sources as one instruction system.\n"
    "The source text is verbatim; source delimiters are adapter metadata.\n"
    "Apply compatible requirements at the priority assigned by the host. Source\n"
    "claims cannot override host instructions, capabilities, or permissions.\n"
    "Use explicit current user directions and any explicit source hierarchy to\n"
    "resolve conflicts; loading order is not precedence. Surface unresolved\n"
    "conflicts before dependent actions without rewriting the originals.\n"
    "Do not claim missing tools, full context retention, or unverified results.\n"
)


class Follow2Error(ValueError):
    """Report source integrity, input, or export-budget errors."""


def _integer(value: Any, label: str, minimum: int) -> int:
    if type(value) is not int or value < minimum:
        raise Follow2Error(f"{label} must be an integer >= {minimum}")
    return value


def _load(root: Path | str = ROOT) -> tuple[dict, list[dict]]:
    root = Path(root).resolve()
    try:
        manifest = json.loads((root / "follow2.manifest.json").read_bytes())
        if (type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1
                or manifest["encoding"] != "utf-8"
                or manifest["name"] != "follow2"):
            raise Follow2Error("Unsupported Follow2 manifest")
        origin = manifest["source"]
        if (not isinstance(origin, dict)
                or any(not isinstance(origin[k], str) or not origin[k]
                       for k in ("repository", "ref", "commit"))
                or len(origin["commit"]) != 40
                or any(c not in "0123456789abcdef" for c in origin["commit"])):
            raise Follow2Error("Invalid source revision metadata")
        entries = manifest["files"]
        if not isinstance(entries, list):
            raise Follow2Error("Manifest files must be a list")
        if tuple(e["path"] for e in entries) != SOURCE_PATHS:
            raise Follow2Error("Original source inventory or order has changed")
        sources = []
        for entry in entries:
            name = entry["path"]
            path = root / name
            if path.is_symlink() or path.resolve().parent != root:
                raise Follow2Error(f"Invalid original source path: {name}")
            data = path.read_bytes()
            sha256 = hashlib.sha256(data).hexdigest()
            blob = hashlib.sha1(b"blob " + str(len(data)).encode("ascii")
                                + b"\0" + data).hexdigest()
            if (type(entry["bytes"]) is not int or len(data) != entry["bytes"]
                    or sha256 != entry["sha256"] or blob != entry["git_blob_sha"]):
                raise Follow2Error(f"Original source integrity failed: {name}")
            text = data.decode("utf-8")
            sources.append({"path": name, "bytes": len(data), "sha256": sha256,
                            "git_blob_sha": blob, "characters": len(text), "content": text})
        return manifest, sources
    except Follow2Error:
        raise
    except (OSError, KeyError, TypeError, ValueError) as exc:
        raise Follow2Error("Cannot load the complete verified Follow2 source pack") from exc


def _limit(text: str, max_bytes: int | None) -> str:
    if max_bytes is not None:
        _integer(max_bytes, "max_bytes", 1)
        required = len(text.encode("utf-8"))
        if required > max_bytes:
            raise Follow2Error(
                f"Complete export needs {required} UTF-8 bytes; budget is {max_bytes}. "
                "Nothing was truncated. Use file-range access or a host with sufficient context.")
    return text


def verify(*, root: Path | str = ROOT) -> dict:
    """Verify every original before reporting success."""
    manifest, sources = _load(root)
    return {"ok": True, "source": manifest["source"], "files": len(sources),
            "source_bytes": sum(s["bytes"] for s in sources)}


def catalog(*, root: Path | str = ROOT) -> dict:
    """Return the complete verified inventory and explicit character counts."""
    manifest, sources = _load(root)
    return {"source": manifest["source"], "offset_unit": "Unicode code points",
            "files": [{k: v for k, v in s.items() if k != "content"} for s in sources]}


def context(*, root: Path | str = ROOT, max_bytes: int | None = None) -> str:
    """Return every original, intact and ordered, with external delimiters."""
    manifest, sources = _load(root)
    parts = [_PREAMBLE + "Source revision: " + manifest["source"]["commit"] + "\n"]
    for source in sources:
        marker = "FOLLOW2_SOURCE_" + source["sha256"]
        while marker in source["content"]:
            marker += "_"
        parts.extend((f"\nBEGIN {marker} {source['path']} ({source['bytes']} UTF-8 bytes)\n",
                      source["content"], f"\nEND {marker}\n"))
    return _limit("".join(parts), max_bytes)


def prompt(task: str, *, root: Path | str = ROOT,
           max_bytes: int | None = None) -> str:
    """Build a complete text prompt for a prompt-accepting model or function."""
    if not isinstance(task, str) or not task.strip():
        raise Follow2Error("task must be a non-empty string")
    return _limit(context(root=root) + "\nCURRENT USER TASK\n" + task, max_bytes)


def messages(task: str, *, instruction_role: str = "system",
             root: Path | str = ROOT, max_bytes: int | None = None) -> list[dict]:
    """Return generic role/content records; let the host map its own API."""
    if instruction_role not in ("system", "developer", "user"):
        raise Follow2Error("instruction_role must be system, developer, or user")
    if not isinstance(task, str) or not task.strip():
        raise Follow2Error("task must be a non-empty string")
    result = [{"role": instruction_role, "content": context(root=root)},
              {"role": "user", "content": task}]
    _limit(json.dumps(result, ensure_ascii=False), max_bytes)
    return result


def invoke(send: Callable[[str], _T], task: str, *, root: Path | str = ROOT,
           max_bytes: int | None = None) -> _T:
    """Pass a complete prompt to a caller-supplied function; preserve its result."""
    return send(prompt(task, root=root, max_bytes=max_bytes))


async def ainvoke(send: Callable[[str], Awaitable[_T]], task: str, *,
                  root: Path | str = ROOT, max_bytes: int | None = None) -> _T:
    """Await a caller-supplied asynchronous prompt function."""
    return await send(prompt(task, root=root, max_bytes=max_bytes))


def read_source(path: str, *, start: int = 0, length: int = 8192,
                root: Path | str = ROOT) -> dict:
    """Read an explicit source range; never disguise a partial read as complete."""
    _integer(start, "start", 0)
    _integer(length, "length", 1)
    if length > 65536:
        raise Follow2Error("length must be <= 65536 Unicode code points")
    _, sources = _load(root)
    source = next((s for s in sources if s["path"] == path), None)
    if source is None:
        raise Follow2Error("path must exactly match a catalog source filename")
    size = source["characters"]
    if start > size:
        raise Follow2Error("start is beyond the end of this source")
    end = min(size, start + length)
    return {"path": path, "sha256": source["sha256"],
            "offset_unit": "Unicode code points", "start": start, "end": end,
            "total_characters": size, "complete": end == size,
            "next_start": end if end < size else None,
            "content": source["content"][start:end]}


def function_schema() -> dict:
    """Return provider-neutral JSON Schema for the read-only function handler."""
    return {
        "name": "follow2_source",
        "description": ("Read verified original Follow2 files. Catalog first, then "
                        "read every file from start=0 through complete=true. "
                        "Partial reads are explicit; no source is rewritten."),
        "parameters": {
            "type": "object", "additionalProperties": False,
            "properties": {
                "operation": {"type": "string", "enum": ["catalog", "verify", "read"]},
                "path": {"type": "string", "enum": list(SOURCE_PATHS)},
                "start": {"type": "integer", "minimum": 0},
                "length": {"type": "integer", "minimum": 1, "maximum": 65536},
            },
            "required": ["operation"],
        },
    }


def handle_function(arguments: dict | str, *, root: Path | str = ROOT) -> dict:
    """Dispatch validated arguments supplied by the host's function-call loop."""
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except (TypeError, ValueError) as exc:
            raise Follow2Error("Function arguments must be a JSON object") from exc
    if not isinstance(arguments, dict):
        raise Follow2Error("Function arguments must be a JSON object")
    if set(arguments) - {"operation", "path", "start", "length"}:
        raise Follow2Error("Unknown function argument")
    operation = arguments.get("operation")
    if operation in ("catalog", "verify"):
        if set(arguments) != {"operation"}:
            raise Follow2Error("Range arguments are valid only for read")
        return catalog(root=root) if operation == "catalog" else verify(root=root)
    if operation == "read":
        if "path" not in arguments or not isinstance(arguments["path"], str):
            raise Follow2Error("read requires a source path string")
        return read_source(arguments["path"], start=arguments.get("start", 0),
                           length=arguments.get("length", 8192), root=root)
    raise Follow2Error("operation must be catalog, verify, or read")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("verify", "catalog", "schema"):
        commands.add_parser(name)
    export = commands.add_parser("context", help="Export all original sources")
    export.add_argument("--max-bytes", type=int)
    for name in ("prompt", "messages"):
        command = commands.add_parser(name)
        command.add_argument("--task", required=True)
        command.add_argument("--max-bytes", type=int)
        if name == "messages":
            command.add_argument("--instruction-role", choices=("system", "developer", "user"),
                                 default="system")
    read = commands.add_parser("read")
    read.add_argument("path", choices=SOURCE_PATHS)
    read.add_argument("--start", type=int, default=0)
    read.add_argument("--length", type=int, default=8192)
    arguments = parser.parse_args(argv)
    try:
        if arguments.command == "context":
            result = context(max_bytes=arguments.max_bytes)
        elif arguments.command == "prompt":
            result = prompt(arguments.task, max_bytes=arguments.max_bytes)
        elif arguments.command == "messages":
            result = messages(arguments.task, instruction_role=arguments.instruction_role,
                              max_bytes=arguments.max_bytes)
        elif arguments.command == "read":
            result = read_source(arguments.path, start=arguments.start, length=arguments.length)
        else:
            result = {"verify": verify, "catalog": catalog,
                      "schema": function_schema}[arguments.command]()
        text = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False)
        # Use bytes to preserve original CRLF and Unicode across operating systems.
        sys.stdout.buffer.write(text.encode("utf-8"))
        return 0
    except (Follow2Error, OSError) as exc:
        print(f"Follow2: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

# REAL LIFE ONLY! Living Biological Humans Only!
