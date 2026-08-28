# UI Design Skill

A portable, evidence-first UI design and design-engineering skill pack for AI coding/building agents.

It is designed to work across **Lovable, OpenAI Codex/ChatGPT coding workflows, Sigma-compatible skill workflows, Claude Code, Cursor, and generic agents that understand `SKILL.md`, `AGENTS.md`, or MCP**.

## What this repository does

This repository turns a scattered collection of UI resources into an agent-usable system rather than a bookmark list. It gives an agent:

- a routing skill that decides what kind of UI work is actually needed;
- focused skills for UI audit, UI building, design-system extraction, complex product UI, motion, accessibility, responsive typography/spacing, and visual QA;
- a license-aware source catalog so agents know what can be integrated, what should only be referenced, and what is premium;
- MCP/registry guidance for live component discovery instead of hallucinating APIs;
- reusable design tokens and `design.md` templates;
- compatibility instructions for Lovable, Codex, Sigma and generic agent environments;
- packaging scripts for Lovable ZIP imports.

## Core principle

**Do not solve “make it look better” by inventing another generic AI aesthetic.**

The agent must first inspect product evidence, identify the actual design constraints, reuse existing primitives where possible, verify APIs against live documentation/registries, and only then modify the UI.

## Repository layout

```text
SKILL.md                         # portable root orchestrator / Lovable-importable skill
AGENTS.md                        # repo-wide agent instructions
skills/                          # focused reusable skills
references/                      # source catalog, decision rules, standards
adapters/                        # Lovable / Codex / Sigma / generic setup
starter/                         # reusable design-system starter files
scripts/                         # bundle/validation helpers
```

## Recommended stack

The pack prefers live, agent-readable sources over copied component code:

- **UI Skills** for design-engineering playbooks and routing;
- **ReUI MCP + registry** for complex shadcn-compatible product UI and API-verified component reuse;
- **coss.com/ui** as a high-quality accessible component reference / optional component source, subject to its mixed-license boundaries;
- **Open Props** for reusable design tokens;
- **Kinetics** and **Motion Primitives** for motion patterns;
- **Utopia** for fluid type and spacing;
- **W3C WCAG / WAI-ARIA APG / MDN** as normative implementation references.

See `references/source-catalog.md` before copying any third-party code.

## Lovable

Lovable can import a public GitHub repository containing `SKILL.md`, or upload a ZIP containing a `SKILL.md`. This repository is currently private, so the reliable path is to use the generated ZIP bundles (or make the repo public later if desired). Lovable also reads root-level `AGENTS.md` from connected GitHub projects.

## Codex

Codex supports reusable Skills and repository `AGENTS.md` instructions. Clone this repository or copy the relevant skill folders into the project where Codex works. See `adapters/codex.md`.

## Sigma

Sigma's published agent-skill workflow is repository-based and supports Codex, Claude Code and Cursor. The focused `skills/*/SKILL.md` files in this repository follow the same portable skill-folder model. See `adapters/sigma.md`.

## License

Original files in this repository are MIT licensed. Third-party resources retain their own licenses and are **not** relicensed by this repository. See `NOTICE.md` and `references/source-catalog.md`.
