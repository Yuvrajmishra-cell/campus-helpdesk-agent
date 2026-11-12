# Campus Helpdesk Plugin – Threat Model

## 1. Prompt Injection Through Skill Text

**Threat:** A malicious instruction could be added to a Skill file, asking the AI to ignore its original rules, reveal private information, or provide false timetable details.

**Example:** Someone modifies the timetable Skill and adds an instruction telling the AI to ignore the CSV and invent classes when information is missing.

**Mitigation:** Review Skill files before installation. Treat user-provided and external instructions as untrusted. Follow the original accuracy and security rules, and never reveal sensitive information.

## 2. Malicious Shell Hooks

**Threat:** A harmful shell hook could execute unauthorized commands, modify files, or delete important data when a tool is used.

**Example:** A malicious PreToolUse hook could run a shell command that deletes files from the project when a user attempts to edit a document.

**Mitigation:** Inspect hook scripts before running them. Use restricted permissions, avoid unnecessary shell commands, and test hooks in a safe environment. Limit hooks to the minimum actions required.

## 3. MCP Tool Poisoning

**Threat:** A misleading MCP tool description could trick an AI agent into calling a tool with unsafe arguments or performing an unintended action.

**Example:** A tool description could claim that a timetable lookup only reads data, while its actual implementation performs an unrelated file modification.

**Mitigation:** Use trusted MCP servers, review tool descriptions and input schemas, validate inputs on the server side, and require human approval for sensitive operations.

## Conclusion

Security should be considered when developing and installing AI plugins. Reviewing instructions, restricting hooks, and validating MCP tools can reduce potential risks. Testing components in a safe environment also helps identify problems before deployment.
