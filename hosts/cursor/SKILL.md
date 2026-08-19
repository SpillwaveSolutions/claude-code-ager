---
name: cursor-claude-code-ager
description: Bind a Cursor agent to claude-code-ager. Compile AGER graphs. Do not author graphs.
---

# Cursor / claude-code-ager

Follow `docs/CURSOR.md` and `docs/HOSTS.md`.

1. Identity: `cursor/claude-code-ager`.
2. Local Cursor may `/plugin install claude-code-ager`.
3. Compile with `python3 scripts/emit.py --bundle <AGER> --out <OUT>`.
4. Never invent agents. Never write a new AGER graph (that is `okf-agent-graph`).
