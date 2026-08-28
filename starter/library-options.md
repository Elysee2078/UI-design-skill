# Optional libraries and live sources

Do **not** install everything below. This is a decision menu, not a default dependency list.

## UI Skills — live design-engineering knowledge

No project dependency is required for the remote MCP.

MCP endpoint:

```text
https://www.ui-skills.com/mcp
```

CLI exploration:

```bash
npx ui-skills
npx ui-skills start
npx ui-skills categories
npx ui-skills list
npx ui-skills get baseline-ui
```

Use when a live design-engineering playbook improves the task. Do not clone the whole corpus into every project.

## ReUI — complex product UI

Best fit: React 19 + Tailwind CSS v4 + shadcn-compatible projects that need complex grids, calendars, filters, kanban, command surfaces and advanced product patterns.

Registry starter: `starter/components.json`.

MCP:

```text
https://mcp.reui.io
```

Agent rule: search → fetch current API/examples → install/reuse → adapt to project tokens → validate usage.

Premium resources require a legitimate `REUI_LICENSE_KEY`. Keep it outside Git.

## Open Props — token source

If the project benefits from a broad maintained token package rather than its current system:

```bash
npm install open-props
```

Prefer mapping only the tokens you need into semantic project roles instead of coupling every component directly to a huge primitive namespace.

## Motion Primitives / Kinetics

Use when the interaction model actually benefits from reusable motion patterns. For a simple hover/focus/opacity transition, CSS is usually lower-cost.

Verify the current package/API from upstream before install.

## Playwright — visual/interaction QA

```bash
npm install -D @playwright/test
npx playwright install
```

Use the consumer project's existing test runner if one already exists.

## axe-core

Use directly or through the consumer project's testing integration for automated accessibility findings. Automated output does not replace keyboard/semantic/manual review.

## Storybook

Add only when the project benefits from maintained isolated component documentation/testing. Do not create a Storybook solely because the UI skill repository mentions one.

## coss.com/ui

Treat as a high-quality component/reference source with **mixed upstream licensing**. Verify the exact source path before copying. Do not turn an AGPL directory into an MIT dependency by assumption.

## Reference-only tools

Component Gallery, Design Systems One, Utopia, VibePrompts, Icon Creator, Rauno's Interfaces, background galleries and similar resources can materially improve pattern research without becoming runtime dependencies.

See `references/source-catalog.md` for the full classification.
