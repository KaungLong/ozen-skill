---
name: async-researcher
description: Delegates long-running search, web crawling, or background analysis tasks to an asynchronous sub-process (like Gemini CLI or background tmux) without blocking the main AI thread.
triggers:
  - run background research
  - async search
  - background task
---

# Async Researcher Skill 🕵️‍♂️ (Background Minions)

When you need to crawl multiple sites, summarize a massive codebase, or ask another LLM to do something that takes time, you should **NOT block the main conversational thread**. Instead, delegate it to the background using this skill.

## 🎯 When to use this skill:
- You need to crawl the web for the latest API documentation of a framework.
- You need to run a heavy `grep` or `find` across an entire mono-repo.
- You want to use an alternative model (e.g., Gemini CLI) as a fallback when a site blocks Claude's crawler.

## 🔁 Operating Procedure

1. **Write the Task Prompt (Delegation)**
   Write down exactly what the 'minion' needs to find or research in a temporary file: `/tmp/ozen-research-prompt.md`.

2. **Execute in Background (Fire and Forget)**
   Use basic background operators (`&`) or `nohup` to run the shell command in the background, redirecting the output to a results file.
   *Example using Gemini CLI (if available) or a generic Python crawler:*
   ```bash
   (gemini query "$(cat /tmp/ozen-research-prompt.md)" > /tmp/ozen-research-results.md) &
   ```
   *Example for a long-running find/grep:*
   ```bash
   (find /src -type f -name "*.ts" -exec grep -l "TODO" {} \; > /tmp/ozen-todos.txt) &
   ```

3. **Continue Main Work (Concurrency)**
   **Crucial Step:** Do not wait (`wait`) or poll immediately for the command to finish. Immediately proceed to answer the user or write code for other independent components. State that "The research has been dispatched to the background."

4. **Poll (Exponential Backoff)**
   Check back later in the conversation using a simple command to see if the file is populated or if the process has finished:
   ```bash
   cat /tmp/ozen-research-results.md
   ```
   Once the results are in, read them and incorporate the knowledge into the main project. Delete the temporary files.
