---
name: brain
description: Second brain system - store notes, recall with semantic search, setup sync. Use for "save this", "remember", "store note", "recall", "find in notes", "search memory", "what did I save about X", "brain store", "brain recall", "brain setup", "setup brain sync".
---

# Second Brain

Store notes and recall them with semantic search.

## Actions

### Store (`/brain store [note]` or "save this to brain")

Save a note to daily brain file:

1. Get today's date (YYYY-MM-DD)
2. Append to `brain/{date}.md` in the workspace (or `~/clawd/brain/` if not found)
3. Format:
   ```markdown
   ## {time} {timezone}
   {note}
   Source: Claude Code
   
   ---
   ```
4. Confirm: "🧠 Saved to brain!"

### Recall (`/brain recall [query]` or "search brain for X")

Search with semantic embeddings:

```bash
python3 scripts/recall.py "search query"
```

Requirements: `pip install google-generativeai` and `GEMINI_API_KEY` env var.

### Setup (`/brain setup`)

Configure iCloud sync for cross-device access:

1. Create iCloud directories:
   ```bash
   mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/brain
   mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory
   ```

2. For each (brain, memory): if `~/clawd/{dir}` exists as regular directory, ask to move contents to iCloud, then remove it.

3. Create symlinks:
   ```bash
   ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/brain ~/clawd/brain
   ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory ~/clawd/memory
   ```

4. Confirm: "✅ Brain sync configured!"
