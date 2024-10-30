# Git Bisect Demo

This repository is a simple demo of the git bisect command, which helps identify the specific commit that introduced a bug or issue by performing a binary search across the commit history. Find a very basic calculate.py which contains several functions and some bugs introduced (on purpose).

## Purpose

- **Learn how to use git bisect**: This demo demonstrates how to find the commit that introduced a bug using git bisect.
- **Practice using git bisect commands**: We'll cover marking commits as "good" or "bad" and interpreting the output.

## Steps to Use git bisect in this Demo

### Step 1: Clone the Repository

   
```bash
   git clone https://github.com/YOUR_USERNAME/git-bisect-demo.git
   cd git-bisect-demo
```

### Step 2: Identify a "Good" and a "Bad" Commit

Use git log to review the commit history and identify:
- A "good" commit: one before the bug was introduced.
- A "bad" commit: one where the bug is confirmed to exist.

### Step 3: Start git bisect

Begin the bisect session by marking the known good and bad commits:
   
```bash
    git bisect start
    git bisect bad <bad_commit_hash>
```
or use
```bash
    git bisect bad HEAD                 #last commit
    git bisect good <good_commit_hash>
```

### Step 4: Mark Each Commit as "Good" or "Bad"

git bisect will now automatically check out commits between the "good" and "bad" points. Test each checked-out commit for the bug. Based on the results, mark each commit:

 ```bash
    git bisect good   # if the bug is absent
    git bisect bad    # if the bug is present
```
### Step 5: Complete the Bisect Session

Once git bisect has identified the exact commit that introduced the bug, reset the bisect session: (very important)

```bash
    git bisect reset
```