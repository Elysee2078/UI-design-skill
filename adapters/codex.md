# Codex adapter

Codex supports reusable Skills plus repository `AGENTS.md` instructions. This repository provides both.

## Repository use

When Codex is working inside this repository, root `AGENTS.md` routes UI tasks into the portable root `SKILL.md` and focused `skills/*/SKILL.md` files.

For another project, either:

- clone/copy the relevant skill folders into the project's agent-skill location;
- or keep this repository available as a reusable reference and explicitly load the relevant skill files.

Do not duplicate project-specific tokens or product rules into this generic repository. Keep those in the consumer project.

## ReUI MCP

For data-heavy/complex product UI, configure the current ReUI MCP:

```bash
codex mcp add reui --url https://mcp.reui.io
codex mcp list
codex mcp login reui
```

Then use the live ReUI tools to search components, inspect current APIs/examples, validate usage and obtain install commands before implementation.

## UI Skills MCP

UI Skills exposes a live MCP endpoint:

```text
https://www.ui-skills.com/mcp
```

Use its `list_skills` / `get_skill` style workflow when an additional design-engineering playbook is useful. Prefer this to freezing a large upstream skill corpus inside the repo.

## Security

Do not commit MCP tokens, premium registry keys or secrets. Use environment/secret management supported by the runtime.
