# Claude Code mapping

## Plugin identity

Emitted `plugin.json` name is the AGER graph id (`parallel-research` → `parallel-research`).
Version starts at `0.1.0`. `ager_version` is copied from the bundle.

## Agents

- Orchestrator → `agents/<id>.md` with `isolation: worktree` when `ephemeral` workers exist.
- Worker → skill only unless the graph marks it as a long-lived specialist.
- Judge / Synthesizer → skills invoked by the orchestrator skill, not as parallel user-facing agents.

## LoopPolicy → ager-run

Check order (normative AGER): goal → deadline → price → max_turns → no_progress.

Claude Code cannot natively enforce USD budgets. The emitted `ager-run` skill
instructs the lead to **stop and report** when a control would fire.

## Tools

Each AGER Tool becomes a section in the worker skill:

- input schema (JSON Schema)
- cost
- ToolRules as "block if …" bullets

Do not invent MCP servers. If the AGER tool is `web_search`, tell the host to
use its existing web tool.

## ScratchPad

List keys become explicit write targets:

- `orchestrator_plans` append
- `worker_outputs` append
- `judgments` append
- `final_report` set

Write Markdown files under `runs/<ulid>/scratchpad/` in the emitted project, or
append to the host's artifact store if one exists. Do not dump full transcripts.
