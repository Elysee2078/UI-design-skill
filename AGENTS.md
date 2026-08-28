# Agent instructions

This repository is an agent-facing UI design and design-engineering toolkit.

## When these instructions apply

For any task involving UI design, redesign, frontend composition, component selection, visual polish, responsive behavior, interaction design, accessibility, motion, design systems, or visual QA:

1. Read `SKILL.md` first.
2. Route to the smallest relevant focused skill in `skills/`.
3. Read `references/source-catalog.md` before copying or installing third-party UI code.
4. Prefer existing project components/tokens before introducing new dependencies.
5. If ReUI MCP/registry or UI Skills MCP is configured, query it instead of guessing current APIs.
6. Do not treat reference galleries, screenshots, premium examples, or prompt libraries as permission to copy their source.

## Evidence-first rule

Never claim a route, component, screenshot, stylesheet, design token, test, browser state, external source, or MCP result was inspected unless it actually was. Separate verified facts from design inference.

## Change discipline

- If the user asked for an audit only, stay read-only.
- Do not rewrite working architecture solely to achieve visual novelty.
- Avoid adding a second component system when the existing one can satisfy the requirements.
- Keep changes scoped and reversible.
- Preserve real product data and behavior; do not replace difficult states with fake demo data.
- Do not include credentials, API keys, paid registry tokens, or private design assets in committed files.

## Design baseline

Every production UI should account for:

- hierarchy and task priority;
- semantic HTML and keyboard navigation;
- visible focus;
- loading, empty, error, disabled and success states where applicable;
- mobile/touch behavior;
- overflow and long content;
- reduced-motion preferences;
- reusable semantic tokens;
- visual and functional verification.

## Validation

For this repository itself:

```bash
python scripts/validate_skills.py
python scripts/build_lovable_bundles.py
```

For consumer projects, use the project's own lint/typecheck/test/build commands plus screenshot/interaction checks described in `skills/visual-qa/SKILL.md`.

## Third-party boundaries

Original material in this repository is MIT licensed. Third-party code is not vendored unless explicitly identified. Each linked source retains its own license and commercial terms. Mixed-license and premium resources must be handled according to `references/source-catalog.md`.
