# Part A – Claim Audit

**Assignment:** Building and Auditing an AI-Agent Toolchain  
**Verification date:** 11 November 2026

## Claim 1 – TRUE

**Claim:** MCP uses JSON-RPC 2.0 as its message format and provides server features such as tools, resources, and prompts.

**Correction:** No correction required. The MCP specification defines JSON-RPC 2.0 messages and describes tools, resources, and prompts as server features.

**Reasoning:** MCP uses JSON-RPC 2.0 for communication between clients and servers. Tools allow models to perform actions, resources provide contextual data, and prompts provide reusable message templates. These features serve different purposes in an MCP application.

**Official source:** https://modelcontextprotocol.io/specification/2025-11-25/basic/index.mdx

## Claim 2 – FALSE

**Claim:** The claim describes a specification dated 2025-02-30 and presents a Persistent Memory Primitive as a mandatory MCP server feature.

**Correction:** February 30 is not a valid calendar date. The MCP specification does not require a Persistent Memory Primitive as a standard server feature.

**Reasoning:** MCP defines standard communication and server capabilities, including tools, resources, and prompts. It does not make a persistent conversation-memory feature mandatory for every server. A developer may implement application-specific memory, but that is different from a required MCP primitive.

**Official source:** https://modelcontextprotocol.io/specification/2025-11-25

## Claim 3 – TRUE

**Claim:** An Agent Skill is organised as a folder containing a `SKILL.md` file with YAML frontmatter, and it uses progressive disclosure.

**Correction:** No correction required for the described Skill format.

**Reasoning:** The Agent Skills documentation describes a `SKILL.md` file containing YAML frontmatter and Markdown instructions. Progressive disclosure allows an agent to discover a Skill through its name and description before loading the full instructions when the Skill is relevant. Supporting files such as references and scripts can also be included.

**Official source:** https://github.com/microsoft/skills/blob/main/.github/docs/skills.md

## Claim 4 – FALSE

**Claim:** The Agent Skills format requires a separate `skill.config.yaml` file and a mandatory runtime field such as `python3.14`.

**Correction:** A separate `skill.config.yaml` file and a mandatory Python runtime field are not requirements of the documented Agent Skills format.

**Reasoning:** The documented format requires a `SKILL.md` file with the appropriate YAML frontmatter and Markdown instructions. Additional reference documents, scripts, and supporting folders can be included when needed. These optional files do not create a requirement for a separate configuration file or a fixed Python runtime.

**Official source:** https://github.com/microsoft/skills/blob/main/.github/docs/skills.md

## Claim 5 – TRUE

**Claim:** Git supports multiple linked worktrees connected to one repository, with separate working directories and shared repository data.

**Correction:** No correction required.

**Reasoning:** Git worktrees allow developers to work on multiple branches at the same time without repeatedly switching the main working directory. Each worktree has its own working directory and worktree-specific metadata, while the worktrees remain connected to the same repository. This makes parallel development and testing easier.

**Official source:** https://git-scm.com/docs/git-worktree

## Claim 6 – FALSE

**Claim:** Git provides a command called `git worktree sync --all`.

**Correction:** The documented Git worktree command set does not include `git worktree sync --all`.

**Reasoning:** The official documentation lists supported operations such as `add`, `list`, `remove`, `prune`, `move`, `lock`, `unlock`, and `repair`. The claimed `sync --all` operation is not part of the documented command syntax. Developers should use supported Git operations for branch and repository updates instead of assuming this command exists.

**Official source:** https://git-scm.com/docs/git-worktree

## Claim 7 – TRUE

**Claim:** Claude Code plugins can package reusable commands, agents, Skills, hooks, and MCP server configurations.

**Correction:** No correction required for these plugin capabilities.

**Reasoning:** Claude Code plugins are designed to package related extensions into a reusable unit. The documented plugin structure supports custom slash commands, agents, Skills, hooks, and MCP server configurations. This makes it easier to share related development workflows with other users or teams.

**Official sources:**
- https://claude.com/blog/claude-code-plugins
- https://github.com/anthropics/claude-plugins-official

## Claim 8 – FALSE

**Claim:** RFC 9999 establishes an MCP transport security rule and requires every stdio MCP server to have an Ed25519 signature.

**Correction:** RFC 9999 is titled *Remote ATtestation procedureS (RATS) Conceptual Message Wrapper (CMW)*. It does not establish the claimed mandatory signing rule for all stdio MCP servers.

**Reasoning:** The RFC describes a conceptual message wrapper used in remote attestation procedures. It discusses cryptographic protection mechanisms for those wrappers, but this does not establish the claimed MCP-specific requirement. The claim incorrectly connects the RFC to a mandatory Ed25519 signing rule for stdio MCP servers.

**Official source:** https://www.rfc-editor.org/rfc/rfc9999.html

## Claim 9 – FALSE

**Claim:** Git normally allows the same branch to be checked out in multiple worktrees at the same time.

**Correction:** Git normally prevents a branch from being checked out in more than one worktree simultaneously. Force options can override certain safeguards.

**Reasoning:** The Git worktree documentation describes safeguards against creating another worktree using a branch that is already checked out elsewhere. This prevents developers from unintentionally editing the same branch through multiple working directories. I also observed this restriction during my assignment when Git refused to switch to `main` because it was already checked out in the main worktree.

**Official source:** https://git-scm.com/docs/git-worktree

## Claim 10 – UNVERIFIED

**Claim:** A study by Hendricks and Oyelaran reported a 40% accuracy reduction and introduced the term "skill collapse".

**Correction:** No verified correction can be provided because the original research claim could not be independently confirmed.

**Reasoning:** A reliable publication or official research record supporting the named authors, the reported 40% reduction, and the term "skill collapse" was not located during verification. A search that does not find supporting evidence does not prove that the study does not exist. Therefore, the responsible verdict is Unverified rather than True or False.

**Verification search:** https://scholar.google.com/scholar?q=Hendricks+Oyelaran+skill+collapse

---

## Final Observation

The claim audit demonstrates why technical information should be checked against official documentation before being accepted. Some claims contained incorrect commands, invalid dates, or unsupported technical requirements. Other claims were consistent with the documentation. The Unverified category was important because a lack of reliable evidence is not the same as proof that a statement is false.

**Access date for the official sources:** 11 November 2026.