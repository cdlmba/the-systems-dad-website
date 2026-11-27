# 02. Four Copy-Paste Workflows for Real Work

AI can start the job, but a person still has to finish it.

Each setup below handles the slow prep work that usually eats forty-five minutes of your afternoon, then hands you a short brief you can check in five minutes before you send the message or pick up the phone. Run these inside a Project or workspace that already has your `AGENTS.md` file loaded.

---

## Workflow 1: Messy Notes or Chat Threads to Written Owners

**When to use it:** Right after a wandering call, or on Monday morning when thirty Slack or email replies piled up over a long weekend.  
**What you paste in:** Raw call transcript, rough bullet notes, or a copied chat thread.

### Copy-Paste Prompt
```text
Read the raw notes below. Do not write a polite summary paragraph.

Pull out only two things:

1. Decisions actually made (quote or state what was agreed, and who agreed to it).
2. Open tasks. Put these in a simple table with four columns:
   - Task (plain verb first, under 12 words)
   - Owner (one person's name, or [NEEDS OWNER] if nobody claimed it)
   - Date (exact date, or [NEEDS DATE] if none was stated)
   - Blocker or open question

After the table, give me a 4-line plain-text note I can paste into chat so the people with [NEEDS OWNER] or [NEEDS DATE] reply before 3:00 PM.

RAW NOTES:
[Paste transcript, notes, or thread here]
```

**Your 3-minute human check:** Delete any side chatter that isn't a real task, verify the names, and post the 4-line note yourself.

---

## Workflow 2: Plan, Quote, or Paperwork Red-Line Check

**When to use it:** Before walking into a project review, signing a vendor quote, or reading through a stack of contract disclosures.  
**What you paste in:** Draft plan, statement of work, proposal, or disclosure PDF.

### Copy-Paste Prompt
```text
Read the document below like a skeptical operator who has to live with this plan when things go sideways next month.

Skip compliments. List only:

1. Missing dates or vague handoffs (where two people will assume the other person owns the step).
2. Unstated costs, exclusions, or "buyer/client is responsible for..." lines buried in the text.
3. Assumptions that only hold if nothing goes wrong on the ground (weather, shipping, approvals, physical access, staffing).
4. Five blunt, plain-English questions I should ask on a 5-minute phone call before I agree to this.

DOCUMENT:
[Paste document or upload PDF]
```

**Your 5-minute human check:** Cross off anything you already know from real life on the ground, keep the two or three sharpest questions, and make the call.

---

## Workflow 3: Vendor & Options Side-by-Side Brief

**When to use it:** When a work or personal project (moving, hiring a contractor, comparing three tools, booking inspections) needs hours of tedious comparison prep.  
**What you paste in:** Your hard rules, your target date, and the links, quotes, or vendor names you are comparing.

### Copy-Paste Prompt
```text
I am comparing options for: [State the job in one line, e.g., booking movers from NC to Missouri by Dec 1].

My hard rules that cannot move:
- Target date: [Date]
- Budget or physical constraint: [e.g., narrow country driveway, max $X, must include Y]
- Dealbreakers: [List 1-2 dealbreakers]

Using the vendor info / quotes below (or searching current listings if web search is on):
1. Build a side-by-side comparison table showing Price, Availability against my date, What's Included, What's Extra, and Phone Number.
2. Flag any option that breaks my hard rules right away so I stop wasting time on it.
3. Write a 3-question phone script for the top two contenders so I can confirm the details with a real person in five minutes.

VENDOR INFO / QUOTES:
[Paste quotes, emails, or vendor names]
```

**Your 5-minute human check:** Check the physical reality AI cannot see (driveway clearance, local reputation, gut feel on the phone), then pick up the phone and close the loop yourself.

---

## Workflow 4: The 4:50 Open-Loop Capture

**When to use it:** At 4:50 PM when your head is still spinning with half-finished tasks and you don't want work following you to the dinner table.  
**What you paste in:** A messy 2-minute voice dictation or brain-dump of everything still nagging you, plus tomorrow's open calendar windows.

### Copy-Paste Prompt
```text
It is the end of my workday. Below is a raw dump of everything still open in my head, plus my open calendar windows tomorrow.

1. Pick the ONE task that matters most tomorrow morning before I open email or chat, and slot it into my first open 60-minute window.
2. Group the rest into two buckets:
   - Needs a 30-minute calendar block tomorrow or Thursday (tell me which slot).
   - Noise that can wait or get a 1-sentence "I'll look at this Friday" reply.
3. Give me any 1-sentence replies I should send in the next three minutes before I shut my laptop lid.

OPEN LOOPS IN MY HEAD:
[Paste brain-dump or voice transcript]

TOMORROW'S OPEN WINDOWS:
[e.g., 8:15-9:30 AM, 1:30-2:30 PM]
```

**Your 3-minute human check:** Put those two blocks onto tomorrow's actual calendar as meetings with yourself, send the 1-line note if needed, and shut the laptop.

---

*The Systems Dad · thesystemsdad.com*
