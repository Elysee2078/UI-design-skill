---
name: accessibility-and-input
description: Use when designing or reviewing forms, interactive controls, keyboard navigation, focus behavior, touch targets, semantics, ARIA patterns, contrast, reduced motion, and assistive-technology compatibility.
---

# Accessibility and Input

Use WCAG 2.2 and WAI-ARIA Authoring Practices as primary references. Automated checks are supporting evidence, not proof of accessibility.

## Native first

Prefer native elements (`button`, `a`, `input`, `select`, headings, lists, landmarks) before adding ARIA. Do not put click handlers on non-interactive elements when a semantic control exists.

## Controls

- Every input has a programmatically associated label or an equivalent accessible name.
- Icon-only buttons require an accessible name.
- Visible focus must remain obvious against all relevant surfaces.
- Keyboard order follows reading/task order.
- Disabled state is communicated semantically and visually; do not rely only on opacity.
- Prevent accidental duplicate submission during pending actions without trapping focus.
- Destructive actions communicate their scope and consequences.
- Touch targets should be comfortably operable; use roughly 44×44 CSS px as a strong baseline for primary touch controls where feasible.
- Keep mobile text inputs at 16px or larger when avoiding unwanted browser zoom is relevant.

## Complex widgets

For dialogs, comboboxes, menus, tabs, grids, tree views, listboxes and similar composite widgets, follow an established accessible primitive or the APG keyboard pattern. Do not improvise ARIA roles without implementing their keyboard contract.

## Forms and errors

- Put instructions before they are needed.
- Connect field errors to the affected control.
- On failed submission, make the error summary/action path discoverable.
- Do not erase user input unnecessarily.
- Make required/optional status understandable without color alone.

## Motion and media

Honor reduced-motion preferences. Avoid flashing/strobing patterns. Keep autoplaying/looping media from becoming an unavoidable distraction.

## Verification

At minimum for critical flows:

1. Complete the task keyboard-only.
2. Inspect visible focus across states.
3. Check accessible names/roles for custom controls.
4. Run an automated axe-style check if available.
5. Verify zoom/reflow and narrow viewport behavior.
6. Treat unresolved screen-reader-specific behavior as a manual check rather than claiming it passed.
