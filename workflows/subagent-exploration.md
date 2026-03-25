---
description: How to safely branch out conversations and explorations using Subagents
---
# Subagent Exploration Protocol (Context Forking)

This workflow dictates how Ozen Team agents should handle situations that require significant exploration, risky logic testing, or when hitting a roadblock in problem-solving. This strategy heavily utilizes **Context Compression** to protect the main AI thread from being polluted by failed attempts.

## 🚨 When to use this workflow:
- ❌ **Debugging Dead End**: When you've tried 2-3 different solutions for a bug and none of them worked.
- 🚧 **Risky Refactor**: When you are about to attempt a complex library mock or rewrite and are unsure if it will break the test suite.
- 🗑️ **Context Pollution**: When your current reasoning history is getting filled with error logs and trial-and-error noise.

## 🔄 The Subagent Operating Procedure

1. **Stop & Assess (OODA - Orient)** 
   DO NOT continue modifying the core project files in a panic cycle. Stop immediately. Revert the project back to the last stable commit or state.

2. **Branch the AI Thread (Fork / Subagent)**
   - **If your IDE supports native session forking** (e.g., Claude Code's `/fork` or `/dx:half-clone`): Fork the session from *before* you started the failed attempts. Let the new forked "Subagent" handle the risky debug.
   - **If you are in a standard workspace**: Conceptualize a branch. Create an isolated scratchpad file (e.g., `/tmp/exploration-test.ts`) instead of modifying production files. 

3. **Explore in Isolation (Sandbox Test)**
   - If the task is extremely dangerous (e.g., recursive file deletion or heavy package updates), consider passing the task to the `sandbox-engineer` role to run within a Docker container.
   - Let the Subagent (or your current thread acting as one) figure out the exact root cause by rewriting, breaking, and testing the isolated components.

4. **Strategic Compaction (Distill the Win)**
   Once the Subagent finds the correct solution, **DO NOT copy the entire thought process**. 
   - Extract **ONLY** the exact, victorious code changes and a 1-sentence explanation of *why* it works.
   - Write this to a markdown file: `distilled_solution.md`.

5. **Merge Back to Main Reality**
   - The original "Architect" or "Engineer" reads `distilled_solution.md`.
   - Apply the clean, working diff to the main codebase.
   - Delete all temporary scratchpads (`/tmp/*`) and `distilled_solution.md`.

> **Goal**: Treat your AI context window like RAM. Trial-and-error operations cause memory leaks. Dump the memory, spawn a sub-process, and only return the distilled binary result.
