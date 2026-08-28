---
name: motion-and-microinteractions
description: Use when adding or auditing transitions, microinteractions, spring motion, disclosure animation, drag feedback, list changes, loading feedback, or other interface motion.
---

# Motion and Microinteractions

Motion must explain state, continuity, causality or feedback. If it does none of those, remove it.

## Priority order

1. Immediate interaction feedback.
2. State transition/continuity.
3. Spatial relationship between origin and destination.
4. Hierarchy/attention for genuinely new information.
5. Decorative motion only when it supports brand and does not interfere with tasks.

## Baseline

- Keep frequent UI transitions brief; many hover/focus/press transitions should feel effectively immediate and commonly fit below roughly 200ms.
- Use modest scale changes; large zooms make controls feel unstable.
- Prefer transform/opacity over layout-triggering animation when possible.
- Pause or avoid looping animation when offscreen.
- Never require hover to reveal a critical action on touch-relevant interfaces.
- Respect `prefers-reduced-motion`; reduced mode should preserve state communication without unnecessary movement.

## Sources

Use Kinetics for spring/microinteraction pattern research and Motion Primitives when an existing React project benefits from reusable primitives. Verify current APIs and licenses before copying. Do not add a motion dependency for a one-line CSS transition.

## Review

For every animation ask:

- What changed?
- Does motion make the change easier to understand?
- Is the duration proportional to interaction frequency?
- Can users continue working while it runs?
- Does reduced-motion mode remain understandable?
- Does the animation preserve focus and accessibility semantics?

Test rapid repeated actions, interrupted transitions and low-performance conditions where relevant.
