# Hosts — one tree, many manifests

A host gets a **manifest**, never a fork. Same rule as `okf-agent-graph`.

| Host | What it reads |
| --- | --- |
| **Agent Plugins 1.0** (Cursor, Copilot, VS Code, Kiro, ChatGPT) | root `plugin.json` + `skills/` |
| **Claude Code** | `.claude-plugin/` |
| **Grok Build** | Claude layout (zero-config) + `.grok-plugin/` |
| **Codex** | `.codex-plugin/` + `$` commands |
| **Cursor** | Agent Plugins 1.0 + `hosts/cursor/SKILL.md` |
