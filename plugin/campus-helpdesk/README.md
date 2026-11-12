# Campus Helpdesk Plugin

## Overview

Campus Helpdesk is a Claude Code plugin designed to help college students access timetable information and campus-related assistance.

## Features

- **Timetable Skill:** Helps students find scheduled classes using timetable data.
- **Timetable Command:** Provides a custom command for timetable queries.
- **Security Hook:** Blocks file modifications inside the protected folder.
- **MCP Integration:** Includes its own bundled Campus Helpdesk MCP server.

## Project Structure

- `.claude-plugin/` – Plugin manifest
- `skills/` – Timetable helper Skill, references, script and CSV data
- `commands/` – Custom timetable command
- `hooks/` – Security hook and configuration
- `mcp-server/` – Bundled MCP server and hostel rules resource
- `data/` – Timetable CSV used by the MCP server
- `.mcp.json` – MCP server configuration

## MCP Server

The plugin includes its own MCP server at `mcp-server/server.py`.

It provides:

- `get_timetable(batch, day)` – Retrieves scheduled classes from the bundled timetable CSV.
- `get_fee_status(student_id)` – Checks mock student fee records.
- `campus://hostel-rules` – Provides the sample hostel rules document.

The MCP configuration uses `${CLAUDE_PLUGIN_ROOT}` to locate the bundled server.

**Dependency:** Python and the MCP SDK must be installed in the environment running the server.

## Testing Status

- Timetable helper script: Successfully tested.
- Security hook: Three tests passed — blocked a file inside the project's protected folder, allowed a documentation file, and allowed an unrelated protected folder outside the project.
- Bundled MCP server: Successfully launched using MCP Inspector.
- `get_timetable`: Passed with Monday and CSE-A.
- `get_fee_status`: Passed with STU002.
- `campus://hostel-rules`: Resource successfully read.
- Live Claude Code plugin installation: Not tested because the Claude Code CLI was unavailable in the development environment.

## Security Considerations

The security hook should be reviewed and tested in the actual plugin host before production use. AI-generated instructions and external MCP tool descriptions should also be reviewed before being trusted.

## Author

Student Developer