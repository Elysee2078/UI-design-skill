# Lovable adapter

## Native skill route

Lovable workspace skills use Markdown skill packages centered on `SKILL.md`.

Current Lovable documentation supports:

- importing a **public GitHub repository** that contains `SKILL.md` at its root (or inside one top-level folder);
- uploading a ZIP containing `SKILL.md`;
- root-level `AGENTS.md` in a connected GitHub project as always-read project instructions.

Because this repository is private, use the ZIP route unless you intentionally make the repository public.

## Build import bundles

From the repository root:

```bash
python scripts/build_lovable_bundles.py
```

This generates:

```text
dist/lovable/ui-design-orchestrator.zip
dist/lovable/ui-audit.zip
dist/lovable/ui-build.zip
...
```

Import the orchestrator as the general UI skill. Add focused skills separately only when you want them discoverable as independent Lovable workspace skills.

## Recommended setup

1. Upload `ui-design-orchestrator.zip` as the broad routing skill.
2. Upload `ui-audit.zip`, `ui-build.zip`, `complex-product-ui.zip`, and other focused skills your workspace needs.
3. Put project-specific permanent design rules in that project's Knowledge or root `AGENTS.md`, not inside this generic repository.
4. Connect ReUI MCP for projects that need complex shadcn-compatible UI.

## ReUI in Lovable

Use Lovable's custom MCP connector:

- server name: `reui`
- URL: `https://mcp.reui.io`
- authentication: OAuth

Then ask the agent to retrieve the ReUI agent skill/current component documentation before implementing ReUI components.

For premium ReUI registries, keep `REUI_LICENSE_KEY` in Lovable/project secret management. Never commit it.

## Boundaries

A workspace skill can tell Lovable **how** to work. It does not replace project evidence. The agent must still inspect the connected project's actual code, tokens, components and routes before redesigning it.
