# claude-code-ager

AGER translator. Compiles a validated bundle into **one tree** every host can load.

A host gets a manifest, never a fork. See [docs/HOSTS.md](docs/HOSTS.md).

| Host | Reads |
| --- | --- |
| **Agent Plugins 1.0** | [`plugin.json`](plugin.json) + `skills/` |
| **Claude Code** | `.claude-plugin/` |
| **Grok Build** | Claude layout (zero-config) + `.grok-plugin/` |
| **Codex** | `.codex-plugin/` (`$ager-to-claude-code`) |
| **Cursor** | Agent Plugins 1.0 + [hosts/cursor/SKILL.md](hosts/cursor/SKILL.md) |

## Install

```bash
claude plugin marketplace add SpillwaveSolutions/claude-code-ager
claude plugin install claude-code-ager@claude-code-ager-marketplace

codex plugin marketplace add SpillwaveSolutions/claude-code-ager
```

Cursor: `/plugin install claude-code-ager` — see [docs/CURSOR.md](docs/CURSOR.md).

```bash
python3 scripts/emit.py --bundle path/to/sample-ager --out ./generated
```

## License

MIT
