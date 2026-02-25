# Contribution Guidelines

To maintain a clean and organized codebase, please follow these guidelines when contributing to **SmartBiz-Insight**.

## 1. Branching Strategy

- **main**: The stable version of the project. Do not commit directly to `main` unless it's a small documentation fix.
- **feature/[task-name]**: Create a new branch for every major feature or member-specific task.
  - Example: `feature/sbi-lstm-model` or `feature/eda-plots`.

## 2. Commit Messages

Keep commit messages concise and descriptive:
- `Setup: Install tensorflow and keras`
- `Feature: Add correlation matrix script`
- `Docs: Update checklist with Week 2 progress`

## 3. Code Standards

- Follow PEP 8 for Python code.
- Add comments to complex logic, especially LSTM layer configurations.
- Ensure all datasets are kept in the `data/` folder and not committed if they are too large (use `.gitignore`).

## 4. Pull Requests (PRs)

Before merging into `main`:
1. Ensure the code runs without errors.
2. Update the [CHECKLIST.md](CHECKLIST.md) to mark your task as complete.
3. Ask a teammate to review your code (via Live Share or PR comments).

---
*Happy Collaborating!*
