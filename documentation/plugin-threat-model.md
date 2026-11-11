# Campus Helpdesk Plugin – Threat Model

## 1. Prompt Injection Through Skill Text

**Threat:** A malicious instruction could be added to a Skill file, asking the AI to ignore its original rules or reveal private information.

**Mitigation:** Review Skill files before installation. Follow trusted instructions only and never allow a Skill to override security rules or disclose sensitive information.

## 2. Malicious Shell Hooks

**Threat:** A harmful shell hook could execute unauthorized commands, modify files, or delete important data.

**Mitigation:** Inspect hook scripts before running them. Use restricted permissions, avoid unnecessary shell commands, and test hooks in a safe environment.

## 3. MCP Tool Poisoning

**Threat:** A misleading MCP tool description could trick an AI agent into calling a tool with unsafe arguments or performing an unintended action.

**Mitigation:** Use trusted MCP servers, review tool descriptions and input schemas, validate inputs, and require human approval for sensitive operations.

## Conclusion

Security should be considered when developing and installing AI plugins. Reviewing instructions, restricting hooks, and validating MCP tools can reduce potential risks.
