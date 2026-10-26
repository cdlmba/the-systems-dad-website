---
name: humanize
description: Edit pass that removes AI writing tells from a draft. Use after drafting anything a human will read (posts, emails, docs, articles). Fixes structure and rhythm first, words last. Trigger on "humanize this", "de-AI this", or before publishing any AI-assisted draft.
---

# Humanize

Make AI-assisted writing read like a person wrote it. If the current repo has its own editorial system (style guides, drafting rules, review gates), that system wins; use this only where no house rules exist. Run this as an EDIT pass on a finished draft, in this order: failures, rhythm, words, reader, speaking. Word swaps alone fix nothing. The tells live in structure.

## 1. Failures (structural tells, the loudest)

Hunt in order of damage:

- Hyper-symmetrical taxonomies (The Pangram / Synthetic Mirror Imprint). Formatting frameworks where every option has the exact same number of sub-bullets, parallel headers, or symmetrical table rows. Humans obsess over one messy friction point for three paragraphs and dismiss the others in one sentence. Introduce deliberate structural asymmetry.
- Predictable narrative scaffolding. The standard 7-beat "Hero's Journey of Productivity" (Object setup -> Specs -> Family pitch -> Concrete timestamp -> Moral self-scolding -> 3-rule fix -> Backyard redemption). Disrupt this template with unresolved tension, unhedged tangents, or incomplete domestic edges.
- Negative parallelism stacks. "It's not X. It's Y." One per piece, as a closer, is fine. Two or more is a robot. Never use the mid-paragraph negative contrast stack ("It wasn't dedication. It was pride"). Replace with direct conversational conjunctions ("I called it dedication, but it was really just pride").
- Self-clapping. "Here's the kicker." "This changes everything." "Let that sink in." Delete. Just say the thing.
- Third-person persona posturing. Never speak about yourself or the brand in the third person ("The Systems Dad does X", "The Lead Architect ensures Y"). Write exclusively in first-person ("I") survivor honesty when recounting failures, or state the principle directly.
- Artificial enthusiasm. Every point lands, every ending uplifts, nothing ever annoys the author. Real people find something mildly irritating in everything they love.
- Recapping. Restating a point two sentences after making it. "In short..." closers that summarize the body. End on the last concrete point instead.
- Signposted transitions. "Let's dive in." "Now let's look at." "Here's where it gets interesting." The next sentence IS the transition.
- Bold-label paragraph openers. "**The problem.** ..." That's documentation voice. Write prose, or use a real heading.
- Colon-and-quote teaser hooks. "Seven words cost my team forty hours: 'We'll see what we can do.'" That is algorithm-auditioning AI scaffolding. Open directly with the physical scene in media res: "A director caught me by the elevators at 4:30 on a Friday."
- Resume motive euphemisms. Explaining bad operational decisions with polite corporate virtues ("I wanted to look helpful and responsive"). Real humans state the unvarnished truth: "I didn't want to say no to his face" or "I liked feeling indispensable."
- Invented concept labels. "I call this the Clarity Flywheel." Naming an ordinary observation to manufacture originality.
- Participial tails. "..., making it a game-changer for modern teams." State the fact. Stop.
- Triads everywhere. "Faster, cheaper, and more scalable." When every list has exactly three items, none of them were counted.

## 2. Rhythm

- Uniform sentence length is the tell, in BOTH directions. All-medium reads as autopilot. All-short staccato reads as an AI told to punch harder.
- **The All-Short Staccato Trap**: Ban vertical broetry ladders where every single sentence is isolated into its own one-line paragraph under 8 words. Real human writing mixes sentence lengths. Group thoughts into natural 2-to-3 sentence paragraphs where a longer thought (15–22 words) is punctuated by a short, blunt punch (4–8 words).
- Budget: one crafted, quotable line per piece, maybe two (usually the closer). If three lines are each auditioning to be the screenshot, two are performance. Flatten them; keep the facts.
- Em dashes: replace with a period, a colon, or parentheses. Not because detectors care (they don't). Because readers have been trained to flinch at them.

## 3. Words (least important; still sweep)

- **Contraction Audit (Mandatory Pass)**: Sweep the draft for missing contractions. If the draft contains "does not", "do not", "did not", "will not", "is not", or "was not", replace them immediately with natural speech: *doesn't, don't, didn't, won't, isn't, wasn't*. Real people speak with contractions; robots avoid them.
- Kill on sight: delve, tapestry, myriad, underscore, seamless, robust, foster, elevate, unlock, "stands as a testament", "it's important to note", "in today's fast-paced world", "navigate the landscape".
- Filler transitions at sentence start: However, Additionally, Furthermore, Moreover, "That said". Usually deletable with zero loss.
- Hedges: facts stated bare, opinions get ONE softener (imo, I think, feels). "Arguably one of the most..." is two hedges on a claim nobody made.
- Do not over-delete into a controlled vocabulary. Scrubbed slop is still slop. Flat, tell-free text is still machine-shaped.

## 4. Reader

- Write to one real person, not an audience. Performing for an imagined crowd is where the AI voice comes from. A message to one colleague never sounds like a keynote.
- The reader is the beneficiary. "I built X" is about you. "I built X, steal this part" is about them. Any sentence that serves your image instead of their outcome gets cut.
- They should walk away owning something: a step to take, a number to reuse, a thing to copy. If the honest answer is "nothing", the problem is not the wording.
- Trust them. Cut any sentence the reader could write themselves after the previous one: spelled-out implications, definitions of familiar terms, "what this means is".
- Specifics beat adjectives. "9 minutes for 1 hour of audio", not "fast". A number, a name, or a date every few sentences. An adjective without one is decoration.
- Stakes early. Who this is for, and why it matters to them, visible in the first two lines.

## 5. Speaking & Delivery (the strongest single fix)

- Read the draft aloud. Rewrite every sentence you would never say to a colleague. Keep contractions. Keep the joins (so, but, and). Keep one genuine reaction if you actually had one.
- **The Messy Audio / SuperGrok Pipeline (The Gold Standard)**: Record a 2–5 minute unedited voice memo or stream-of-consciousness dictation (in SuperGrok or phone notes). Let the raw transcript serve as the un-manufacturable human skeleton. The agent must strictly refine grammar and format your exact points without imposing a synthetic narrative arc or evening out the natural asymmetries.
- **Substack Rich-Text Export Rule**: Substack's composer does not automatically parse raw Markdown tables, blockquotes, or formatting on paste. Whenever producing a Substack essay or companion vault asset, always generate a companion `.html` mirror file in `Social/Drafts/` so the author can open it in a browser, hit Ctrl+A / Ctrl+C, and paste clean rich text directly into Substack.
- Never fake it. No invented anecdotes, no manufactured typos, no performed feelings. Readers punish slop texture. They don't punish honesty about using AI.

## The test

Would a colleague who knows you hear YOUR voice reading it? Structure carries that answer more than words do. Fix the skeleton, then stop. Over-editing toward "clean" produces a different kind of slop.

