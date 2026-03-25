---
name: app-store-screenshots
description: Scaffold a Next.js environment to dynamically generate, design, and export App Store ready advertising screenshots with localized copy and RTL support.
triggers:
  - build app store screenshots
  - generate marketing assets
  - export ios screenshots
---

# App Store Screenshots Skill 📸

When requested to create App Store screenshots, use this skill to dynamically scaffold an interactive framework that renders Apple-compliant marketing assets.

## 📦 Protocol Workflow

### Step 1: Install the External AI Capability
This skill relies on a high-level `npx` plugin built specifically for Agentic usage. To activate the generator, run the following in your terminal:
```bash
npx skills add ParthJadhav/app-store-screenshots
```
*(If the user is using Claude Code, Cursor, or Windsurf, this will automatically install the tool into their environment.)*

### Step 2: Information Gathering
Before starting the generation process, ensure you have extracted or asked for the following parameters from the `spec/` or the Product Manager:
- **Brand Colors**: (Primary, Accent, Background)
- **App Features**: (What are the top 3-5 selling points?)
- **Target Locales**: (e.g., `en`, `zh-TW`, `ar`)
- **Theme Direction**: (Clean, Bold, Dark Mode, Editorial)

### Step 3: Scaffold and Generate
Once the tool is installed, prompt the tool to begin building the marketing assets. 
The tool will scaffold a minimal Next.js application that renders the advertisements using a pre-measured iPhone `mockup.png` asset.

```bash
# Example invocation (if triggering manually or delegating via CLI)
npx create-app-store-screenshots@latest ./marketing-assets
```
*(Rely on the installed skill's internal prompts to guide you through the scaffolding).*

### Step 4: Validate Export Matrix
You must verify that the tool successfully exported PNG files in the `./public/screenshots/<locale>/` directory, strictly adhering to the App Store dimension requirements:
- 6.9-inch (Pro Max)
- 6.5-inch 
- 6.3-inch
- 6.1-inch

### Step 5: (Optional) Background Rendering
If the matrix is large (multiple languages), move the export rendering process to the background using traditional bash background control (`&` or `tmux`), and inform the user that the Marketing Designer is generating the assets concurrently.
