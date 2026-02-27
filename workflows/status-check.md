---
description: Quick check of project status including build health, git status, and completion progress
---

# Status Check Workflow

## Steps

// turbo
1. **Git Status**
   - `git status` — any uncommitted changes?
   - `git log -5 --oneline` — recent commits

// turbo
2. **Build Health**
   - Run build commands from spec/ for each platform
   - Report: ✅ pass / ❌ fail for each

3. **Progress Review**
   - Read `spec/DEVELOPMENT.md` for planned vs completed items
   - Read `spec/SCREENS.md` for screen completion status (if applicable)
   - Summarize: X% complete, next priorities

4. **Issues**
   - Check `ERROR_JOURNAL.md` for unresolved issues
   - Check for any un-digested errors (not yet added to skill traps)

5. **Report**
   - Output a structured status summary to the user
