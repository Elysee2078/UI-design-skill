# Agent instructions

This repository is an agent-facing UI design, design-engineering and brand-art-direction toolkit.

## When these instructions apply

For any task involving UI design, redesign, frontend composition, component selection, visual polish, responsive behavior, interaction design, accessibility, motion, design systems, visual QA, brand identity application, Canva, campaign graphics, business cards, print collateral, ads, social graphics, merch or branded image generation:

1. Read `SKILL.md` first.
2. Route to the smallest relevant focused skill in `skills/`.
3. Read `references/source-catalog.md` before copying or installing third-party UI code.
4. For brand/collateral work, read `skills/brand-art-direction/SKILL.md` and inspect authoritative brand assets before generation.
5. Prefer existing project components/tokens and official brand assets before introducing new dependencies or visual language.
6. If ReUI MCP/registry or UI Skills MCP is configured, query it instead of guessing current APIs.
7. Do not treat reference galleries, screenshots, premium examples, prompt libraries or search-engine images as permission to copy their source or as higher authority than the project's own Brand Kit.

## Evidence-first rule

Never claim a route, component, screenshot, stylesheet, design token, test, browser state, Brand Kit, logo/font/color asset, external source or MCP result was inspected unless it actually was. Separate verified facts from design inference.

For brand-critical work, a category description is not brand evidence. If official assets are available, inspect them before designing.

## Change discipline

- If the user asked for an audit only, stay read-only.
- Do not rewrite working architecture solely to achieve visual novelty.
- Avoid adding a second component system when the existing one can satisfy the requirements.
- Keep changes scoped and reversible.
- Preserve real product data and behavior; do not replace difficult states with fake demo data.
- Do not invent logos, monograms, taglines, brand colors, fonts, features, legal/company/contact data or social handles.
- Do not include credentials, API keys, paid registry tokens, private design assets or font files in committed public files.

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

Every brand-critical visual should account for:

- authoritative Brand Kit / asset inspection;
- exact logo/font/color/tagline fidelity;
- reference-role separation;
- hierarchy, composition and typography craft;
- no hallucinated identity elements or company facts;
- editable critical text where practical;
- target-platform or print production constraints;
- brand-fidelity and production-readiness QA.

## Validation

For this repository itself:

```bash
python scripts/validate_skills.py
python scripts/build_lovable_bundles.py
```

For consumer projects, use the project's own lint/typecheck/test/build commands plus screenshot/interaction checks described in `skills/visual-qa/SKILL.md`. For brand/collateral work use the scorecard and production gates in `skills/brand-art-direction/SKILL.md`.

## Third-party boundaries

Original material in this repository is MIT licensed. Third-party code and creative references are not vendored unless explicitly identified. Each linked source retains its own license and commercial terms. Mixed-license and premium resources must be handled according to `references/source-catalog.md`.
