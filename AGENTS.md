# AGENTS.md — claude-code-ager

Multi-host translator. Author graphs with `okf-agent-graph`.

## Hosts

- Agent Plugins 1.0: root `plugin.json` + `skills/`
- Claude Code: `.claude-plugin/`
- Grok Build: Claude layout + `.grok-plugin/`
- Codex: `.codex-plugin/`
- Cursor: `hosts/cursor/SKILL.md` — see `docs/CURSOR.md`

## Commands

- `/ager-to-claude-code` · `$ager-to-claude-code`
- Deterministic: `python3 scripts/emit.py --bundle <AGER> --out <OUT>`

Never claim the emitted plugin is production-ready without tests.
