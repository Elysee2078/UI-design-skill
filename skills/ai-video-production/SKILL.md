---
name: ai-video-production
description: Use when planning, producing, auditing or repurposing educational videos, reels, tutorials, UGC-style spots, product demos, explainers, thumbnails or captions, with or without AI video providers.
---

# AI Video Production — evidence-first, brand-locked

This is the **provider-independent** production skill. Read the root `SKILL.md` and `skills/brand-art-direction/SKILL.md` first for any branded video; read `skills/higgsfield-video-integration/SKILL.md` only when Higgsfield is requested, connected and appropriate. Never require a paid provider to create a video that can be composed from approved stills, human footage, real UI recordings, an existing MP3 and an editor such as Canva or FFmpeg.

## Output and scope

Before producing, confirm the requested artifact: concept, standalone voiceover, storyboards/cards/PNG, clips, editable Canva components, final MP4, subtitles, cover, or publication package. Do not render a video if the user explicitly wants only static cards or intends to assemble in Canva. Do not create or publish extra formats without a user request or an existing production brief.

### Production pipeline

`brief -> fact + brand evidence -> learning objective -> hook/script -> scene map -> source footage/assets -> narration -> assembly -> accessibility/safe-area/privacy QA -> human approval -> channel export -> optionally schedule/publish with a separately authorised tool`

1. **Source & audience:** Read the primary Notion/content brief, approved script, product/version source, audience, language and platform; identify one audience job-to-be-done, one teachable outcome and whether this is an ad or education.
2. **Claims ledger:** Every feature, pricing, model capability, screenshot, performance promise, health claim or statistic must be verified against current primary evidence. A code path is not proof of a working live production flow. Use conditional narration or omit unverified features.
3. **Brand lock:** Use official brand palette, actual fonts, official logo, approved templates and design tokens. Existing official brand evidence outranks generated style. Never re-create a real logo with a generator. Keep third-party brands and actual people permissioned.
4. **Script:** Capture attention through a specific coach/athlete problem, provide practical steps and a human payoff. Separate **voiceover text** (spoken, natural) from **on-screen copy** (minimal keywords). Never put a narrated paragraph on one slide.
5. **Storyboard:** Each scene records beat, seconds, spoken text, visible text, source asset type, real demonstration or AI allowed, callout/safe area, transition and test.
6. **Media:** Use user-approved images, official branding and authentic UI screen recordings. Generate only supporting human/B-roll/stylised assets when needed; do not fabricate application workflows, screenshots, training outcomes or customer testimonials.
7. **Identity:** If using presenter/avatar, obtain permission, provenance and usage rights. For any real person's likeness, explicit rights/consent; a fictional actor must not be represented as a real coach or customer.
8. **Audio:** Prefer the supplied recorded MP3 if it already exists; verify duration. Any new synthesis, voice cloning or music needs a license and approval. Never clone a real voice without explicit permission. Match cut duration to actual waveform instead of assuming word counts.
9. **Assembly:** Maintain 9:16 1080×1920 for TikTok/Reels/Shorts by default where relevant; keep captions in platform safe area; coherent sequence, readable type, adequate image dwell time, distinct layouts, no forced header/footer. Check 16:9 or 4:5 only when requested. Canva-editable cards and captions are separate from generated media footage.
10. **Verification:** Brand fidelity, exact copy, product truth, privacy frame check, rights, spelling, captions against audio, no cropped controls/faces/text, safe audio levels, mobile legibility and clip continuity. Mark evidence `verified | inferred | blocked`.
11. **Release:** The social content pipeline's date is a *planning* date, not a native scheduler booking. Human approval and observed upload/permalink are necessary before marking the item published.

## Scene spec (example)

```yaml
scene_id: "coach-video-library-03"
learning_goal: "turn one workout clip into reusable exercise instructions"
audience: "independent sports coaches"
format: "9:16"
duration_s: 6
voiceover: "Give it a clear name and two coaching cues."
onscreen: "1 EXERCISE / 2 COACHING CUES"
visual_source: "authentic product capture"
provider: "none"
brand_assets: "official only"
claims: ["exercise_library_and_instructions"]
proof_status: "requires live UI capture"
privacy_review: "pending"
release_status: "draft"
```

## TrainMaster reference case

One episode = one real trainer pain point. For **turning workout videos into an exercise library**, show a real own-exercise record with an external video link and coaching cues, then a verified client workout-plan action. An AI Coach plan suggestion must be live-tested and reviewed by the trainer. Do not claim raw social videos are automatically imported, that a clip converts to a plan in one click or that platform payments are fee-free. Pricing and link-in-bio sales belong to another episode if educational clarity would suffer. Community/SportsFam posts should reward belonging, access, trust and useful coaching; avoid generic calendar opportunism.

## Future automation / gates

- **Stage 1**: Assisted manual creation — Notion draft → script/cards/VO options → user assembles in Canva → manual QA.
- **Stage 2**: Deterministic engine — storyboard schema, reusable templates, licensed assets, FFmpeg/Remotion timeline render, SRT/VTT, review contact sheet, versioned exports.
- **Stage 3**: Optional provider jobs — Higgsfield/other generative clips behind explicit budget and consent gates, with recorded parameters/job IDs and reversible outputs.
- **Stage 4**: Review-aware orchestration — refreshed product capture, job provenance, automated visual/privacy checks, approval, scheduler connector with per-channel publication confirmation. Never auto-publish on the strength of a successful render.

Every job should be idempotent by content ID + script revision + brand revision + product build + provider config, with artifacts and a short manifest. Respect vendor rate limits and avoid silent retries of billable jobs. External provider jobs and upload of private media require explicit cost and data-transfer authorisation. `No provider` is a valid and often preferable production mode.

## Deliverables / QA report

Deliver requested assets; editable text/captions if available; media manifest (provider, model, prompt hash, source/license, brand lock, resolution, date); proof gaps; and next manual approval. Do not claim an MP4, Canva design, scheduled post or media link exists without verifying it.

Read also `references/higgsfield-ai-video-review.md` when using that provider.
