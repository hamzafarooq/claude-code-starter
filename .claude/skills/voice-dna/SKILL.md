---
name: voice-dna
description: Analyze writing samples and extract the patterns that define the user's voice. Use when the user wants to capture their writing style, train Claude on how they write, or make future writing sound like them.
---

Ask the user to paste 3–5 samples of their writing (emails, posts, articles, anything they've written).

Analyze the samples and produce:

## Voice DNA: [Name]

### Tone
One sentence describing the overall register (e.g. "Direct and slightly irreverent — sounds like a senior colleague, not a textbook").

### Sentence patterns
- Average length: [short / medium / long]
- Structure tendencies: [e.g. "leads with the point, explains after" or "builds to the punchline"]
- Punctuation style: [e.g. "uses em-dashes, avoids semicolons"]

### Vocabulary fingerprint
- Words/phrases you use often: [list 5–8]
- Words/phrases you never use: [list 3–5]
- Formality level: [1–5, where 1 = casual text, 5 = legal brief]

### What makes it yours
3 specific stylistic moves that show up across multiple samples. Be precise (e.g. "opens paragraphs with a counterintuitive claim" not "writes engagingly").

### What to avoid
3 patterns that would immediately break the voice.

### Prompt you can reuse
> "Write in my voice: [paste the Voice DNA summary above]. The topic is: [X]."

---

At the end, ask: "Want me to test this by writing something in your voice right now?"
