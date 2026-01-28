---
name: brain
description: Second brain system for storing and recalling notes. Use when the user wants to save notes, search their knowledge base, or recall information they've previously stored. Triggers on queries like "save this", "remember", "store note", "recall", "find in notes", "search memory", "what did I save about X", "when is my anniversary", "how do I deploy".
---

# Second Brain System

Store notes and recall them with semantic search.

## Recalling Information

When the user wants to find/recall/search for something, run the bundled recall script:

```bash
python3 scripts/recall.py "user's search query"
```

The script:
- Searches `memory/*.md` and `brain/*.md` files
- Uses Gemini embeddings for semantic matching
- Returns top 5 relevant snippets with scores

**Requirements:** `pip install google-generativeai` and `GEMINI_API_KEY` env var.

## Storing Notes

When the user wants to save/store a note:

1. Get today's date (YYYY-MM-DD)
2. Append to `~/clawd/brain/{date}.md` (or `memory/` for organized notes)
3. Format:
   ```markdown
   ## {time} {timezone}
   {note}
   Source: Claude Code
   
   ---
   ```
4. Confirm: "🧠 Saved to brain!"

## Setup (First Time)

If user hasn't set up iCloud sync, suggest running `/brain:setup` to link `~/clawd/brain/` and `~/clawd/memory/` to iCloud Drive for cross-device access.
