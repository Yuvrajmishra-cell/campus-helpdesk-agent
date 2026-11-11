# Campus Helpdesk Plugin

## Overview

Campus Helpdesk is a Claude Code plugin designed to help college students access timetable information and campus-related assistance.

## Features

- **Timetable Skill:** Helps students find scheduled classes using timetable data.
- **Timetable Command:** Provides a custom command for timetable queries.
- **Security Hook:** Blocks file modifications inside the protected folder.
- **MCP Integration:** Connects to the Campus Helpdesk MCP server.

## Project Structure

- `.claude-plugin/` – Plugin manifest
- `skills/` – Bundled timetable helper Skill and its data
- `commands/` – Custom timetable command
- `hooks/` – Security hook and configuration
- `.mcp.json` – MCP server configuration

## MCP Server

The plugin's MCP configuration references the repository's `mcp-server/server.py` file.

The MCP server provides:
- `get_timetable(batch, day)` – Retrieves scheduled classes.
- `get_fee_status(student_id)` – Checks mock student fee records.
- `campus://hostel-rules` – Provides the hostel rules resource.

**Dependency:** The MCP configuration uses a relative path to the repository's `mcp-server` directory. Therefore, the complete repository structure must be available. The plugin has not been verified as a standalone installation.

## Testing Status

- Timetable helper script: Successfully tested using the bundled CSV.
- Security hook: Simulated allow and deny tests passed.
- MCP server: Tools and resource tested using MCP Inspector.
- Live Claude Code plugin installation: Not tested because the Claude Code CLI was unavailable in the development environment.

## Security Considerations

The security hook should be reviewed and tested in the actual plugin host before production use. AI-generated instructions and external MCP tool descriptions should also be reviewed before being trusted.

## Author

Student Developer