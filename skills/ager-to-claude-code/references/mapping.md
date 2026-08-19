# Claude Code mapping

Emitted `plugin.json` name is the AGER graph id. Version starts at `0.1.0`.

- Orchestrator → `agents/<id>.md`
- Worker → skill only unless long-lived specialist
- Judge / Synthesizer → skills invoked by the orchestrator
- LoopPolicy check order: goal → deadline → price → max_turns → no_progress
- Claude Code does not meter USD; `ager-run` instructs the lead to stop and report
- Do not invent MCP servers. Use the host web tool for `web_search`
- ScratchPad keys only — no full transcripts
