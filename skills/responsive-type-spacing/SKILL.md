---
name: responsive-type-spacing
description: Use when an interface needs fluid typography, spacing, layout density, responsive recomposition, container behavior, or removal of breakpoint-by-breakpoint arbitrary sizing.
---

# Responsive Type and Spacing

Use responsive rules to preserve hierarchy and task completion across space, not merely to shrink desktop.

## Fluid scales

Utopia-style `clamp()` formulas are useful when a value should interpolate continuously between sensible minimum and maximum sizes. Use them for selected type/spacing/layout values, not every dimension.

Example pattern:

```css
font-size: clamp(var(--min), var(--fluid), var(--max));
```

Prefer a small named scale over dozens of unrelated clamps.

## Typography

- Keep body text comfortably readable; do not trade legibility for fitting more content.
- Use line height proportional to measure and font size.
- Limit line length for long-form reading while allowing operational UIs to use denser measures.
- Define heading hierarchy by function, not by a fixed visual template.
- Test wrapping with long titles, localization and large numbers.

## Spacing

Create a deliberate rhythm. Use semantic layout gaps where helpful (`--space-section`, `--space-stack`, `--space-control`) mapped to a restrained primitive scale.

Avoid using large whitespace to disguise weak hierarchy and avoid compressing touch controls to make dense data fit.

## Recomposition questions

At each constrained width decide:

- what must stay visible;
- what may wrap;
- what may scroll;
- what may collapse into disclosure;
- what changes orientation;
- what moves closer to the object it controls;
- whether the task itself should become a different mobile pattern.

Use container queries when component behavior depends on its own available space and the project/browser targets support them.

## Verification

Check at minimum one narrow mobile width, a larger mobile/tablet width, common desktop and a wide desktop. Also inspect intermediate widths where grids commonly break. Verify zoom and long-content behavior, not only pristine demo copy.
