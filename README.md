# UI Design Skill

A portable, evidence-first UI design and design-engineering skill pack for AI coding/building agents.

It is designed to work across **Lovable, OpenAI Codex/ChatGPT coding workflows, Sigma-compatible skill workflows, Claude Code, Cursor, and generic agents that understand `SKILL.md`, `AGENTS.md`, or MCP**.

The pack was seeded from Levi's 15-resource UI thread and then expanded with implementation standards, agent routing, licensing controls, testing and live MCP/registry integrations. See `references/original-thread.md` and `references/source-catalog.md`.

## What this repository does

This repository turns a scattered collection of UI resources into an agent-usable system rather than a bookmark list. It gives an agent:

- a routing skill that decides what kind of UI work is actually needed;
- focused skills for audit, production UI building, design-system extraction, complex product UI, motion, accessibility, responsive typography/spacing, and visual QA;
- a license-aware source catalog so agents know what can be integrated, what should only be referenced, and what is premium;
- MCP/registry guidance for live component discovery instead of hallucinating APIs;
- reusable semantic design tokens and a `design.md` template;
- compatibility instructions for Lovable, Codex, Sigma-compatible and generic agent environments;
- validation and automatic Lovable ZIP packaging via GitHub Actions.

## Core principle

**Do not solve “make it look better” by inventing another generic AI aesthetic.**

The agent must first inspect product evidence, identify the actual design constraints, reuse existing primitives where possible, verify APIs against live documentation/registries, and only then modify the UI.

## Skill set

| Skill | Purpose |
|---|---|
| `SKILL.md` | Root orchestrator and routing policy |
| `ui-audit` | Evidence-based read-only UI diagnosis |
| `ui-build` | Production screen/component implementation |
| `design-system-bootstrap` | Extract/establish semantic tokens and component invariants |
| `create-design-md` | Generate durable design-system documentation from implemented evidence |
| `complex-product-ui` | Dashboards, tables, grids, filters, kanban, calendars and dense operational UI |
| `motion-and-microinteractions` | Intentional motion, springs, transitions and reduced-motion behavior |
| `accessibility-and-input` | Semantics, forms, focus, keyboard, touch and ARIA patterns |
| `responsive-type-spacing` | Fluid typography/spacing and responsive recomposition |
| `visual-qa` | Rendered-state, responsive, keyboard and regression verification |

## Repository layout

```text
SKILL.md                         # portable root orchestrator / Lovable-importable skill
AGENTS.md                        # repo-wide agent instructions
skill-manifest.json              # machine-readable skill index
skills/                          # focused reusable skills
references/                      # source catalog, source thread, principles, design.md template
adapters/                        # Lovable / Codex / Sigma / generic / MCP setup
starter/                         # registry config, semantic tokens, motion and library menu
scripts/                         # bundle/validation helpers
.github/workflows/               # CI validation + Lovable ZIP artifacts
```

## Recommended source strategy

The pack prefers live, agent-readable sources over copied component code:

- **UI Skills** for design-engineering playbooks and routing;
- **ReUI MCP + registry** for complex shadcn-compatible product UI and API-verified component reuse;
- **coss.com/ui** as a high-quality accessible component reference / optional component source, subject to its mixed-license directory boundaries;
- **Open Props** when a maintained token package genuinely reduces project debt;
- **Kinetics** and **Motion Primitives** for motion patterns where a reusable motion dependency is justified;
- **Utopia** for fluid type and spacing calculations;
- **W3C WCAG / WAI-ARIA APG / MDN** as primary correctness references.

Reference galleries/prompt collections remain research sources unless their current license explicitly supports redistribution.

## Quick validation

```bash
python scripts/validate_skills.py
python scripts/build_lovable_bundles.py
```

The GitHub Action `.github/workflows/validate-and-bundle.yml` performs both steps and uploads `lovable-ui-skills` ZIP artifacts.

## Lovable

Lovable can import a public GitHub repository containing `SKILL.md`, or upload a ZIP containing `SKILL.md`. This repository is private, so the reliable route is the generated ZIP artifacts unless you intentionally make the repository public later.

See `adapters/lovable.md`.

## Codex / ChatGPT coding workflows

Codex supports reusable Skills and repository `AGENTS.md` instructions. Use the root router plus only the focused skills needed by the task. Connect ReUI/UI Skills MCP when current live component/skill knowledge materially improves the implementation.

See `adapters/codex.md` and `adapters/mcp-sources.md`.

## Sigma-compatible workflows

Sigma's published agent-skill model is repository-based and uses `AGENTS.md` plus skill files for assistants including Codex and Cursor. This repository follows the same portable pattern. For Sigma-specific workbook behavior, combine this UI pack with Sigma's maintained domain skill rather than duplicating Sigma APIs here.

See `adapters/sigma.md`.

## License

Original files in this repository are MIT licensed. Third-party resources retain their own licenses and are **not** relicensed by this repository. See `NOTICE.md` and `references/source-catalog.md` before copying any third-party source.
