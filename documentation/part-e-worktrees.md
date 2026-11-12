# Part E – Git Worktrees

## 1. Overview

Git worktrees allow multiple branches of the same Git repository to be checked out in separate working directories. This makes it possible to work on different features at the same time without repeatedly switching branches in one directory.

For this project, I created three linked worktrees for Skill testing, MCP server development, and security hook fixes.

## 2. Worktrees Created

The following worktrees were created and verified using `git worktree list`.

| Working directory | Branch |
|---|---|
| `/workspaces/campus-helpdesk-agent` | `main` |
| `/workspaces/campus-skill-tests` | `feature/skill-tests` |
| `/workspaces/campus-mcp-server` | `feature/mcp-server` |
| `/workspaces/campus-hook-fix` | `bugfix/hook-path` |

Each worktree has its own working directory, while all worktrees belong to the same Git repository.

## 3. Deliberate Merge Conflict

To demonstrate Git conflict resolution, I modified the same `conflict-demo.txt` file in two different branches.

- The Skill branch contained commit `0589db9`.
- The MCP branch contained commit `3d191ee`.
- Both branches changed the same file, resulting in a merge conflict.

I compared the conflicting versions, selected the appropriate content, removed the conflict markers, and completed the merge.

**Merge commit:** `8f46253` – Merge MCP branch and resolve conflict.

The Git history confirmed that the merge was completed successfully.

## 4. Git History Verification

The following command was used to inspect the repository history and branch relationships:

```bash
git log --oneline --graph --all -15
```

The output showed the Skill and MCP branches, their separate commits, and the merge commit `8f46253`.

The following command was used to verify the linked worktrees:

```bash
git worktree list
```

It displayed the main working directory and all three feature worktrees.

## 5. Understanding Git Worktrees

**Q1. What is the difference between a branch and a worktree?**

A branch is a movable reference to a commit in Git history. A worktree is a separate working directory connected to the repository. A worktree can have a branch checked out in it.

**Q2. Why can't the same branch normally be checked out in multiple worktrees?**

Git prevents this to avoid accidental changes to the same branch from multiple working directories. This helps protect repository consistency.

**Q3. What happens when two branches modify the same lines?**

Git may report a merge conflict because it cannot automatically determine which changes should be kept. The developer must review the changes and resolve the conflict.

**Q4. Why are worktrees useful for parallel development?**

They allow developers to work on multiple features or fixes simultaneously in separate folders. This reduces the need to switch branches repeatedly.

## 6. Worktree Merge Command Evaluation

The assignment also referred to a `/worktree-merge` command.

I could not independently verify the availability or behaviour of this command in my development environment. Instead, I used standard Git commands to perform and verify the merge conflict resolution.

This distinction is important because an unverified command should not be presented as successfully tested.

## 7. Conclusion

This part of the project helped me understand how Git worktrees support parallel development. I created three linked worktrees, worked with separate feature branches, deliberately created a merge conflict, and resolved it successfully. I also used Git history and worktree listing commands to verify the results.