---
name: systems-dad-prompt-vault
description: A collection of high-leverage prompts for Microsoft Copilot and Google Gemini, optimized for the "Systems Dad" workflow.
---

# Systems Dad Prompt Vault (Copilot & Gemini Edition)

## 1. The High-Stakes Week Ahead Reviewer
**Name/ID**: `systems-dad-weekly-prep`
**Description**: Analyzes the upcoming calendar to isolate critical meetings and prep requirements.

### For Microsoft Copilot (M365)
```markdown
Scan my Outlook calendar for the upcoming week. Identify the 3 most important meetings based on the participants and descriptions. 

For each, tell me:
1. The primary goal of the meeting.
2. What specific prep (emails, files, or data) I need to review.
3. Suggest a "Systems Dad" approach to keep the meeting focused on high-growth decisions.
```

### For Google Gemini (@Google Workspace)
```markdown
@Google Calendar, show me my meetings for the upcoming week. 

Identify the most critical sessions and for each:
1. Define the specific outcome we need to achieve.
2. @Gmail, find any recent related threads that I should review for context.
3. Create a short checklist of prep items I need to complete to be 100% ready.
```

**Configuration**: Model: Copilot/Gemini | Temp: 0.4
**Notes**: Best run on Sunday evenings or Monday mornings to align the system for the week.

---

## 2. The "Loose Ends" & Missed Opportunity Audit
**Name/ID**: `systems-dad-loose-ends`
**Description**: Catch dropped balls and identify moments to improve systems before the weekend shutdown.

### For Microsoft Copilot (M365)
```markdown
Review my sent emails and Teams messages from this week. 

Identify:
1. "Waiting For": People I need to follow up with who haven't replied.
2. "Loose Ends": Small tasks I mentioned I would do but haven't finished.
3. "System Upgrade": Identify one task I did manually this week that could be automated or templated next week.
```

### For Google Gemini (@Google Workspace)
```markdown
@Gmail and @Google Drive, summarize my main activities and communications from the last 5 days.

1. List any follow-ups I owe based on recent emails.
2. Identify internal/family open loops that haven't been resolved.
3. Suggest one "Systems Dad" automation I can set up to prevent a recurring headache from this week.
```

**Configuration**: Model: Copilot/Gemini | Temp: 0.6
**Notes**: Part of the "Friday Shutdown Ritual."

---

## 3. The Time-Buyback (Delegation/Async) Filter
**Name/ID**: `systems-dad-time-buyback`
**Description**: Filters upcoming meetings to reclaim time for deep work and family.

### For Microsoft Copilot (M365)
```markdown
Look at my Outlook calendar for next week. 

Find meetings where:
1. I am not the organizer and there are more than 5 participants.
2. The topic could be handled via a Teams status update or email thread.
Draft a polite message for each suggesting we handle it asynchronously to buy back time for deep work.
```

### For Google Gemini (@Google Workspace)
```markdown
@Google Calendar, analyze my meetings for next week. 

1. Identify sessions that are likely "status updates" rather than "active decision-making."
2. For those sessions, suggest how I can delegate my attendance or move them to a shared Google Doc for async updates.
3. Goal: Reclaim 3 hours of my schedule for deep strategic thinking and family time.
```

**Configuration**: Model: Copilot/Gemini | Temp: 0.2
**Notes**: Run this 48 hours before the start of the week.

---

## 4. The Weekly Retro (Mental Reset & Systems Fix)
**Name/ID**: `systems-dad-weekly-retro`
**Description**: Conducts a final Friday scan to close open loops, celebrate wins, and architect a better system for next week.

### For Microsoft Copilot (M365)
```markdown
Review my sent emails, Teams chats, and calendar from the last 5 days. 

Execute the **Weekly Retro** protocol:
1. **The Wins**: Identify 3 strategic moves I made this week that created leverage. 
2. **The Logic Gaps**: Find where the system failed or where I hit recurring friction.
3. **The Architecture Fix**: Suggest one operational change (a prompt, a checklist, or a sync) to prevent that friction next week.
4. **The Shutdown**: Identify any tasks I can delegate or delay until Monday so I can fully disconnect for the weekend.
```

### For Google Gemini (@Google Workspace)
```markdown
@Gmail, @Google Calendar, and @Google Drive: Summarize my week. 

Run the **Weekly Retro** sync:
1. **Wins & Leverage**: What were my 3 biggest accomplishments? How did they buy back time?
2. **The Residue Audit**: Where did I lose my margin this week? (e.g., manual work or meetings).
3. **Systems Move**: Suggest one "Systems Dad" automation or template to build on Monday.
4. **Weekend Hand-Off**: List any unresolved tasks I should move to my **Information Hub** for next week so I can reach a "Shutdown State" today.
```

**Configuration**: Model: Copilot/Gemini | Temp: 0.6
**Notes**: Run this every Friday afternoon before signing out to ensure maximum presence for your family.

---

## 5. The Weekly Content Architect
**Name/ID**: `systems-dad-content-multiplier`
**Description**: Generates a 6-day platform-optimized content schedule (LinkedIn vs. X).

### For Microsoft Copilot / Google Gemini
```markdown
Analyze my calendar and recent documents for this week. 

Execute the **Weekly Content Architect** protocol:
1. **The LinkedIn Slant (PM/AI)**: Identify exactly 3 strategic wins or processes I managed this week. Turn them into vertical, scroll-optimized posts about leadership, AI adoption, or Program Management (intended for Mon/Wed/Fri).
2. **The X Slant (Home Side)**: Identify 3 moments where a workflow or system saved my family time. Turn them into punchy, vertical posts about the "Home API," presence, or dad-life logistics.
3. **The Format**: Use the "Systems Dad" mobile-first formatting: one thought per line, double line breaks, and scroll-stopping hooks.

Draft a Monday-Saturday posting schedule.
```

**Configuration**: Model: Copilot/Gemini | Temp: 0.7
**Notes**: Run this on Sunday evening to align the system for the week.
