# Setup Memory Sync

Set up the memory directory symlink to iCloud for cross-device access.

## Usage

```
/recall:setup
```

## Instructions

When this command is invoked:

1. Check if the iCloud clawd directory exists:
   ```bash
   ls ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/
   ```

2. If the memory directory doesn't exist in iCloud, create it:
   ```bash
   mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory
   ```

3. Check if ~/clawd/memory already exists:
   - If it's already a symlink pointing to iCloud → report "Already set up!"
   - If it's a regular directory → ask user if they want to move contents to iCloud
   - If it doesn't exist → create the symlink

4. Create the symlink (if needed):
   ```bash
   ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory ~/clawd/memory
   ```

5. Verify the setup:
   ```bash
   ls -la ~/clawd/memory
   ```

6. Report success: "✅ Memory directory linked to iCloud! Your notes will sync across devices."

**Note:** This assumes macOS with iCloud Drive enabled. Adjust paths if the user's workspace is not at `~/clawd`.
