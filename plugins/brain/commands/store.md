# Store to Brain

Save a note to your second brain. Notes are stored in daily files and sync via iCloud.

## Usage

```
/brain:store [your note here]
```

## Examples

```
/brain:store This API uses cursor-based pagination with a "next" field
/brain:store The deploy script needs NODE_ENV=production
/brain:store Great article on React Server Components: [url]
```

## Instructions

When this command is invoked with `$ARGUMENTS`:

1. Get today's date in YYYY-MM-DD format
2. Determine the brain path:
   - First check for symlink at `~/clawd/brain/` (preferred, iCloud-synced)
   - Otherwise use `~/Library/Mobile Documents/com~apple~CloudDocs/clawd/brain/`
   - Create the directory if it doesn't exist
3. Create or append to `{date}.md`
4. Format the entry as:
   ```markdown
   ## {time} {timezone}
   {note}
   Source: Claude Code
   
   ---
   ```
5. Confirm: "🧠 Saved to brain!"

**Tip:** Run `/brain:setup` first to configure iCloud sync.

Save this note:
$ARGUMENTS
