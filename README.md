# Claude Plugins

Personal Claude Code plugins and tools.

## Installation

Add this marketplace to Claude Code:

```
/plugin marketplace add Noahbrat/claude-plugins
```

Then install plugins:

```
/plugin install brain@noahbrat-tools
```

## Available Plugins

### brain
Save notes to your second brain (iCloud-synced across devices).

```
/brain:brain OAuth tokens expire after 30 days
/brain:brain Great restaurant: Rosa's on Main, get the al pastor
```

Notes are saved to `~/Library/Mobile Documents/com~apple~CloudDocs/clawd/brain/` and sync via iCloud.

## Updating

Pull the latest plugins:

```
/plugin marketplace update
```

## Adding New Plugins

1. Create a new folder under `plugins/`
2. Add `.claude-plugin/plugin.json` manifest
3. Add commands in `commands/` folder
4. Update `marketplace.json` to list the new plugin
5. Commit and push
