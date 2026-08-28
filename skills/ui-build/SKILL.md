---
name: ui-build
description: Use when building or redesigning production web or app screens, components, forms, navigation, landing pages, onboarding, settings, account surfaces, or other interface flows from product requirements or an existing codebase.
---

# UI Build

Build from product evidence, not from a generic visual recipe.

## Before implementation

Determine from the project:

- framework, styling system and existing component primitives;
- current tokens and brand constraints;
- primary user task and primary action;
- expected data/content and edge cases;
- target viewport range;
- whether the surface is marketing, transactional, content-heavy or operational;
- accessibility and performance constraints.

If the project already answers these questions, do not stop to interview the user again.

## Composition rules

1. Establish page hierarchy before styling details.
2. Use a restrained number of containers; grouping does not always require a card.
3. Make the primary action visually obvious and secondary actions genuinely secondary.
4. Keep repeated action placement consistent across related screens.
5. Give dense operational UIs enough information per viewport; do not apply marketing-page whitespace indiscriminately.
6. Use progressive disclosure for advanced/rare options.
7. Keep copy specific to the actual product. Do not invent placeholder claims, metrics or social proof.

## Component selection

Follow `references/source-catalog.md`.

- Reuse existing project primitives first.
- For complex shadcn-compatible product patterns, query ReUI MCP/registry if available.
- For accessible primitive behavior, prefer an established primitive over hand-rolled ARIA.
- Treat galleries and prompt libraries as research, not as code dependencies.

When taking an external component, adapt its colors, typography, spacing and states to the project's semantic tokens. Do not import another product's visual identity intact.

## Required states

Implement applicable states at the same time as the happy path:

- loading/skeleton;
- empty/no-results;
- validation error;
- request/server error;
- disabled/busy;
- success/confirmation;
- destructive confirmation;
- permission-limited/read-only;
- long content/overflow;
- focus/hover/pressed/selected.

## Responsive implementation

Treat narrow layouts as a priority transformation, not only a scale change. Decide what wraps, scrolls, collapses, stacks, moves into a disclosure, or remains fixed. Preserve the primary task.

## Accessibility baseline

Use native semantic elements whenever possible. Label controls. Make icon-only actions named. Preserve logical DOM/tab order. Provide visible focus. Use sufficiently large touch targets. Respect reduced motion. Route complex patterns to `accessibility-and-input`.

## Final checks

Before declaring completion:

- no unjustified new design-system dependency;
- semantic tokens instead of scattered raw values;
- no broken overflow at target widths;
- major UI states implemented;
- keyboard path works for critical actions;
- visual QA performed using `skills/visual-qa/SKILL.md`.
