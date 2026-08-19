#!/usr/bin/env python3
"""Emit a Claude Code plugin from an AGER bundle."""
from __future__ import annotations
import argparse, json
from pathlib import Path
from ir import load_bundle

def write(out: Path, rel: str, content: str) -> Path:
    dest = out / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content if content.endswith("\n") else content + "\n", encoding="utf-8")
    return dest

def emit(graph, out: Path):
    written = []
    ident = {"name": graph.id, "version": "0.1.0", "description": f"Compiled AGER graph: {graph.title}", "ager_version": graph.ager_version, "license": "MIT"}
    written.append(write(out, "plugin.json", json.dumps(ident, indent=2)))
    written.append(write(out, "marketplace.json", json.dumps({"$schema": "https://anthropic.com/claude-code/marketplace.schema.json", "name": f"{graph.id}-marketplace", "plugins": [{"name": graph.id, "source": "./", "version": "0.1.0"}]}, indent=2)))
    written.append(write(out, ".claude-plugin/plugin.json", json.dumps(ident, indent=2)))
    written.append(write(out, "AGENTS.md", f"# AGENTS.md \u2014 {graph.title}\n\nCompiled from AGER {graph.ager_version}. Entry: `{graph.entry}`.\nLoopPolicy: {' → '.join(graph.loop_priority)}. max_turns={graph.max_turns} price=${graph.price_budget} deadline_ms={graph.deadline_ms}\nUse `/ager-run`. Do not invent extra agents.\n"))
    lead = next(a for a in graph.agents if a.role == "orchestrator")
    written.append(write(out, f"agents/{lead.id}.md", f"---\nname: {lead.id}\ndescription: {lead.description}\n---\n\n# {lead.title}\n\n{lead.instructions}\n\nHonor skills/ager-run. Record to `{lead.record_key}`.\n"))
    written.append(write(out, "skills/ager-run/SKILL.md", f"---\nname: ager-run\ndescription: Execute compiled AGER graph {graph.id}.\n---\n\n# Run {graph.title}\n\nEntry **{lead.title}**. Stop on goal / {graph.deadline_ms}ms / ${graph.price_budget} / {graph.max_turns} turns / no_progress.\nClaude Code does not meter USD. Track an estimate and stop.\n"))
    for agent in graph.agents:
        written.append(write(out, f"skills/{agent.id}/SKILL.md", f"---\nname: {agent.id}\ndescription: {agent.description}\n---\n\n# {agent.title}\n\nRole: `{agent.role}`\n\n{agent.instructions}\n\nTools: {', '.join(agent.tools) or 'none'}\nRecord: `{agent.record_mode}` → `{agent.record_key or agent.id}`\n"))
    written.append(write(out, "commands/ager-run.md", f"---\nname: ager-run\ndescription: Run compiled AGER graph {graph.id}.\n---\n\nFollow **ager-run** and orchestrator `{lead.id}`.\n"))
    rules = []
    for t in graph.tools:
        for r in t.rules:
            rules.append(f"- `{t.id}` / `{r.get('id')}`: {r.get('action')} — {r.get('message', '')}")
    written.append(write(out, "hooks/README.md", "# Hook notes (not executable)\n\n" + "\n".join(rules) + "\n"))
    return written

def main():
    p = argparse.ArgumentParser(prog="ager-to-claude-code")
    p.add_argument("--bundle", type=Path)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    written = emit(load_bundle(args.bundle), args.out)
    print(f"wrote {len(written)} files to {args.out}")
    for w in written:
        print(" ", w)

if __name__ == "__main__":
    main()
