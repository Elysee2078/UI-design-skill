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

## Optional Higgsfield AI video provider

Official agent skill repository: https://github.com/higgsfield-ai/skills

Official CLI and MCP overview: https://higgsfield.ai/CLI and https://higgsfield.ai/skills

This is a remote, **optional paid media provider**, not a live UI component registry. Use `skills/higgsfield-video-integration/SKILL.md` for provider-specific video routing and `skills/ai-video-production/SKILL.md` for provider-neutral production.

Do not claim a Higgsfield MCP or CLI connection is already configured merely because these links are in this repository. Before any use, verify the user's connected/installed host capabilities and live model API contracts. OAuth login, installer execution and credit-consuming jobs require explicit permission. Never store Higgsfield auth data in code, docs, Notion or a public skill package; never train a face/voice model without consent.

`npx skills add higgsfield-ai/skills` is the upstream's optional host-side install command; it is **not executed** as part of this package, and bundled Lovable skills do not contain a runnable Higgsfield CLI.

## Consumer-agent rule

MCP output is current external evidence, not authority over the project's own constraints. Before accepting a recommended component verify:

- framework/version compatibility;
- existing project primitive overlap;
- accessibility behavior;
- dependency cost;
- visual/token fit;
- licensing/access class.

Never place authentication tokens in this repository.
