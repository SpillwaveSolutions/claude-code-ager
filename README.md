# claude-code-ager

AGER translator plugin. Author graphs with
[`okf-agent-graph`](https://github.com/SpillwaveSolutions/okf-agent-graph).
This plugin **compiles** a validated bundle into **one tree** that every host can load.

A host gets a manifest, never a fork. See [docs/HOSTS.md](docs/HOSTS.md).

| Host | Reads |
| --- | --- |
| **Agent Plugins 1.0** | [`plugin.json`](plugin.json) + `skills/` |
| **Claude Code** | `.claude-plugin/` |
| **Grok Build** | Claude layout (zero-config) + `.grok-plugin/` |
| **Codex** | `.codex-plugin/` (`$ager-to-claude-code`) |
| **Cursor** | Agent Plugins 1.0 + [hosts/cursor/SKILL.md](hosts/cursor/SKILL.md) |

## Install

Claude Code:

```bash
claude plugin marketplace add SpillwaveSolutions/claude-code-ager
claude plugin install claude-code-ager@claude-code-ager-marketplace
```

Codex:

```bash
codex plugin marketplace add SpillwaveSolutions/claude-code-ager
```

Grok Build: add the repo; it loads the Claude layout with zero extra config.

Cursor (Agent Plugins 1.0): see [docs/CURSOR.md](docs/CURSOR.md).

```
/plugin install claude-code-ager
```

## Use

```
/ager-to-claude-code
$ager-to-claude-code
```

```bash
python3 scripts/emit.py --bundle path/to/sample-ager --out ./generated
```

The emitted directory is itself Agent Plugins 1.0 + Claude + Grok + Codex + Cursor.

## License

MIT
