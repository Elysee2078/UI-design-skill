# Live MCP / registry sources

Use live sources for fast-moving component APIs and skill catalogs so agents do not freeze stale documentation into project prompts.

## UI Skills

MCP endpoint:

```text
https://www.ui-skills.com/mcp
```

Expected workflow:

1. list/search available skills;
2. retrieve the smallest relevant skill;
3. apply it together with this repository's evidence/license rules.

CLI alternative:

```bash
npx ui-skills list
npx ui-skills get baseline-ui
```

## ReUI

MCP endpoint:

```text
https://mcp.reui.io
```

Registry template:

```text
https://reui.io/r/{style}/{name}.json
```

Use for current component discovery, API/examples, validation and installation guidance. Treat free/open-source and paid Pro content as separate access classes.

## Consumer-agent rule

MCP output is current external evidence, not authority over the project's own constraints. Before accepting a recommended component verify:

- framework/version compatibility;
- existing project primitive overlap;
- accessibility behavior;
- dependency cost;
- visual/token fit;
- licensing/access class.

Never place authentication tokens in this repository.
