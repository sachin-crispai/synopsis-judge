# Operations Notebook

Accepted operational commands and standard run patterns for synopsis-judge.

## Atlas Browser

- `atlas open left <url>`
  - Open command: `open -a "/Applications/ChatGPT Atlas.app" "<url>"`
  - Snap-left (AppleScript): activate Atlas, set window `{x=0, y=0, width=screenW/2, height=screenH}`
  - Example: `atlas open left https://github.com/sachin-crispai/synopsis-judge`

- `atlas open right <url>`
  - Open command: `open -a "/Applications/ChatGPT Atlas.app" "<url>"`
  - Snap-right (AppleScript): activate Atlas, set window `{x=screenW/2, y=0, width=screenW/2, height=screenH}`

- `atlasread <url>`
  - Command: `open -a "ChatGPT Atlas.app" "<url>"`

### AppleScript template

```applescript
tell application "ChatGPT Atlas"
    activate
    delay 1
    set screenW to do shell script "system_profiler SPDisplaysDataType | awk '/Resolution/{print $2; exit}'"
    set screenH to do shell script "system_profiler SPDisplaysDataType | awk '/Resolution/{print $4; exit}'"
    set W to (screenW as integer)
    set H to (screenH as integer)
    -- Left half:
    set bounds of front window to {0, 0, W / 2, H}
    -- Right half: set bounds of front window to {W / 2, 0, W, H}
end tell
```

## Document Readers

- `skimread <file>`
  - Command: `open -a Skim <file>`

## Post-Push Verification

After every push, run `atlas open left` on the GitHub repo URL to confirm remote visibility.

## GitHub

- Repo: https://github.com/sachin-crispai/synopsis-judge
- SSH alias: `git@sachin-crispai:sachin-crispai/synopsis-judge.git`
- Always use account: `sachin-crispai`

## sync_operations

Commit and push OPERATIONS_NOTEBOOK.md (and any pending ops changes):

```bash
git add OPERATIONS_NOTEBOOK.md
git commit -m "docs: update operations notebook"
git push origin main
```

## Change Log

- 2026-03-10: Initial notebook. Added `atlas open left/right`, `atlasread`, `skimread`, post-push verification, SSH alias, sync_operations workflow.
