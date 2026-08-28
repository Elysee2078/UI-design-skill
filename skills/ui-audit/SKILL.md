---
name: ui-audit
description: Use when an existing interface needs a read-only or pre-change audit for visual quality, generic AI-looking patterns, hierarchy, consistency, interaction states, responsiveness, accessibility, or design-system debt.
---

# UI Audit

Audit before proposing visual changes. If the user asked only for an audit, do not edit code.

## Evidence to collect

Inspect what is actually available:

- key routes/screens and their task priority;
- screenshots or rendered views at representative widths;
- component library and repeated primitives;
- global styles, theme files and token definitions;
- typography loading and scale;
- spacing, radius, border and shadow values;
- navigation and information architecture;
- forms and validation states;
- loading, empty, error, success, disabled and destructive states;
- interactive behavior with mouse, keyboard and touch where testable;
- existing accessibility tooling/results;
- relevant product data shapes and content extremes.

## Audit dimensions

Score findings by **impact**, not taste:

1. **Task clarity** — can users see what matters and what to do next?
2. **Information hierarchy** — headings, grouping, density and action prominence.
3. **System consistency** — token drift, duplicated component variants, arbitrary values.
4. **Interaction quality** — feedback, states, target sizes, disabled/destructive behavior.
5. **Responsive behavior** — overflow, reflow, content priority and touch use.
6. **Accessibility** — semantics, labels, focus, keyboard, contrast, motion preferences.
7. **Visual distinctiveness** — does the UI express product/brand intent or rely on generic AI defaults?
8. **Implementation cost** — dependency sprawl, one-off CSS, duplicated primitives.

## Finding format

For each material issue provide:

- **Evidence:** exact screen/component/file/state inspected.
- **Problem:** observable failure, not a preference statement.
- **User/business consequence:** what becomes slower, less clear, less trustworthy or inaccessible.
- **Severity:** P0 blocker, P1 high, P2 medium, P3 polish.
- **Root cause:** token/system/architecture/content/state/implementation.
- **Smallest effective fix:** prefer systemic fixes over local patches.
- **Confidence:** verified / strong inference / hypothesis.

## Generic-AI-pattern check

Flag only when supported by evidence:

- excessive cards and nested rounded containers;
- decorative gradients/glows without hierarchy function;
- repeated generic icon + headline + paragraph feature grids;
- enormous type that crowds out product information;
- inconsistent radii/shadows/spacing from prompt-by-prompt generation;
- fake dashboard metrics or placeholder-looking content;
- interchangeable SaaS aesthetic with no product-specific visual logic.

Do not remove a pattern merely because it is common. Remove it when it conflicts with hierarchy, brand, usability, density or maintainability.

## Finish

Prioritize the **3-5 highest-leverage systemic changes**. Separate changes that can be safely automated from those requiring product/brand judgment. If implementation is requested next, route to `ui-build` or `design-system-bootstrap`.
