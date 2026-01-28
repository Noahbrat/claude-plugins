# Recall from Brain

Search your brain and memory files using semantic search (Gemini embeddings).

## Usage

```
/brain:recall [search query]
```

## Examples

```
/brain:recall how to deploy to production
/brain:recall SSH server credentials
/brain:recall git branching workflow
```

## Requirements

- Python 3.8+
- `google-generativeai` package: `pip install google-generativeai`
- Gemini API key (set `GEMINI_API_KEY` env var or configure in `~/.clawdbot/clawdbot.json`)

## Instructions

When this command is invoked with `$ARGUMENTS`:

1. Locate the recall script bundled with this plugin at `scripts/recall.py`

2. Run the script with the search query:
   ```bash
   python3 scripts/recall.py "$ARGUMENTS"
   ```

3. The script will:
   - Search `memory/*.md` and `brain/*.md` files in the workspace
   - Also search `MEMORY.md` if it exists
   - Use Gemini embeddings for semantic matching
   - Return the top 5 most relevant snippets with scores

4. Present the results to the user

**Tip:** Run `/brain:setup` first to configure iCloud sync so your notes are searchable from any device.

Search for:
$ARGUMENTS
