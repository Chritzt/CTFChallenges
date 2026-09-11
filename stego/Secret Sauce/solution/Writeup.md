## Secret Sauce

### 1. Vulnerability Analysis
The repository looks completely clean with only two standard commits in `git log`. However, the challenge description hints that a developer tried to clear a mistake using `git push --force`. 

When a developer uses `git reset --hard` or forces a push, the unwanted commits disappear from the standard history, but their underlying data objects remain in the `.git/objects/` directory as unreferenced or **"dangling" objects** until the Git garbage collector cleans them up.

### 2. Exploitation / Solution

Since the local reflog was wiped, standard commands like `git reflog` will not show the history. Instead, players must inspect the internal Git object database directly.

### Step 1: Recover Dangling Objects
Run Git's filesystem check tool to identify unreachable commits:

```bash
git fsck --lost-found

```

### Output

```
Checking object directories: 100% (256/256), done.
dangling commit 9d3421b121ae6cb99f55f928a8583d1896c460c4
```

### 2. Inspect the commit 

```
git show 9d3421b121ae6cb99f55f928a8583d1896c460c4
```

There we get the commit with the Flag in it: 

```
# TODO: Move this to environment variables later, nobody will see it anyway
API_KEY = 'CLA{G1t_N3v3r_F0rg3ts_D4ngl1ng_0bj3cts}'
```