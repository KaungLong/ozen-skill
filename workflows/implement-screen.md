---
description: Standard operating procedure for implementing a new screen in the app
---

# Implement Screen Workflow

## Steps

1. **Read spec/**
   - Read `spec/SCREENS.md` for the target screen's UI spec
   - Read `spec/OVERVIEW.md` for design system tokens
   - Load relevant skills (navigation, UI framework, DI)

2. **Design Review**
   - Confirm all UI elements, interactions, and navigation targets
   - Identify required data from ViewModel

3. **Create ViewModel** (if needed)
   - Define UI state data class
   - Implement state management with StateFlow
   - Inject dependencies via DI framework (check DI skill)

4. **Create Screen Composable / View**
   - Follow design system tokens from spec/
   - Use screen template pattern from UI skill
   - Implement all states: loading, content, empty, error

5. **Wire Navigation**
   - Add route config (check navigation skill)
   - Register in navigation component's child factory
   - Connect callbacks to navigation actions

6. **Register in DI**
   - Add ViewModel to DI module (check DI skill)

7. **Verify**
   // turbo
   - Build for all platforms
   - Verify screen renders correctly
   - Test navigation to and from the screen

8. **Update spec/**
   - Mark screen as completed in spec/SCREENS.md or spec/DEVELOPMENT.md
