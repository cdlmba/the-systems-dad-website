---
name: design-inspiration
description: Generates daily visual inspiration by pulling from curated design websites and color palettes.
---

# Daily Design Inspiration Generation

When the user asks for daily design inspiration (or as part of a scheduled daily task), follow these steps:

1. **Gather Curated Design Screenshots:**
   - Spawn a `browser_subagent` with the task: "Go to http://craftwork.design/curated/websites. Scroll down slightly to view the grid of curated websites. Take a screenshot capturing the top 2-3 featured website thumbnails to capture their aesthetic."
   - Save the screenshot to the artifacts directory.

2. **Gather Color Palette:**
   - Spawn a `browser_subagent` with the task: "Go to http://chromatic.colorion.co. Find a vibrant or high-contrast color palette on the home page. Extract the exact hex codes for that palette. You do not need to take a screenshot, just return the hex codes."
   - *Note: You can also try using `read_url_content` for this if it's faster and the site doesn't require JS rendering.*

3. **Format the Inspiration:**
   - Look for today's Daily Log in the workspace (e.g., `Social/daily-log/YYYY-MM-DD.md`). 
   - If it exists, append a new section at the bottom called `## 🎨 Daily Design Inspiration`.
   - If it doesn't exist, create a new artifact named `design_inspiration_[DATE].md`.
   - Include the extracted color palettes (formatted clearly with hex codes).
   - Embed the screenshot(s) taken by the browser subagent using the correct absolute path markdown syntax.

4. **Present to User:**
   - Summarize the pulled assets briefly in your response.
   - Provide a clickable link to the updated Daily Log or artifact so the user can review it.
