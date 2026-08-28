# Generic agent adapter

This repository intentionally avoids relying on one vendor's proprietary skill format.

For an agent that can read repository instructions but does not natively understand Skills:

1. Load `AGENTS.md` as persistent repository guidance.
2. Load `SKILL.md` when the task concerns UI/product frontend work.
3. Load only the focused `skills/*/SKILL.md` files needed by the task.
4. Give the agent `references/source-catalog.md` before it installs or copies third-party UI code.
5. Expose live MCP sources when the runtime supports MCP.

## Minimal system prompt bridge

Use a short pointer rather than pasting the whole repository into a prompt:

```text
For UI/frontend tasks, follow this repository's AGENTS.md and SKILL.md. Route to the smallest relevant skills/*/SKILL.md file. Treat references/source-catalog.md as the license and source-selection policy. Verify external component APIs from current docs/MCP before implementation.
```

## Tool-aware behavior

If the runtime lacks browser rendering, accessibility tooling or MCP, the skill should report those verification gaps. It must not convert unavailable tests into claims of success.
