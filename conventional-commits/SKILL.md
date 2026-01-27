---
name: conventional-commits
description: Help create git commits and PRs following the Conventional Commits (Angular) standard. Use this skill when the user asks to create a commit, needs help writing a commit message, or is preparing a pull request description.
---

# Conventional Commits Assistant

Generate standardized commit messages (Angular convention).

## Standard Format

```text
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

## Workflow

1.  **Analyze**: Run `git diff --staged` to see changes.
2.  **Draft**: Create message using the types below.
3.  **Confirm**: Show full message to user before committing.

## Types

| Type | Intention | Example |
| :--- | :--- | :--- |
| **feat** | New feature | `feat(auth): add google login` |
| **fix** | Bug fix | `fix(nav): correct back button` |
| **docs** | Documentation | `docs: update api guide` |
| **style** | Formatting (no code change) | `style: fix indentation` |
| **refactor** | Code restructuring | `refactor(core): simplify state` |
| **perf** | Performance | `perf(list): use virtualization` |
| **test** | Tests | `test(api): add unit tests` |
| **chore** | Build/Tools | `chore: update deps` |
| **revert** | Revert commit | `revert: feat(auth): ...` |

## Rules

*   **Subject**: Imperative mood ("add" not "added"), no period, lowercase.
*   **Body**: Explain *what* and *why* (wrap at 72 chars).
*   **Footer**: `issue #123` or `BREAKING CHANGE: ...`.
