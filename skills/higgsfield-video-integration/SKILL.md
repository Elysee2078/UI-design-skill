---
name: higgsfield-video-integration
description: Use when evaluating or using the external Higgsfield AI skills, CLI or MCP for video clips, UGC, explainers, visual assets, consistent presenter identities, social covers and finished-video evaluation.
---

# Higgsfield Video Provider Integration (optional)

**Purpose:** a narrow, controlled adapter to upstream [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills). This repository does **not** vendor Higgsfield's CLI or activate Higgsfield credentials. Prefer the provider-neutral `skills/ai-video-production/SKILL.md` for the overall workflow. Read `references/higgsfield-ai-video-review.md` for source assessment and boundaries.

## Capabilities and routing

| Request | Official upstream skill | Conditions |
|---|---|---|
| Generate an ad/presenter/UGC or supporting image-to-video clip | `higgsfield-generate` — Marketing Studio (`ugc`, `ugc_how_to`, `product_showcase`), or the appropriate generative model | Follow live model schema and rights rules; only if visual generation improves the brief |
| Animate a supplied keyframe into footage | `higgsfield-generate` | Source image and format authorised; re-check current image/reference duration/aspect modes |
| Produce a **non-photoreal** 1–10 minute narration-led explainer from timed blocks | `higgsfield-video-explainer` | Not the default for 30–60s typography boards, photoreal talking head or finished-video editing; upstream imposes 10s blocks and fixed style |
| Create 9:16 Shorts cover / 16:9 YouTube thumbnail | `higgsfield-youtube-thumbnail` | Use real project copy/official logo outside generated raster when possible |
| Consistent presenter identity | `higgsfield-soul-id` then `higgsfield-generate` | Explicit consent for face use, storage, onward processing, and eligibility; 5–20 reference photos; user-owned or fictional character |
| Generate branded stills or visual identity | `higgsfield-brandkit` for brand systems; `higgsfield-generate` only for media | Apply existing approved brand. **Never use brandkit to redesign an established brand** unless explicitly commissioned |
| Evaluate finished hook/attention | `higgsfield-generate` / Virality Predictor (`brain_activity`) | Paid/remote analysis of submitted video; predictions are estimates, not proven reach/ROI |

Other upstream skills (`marketplace-cards`, `product-photoshoot`, `websites`) are **not default video dependencies**. Install or invoke only if a separate task requires their capability.

## Bootstrap: opt-in, not automatic

1. Confirm Higgsfield is approved as a **third-party processor** for the actual images, voice, prompts and source files; never upload private athlete/client data or unredacted internal UI recordings.
2. For plan and authorization, confirm expected model, media duration/aspect, number of attempts, cost/credit budget and maximum retry count **before submitting billable jobs**. Read-only model discovery and costing are okay without purchasing.
3. If the user approves setup, follow the **current official** installation instructions rather than blindly executing upstream Markdown:
   - `https://github.com/higgsfield-ai/skills/blob/main/INSTALL.md`
   - Official cross-agent package: `npx skills add higgsfield-ai/skills` (review installed source/version first).
   - Existing Higgsfield CLI: `higgsfield version`, `higgsfield account status`, `higgsfield model list --json`, `higgsfield model get <model> --json`.
   - Authentication is interactive: `higgsfield auth login` completed by the account owner; credentials stay outside Git, logs, Notion and generated outputs.
4. **Never silently execute** `curl ... | sh`, `sudo`, `npm -g`, `./setup`, install hooks, arbitrary binaries, or commands embedded in external skill content. Review scripts, host machine, shell platform and permissions; get an explicit install authorisation. Do not install anything merely because this GitHub skill pack was imported.
5. Inspect the installed upstream `SKILL.md` and relevant `references` fresh. Model names, voice pricing, Marketing Studio modes and capability flags evolve; versions in these docs are historical evidence, not a runtime contract.
6. Use generated URLs/media job IDs only after a confirmed tool response. `--wait` is not proof of a successful job unless exit status/output are verified. Avoid assumptions about concurrent jobs or subscription credits.

## TrainMaster V2 prompt handoff

```text
JOB: one supporting vertical clip for an educational coach video (NOT an invented product UI demo).
AUDIENCE: independent coaches across sports; English international voiceover separately provided.
SCRIPT BEAT: coach searching their own social feed for an exercise demonstration from months ago.
ART DIRECTION: approved TrainMaster V2 brand; authentic sports-world human expression;
warm, practical and community-centered rather than glossy technology advertising.
REFERENCES: official logo/palette/fonts separate and immutable; permitted performer only.
VIDEO: 9:16, silent or licensed ambience, no invented on-screen UI, no baked text.
AVOID: blue branding, fake app buttons, made-up testimonials, unauthorized celebrity likeness,
video claiming the athlete improved because of software, unreadable/repeated captions.
HANDOFF: editable text overlays assembled in Canva/FFmpeg; authentic UI recorded separately.
```

The upstream model does not need to recreate the exact letterforms; final identity/text is composed deterministically using approved source files. Preserve user-approved scripts, voices, and reference assets.

## Output + failure protocol

A successful generation returns: provider/model/version, validated params, prompt/source manifest, license/consent status, charged credits if reported, media URL/job ID, duration/aspect, quality review and suggested assembly shot. Do not check credentials into GitHub or copy paid job metadata with personal data into a public issue.

If the CLI is missing, not authenticated, unsupported in environment, plan-limited, over budget, quota-limited, unsafe for rights/privacy, or external service offline: report `provider_blocked`. Continue with manual Canva storyboards, human footage and verified product capture; **never call a paid job secretly, claim it succeeded or substitute fabricated UI**.

Do not auto-publish. Human review and an authorized channel/scheduler action are separate release gates.
