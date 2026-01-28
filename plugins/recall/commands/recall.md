# Semantic Memory Search

Search your memory files using semantic understanding (Gemini embeddings).

## Usage

```
/recall:recall [your query]
```

## Examples

```
/recall:recall how to deploy to production
/recall:recall SSH server credentials
/recall:recall git branching workflow
```

## Instructions

When this command is invoked with `$ARGUMENTS`:

1. Find the recall script at `plugins/recall/scripts/recall.py` (relative to the plugins repo) or use the version installed at `~/.claude/plugins/recall/scripts/recall.py`

2. Run the script with the query:
   ```bash
   python3 /path/to/recall.py "$ARGUMENTS"
   ```

3. The script will:
   - Search `memory/*.md` files and `MEMORY.md` in the current workspace
   - Use Gemini embeddings for semantic matching
   - Return the top 5 most relevant snippets with scores

4. Present the results to the user, highlighting the most relevant matches

**Requirements:**
- `google-generativeai` Python package (`pip install google-generativeai`)
- Gemini API key (set `GEMINI_API_KEY` env var or configure in `~/.clawdbot/clawdbot.json`)

**Note:** The script auto-discovers the memory directory by checking the current workspace and common locations.

Search for:
$ARGUMENTS
