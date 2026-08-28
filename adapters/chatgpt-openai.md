# ChatGPT / OpenAI adapter

Use this repository as a portable design-intelligence layer for ChatGPT and OpenAI coding workflows.

## In ChatGPT

When repository/file access is available, provide the agent with the root `SKILL.md` plus only the focused skill needed for the current job. Avoid dumping the entire repository into context on every turn.

Recommended routing:

- audit or critique existing UI → `skills/ui-audit/SKILL.md`
- build or redesign → `skills/ui-build/SKILL.md`
- establish design tokens/system → `skills/design-system-bootstrap/SKILL.md`
- complex dashboard / table / kanban / calendar / filters → `skills/complex-product-ui/SKILL.md`
- motion → `skills/motion-and-microinteractions/SKILL.md`
- accessibility → `skills/accessibility-and-input/SKILL.md`
- responsive type/spacing → `skills/responsive-type-spacing/SKILL.md`
- final screenshot/state validation → `skills/visual-qa/SKILL.md`

## Product context

Before generating or changing UI, load project-specific product/design context if available. The skill must not override an existing product design system merely because a third-party pattern looks more polished in isolation.

## Tool-aware behavior

If the OpenAI environment has access to browser, repository, Figma, image generation, or other design tools:

1. inspect existing implementation and evidence first;
2. use live documentation for external component APIs;
3. generate visual concepts only when they improve a concrete design decision;
4. implement against the project's current stack and tokens;
5. validate with screenshots and interaction states when possible.

## External resources

Treat `references/source-catalog.md` as the source-selection and licensing gate. Prefer live agent-readable registries/skills over stale copied component snippets.

## Completion contract

Do not report UI work as complete unless the response distinguishes:

- what was actually inspected;
- what was changed or proposed;
- which external dependencies were used;
- which validations were actually run;
- what remains uncertain or unverified.
