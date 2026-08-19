---
name: ager-to-claude-code
description: Translate a validated AGER/OKF AgentGraph into a Claude Code plugin (skills, agents, commands, hooks). Use when the user wants to compile an AGER graph for Claude Code.
---

# AGER → Claude Code

This plugin **compiles**. It does not author AGER. Authoring is `okf-agent-graph` (`/ager-author`, `/ager-validate`).

## Mapping

| AGER | Claude Code |
| --- | --- |
| AgentGraph | plugin root + `AGENTS.md` |
| OrchestratorAgent | `agents/<id>.md` lead + `skills/<id>/SKILL.md` |
| WorkerAgent / Judge / Synthesizer | `skills/<id>/SKILL.md` + optional `agents/<id>.md` |
| Tool + ToolRule | skill "Allowed tools" + hook notes in `hooks/` |
| LoopPolicy | `skills/ager-run/SKILL.md` stop conditions |
| ScratchPad keys | skill "Write to" / "Read from" |
| HumanGate | command that pauses for the user |

## Steps

1. Locate the AGER bundle (`--bundle`, `sample-ager`, `SECOND_BRAIN_ROOT`, or cwd with `index.md` + `runtime/agent-graph.md`).
2. If `okf-agent-graph` is installed, run `ager-validate` first. If validation fails, stop.
3. Run the deterministic emitter (do not freehand the tree):

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/emit.py --bundle <AGER_ROOT> --out <OUT>
```

4. Report written paths. Never claim production-ready without tests.

## References

- `references/mapping.md`
- `references/output-tree.md`
