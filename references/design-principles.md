# Evidence-first interface principles

## 1. Product truth before visual taste

A strong interface makes the product's real jobs, information and consequences legible. Start from users, flows, data, content and constraints. A visual trend is not a requirement.

## 2. Hierarchy before decoration

Establish what must be noticed first, what can wait and what belongs together. Use type, spacing, alignment, contrast and placement before introducing shadows, gradients or animation.

## 3. Reduce arbitrary choices

Every repeated visual decision should become a token or component rule. A coherent system with fewer values usually looks more deliberate than a page with more visual effects.

## 4. Design every state

A component is not only its ideal populated screenshot. Account for loading, empty, long content, errors, partial permissions, disabled actions, destructive confirmation, success, keyboard focus, hover and touch.

## 5. Reuse interaction conventions

Novel interaction has a comprehension cost. Use familiar patterns for standard jobs. Spend novelty where it improves the product's distinctive value, not on checkboxes and navigation.

## 6. Density follows task frequency

Marketing pages can breathe. Operational software often needs efficient information density. Do not force the same card-heavy, oversized pattern language onto both.

## 7. Motion explains change

Good motion communicates where something came from, what changed, or whether an action succeeded. Keep common interaction transitions brief; use springs where physical continuity helps. Honor `prefers-reduced-motion`.

## 8. Accessibility improves the interaction model

Semantic controls, labels, visible focus, robust keyboard navigation and sufficient target size are not post-processing. They expose whether the interaction design is actually coherent.

## 9. Responsive means recomposition

Do not only shrink desktop. Re-prioritize, reflow, collapse, wrap, scroll or progressively disclose based on available space and task importance.

## 10. Validate against failure modes

Ask what would make the interface fail: long translations, empty datasets, slow requests, one-handed mobile use, keyboard-only use, zoom, stale permissions, 1000 table rows, destructive mistakes, or ambiguous status. Test the high-risk cases.

## Review questions

Before calling a UI complete:

- Can a first-time user identify the primary action without explanation?
- Are repeated patterns visibly and behaviorally consistent?
- Are there raw visual values that should be semantic tokens?
- Is any text or icon doing decorative rather than communicative work?
- Does the layout survive long content and narrow widths?
- Can all important actions be completed without a mouse?
- Are error and empty states useful rather than dead ends?
- Does motion help understanding or merely advertise itself?
- Did a new dependency solve a measurable implementation problem?
- Was the result actually tested rather than inferred from code?
