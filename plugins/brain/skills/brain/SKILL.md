---
name: brain
description: Second brain system for storing and recalling notes. Use when the user wants to save notes, search their knowledge base, or recall information they've previously stored. Triggers on queries like "save this", "remember", "store note", "recall", "find in notes", "search memory", "what did I save about X".
---

# Second Brain System

A unified system for storing notes and recalling them with semantic search.

## Commands Available

- `/brain:store [note]` — Save a note to daily brain file
- `/brain:recall [query]` — Semantic search across brain and memory
- `/brain:setup` — Configure iCloud sync for cross-device access

## Automatic Behavior

When the user asks to save/store something, use `/brain:store`.
When the user asks to find/recall something, use `/brain:recall`.

## Requirements for Recall

- Python 3.8+
- `google-generativeai` package
- Gemini API key (env var `GEMINI_API_KEY` or in `~/.clawdbot/clawdbot.json`)

## Storage Locations

Notes are stored in:
- `brain/YYYY-MM-DD.md` — Daily brain dumps
- `memory/*.md` — Organized knowledge files

Both can be synced via iCloud using `/brain:setup`.
