# AGENTS.md — claude-code-ager

A **translator**. It does not author AGER graphs (`okf-agent-graph`).
It compiles a validated AGER bundle into a Claude Code plugin.

- `/ager-to-claude-code`
- `python3 scripts/emit.py --bundle path/to/ager --out ./generated/claude-code`

Never claim the emitted plugin is production-ready without tests.
