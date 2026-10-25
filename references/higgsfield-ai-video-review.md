# Higgsfield AI skills — video integration review (2026-10-25)

**Primary source:** [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills), MIT, © 2026 Higgsfield AI. **Reviewed upstream files:** `README.md`, `LICENSE`, `INSTALL_FOR_AGENTS.md`, `setup`, `higgsfield-generate/SKILL.md`, `higgsfield-video-explainer/SKILL.md`, `higgsfield-youtube-thumbnail/SKILL.md`, `higgsfield-soul-id/SKILL.md`, `higgsfield-brandkit/SKILL.md`. Current reviewed skill version: **0.13.0** on default branch when fetched. This is a **reference integration**; none of the external package scripts are copied or executed.

## What the source provides

Upstream is eight main Markdown agent skills: `higgsfield-generate`, `higgsfield-soul-id`, `higgsfield-product-photoshoot`, `higgsfield-brandkit`, `higgsfield-marketplace-cards`, `higgsfield-websites`, `higgsfield-video-explainer`, and `higgsfield-youtube-thumbnail`. The `generate` skill provides generic generation, Marketing Studio for branded UGC/ad modes, and Virality Predictor finished-video scoring (`brain_activity`). The `video-explainer` skill is a specific **non-photoreal, one-to-ten-minute** audio/video assembly process built from 10-second blocks; it is **not** a general-purpose short-form reel generator. `soul-id` trains an identity reference from 5–20 face images, on an eligible paid plan. `brandkit` can develop or apply brand material, but for our projects must remain subordinate to existing brand identity.

### Fit to our video pipeline

| Stage | Higgsfield contribution | Internal/fallback production |
|---|---|---|
| Insight/educational outline | Model could assist, but **our editorial brief remains source of truth** | Notion Content Pipeline, evidence/claim ledger |
| Hook/script | UGC How-to/presenter support in Marketing Studio | Authored/approved VO, captions, audience proof |
| Identity & scene | `soul-id` and reference-based generation where consented | User-shot B-roll and approved characters/imagery |
| B-roll/clip | `generate` with video models or Marketing Studio | Existing video, Canva scenes, editor-built animation |
| Narrated non-photoreal explainer | `video-explainer` | Existing voice audio + scenes + FFmpeg/Canva |
| On-brand cover | `youtube-thumbnail` with official refs | Deterministic typography and original logo |
| Actual app tutorial | **Higgsfield must not invent product UI** | Real privacy-safe TrainMaster screen capture |
| Final film/audio | `video-explainer` only for its compatible workflow | Canva/CapCut or FFmpeg/Remotion; timing follows existing MP3 |
| Quality scoring | Virality Predictor as optional review *proxy* | Human hook/content assessment; retention verified after publication |
| Distribution/metrics | No proven native end-to-end channel publishing in reviewed skills | Human approval, scheduler connector, published URL, analytics |

### Provenance and known risks

1. License: Upstream `LICENSE` is MIT; retain notice for any future direct copy. This adapter contains **original integration guidance and links**, not pasted upstream scripts. Higgsfield services/models are third-party and may be subject to separate plans, credit pricing and commercial/biometric/media data terms.
2. **Bootstrapping risk:** Upstream skill instructions can attempt shell install via `curl ... | sh`; `INSTALL_FOR_AGENTS.md` asks for global CLI install, account login and a paid test generation. These steps are **not safe implicit consequences** of linking/installing skill Markdown. Do not execute them automatically.
3. **Auth/data boundary:** `higgsfield auth login` requires the account owner's participation; never commit tokens, face/voice training datasets, private athlete data or media URLs that expose credentials.
4. **Spend:** jobs consume external credits; preset model names/pricing change. Require live `model get` and `generate cost` (where supported), a declared credit budget and an explicit approval before any billable generation or Virality Predictor submission. Never silently retry a paid request.
5. **Output quality:** generated logo/text/UI can hallucinate. Existing design system and authentic app capture outrank generated output. Keep titles, logos, product UI and subtitles in deterministic editable layers.
6. **Identity/rights:** explicit consent before training a likeness or voice; verify licenses for soundtrack, presenter assets, imagery and use of existing social clips. Soul ID training is optional; never a precondition for basic video production.
7. **Feature/version drift:** Upstream `higgsfield-generate/SKILL.md` mentions `seedance_2_5` while other pages may list different defaults; use fresh live model discovery and schema; do not hardcode provider availability.
8. **No universal auto-video:** Upstream is a set of provider workflows. A fully autonomous process still requires content orchestration, brand/proof locks, product UI capture, safe audio, continuity checks, approvals, exports, schedulers and measurements.

## Proposed future architecture

```text
Notion approved brief + source evidence + brand lock
   -> narrative/storyboard + claim gate + asset manifest
   -> choose provider mode [none | Higgsfield | other approved]
   -> real UI capture + optional licensed AI clip generation
   -> voice or supplied MP3 -> timed cuts -> editable titles -> captions
   -> rendered variants (9:16/4:5/16:9) + automated QA + human review
   -> approved distribution action -> native post URLs -> performance/learning
```

An `assets.json` / `render-manifest.json` should track `content_id`, `script_revision`, `brand_asset_refs`, `product_build_sha`, `media_sources`, `model/params`, `credit_cost`, `voice_license`, `approval`, `render_urls`, `published_urls`, `qc_evidence`. Never store secrets or private face-training photos in the public repository.

## Adoption roadmap

**P0 — now:** add provider-neutral video orchestrator and optional Higgsfield adapter to UI Design Skill router and bundle/manifest; require no account or paid service. Test standalone readme/skill lint and Lovable bundle output.

**P1 — supervised pilot:** one TrainMaster educational video using approved script, real UI capture and brand V2. Use generated B-roll only if budget, auth, content and identity rights have been approved. Compare edit-time/quality against Canva-only workflow; record all artifacts and costs.

**P2 — deterministic video builder:** machine-readable storyboard and safe-area presets, local audio-aligned timeline, FFmpeg/Remotion renderer, captions, brand QA, previews and source provenance.

**P3 — review-aware semi-autonomous system:** job queue, provider fallback, retries within approved budget, human approval gates, authorized publishing, link and analytics verification. Full unattended automatic release is **not** enabled.

## Provider setup handoff (optional; user action required)

Official docs: [installation](https://github.com/higgsfield-ai/skills/blob/main/INSTALL.md), [README](https://github.com/higgsfield-ai/skills/blob/main/README.md), [CLI help](https://higgsfield.ai/CLI). Install skill pack in the *agent host* only after review and permission (official command `npx skills add higgsfield-ai/skills`). Separately authorize Higgsfield CLI installation and browser OAuth `higgsfield auth login`. This UI repo alone does not install the CLI, make generations or authenticate with Higgsfield.

The reviewed upstream `higgsfield-generate` blob SHA was `67189d84a99432c6429ecfa8b9c02b8571a90624`; `higgsfield-video-explainer` blob SHA `8f50a15dda4a9c8a448d4ccbd1cdc1267ed65b2b`. Recheck at execution time to avoid stale instructions.
