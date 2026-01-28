# Setup Brain Sync

Set up iCloud sync for your brain and memory directories.

## Usage

```
/brain:setup
```

## What It Does

Creates symlinks so your notes sync across all your Apple devices:
- `~/clawd/brain/` → iCloud Drive
- `~/clawd/memory/` → iCloud Drive

## Instructions

When this command is invoked:

1. **Check iCloud availability:**
   ```bash
   ls ~/Library/Mobile\ Documents/com~apple~CloudDocs/
   ```
   If this fails, iCloud Drive isn't set up.

2. **Create iCloud directories:**
   ```bash
   mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/brain
   mkdir -p ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory
   ```

3. **For each directory (brain, memory):**
   
   Check if `~/clawd/{dir}` exists:
   - **If it's already a symlink to iCloud** → Skip, already configured
   - **If it's a regular directory with files** → Ask user: "Move existing files to iCloud?"
     - If yes: `mv ~/clawd/{dir}/* ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/{dir}/` then `rmdir ~/clawd/{dir}`
     - If no: Skip this directory
   - **If it doesn't exist** → Proceed to create symlink

4. **Create symlinks:**
   ```bash
   ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/brain ~/clawd/brain
   ln -s ~/Library/Mobile\ Documents/com~apple~CloudDocs/clawd/memory ~/clawd/memory
   ```

5. **Verify and report:**
   ```bash
   ls -la ~/clawd/brain ~/clawd/memory
   ```
   
   Report: "✅ Brain sync configured! Your notes will sync across devices."

## Notes

- Requires macOS with iCloud Drive enabled
- Adjust paths if workspace is not at `~/clawd`
- Run this once on each new machine
