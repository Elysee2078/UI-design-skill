# Sigma-compatible adapter

Sigma Computing's published agent-skill workflow is repository-based and distributes skills for AI assistants including Codex, Claude Code and Cursor. Its public skills repository uses `AGENTS.md` plus focused skill folders, which makes this repository's structure intentionally compatible with that model.

## Use this repository with Sigma-oriented agent workflows

- Treat root `AGENTS.md` as the routing and safety layer.
- Treat each `skills/<name>/SKILL.md` as an independent capability.
- Copy only the skills relevant to the working repository rather than loading every reference on every task.
- Keep product-specific instructions in the consumer project.

## If the task is specifically building Sigma workbooks

This UI repository is not a replacement for Sigma's own workbook/domain skill. Use Sigma's official current skill for Sigma-specific YAML/API/workbook behavior, and use this repository for general interface reasoning: hierarchy, density, accessible interaction, responsive presentation, design-system coherence and visual QA.

Do not invent Sigma APIs from this repository. Retrieve current Sigma-specific instructions from Sigma's maintained skill source.

## Why the split matters

A domain skill answers “how Sigma works.” This pack answers “how to design and verify the interface well.” Combining the two at runtime is more maintainable than copying Sigma-specific behavior into a generic UI skill that will go stale.
