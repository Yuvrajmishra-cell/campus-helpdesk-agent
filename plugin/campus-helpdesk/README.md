# Campus Helpdesk Plugin

## Overview
Campus Helpdesk is a Claude Code plugin designed to help college students access timetable information and campus-related assistance.

## Features

- **Timetable Skill:** Helps students find classes using timetable data.
- **Timetable Command:** Provides a custom command for timetable queries.
- **Security Hook:** Blocks file modifications inside the protected folder.
- **MCP Integration:** Configured to connect to a campus helpdesk MCP server.

## Project Structure

- `.claude-plugin/` – Plugin manifest
- `skills/` – Timetable helper Skill
- `commands/` – Custom timetable command
- `hooks/` – Security hook
- `.mcp.json` – MCP server configuration

## MCP Server

The plugin is configured to connect to the repository's `mcp-server/server.py` file. The server implementation will be completed separately.

## Testing Status

The security hook has passed simulated allow and deny tests. Live Claude Code plugin installation and runtime testing have not yet been performed.

## Author
Student Developer
