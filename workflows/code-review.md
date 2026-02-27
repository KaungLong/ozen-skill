---
description: Code review checklist for pull requests and changes
---

# Code Review Workflow

## Steps

1. **Architecture Check**
   - Dependency direction correct? (`presentation → domain ← data`)
   - No domain layer coupling to frameworks?
   - New dependencies compatible with all target platforms? (check spec/)

2. **Code Quality**
   - Follow coding-standards skill
   - No hardcoded values that should be in config/spec
   - Error handling present for all IO operations
   - No memory leaks (unsubscribed listeners, unclosed resources)

3. **Cross-Platform**
   - `expect` declarations have ALL `actual` implementations?
   - Platform-specific code in correct source set?
   - No platform-specific imports in shared layer?

4. **UI (if applicable)**
   - Design system tokens used consistently? (check spec/)
   - All states handled? (loading, empty, error, content)
   - Accessibility IDs on interactive elements?

5. **Testing**
   - Core business logic has unit tests?
   - Edge cases covered?

6. **Skill Traps**
   - Check `⚠️ 已知陷阱` in relevant skills
   - No known trap patterns in the code?
