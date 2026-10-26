---
name: daily-retro
description: Generates a comprehensive retrospective of all activity from the previous day.
---

# Daily Retrospective Generation

When the user asks to write up a retro for yesterday's activity, follow these steps:

1. **Gather Activity Data:**
   - Run `git log --since="yesterday.midnight" --until="today.midnight" --oneline` to review code changes.
   - Look at recently modified files in the workspace.
   - Review recent agent conversation summaries and transcripts (if needed) for the past 24 hours to recall complex debugging or planning sessions.

2. **Format the Retro:**
   - Create an artifact named `daily_retro_[DATE].md`.
   - Organize the artifact using the following structure:
     - **Summary:** A high-level overview of the main objectives tackled.
     - **Completed Work:** Bullet points of specific tasks finished and code merged.
     - **Challenges/Blockers:** Any issues encountered or workarounds used.
     - **Next Steps:** Open loops to tackle today.

3. **Present to User:**
   - Summarize the artifact briefly and ask the user if they'd like to add any personal notes or updates to it before finalizing.
