# CSEPrompts releases

Both folders are byte-identical copies of [mraihan-gmu/CSEPrompts](https://github.com/mraihan-gmu/CSEPrompts)
at the commit in their name. Nothing in them is edited.

| Folder | Commit | Status |
|---|---|---|
| `CSEPrompts-57275c2/` | `57275c2` (2026-10-11, "fixed test case issues") | **Current.** Used by default. Tests: `data/processed/pytest/original/` |
| the `58d7ea0` copy (`CSEPrompts-main/` in the working repo, `OUTDATED_CSEPrompts-58d7ea0/` in the public replication repo) | `58d7ea0` (2024-09-25), identical to the journal's supplementary material | **OUTDATED.** The version the paper used. Kept only to reproduce results computed on it. Tests: `data/processed/pytest_OUTDATED_58d7ea0/original/` |

The code picks the release from the environment variable `CSE_RELEASE` (default `57275c2`). Set
`CSE_RELEASE=58d7ea0` to work with the outdated release.
