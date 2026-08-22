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

<!-- worklog:policy:start -->
## WikiTicket SDD (worklog)

This plugin tracks implementation with [WikiTicket SDD](https://github.com/SpillwaveSolutions/wiki_ticket_sdd).

- Install the `worklog` plugin from `SpillwaveSolutions/wiki_ticket_sdd` (Claude Code, Grok Build, Codex, Cursor).
- Config lives in `.work/config.yml`. Event log is `.work/todo.jsonl`.
- Every plan MUST end by running `worklog plan-capture`.
- Work discovered mid-flight: `worklog add --unplanned --discovered-during <item>` BEFORE doing the work.
- Never hand-edit `.work/*.jsonl` (use `worklog`) or `docs/roadmap.md` (generated).
- After changing work items, run `worklog roadmap-render` and commit the log and roadmap together.
- CLI: `worklog` on PATH, or `python3 <wiki_ticket_sdd>/bin/worklog`.
<!-- worklog:policy:end -->

