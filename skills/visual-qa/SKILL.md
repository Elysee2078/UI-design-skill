---
name: visual-qa
description: Use when UI implementation is ready for final verification through rendered screenshots, responsive checks, interaction states, regression review, keyboard checks, and accessibility/performance sanity checks.
---

# Visual QA

Do not validate a visual interface from source code alone when a rendered browser is available.

## Test matrix

Choose representative high-risk screens and test:

- narrow mobile;
- larger mobile/tablet when relevant;
- common desktop;
- wide desktop for max-width and density behavior;
- critical light/dark themes if both exist.

For each relevant screen exercise:

- loading;
- empty/no results;
- normal populated;
- long/overflowing content;
- validation/request error;
- disabled/busy;
- success;
- selected/focused/hovered;
- permission-limited/destructive states.

## Visual review

Look for:

- unintended horizontal scroll;
- clipped text or controls;
- unstable layout shifts;
- inconsistent spacing/radii/icon sizing;
- misaligned baselines;
- hidden primary actions;
- weak contrast/focus visibility;
- sticky/fixed elements covering content;
- modals/drawers escaping the viewport;
- tables/grids becoming unusable at constrained widths;
- dark-mode surfaces with incorrect semantic token mapping.

## Functional review

Test the critical path, not only isolated controls. Use keyboard-only navigation for key tasks. Verify error recovery and repeated rapid actions when relevant.

## Automation

Use Playwright or the consumer project's browser-test stack when available for deterministic routes/states and screenshot capture. Use axe-core or equivalent for automated accessibility findings, while explicitly keeping manual keyboard/semantic review in scope.

## Reporting

Do not write “looks good.” Report:

- viewport/state tested;
- defect and exact location;
- severity;
- reproduction conditions;
- fix applied or remaining;
- evidence that the fix was re-tested.

Separate visual preference from observable defects.
