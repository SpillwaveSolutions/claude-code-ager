---
name: cursor-claude-code-ager
description: Bind a Cursor agent (including Grok Bot cloud sessions) to the AGER translator. Cursor loads Agent Plugins 1.0 (plugin.json + skills/).
---

# Cursor / claude-code-ager

Follow `docs/CURSOR.md`.

1. Identity: `cursor/claude-code-ager`
2. Cursor reads root `plugin.json` + `skills/`. No Cursor-only fork.
3. Compile with `python3 scripts/emit.py --bundle <AGER> --out <OUT>`.
4. Never document a private remote.
