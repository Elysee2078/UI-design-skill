# Brand Art Direction — source analysis and provenance

This reference documents what informed `skills/brand-art-direction/SKILL.md`, what was
adopted, what was rejected as insufficient, and what remains unverified.

## User-supplied source links

- Amir Mušić / @AmirMushich — X post ID `2095182776249049456`, 2 Sep 2026:
  https://x.com/amirmushich/status/2095182776249049456
- Amir Mušić / @AmirMushich — X post ID `2095494571312496912`, 3 Sep 2026:
  https://x.com/amirmushich/status/2095494571312496912

Direct retrieval of the post bodies was blocked by X in the available browsing environment.
Therefore this skill does **not** claim to reproduce those two posts verbatim. Their links
are preserved as provenance, while the operational rules below are grounded in related
publicly retrievable material from the same author plus the user's real failure case.

## Verified Amir Mušić principles used

### Direction before acceleration

Amir's public work describes AI as a medium in which faster production makes creative
direction, visual standards and strategic clarity more important, not less. This is the
foundation for the skill's requirement to establish brand evidence and an art-direction
thesis before generation.

Source: https://mushich.com/about/

### Reference-driven design agent workflow

A public Thread Reader archive of Amir's design-agent workflow describes dropping visual
references into the design agent, letting it read those files, and then prompting from
those references. This supports the skill's reference hierarchy and the rule that agents
must inspect actual visual inputs instead of designing from generic prose alone.

Source: https://threadreaderapp.com/user/AmirMushich

### Target audience -> visual tags -> moodboard -> key visuals

Amir's published workflow for campaign development explicitly starts from the concept,
defines an ICP, derives a set of visual tags, builds a curated moodboard, and then uses it
for key visuals. The skill keeps this pattern for *new creative directions*, while adding
a guardrail: moodboards must not replace an existing Brand Kit.

Source: Thread Reader archive above.

### Decode first, then remix

A public prompt-library derived from Amir's 2026 work explains a brand-remix method that
first decodes the brand and then constructs new modules from that visual DNA. The useful
principle is not the named aesthetic itself; it is the separation of brand recognition
rules from new composition.

Source: https://github.com/AgentsORG/naive-design/blob/main/prompts/prompt-library.md

### Authentic logo geometry must remain literal

A public Amir prompt archived by Onlybas explicitly instructs models to preserve the
authentic logo's geometry, proportions, curves, spacing and negative spaces and not
redesign or invent it. This becomes a general no-hallucinated-branding rule in the skill.

Source: https://onlybas.com/ (AmirMušić prompt archive)

## Verified Meng To / Amir gist anti-slop principles used

Amir's public gist summarizing Meng To's anti-AI-slop design guidance includes:

- typography and letter-spacing need deliberate human review;
- real image/site references improve authenticity;
- fonts should be tested rather than accepted blindly;
- generated imagery is a starting point and needs refinement;
- prompting should name brand/product details precisely;
- final human/art-direction choices distinguish finished work from AI output.

Source:
https://gist.github.com/amirmushichge/dd38a549d1ad01308bcb425a8e7aeb98

## What is good but insufficient on its own

The source material is strong as **creative methodology**, but insufficient as a production
skill because it does not, by itself, guarantee:

1. **Brand source authority** — which source wins when Brand Kit, website, old design and
   inspiration conflict.
2. **Asset provenance** — whether a logo/font/color is official, legacy, inferred or copied.
3. **Connected-tool discipline** — inspect Canva/Figma/Drive/Notion/repositories directly
   instead of relying on search-engine images or memory.
4. **No-hallucination enforcement** — explicit prohibition on invented logos, monograms,
   taglines, colors, fonts, features, company/contact data.
5. **Reference role separation** — identity anchor vs layout vs mood vs subject vs production.
6. **Production readiness** — print bleed/safe area, resolution, editable text, export rules.
7. **Brand-specific visual QA** — a result can be beautiful but still wrong for the brand.
8. **Failure recovery** — when a user rejects an output as off-brand, continuing to mutate
   it compounds drift; the workflow must return to source assets.
9. **Copy/data verification** — contact, legal, product and social information should come
   from current authoritative sources, especially for printed collateral.
10. **Acceptance threshold** — no objective minimum gate before calling a design finished.

These gaps are added in `brand-art-direction` rather than treated as optional advice.

## User failure case that shaped the skill

During a TrainMaster.pro business-card task, generation drifted into a generic dark
orange/black sports-tech aesthetic and invented a `TM` monogram despite real TrainMaster
brand assets being available in Canva. A later pass also inferred brand direction from
website/product screenshots instead of first extracting the actual Canva Brand Kit.

This demonstrates the central rule:

> **A category is not a brand, and a screenshot is not a substitute for the Brand Kit when
> the Brand Kit is available.**

The skill therefore makes brand-asset inspection a hard gate before brand-critical
creation.

## Relationship to the existing UI skill pack

The existing UI skills cover product interface design, responsive behavior, accessibility,
components, design tokens and visual QA. `brand-art-direction` deliberately covers a
different surface:

- brand identity application;
- creative direction;
- Canva and marketing collateral;
- paid/social campaign visuals;
- print collateral;
- branded generative imagery;
- asset fidelity and production artwork.

For branded product UI, compose both: use `brand-art-direction` for identity constraints
and the UI skills for interaction/product correctness.
