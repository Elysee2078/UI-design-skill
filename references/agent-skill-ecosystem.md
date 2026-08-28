# Agent UI skill ecosystem

This repository is intentionally not a wholesale fork of other design-skill projects. External skill packs are evaluated as optional upstream intelligence, not automatically merged into the core.

## Impeccable

Upstream: `pbakaus/impeccable`
License: Apache-2.0 at the time of review.

Strongest use:

- rigorous anti-pattern detection;
- design critique / polish vocabulary;
- product/design context loading;
- bounded visual QA and iterative refinement;
- typography, color, spatial, responsive, interaction and UX-writing references.

Use it when the project needs a high-craft frontend review or a more opinionated finishing layer.

Do not blindly merge it into every project. It is a full design operating system and can overlap with this repository's orchestrator. Prefer installing it as an optional upstream skill or borrowing clearly attributed ideas where license-compatible.

## UI/UX Pro Max

Upstream: `nextlevelbuilder/ui-ux-pro-max-skill`
License: MIT at the time of review.

Strongest use:

- searchable design intelligence;
- large catalog of styles, palettes, font pairings, UX guidelines and chart patterns;
- multi-platform agent adapters;
- rapid pattern discovery for web/mobile/desktop interfaces.

Use it as a research/search layer when the agent needs a broader option space.

Do not let a large style catalog replace product context. A design style is not a product strategy. The project must still select patterns based on user tasks, density, brand, accessibility and technical constraints.

## Taste Skill

Upstream: `Leonxlnx/taste-skill`
License: MIT at the time of review.

Strongest use:

- anti-generic frontend guidance;
- adjustable design variance, motion intensity and visual density;
- framework-agnostic layout/typography/motion guidance;
- avoiding repetitive AI-generated composition patterns.

Use it when the interface is technically competent but visually generic or overly template-like.

Do not use higher design variance as an excuse for novelty that hurts task completion. Product UI, healthcare, finance and dense operational tools often need restraint more than visual surprise.

## coss ui skills

Upstream: `cosscom/coss`

coss currently exposes an intended Agent Skills install path and documents progressive skill loading for component APIs, composition rules and examples. The repository has mixed licensing; coss documents `apps/origin/` and `apps/ui/` as MIT while other areas default to AGPL-3.0. Verify the exact upstream path before vendoring source.

Use coss skills when implementing coss components rather than asking an agent to reconstruct component APIs from memory.

## Selection rule

Choose an optional external skill only when it closes a specific gap:

| Gap | Best candidate |
|---|---|
| Existing UI needs a rigorous craft/polish pass | Impeccable |
| Need broad searchable design options / patterns | UI/UX Pro Max |
| UI looks obviously AI-generated or repetitive | Taste Skill |
| Implementing Cal.com-style accessible primitives | coss ui skills |
| Need complex shadcn-compatible product components | ReUI MCP/registry |
| Need motion primitives | Motion Primitives / Kinetics |
| Need fluid type and spacing math | Utopia |

## Non-stacking rule

Do not install multiple overlapping design-operating-system skills by default.

Before adding another skill, answer:

1. What missing capability does it provide?
2. Does the current skill already cover that capability?
3. Will two overlapping rule sets create contradictory design instructions?
4. Can the resource be queried live instead of copied into the repo?
5. Is the current upstream license compatible with the intended use?

If there is no concrete gap, do not add it.
