# Zede Plan Learning Roadmap（学习路线规划）

A goal-driven Codex Skill that turns a learning objective into an evidence-based, executable, verifiable, and continuously adjustable roadmap.

一个目标驱动的 Codex Skill：先澄清目标与诊断基础，再生成有依据、可执行、可验收、可持续调整的学习路线。

## Highlights

- Explains the complete user-facing rules on first use.
- Asks one high-impact question at a time instead of sending a long questionnaire.
- Uses evidence-based diagnostics before deciding the starting level.
- Requires explicit confirmation of the goal card before building the roadmap.
- Researches authoritative competency sources and current learning resources.
- Reserves time for review and schedule buffers.
- Verifies the roadmap before presenting it.
- Replans from real progress without discarding completed milestones.
- Changes the installed Skill only when the user explicitly requests a persistent improvement.

## Workflow

`Rules → clarify → diagnose → confirm → research → plan → verify → iterate`

The Skill plans and replans learning. It does not provide lesson-by-lesson tutoring; use a dedicated interactive tutoring Skill for that purpose.

## Installation

Clone the repository:

```bash
git clone https://github.com/ssuixinsuoyu/zede-plan-learning-roadmap.git
```

Copy the inner `zede-plan-learning-roadmap` directory into your Codex Skills directory:

- Windows: `%USERPROFILE%\.codex\skills\zede-plan-learning-roadmap`
- macOS/Linux: `~/.codex/skills/zede-plan-learning-roadmap`

Start a new Codex task, then invoke:

```text
$zede-plan-learning-roadmap 我想在三个月内学会 Python，每周可以投入 8 小时。
```

## Common Uses

```text
$zede-plan-learning-roadmap 帮我制定数据分析转行路线。
$zede-plan-learning-roadmap 根据这份已保存的路线和本周进度重新安排。
$zede-plan-learning-roadmap 把这条路线规划反馈永久写进 Skill。
```

## Privacy and Feedback

- The Skill does not create progress files unless the user agrees.
- Saved learning records belong in `learning-roadmaps/`, which is ignored by Git.
- Ordinary feedback changes only the current roadmap.
- Personal data, private learning material, credentials, and one-off preferences must not be written into the reusable Skill.

## Repository Layout

```text
.
├── README.md
├── LICENSE
└── zede-plan-learning-roadmap/
    ├── SKILL.md
    └── agents/
        └── openai.yaml
```

## Contributing

Issues and pull requests are welcome. Keep proposed rules general, reusable, and free of personal or private content. Behavior changes should preserve the goal-confirmation, optional-save, verification, and feedback-safety contracts.

## License

[MIT](LICENSE)
