# UI source catalog

This catalog starts with the 15 resources collected in Levi's UI-resource thread and adds primary standards/tooling that make the skill pack safer and more executable.

The status is intentionally conservative. **Reference** means learn patterns from the source but do not vendor its code/assets unless the current upstream license is independently verified. **Integrate** means the upstream exposes an intended package, registry, CLI, MCP or open-source path, still subject to its current license.

## Resources from the thread

| Resource | Best use | Agent strategy | Redistribution / license posture |
|---|---|---|---|
| [UI Skills](https://www.ui-skills.com/) | Design-engineering playbooks: baseline UI, frontend design, motion, accessibility, polish | **Integrate via CLI/MCP**. Prefer live `list_skills` / `get_skill` rather than copying stale text. MCP: `https://www.ui-skills.com/mcp` | Upstream `ibelick/ui-skills` has a current MIT license. Re-check before vendoring future versions. |
| [coss.com/ui](https://coss.com/ui) | Accessible production React component reference from the Cal.com ecosystem | **Reference / selectively integrate** only from explicitly MIT upstream directories | Mixed license upstream: repository default AGPL-3.0; `apps/origin/` and `apps/ui/` are MIT. Other directories are not automatically MIT. Verify exact path. |
| [Design System Checklist](https://www.designsystemchecklist.com/) | Completeness checklist for design-system work | **Reference** as an audit prompt; do not clone site content by default | License not verified for redistribution. |
| [ReUI](https://reui.io/) | Complex shadcn-compatible product UI: grids, calendars, filters, kanban, command surfaces and examples | **Integrate via MCP + registry**. Query component API/examples before implementation. MCP: `https://mcp.reui.io` | ReUI open-source repository is MIT. Pro blocks/templates/icons remain commercial access classes; never bypass premium access. |
| [Kinetics](https://kinetics.colorion.co/) | Spring-based interaction and motion patterns with CSS/React examples | **Reference first**. Reproduce principles in project-native code or copy only after verifying the exact upstream terms for the material being used | At review time the public repository exposed the code/examples but a project-level redistribution license was not established with sufficient confidence. Treat as reference until verified. |
| [Icon Creator](https://iconcreator.dev/) | Creating project-specific icons rather than accepting mismatched stock iconography | **Tool**. Generate/export only assets appropriate for the project | Treat site implementation/assets as reference unless terms say otherwise. |
| [VibePrompts](https://vibeprompts.dev/) | Broad UI prompt/pattern ideation across dashboards, pricing, auth, onboarding, heroes, etc. | **Reference only**. Use to widen pattern search, not as a substitute for product evidence | Do not vendor the prompt library unless its redistribution license is verified. |
| [Animated Buttons](https://animatedbuttons.colorion.co/) | Button microinteraction references | **Reference**; reproduce interaction principles in project-native code when appropriate | License not verified here for bulk redistribution. |
| [Component Gallery](https://component.gallery/) | Compare how real design systems solve the same component | **Reference research** before inventing a novel pattern | Examples belong to their respective source systems/licenses. Do not bulk copy. |
| [Design Systems One](https://designsystems.one/) | Real production design systems, tokens, stacks, `design.md` research and agent-readiness patterns | **Reference / tooling**. Use comparisons to inform `design.md`; retain provenance | Do not rehost third-party design kits without source-specific permission. |
| [Utopia](https://utopia.fyi/) | Fluid type, spacing and layout scales | **Tool/reference**. Use generated formulas/output as a starting point, then test in the product | Do not vendor the application itself. |
| [Open Props](https://open-props.style/) | Reusable CSS design tokens for color, spacing, radii, shadows, easing, etc. | **Integrate as an MIT package or selectively map tokens** when it reduces project debt | Current upstream `argyleink/open-props` license is MIT. Avoid importing a huge primitive namespace when a smaller semantic layer is enough. |
| [Rauno's Interfaces](https://interfaces.rauno.me/) | High-signal interaction details: semantics, forms, motion restraint, typography, feedback | **Reference principles** and convert them into project checks | Use as guidance; do not republish the site wholesale. |
| [bg.ibelick](https://bg.ibelick.com/) | Background pattern inspiration / snippets | **Reference by default** | A clear project redistribution license was not established during preparation; verify before copying source snippets wholesale. |
| [Motion Primitives](https://motion-primitives.com/) | Reusable React motion primitives | **Integrate selectively** where a project already benefits from its motion stack | Current upstream `ibelick/motion-primitives` license is MIT. Verify future versions/dependencies before copying. |

## Primary standards and implementation references added to this repository

These sources should outrank aesthetic galleries when implementation correctness is at stake:

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — accessibility success criteria.
- [WAI-ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) — accessible interaction patterns and keyboard behavior.
- [MDN Web Docs](https://developer.mozilla.org/) — HTML/CSS/platform behavior.
- [Base UI](https://base-ui.com/) — unstyled accessible React primitives; also relevant because current ReUI/coss work can build on Base UI.
- [shadcn/ui](https://ui.shadcn.com/) — source-distributed component conventions and registries.
- [Playwright](https://playwright.dev/) — browser interaction and screenshot testing.
- [axe-core](https://github.com/dequelabs/axe-core) — automated accessibility checks (not a substitute for keyboard/screen-reader review).
- [Storybook](https://storybook.js.org/) — isolated component/state documentation when a product benefits from a maintained component workbench.

## Optional external agent-skill ecosystems

The repository also contains a separately evaluated shortlist in `references/agent-skill-ecosystem.md` covering:

- Impeccable;
- UI/UX Pro Max;
- Taste Skill;
- coss UI's own MIT skill.

These are optional upstream intelligence layers, not dependencies to stack indiscriminately.

## Selection rule

Use this decision order:

1. **Existing project component** if it already satisfies behavior/accessibility and can be restyled safely.
2. **Existing project primitive** composed into a new pattern.
3. **Live registry/MCP component** when it materially saves complex implementation work.
4. **Open-source external component** with a compatible license and justified dependency cost.
5. **Custom component** when product behavior is specific enough that existing primitives are a worse fit.
6. **Reference-only source** for pattern research, never as an unverified code supply.

## Dependency test

Before adding any UI library, answer all five:

1. What exact unresolved problem does it solve?
2. Can the current stack solve that problem with less dependency surface?
3. Is the package/registry maintained and compatible with the project's framework versions?
4. Are its accessibility semantics and interaction model understood?
5. Is its license/commercial boundary compatible with the product?

If the answer to #1 is merely “it looks nicer,” do not add the dependency.
