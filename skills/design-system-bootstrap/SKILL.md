---
name: design-system-bootstrap
description: Use when a project has inconsistent visual values, duplicated component styling, no semantic token layer, or needs a minimal maintainable design system before broader UI work.
---

# Design System Bootstrap

The goal is not to create a giant design-system program. Create the smallest coherent system that removes repeated arbitrary decisions.

## 1. Extract before inventing

Inspect existing styles/components and inventory:

- colors and semantic usage;
- font families, sizes, weights and line heights;
- spacing values;
- radii and border widths;
- shadows/elevation;
- icon set/sizes;
- motion durations/easing;
- container widths/breakpoints;
- repeated control heights and densities.

Cluster near-duplicates. Identify intentional brand exceptions separately from accidental drift.

## 2. Define semantic tokens

Prefer roles over palette coordinates:

- `background`, `surface`, `surface-raised`;
- `text`, `text-muted`, `text-inverse`;
- `border`, `border-strong`;
- `primary`, `primary-foreground`;
- `accent`, `success`, `warning`, `danger`, `info`;
- focus-ring and selection roles.

Keep raw palette primitives below the semantic layer when the stack benefits from them.

Define restrained scales for spacing, type, radius and motion. Reuse values aggressively.

## 3. Define component invariants

For core controls document:

- size/density variants;
- typography;
- icon sizing/alignment;
- disabled/busy/error/selected behavior;
- focus behavior;
- destructive treatment;
- mobile/touch constraints.

Start with the components that appear most often or create the most inconsistency.

## 4. Create `design.md`

Route to `skills/create-design-md/SKILL.md` and record the actual implemented system, not an aspirational one.

## 5. Migration strategy

Do not restyle every page at once unless explicitly requested. Prefer:

1. introduce token aliases without visual changes where possible;
2. migrate shared primitives;
3. migrate highest-traffic/highest-risk screens;
4. remove obsolete values/components after usage is verified.

## Acceptance criteria

- repeated raw values have semantic homes;
- component variants are explicit rather than ad hoc;
- contrast/focus states are accounted for;
- the system can express both dense and spacious surfaces if the product needs both;
- new UI can be built without inventing new values on every screen;
- documentation matches code.
