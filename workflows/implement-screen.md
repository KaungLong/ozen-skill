---
description: Standard operating procedure for implementing a new screen in the app
---

# Implement Screen Workflow

## Steps

1. **Read spec/**
   - Read `spec/SCREENS.md` for the target screen's UI spec
   - Read `spec/OVERVIEW.md` for design system tokens
   - Read `spec/TECH_SPEC.md` for UI framework, state management, and DI patterns
   - Load relevant skills (navigation, UI framework, DI)

2. **Design Review**
   - Confirm all UI elements, interactions, and navigation targets
   - Identify required data from the state management layer (ViewModel / Store / Reducer — per TECH_SPEC)

3. **Create State Management** (if needed)
   - Define UI state model
   - Implement state management following the project's pattern (查 spec/TECH_SPEC.md)
   - Inject dependencies via the project's DI mechanism (check DI skill)

4. **Create Screen / View**
   - Follow design system tokens from spec/
   - Use screen template pattern from UI skill
   - Implement all states: loading, content, empty, error

5. **Wire Navigation**
   - Add route config (check navigation skill)
   - Register in navigation component
   - Connect callbacks / actions to navigation

6. **Register in DI** (if applicable)
   - Add state management component to DI module (check DI skill)

7. **Verify**
   // turbo
   - Build for target platform(s)
   - Verify screen renders correctly
   - Test navigation to and from the screen

8. **Update spec/**
   - Mark screen as completed in spec/SCREENS.md or spec/DEVELOPMENT.md
