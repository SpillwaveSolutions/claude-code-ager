# claude-code-ager

AGER → **Claude Code** translator plugin.

Does **not** author graphs. Author and validate with
[`okf-agent-graph`](https://github.com/SpillwaveSolutions/okf-agent-graph).
This plugin compiles a validated bundle into a Claude Code plugin
(skills, agents, commands, hook notes).

## Install

```bash
claude plugin marketplace add SpillwaveSolutions/claude-code-ager
claude plugin install claude-code-ager@claude-code-ager-marketplace
```

Grok Build loads the Claude plugin layout with zero extra config.

## Use

```
/ager-to-claude-code
```

or:

```bash
python3 scripts/emit.py --bundle path/to/sample-ager --out ./generated/claude-code
```

Sibling compiler: [`ager-translators`](https://github.com/SpillwaveSolutions/ager-translators).

## License

MIT
