# Cross-agent compatibility

Zede-Zero has one source of truth:
`zede-zero-learning-roadmap/SKILL.md`. Platform files only route an agent to
that file; they do not contain a second copy of the workflow.

## Compatibility levels

| Level | Agents | How it works |
|---|---|---|
| Native Skill | Codex, Claude Code, Gemini CLI, OpenCode, GitHub Copilot | Install the canonical Skill folder in a supported Skill directory. The agent discovers its name and description and loads the body when relevant. |
| Repository router | Codex and other `AGENTS.md` readers, Claude Code, Gemini CLI, Cursor, Cline, Windsurf, OpenCode, GitHub Copilot | Clone or download this repository and open its root as the workspace. The thin router tells the agent when to load the canonical Skill. |
| Universal fallback | Any agent that can read attached files or repository files | Attach or expose the canonical Skill folder, then use `adapters/universal-prompt.md`. |

Compatibility means the workflow can be loaded. It does not mean every product
uses the same invocation symbol, automatically grants tools, or supports file
writes and web research in the same way.

## Native installation

From the repository root, preview the destinations:

```bash
python scripts/install_cross_agent.py --target all-native
```

Install after reviewing the preview:

```bash
python scripts/install_cross_agent.py --target all-native --apply
```

Available targets:

| Target | Destination | Covers |
|---|---|---|
| `codex` | `~/.codex/skills/zede-zero-learning-roadmap` | Codex |
| `claude` | `~/.claude/skills/zede-zero-learning-roadmap` | Claude Code |
| `shared` | `~/.agents/skills/zede-zero-learning-roadmap` | Gemini CLI, OpenCode, GitHub Copilot, and other tools that support the shared Agent Skills location |
| `all-native` | all three destinations | All native targets above |

The installer refuses to overwrite a different existing copy. Rename or remove
the old copy after reviewing it, then run the installer again.

## Invocation by product

- Codex: `$zede-zero-learning-roadmap ...` or a matching natural-language request.
- Claude Code: `/zede-zero-learning-roadmap ...` or a matching request.
- Gemini CLI: ask it to use the `zede-zero-learning-roadmap` Skill; approve
  activation when prompted.
- OpenCode: `/zede-zero-learning-roadmap ...` when slash exposure is available,
  or ask it to use the Skill.
- GitHub Copilot: ask it to use the `zede-zero-learning-roadmap` Skill.
- Cursor: open this repository and mention
  `@zede-zero-learning-roadmap`, or make a matching request if the rule is
  available to the agent.
- Cline and Windsurf: open this repository and ask for a learning roadmap; their
  `AGENTS.md` support supplies the router.
- Other agents: attach the canonical folder and paste the universal prompt.

If a product disables Skills, custom instructions, file access, or web access,
the user must enable that capability or use the universal fallback. No
repository can override a host product's permissions.

## Download formats

- The GitHub repository or its source archive contains source, tests, routers,
  documentation, and the installer.
- `zede-zero-learning-roadmap-skill.zip` contains only the installable canonical
  Skill. Use it for products that accept a Skill upload, including eligible
  ChatGPT Skill surfaces.

The Skill ZIP is a release/download artifact, not a second source tree. Changes
are made in the repository, validated, and then packaged into the ZIP.
