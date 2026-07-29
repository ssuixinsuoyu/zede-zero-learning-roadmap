# Zede-Zero

> Start from zero. Keep converging toward truth.

[简体中文](README.md) | **English**

A portable, goal-driven Agent Skill that turns a learning objective into an evidence-based, executable, verifiable, and continuously adjustable roadmap.

Zede-Zero does not merely generate course lists or attempt to cover an entire subject. It clarifies the real outcome, diagnoses the learner's starting point, confirms constraints and acceptance criteria, and works backward from the desired result to design the required capabilities, concrete content, practical tasks, feedback sources, and delayed retests.

Its central principle is simple:

> Do not collect knowledge for its own sake. Learn with a goal, act early, and absorb knowledge through building, creating, solving, explaining, and responding to real feedback.

Current version: `v1.0.0`

## Highlights

- Explains the complete user-facing rules on first use.
- Asks one high-impact question at a time instead of sending a long questionnaire.
- Separates verified facts, user claims, inferences, working assumptions, and unknowns while continuing whenever missing information does not change a key decision.
- Uses a lightweight first-principles gate to identify the real outcome, success evidence, key variables, irreducible capabilities, assumptions, and minimum validation loop.
- Expands academic and technical goals into concrete concepts, subskills, project modules, edge cases, exercises, and tests while pruning content that does not block the goal.
- Starts with a minimal representative task, learns only the blocker, applies it immediately, and digests knowledge through projects, problems, explanations, writing, or real experiments.
- Controls stage-level cognitive load, prioritizes evidenced bottlenecks instead of applying a mechanical 80/20 split, and uses deliberate or interleaved practice only when their conditions are met.
- Fast-passes already-clear exam and technical-project goals instead of forcing abstract discussion.
- Uses evidence-based diagnostics before deciding the starting level.
- Requires explicit confirmation of the goal card before building the roadmap.
- Identifies the goal type before selecting diagnostics, evidence, practice, and acceptance criteria.
- Selects official sources by direct relevance instead of collecting every official document.
- Stops research once additional material no longer changes scope, ordering, resources, or acceptance decisions.
- Can use high-star GitHub projects as candidate signals while checking maintenance, releases, documentation, tests, license, issues, security, and compatibility.
- Offers layered and full roadmap output modes.
- Reserves time for review and schedule buffers.
- Adds stage-level acceptance thresholds, remediation actions, and risk signals.
- Distinguishes guided imitation, independent reproduction, variation, real-world transfer, and boundary explanation instead of treating tutorial completion as mastery.
- Selects the strongest accessible feedback appropriate to the goal and lowers confidence when stronger evidence is unavailable.
- Uses goal-sensitive 7/30/90-day delayed retests without silently exceeding the current time budget.
- Verifies the roadmap before presenting it.
- Blocks only on decision-changing gaps and names the affected decision instead of using vague uncertainty as a reason to avoid progress.
- Replans from real progress without discarding completed milestones.
- Compares planned versus actual time, completion, acceptance, blockers, resource usefulness, and estimate drift at checkpoints.
- Restores legacy, schema v1, and schema v2 roadmaps through a versioned progress protocol.
- Resolves conflicting sources by applicability and authority instead of silently merging them.
- Separates controllable capabilities from external business, hiring, or income outcomes.
- Adds qualification and supervision boundaries for regulated or real-world high-risk goals without blocking general knowledge study.
- Changes the installed Skill only when the user explicitly requests a persistent improvement.
- Keeps one canonical `SKILL.md` while providing native installation, repository
  routers, and a universal prompt fallback for cross-agent use.

## Workflow

`Rules → clarify → first principles → classify → diagnose → confirm → choose output → research → feasibility → plan → transfer/feedback/retest design → verify → save with consent → iterate`

The Skill plans and replans learning. It does not provide lesson-by-lesson tutoring. When the user moves into tutoring, it can produce a tool-neutral handoff card containing the confirmed goal, current stage, next task, acceptance criteria, and known gaps.

## Learning Effectiveness Loop

For each critical capability, the Skill chooses the level of transfer the goal actually requires, the strongest accessible feedback source, and an appropriate delayed-retest schedule:

- Transfer progresses from guided imitation to independent reproduction, variation, real-world use, and boundary explanation.
- Feedback progresses from self-check to objective checks, peers, experts, and real environments.
- Durable skills normally use 7-day independent recall, 30-day variation, and 90-day real transfer; exam and exploration goals use adapted schedules instead of mechanically applying all three.

Retests before the deadline count inside the plan budget. Post-goal maintenance is shown separately. A failed delayed retest triggers focused remediation, not an automatic restart of the whole stage.

## Learning Method Selection

The roadmap selects learning methods instead of stacking every popular method:

- Cognitive-load control is applied at the stage level by limiting simultaneous
  novelty, respecting prerequisites, and recombining modules into a complete
  transfer task.
- Bottlenecks are prioritized by goal impact, evidenced gap, task frequency,
  and downstream unlock value. The 80/20 idea is a heuristic, never a fixed
  deletion ratio.
- Practice is called deliberate only when it targets an evidenced weak
  subskill with suitable difficulty, a clear standard, timely feedback,
  targeted correction, and a retry.
- Interleaving starts only after related single skills are stable and the goal
  requires choosing between confusable methods or situations.

The Skill plans when and why to use these methods, their feedback, and their
acceptance evidence. It does not generate lesson-by-lesson prompts, hints, or
live corrections.

## Goal-Driven Content Depth

The roadmap must contain the actual content needed for the confirmed outcome, not only broad labels such as “learn the basics”:

- Technical projects map project modules, inputs, outputs, constraints, required language or tool knowledge, implementation tasks, edge cases, and tests.
- Exams, languages, theory, and other academic goals expand the concrete knowledge and skills required by the applicable syllabus, task, or assessment.
- Language roadmaps use goal-relevant comprehensible input, active retrieval, meaningful output, corrective feedback, transfer, and delayed retesting instead of defaulting to isolated word lists, grammar order, or passive media time.
- Business, creator, and exploration goals stay lean: they include only the knowledge needed for the current deliverable or experiment and give more space to real output and feedback.

Layered mode fully expands the current stage and preserves key content mappings for later stages. Full mode expands every stage. Neither mode turns the roadmap into a comprehensive subject survey unless comprehensive mastery is itself the confirmed goal.

The Skill does not treat collecting resources, watching lessons, or taking notes as progress by itself. Every planned input must lead to a near-term artifact or acceptance check. Necessary theory remains in scope when it directly determines the quality of the goal, but it is absorbed through solving, explaining, building, writing, or experimenting.

## First-Principles Gate

Before diagnosing the learner, the Skill checks whether the stated learning topic is the real goal or only a tool, course, certificate, or popular label. When needed, it clarifies one question at a time:

- the observable outcome and evidence of success
- the variables that actually determine the result
- capabilities and constraints that cannot be bypassed
- assumptions that still need validation
- the smallest action-output-feedback-revision loop
- related material that does not currently block the result

Clear exam targets with a current official scope and clear technical projects with an input/output contract and acceptance examples are summarized and fast-passed. The gate must not become a generic philosophy lesson.

## Output Modes

- **Layered (`layered`)**: complete evidence, timing, acceptance, and roadmap overview; detailed current stage and first week; compact later stages.
- **Full (`full`)**: all stages expanded with topics, prerequisites, practice, outputs, resources, estimates, acceptance thresholds, and remediation. Daily planning still stops after the first week.

The Skill asks which mode to use after the goal card is confirmed. Both modes preserve the same quality and safety requirements.

## Evidence Policy

Every selected source must directly support the goal scope, applicable version or region, required capability, acceptance standard, or operating constraint. Roadmaps use four evidence levels:

1. Current official standards, syllabi, or specifications
2. Official documentation, tutorials, samples, and product material
3. Professional, academic, job-task, or other primary evidence
4. Textbooks, courses, and supplementary learning resources

Official but irrelevant material is explicitly excluded. When official evidence is incomplete, lower-level evidence may fill the gap only with a clear label and confidence level.

For technical or open-source goals, GitHub stars are only a discovery signal. A repository is selected only after checking direct relevance, maintenance and release activity, documentation and tests, license, issue and security status, and version compatibility. Community repositories never override current official specifications.

## Saved Roadmap Compatibility

Saved roadmaps use schema v2. The Skill can read legacy files without frontmatter and schema v1 files, but migrates them only after the user approves the next write. Unknown future schema versions are never overwritten or silently downgraded. Every create, update, or migration requires fresh user consent.

## Cross-agent compatibility

The project does not claim that every AI product understands the same command.
Instead, it provides three honest compatibility levels:

1. **Native Skill** for Codex, Claude Code, Gemini CLI, OpenCode, and GitHub
   Copilot.
2. **Repository router** for agents that read `AGENTS.md`, `CLAUDE.md`,
   `GEMINI.md`, or Cursor project rules.
3. **Universal prompt fallback** for any agent that can read attached or local
   files.

All routes load the same canonical
`zede-zero-learning-roadmap/SKILL.md`; platform adapters do not duplicate the
workflow. See
[Cross-agent compatibility](docs/cross-agent-compatibility.md) for the support
matrix, invocation differences, and limitations.

## Installation

Clone the published repository:

```bash
git clone https://github.com/ssuixinsuoyu/zede-zero-learning-roadmap.git
```

Preview native installation for all supported Skill hosts:

```bash
python scripts/install_cross_agent.py --target all-native
```

After checking the destinations, install:

```bash
python scripts/install_cross_agent.py --target all-native --apply
```

The three native destinations are:

- Codex: `~/.codex/skills/zede-zero-learning-roadmap`
- Claude Code: `~/.claude/skills/zede-zero-learning-roadmap`
- Shared Agent Skills: `~/.agents/skills/zede-zero-learning-roadmap` for Gemini
  CLI, OpenCode, GitHub Copilot, and compatible hosts

The installer previews by default and refuses to overwrite a different existing
copy. To use the Skill without global installation, open the downloaded
repository as the agent's workspace and make a matching request.

Codex invocation:

```text
$zede-zero-learning-roadmap I want to build a Python automation tool within three months and can invest eight hours per week.
```

Claude Code uses `/zede-zero-learning-roadmap`. Other native hosts can activate
the Skill by name or from a matching natural-language request. Agents without
native Skill discovery can use
[`adapters/universal-prompt.md`](adapters/universal-prompt.md).

## Common Uses

```text
$zede-zero-learning-roadmap Help me plan a career transition into data analysis.
$zede-zero-learning-roadmap Replan this saved roadmap using my actual progress from this week.
$zede-zero-learning-roadmap Make this planning rule a permanent, reusable Skill improvement.
```

## Privacy and Feedback

- The Skill does not create progress files unless the user agrees.
- Saved learning records belong in `learning-roadmaps/`, which is ignored by Git.
- Ordinary feedback changes only the current roadmap.
- Personal data, private learning material, credentials, and one-off preferences must not be written into the reusable Skill.

## Repository Layout

```text
.
├── .cursor/rules/zede-zero-learning-roadmap.mdc
├── .github/workflows/validate.yml
├── adapters/universal-prompt.md
├── docs/cross-agent-compatibility.md
├── evals/
│   ├── cases.json
│   └── judge-schema.json
├── scripts/
│   ├── check_contract.py
│   ├── install_cross_agent.py
│   └── run_forward_evals.py
├── AGENTS.md
├── CLAUDE.md
├── GEMINI.md
├── README.md
├── README.en.md
├── LICENSE
└── zede-zero-learning-roadmap/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── planning-patterns.md
        └── progress-protocol.md
```

## Local Validation

Run the behavior-contract checks before packaging or publishing:

```bash
python scripts/check_contract.py
```

The cases cover first-use onboarding, first-principles clarification and fast-pass behavior, goal confirmation, all goal types, evidence-based diagnostics, layered/full output, source relevance and freshness, transfer evidence, feedback quality, delayed retesting, high-risk boundaries, saved-route compatibility, feedback safety, and replanning.

Run isolated model-based forward evaluations with the locally authenticated Codex CLI:

```bash
python scripts/run_forward_evals.py --dry-run
python scripts/run_forward_evals.py --case first-use-complete-input
python scripts/run_forward_evals.py --severity hard
```

Each case runs against an isolated copy of the installable Skill. The tested agent does not receive expected answers; a separate structured judge checks required and forbidden behavior. Raw responses and summaries are written under `evals/runs/`, which is ignored by Git.

If the configured model is newer than the installed Codex CLI, upgrade the CLI or pass a compatible model explicitly, for example `--model gpt-5.4`. On Windows the runner resolves the native `codex.exe` automatically so Chinese prompts do not pass through a legacy batch-file code page.

## Anonymous Examples

```text
$zede-zero-learning-roadmap I want to prepare for a certification exam, but I have not chosen the exam date yet.
$zede-zero-learning-roadmap I want to automate local spreadsheet processing with Python and can invest six hours per week.
$zede-zero-learning-roadmap I want to explore whether data analysis is a suitable direction for me.
$zede-zero-learning-roadmap Restore progress from this schema v1 roadmap without writing any files yet.
```

## Contributing

Issues and pull requests are welcome. Keep proposed rules general, reusable, and free of personal or private content. Behavior changes should preserve the goal-confirmation, optional-save, verification, and feedback-safety contracts.

## License

[MIT](LICENSE)

