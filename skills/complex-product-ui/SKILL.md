---
name: complex-product-ui
description: Use when building data-heavy product interfaces such as dashboards, data grids, filters, kanban boards, calendars, gantt/timeline views, command palettes, bulk actions, dense forms, or operational admin surfaces.
---

# Complex Product UI

Complex UI fails more often from interaction/state design than from styling. Start with task and data structure.

## Required analysis

Determine:

- primary objects and relationships;
- frequent vs rare actions;
- row/item selection behavior;
- bulk actions;
- filtering/search/sort model;
- pagination or virtualization needs;
- edit model: inline, modal, drawer, detail page;
- permissions and destructive actions;
- loading/empty/error/partial states;
- mobile expectations for dense data.

## ReUI workflow

If ReUI MCP is available, use it as a live component knowledge source:

1. search for the needed pattern/component;
2. fetch the current component API and examples;
3. inspect installation requirements;
4. adapt to the project's existing tokens/primitives;
5. validate usage against the live source.

Do not guess ReUI props or copy premium examples without licensed access.

If ReUI is not available, prefer the project's current primitives or a documented accessible primitive system before custom-building complex widgets.

## Interaction rules

- Keep filtering state visible and reversible.
- Make selected/bulk-action state explicit.
- Preserve context during edits where possible.
- Avoid modal chains.
- Use optimistic updates only when rollback/error behavior is clear.
- For destructive/bulk actions, communicate scope before execution.
- Use tabular numerals for changing numeric values when useful.
- Keep status labels semantically distinct from actions.
- For large data sets, consider virtualization/performance before adding visual complexity.

## Responsive strategy

Do not force a desktop grid into a tiny screen unchanged. Decide whether the mobile job is:

- a reduced-column table;
- horizontally scrollable data with frozen identity column;
- stacked item cards;
- search/filter + detail workflow;
- or intentionally desktop-only with a clear product constraint.

## Accessibility

Dense controls still require labels, focus visibility and logical keyboard order. Complex widgets must follow documented keyboard conventions; route unfamiliar patterns through WAI-ARIA APG rather than improvising ARIA.

## Completion

Test populated, empty, filtered-empty, loading, server-error, permission-limited, long-value and high-volume states. Verify keyboard access to the critical workflow.
