---
name: create-design-md
description: Use when an agent needs to document an existing project's implemented visual and interaction system as a durable design.md for future AI or human contributors.
---

# Create Design.md

Create documentation from evidence in the current project. Do not invent a brand system that is not implemented.

## Inspect

Read the actual theme/tokens, global styles, component variants, typography setup, layout primitives, icon dependencies, motion utilities and representative screens.

## Produce

Document:

1. product/interface character in concrete terms;
2. semantic color tokens and where each is used;
3. typography family, scale, weights and line heights;
4. spacing/layout/container rules;
5. radius, border and elevation rules;
6. core component variants and density rules;
7. iconography;
8. motion and reduced-motion behavior;
9. responsive rules;
10. accessibility invariants;
11. known exceptions/debt;
12. source files that define the truth.

For every section distinguish **implemented**, **inferred convention**, and **recommended but not yet implemented**. Avoid turning recommendations into fake facts.

Use `references/design.md.template` as the structure when useful.
