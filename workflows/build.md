---
description: Build project for specified platform (read build commands from spec/)
---

# Build Workflow

## Steps

1. Read `spec/OVERVIEW.md` to identify target platforms and build commands
2. Determine which platform to build:
   - If user specifies → use that
   - If not → ask user which platform

// turbo
3. Run the build command from spec/ in the project root directory

4. Verify build output:
   - Check exit code = 0
   - Verify output artifact exists
   - Report file size

5. If build fails:
   - Read error output
   - Check relevant skill's `⚠️ 已知陷阱` section
   - Record fix to ERROR_JOURNAL.md if new issue
