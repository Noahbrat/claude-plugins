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

1. **Find the recall script.** It's bundled with this plugin at one of these locations:
   - `~/.claude/plugins/cache/noahbrat-tools/brain/*/scripts/recall.py`
   - Or search for `recall.py` in `~/.claude/plugins/`

2. Run the script:
   ```bash
   python3 /path/to/recall.py "$ARGUMENTS"
   ```

3. The script searches `memory/*.md` and `brain/*.md` files, returning the top 5 matches with similarity scores.

4. Present the results to the user.

**Tip:** Run `/brain:setup` first to configure iCloud sync.

Search for:
$ARGUMENTS
