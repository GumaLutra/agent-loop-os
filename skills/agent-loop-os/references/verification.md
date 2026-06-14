# Verification Gates

Made by sudal.

Pick the closest real signal. Static checks are useful, but they are not always enough.

## Code

- run syntax/type/lint checks when available
- run targeted tests for changed behavior
- inspect diffs for unrelated changes
- verify failure before fix when debugging if practical

## UI

- run the app or open the static file
- inspect the actual rendered screen
- check desktop and mobile when layout changed
- check console errors when using a browser
- use screenshots when visual quality matters

## Data

- confirm target environment, account, collection/table, and date range
- make or locate a backup before destructive changes
- run dry-run when available
- compare before/after counts
- sample representative records
- check duplicates and missing records

## Deployment

- validate config before deploy
- deploy with backup or rollback plan when possible
- check deploy status
- run smoke tests against the deployed target
- confirm the intended environment was changed

## Documentation

- verify examples match the current files
- check commands are copy-pasteable
- check names, paths, and dates
- include known limitations
