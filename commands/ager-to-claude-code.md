---
name: ager-to-claude-code
description: Compile an AGER AgentGraph into a Claude Code plugin.
---

Follow the **ager-to-claude-code** skill completely.

1. Load `${CLAUDE_PLUGIN_ROOT}/skills/ager-to-claude-code/SKILL.md`.
2. Confirm `okf-agent-graph` / `ager-validate` when available.
3. Run `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/emit.py --bundle <AGER> --out <OUT>`.
4. Report created paths. Do not freehand the plugin tree.
