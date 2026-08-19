---
name: grok-bot-claude-code-ager
description: Bind a Grok Bot agent to the AGER → Claude Code translator. Isolation, identity, deterministic writes.
---

# Grok Bot / claude-code-ager

1. Identity: `grok-bot/claude-code-ager`
2. Grok Build loads the Claude plugin layout with zero config. `.grok-plugin/marketplace.json` pins identity.
3. Run `scripts/emit.py`. Do not freehand the emitted tree.
4. If writing a shared second brain, open an isolation session first (`okf-agent-graph` `/ager-session`).
5. Never document a private remote.
