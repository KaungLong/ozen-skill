---
name: sandbox-runner
description: Sets up and runs a temporary Docker container to execute untrusted or risky commands iteratively without breaking the host environment.
triggers:
  - run in sandbox
  - blind execute
  - test in container
---

# Sandbox Runner Skill 🐳

When an Agent (specifically the Sandbox Engineer) requires an isolated environment to run risky commands, blindly update core libraries, or test massive unverified codebase rewrites, trigger this skill.

## 📦 Protocol Workflow

### Step 1: Initialize the Sandbox Volume
Never mount the live `src/` directory directly if you intend to execute destructive commands (like `rm -rf`).
Instead, conceptualize a sandbox:
1. Create a temporary clone on the host: `cp -r /path/to/project /tmp/ozen-sandbox-project`
2. Run tools like Git clone or raw `cp` to ensure you have a disposable copy.

### Step 2: Spin up the Container
Use a generic image (like Node, Python, or Ubuntu) that matches the project's requirements. Keep it running in the background.
```bash
docker run -d --name ozen-sandbox-v1 -v /tmp/ozen-sandbox-project:/app -w /app node:20 tail -f /dev/null
```

### Step 3: Execute Blind Refactor
Connect to the running container and run your commands. Since the environment is ephemeral and isolated, you can confidently run potentially risky installation or formatting scripts:
```bash
docker exec ozen-sandbox-v1 bash -c "npm install && npm run build --force"
```
Or edit files inside the mounted `/tmp/ozen-sandbox-project` volume directly using standard tools, knowing it's safely disposable.

### Step 4: Extract the Value
If your blind execution and refactoring inside the container succeeds and the tests pass:
1. Examine the modified files in the `/tmp/ozen-sandbox-project` volume.
2. Generate a `patch.diff` or write a minimal `distilled_solution.md` to pass back to the main thread.
*(Do not copy gigabytes of node_modules back. Extract ONLY the code changes).*

### Step 5: Clean up (Destroy)
Kill the container and wipe the temporary volume to prevent workspace pollution:
```bash
docker rm -f ozen-sandbox-v1
rm -rf /tmp/ozen-sandbox-project
```

Pass the distilled patch context back to the main Architect or Engineer to apply cleanly to the real repository.
