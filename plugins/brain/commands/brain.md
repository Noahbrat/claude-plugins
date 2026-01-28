# Save to Brain

Save a note to the personal knowledge base (second brain). Works from any machine with iCloud.

## Usage

```
/brain:brain [your note here]
```

## Examples

```
/brain:brain This API uses cursor-based pagination with a "next" field
/brain:brain The deploy script needs NODE_ENV=production
/brain:brain Great article on React Server Components: [url]
```

## Instructions

When this command is invoked with `$ARGUMENTS`:

1. Get today's date in YYYY-MM-DD format
2. Determine the brain path on macOS:
   ```
   ~/Library/Mobile Documents/com~apple~CloudDocs/clawd/brain/{date}.md
   ```
   Expand `~` to the actual home directory (e.g., `/Users/noah/...`)
3. Create the brain directory if it doesn't exist
4. Create the file if it doesn't exist, or append to it
5. Format the entry as:
   ```markdown
   ## {time} {timezone}
   {note}
   Source: Claude Code
   
   ---
   ```
6. Confirm: "🧠 Saved to brain!"

**Important:** This writes to iCloud Drive so notes sync across all devices.

Save this note to the brain:
$ARGUMENTS
