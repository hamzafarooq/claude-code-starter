# PRD: Meeting Notes Summarizer

---

### 1. Problem Statement

Product managers who sit in 5+ meetings a day accumulate messy, unstructured notes that are hard to act on. Turning raw notes into a clean summary with action items is manual, time-consuming, and often skipped entirely. This matters now because PM workloads are increasing and follow-through on meeting commitments is a visible pain point for teams.

---

### 2. Goals

- Reduce time spent cleaning up meeting notes from ~15 minutes to under 1 minute per meeting
- Ensure 100% of action items from a meeting are captured and visible after summarization
- Achieve a task completion rate of 80%+ for first-time users with no onboarding [ASSUMPTION: measured via session analytics]
- Reach 500 active weekly users within 90 days of launch [NEEDS INPUT: is there a growth target?]

---

### 3. Non-Goals

- This tool will NOT store, save, or retrieve past summaries — no history, no accounts
- This tool will NOT integrate with calendar, Notion, Slack, or any external tool (v1)
- This tool will NOT transcribe audio or connect to Zoom/Meet recordings
- This tool will NOT assign action items to specific people or send notifications

---

### 4. Users & Use Cases

**The back-to-back PM**
Sarah runs four syncs before noon. She pastes her raw notes from each into the tool, gets a clean summary and action item list in seconds, and pastes the output into her team's Slack channel — no editing required.

**The first-time attendee**
Marcus joined a stakeholder meeting cold and took scattered notes. He pastes them in, gets a structured summary, and finally understands what was actually decided and what he owns.

**The async collaborator**
Priya wasn't in the meeting but gets the raw notes forwarded. She uses the tool to quickly understand what happened and what needs follow-up, without reading through three pages of stream-of-consciousness text.

---

### 5. User Stories

**Must-have**
- As a PM, I want to paste my raw meeting notes and get a clean summary so that I can share it with my team without editing.
- As a PM, I want action items extracted and listed separately so that I don't miss any follow-ups.
- As a PM, I want the output to be copyable with one click so that I can paste it wherever I need it.

**Should-have**
- As a PM, I want to see who owns each action item if names appear in my notes so that accountability is clear. [ASSUMPTION: the tool infers owner names from note text]
- As a PM, I want the summary to include key decisions made so that I can reference them later.

**Nice-to-have**
- As a PM, I want to choose a summary length (brief vs. detailed) so that I can match the output to my audience.
- As a PM, I want a "copy as Slack message" format option so that posting to my team is instant.

---

### 6. Acceptance Criteria

**"Paste notes and get a summary"**
- Given I am on the homepage, when I paste text into the input area and click "Summarize," then a structured summary appears within 5 seconds
- Given the summary has been generated, when I click "Copy," then the full output is copied to my clipboard and a confirmation message appears

**"Action items are extracted"**
- Given my notes contain phrases like "John will," "we need to," or "action:" followed by a task, when the summary is generated, then those items appear in a dedicated "Action Items" section
- Given my notes contain no clear action items, when the summary is generated, then the Action Items section reads "No action items identified" rather than being blank or hidden

---

### 7. Risks & Assumptions

| Risks | Assumptions |
|---|---|
| LLM output quality varies — garbled input may produce garbled summaries | Users have basic literacy around what "good notes" look like |
| No login means no rate limiting — could be abused or cost-prohibitive at scale | API costs per summarization are low enough to run without a paywall at launch [NEEDS INPUT: what's the cost ceiling?] |
| Users may paste sensitive or confidential meeting content — legal/privacy exposure | Users accept that pasted content is sent to an AI API; no explicit consent flow needed for v1 [NEEDS INPUT: confirm with legal] |
| No save functionality may frustrate users who want to retrieve past summaries | v1 scope is intentionally limited; history is a v2 problem |

---

### 8. Open Questions

1. Which AI API will power the summarization — OpenAI, Claude, or another? Who owns the API key setup? [NEEDS INPUT]
2. Is there a cost ceiling per month before we need rate limiting or a freemium model? [NEEDS INPUT]
3. Does legal need to review the privacy implications of processing meeting notes through a third-party API? [NEEDS INPUT — assign to legal/compliance]
4. What's the target launch date and who is the engineering owner? [NEEDS INPUT]
5. Should the tool support non-English notes in v1? [NEEDS INPUT]

---

### 9. Success Metrics

**Leading indicators (first 2 weeks)**
- % of sessions where user reaches the output screen (target: 70%+)
- Average time from paste to copy (target: under 10 seconds end-to-end)
- Bounce rate on the homepage (target: under 40%)

**Lagging indicators (60-90 days)**
- Weekly active users (target: 500)
- Return usage rate — users who come back more than once [ASSUMPTION: measurable via anonymous session fingerprinting or cookie]
- Qualitative NPS or feedback score from early users [NEEDS INPUT: how will feedback be collected?]

---

Review the **[ASSUMPTION]** and **[NEEDS INPUT]** sections before sharing with engineering.

---

## User Stories

**Story 1:** As a PM, I want to paste my raw meeting notes and receive a structured summary so that I can share it with my team immediately without any editing.

**Acceptance Criteria:**
- Given I land on the homepage, when I paste text into the input area, then the "Summarize" button becomes active
- Given I click "Summarize," when the API processes my notes, then a structured summary appears within 5 seconds
- Given the summary is displayed, when I look at the output, then it is organized into: Summary, Key Decisions, and Action Items sections
- Given my input is empty, when I click "Summarize," then I see an inline message asking me to paste some notes first

**Priority:** Must-have
**Effort:** Large (1 week+)

---

**Story 2:** As a PM, I want action items extracted and listed in their own section so that I never miss a follow-up after a meeting.

**Acceptance Criteria:**
- Given my notes contain clear ownership phrases ("John will," "we need to," "action:"), when the summary is generated, then those tasks appear as a bulleted list under "Action Items"
- Given names appear next to a task in my notes, when action items are displayed, then the owner's name is shown alongside the task
- Given my notes contain no identifiable action items, when the summary is generated, then the Action Items section reads "No action items identified" rather than appearing empty or hidden

**Priority:** Must-have
**Effort:** Medium (2-3 days)

---

**Story 3:** As a PM, I want to copy the full summary with one click so that I can paste it into Slack, email, or Notion without reformatting.

**Acceptance Criteria:**
- Given the summary has been generated, when I click "Copy," then the full output is copied to my clipboard
- Given I click "Copy," when the copy succeeds, then I see a brief confirmation (e.g. "Copied!") that disappears after 2 seconds
- Given my browser does not support clipboard access, when I click "Copy," then the text is selected so I can manually copy it

**Priority:** Must-have
**Effort:** Small (< 1 day)

---

**Story 4:** As a PM, I want to summarize another set of notes without refreshing the page so that I can process multiple meetings back-to-back quickly.

**Acceptance Criteria:**
- Given a summary is displayed, when I click "Start over" or clear the input, then the output area resets and the input is empty and focused
- Given I paste new notes over my previous input and click "Summarize," then the previous output is replaced with the new summary
- Given the new summarization is in progress, when it is loading, then I see a visible loading state so I know it is working

**Priority:** Should-have
**Effort:** Small (< 1 day)

---

**Story 5:** As a PM, I want key decisions from the meeting surfaced in the summary so that I can reference them later without re-reading my notes.

**Acceptance Criteria:**
- Given my notes contain decision language ("we agreed," "decided," "going with"), when the summary is generated, then those decisions appear under a "Key Decisions" section
- Given no clear decisions are present in the notes, when the summary is generated, then "Key Decisions" reads "No decisions recorded" rather than being omitted

**Priority:** Should-have
**Effort:** Small (< 1 day)

---

## Edge Cases to Discuss

- **Very short input** — What happens if someone pastes 3 words? Do we summarize it or show a minimum length warning?
- **Very long notes** — What if someone pastes a 10,000-word transcript? Is there an input character limit, and what happens when it's hit?
- **No names in notes** — Action items exist but no names are mentioned. Do we show the task without an owner, or skip the owner field entirely?
- **Non-English notes** — The PRD leaves this open. Until decided, does the tool attempt to summarize anyway or show an unsupported language message?
- **Sensitive content** — Users may paste confidential notes. Should there be a privacy notice before they submit, even without a formal legal requirement?

---

## Questions for the Team

1. Is there a character limit on input, and if so, what error message does the user see?
2. Which AI API is powering this — Claude, OpenAI, or something else? This affects latency, cost, and output format tuning.
3. Should "Key Decisions" be a separate section or part of the main summary? A product decision is needed before engineering starts.
4. Is there any rate limiting needed at launch, or do we ship open and add it once usage data is available?
5. Who owns the legal review on data privacy before we go live?
