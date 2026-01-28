---
name: recall
description: Semantic memory search using Gemini embeddings. Use when the user asks to search, find, or recall information from their memory files, notes, or knowledge base. Triggers on queries like "recall", "remember", "find in notes", "search memory", "what did I save about X".
---

# Semantic Memory Search

Search through `memory/*.md` files and `MEMORY.md` using Gemini embeddings for semantic matching.

## Requirements

- Python 3.8+
- `google-generativeai` package: `pip install google-generativeai`
- Gemini API key (set `GEMINI_API_KEY` env var or configure in `~/.clawdbot/clawdbot.json`)

## Usage

When the user wants to search their memory/notes, run the bundled script:

```bash
python3 scripts/recall.py "search query here"
```

The script will:
1. Find the `memory/` directory in the current workspace (searches up to 5 parent directories)
2. Also check for `MEMORY.md` in the workspace root
3. Chunk the content and generate embeddings via Gemini API
4. Return the top 5 most relevant snippets with similarity scores

## Example Queries

- "How do I deploy to production?"
- "SSH server credentials"  
- "What's the git workflow?"
- "Database connection info"

## Output Format

The script outputs results like:

```
🔍 Searching for: deploy production
📁 Memory directory: /path/to/memory

Found 3 relevant result(s):

### Result 1 — memory/runbook.md (lines 1-20) — Score: 0.85
[snippet content]
---
```

## Troubleshooting

**"No Gemini API key found"** — Set the `GEMINI_API_KEY` environment variable or add the key to `~/.clawdbot/clawdbot.json` under `models.providers.gemini.apiKey`.

**"Could not find memory/ directory"** — Make sure you're in a workspace that has a `memory/` folder. The script checks the current directory and up to 5 parent directories.

**"google-generativeai not installed"** — Run `pip install google-generativeai`.
