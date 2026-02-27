---
description: Release process for all platforms
---

# Release Workflow

## Steps

1. **Pre-release Check**
   - All builds pass? (run build workflow for each platform)
   - No Blocker or Critical bugs?
   - Changelog prepared?
   - Version number updated?

2. **Build Release Artifacts**
   - Read `spec/OVERVIEW.md` for platform targets
   - For each platform: run production build command from spec/
   - Verify each artifact

3. **Per-platform Release**
   - **Mobile (Android)**: Upload to Play Console (internal/beta/production)
   - **Mobile (iOS)**: Upload to App Store Connect via Xcode/Transporter
   - **Web**: Deploy to hosting (Netlify, Vercel, Firebase Hosting, etc.)

4. **Post-release**
   - Tag git commit with version
   - Update spec/DEVELOPMENT.md with release record
   - Notify stakeholders
