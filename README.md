# Campus Helpdesk Agent

## Project Overview

Campus Helpdesk Agent is an AI-Agent Toolchain project developed as part of an AI Tools and Prompt Engineering assignment.

The project demonstrates how AI Skills, Plugins, Model Context Protocol (MCP), and Git Worktrees can work together to support common college helpdesk tasks.

## Features

### 1. Timetable Helper Skill
- Finds scheduled classes using the college timetable CSV.
- Displays subject names, timings, and classroom locations.
- Handles missing information and days with no scheduled classes.
- Includes reference files and a Python helper script.

### 2. Campus Helpdesk Plugin
- Provides a custom `/timetable` command.
- Includes the timetable-helper Skill.
- Uses a PreToolUse hook to block edits to protected files.
- Includes an MCP server configuration and marketplace manifest.

### 3. MCP Server
The Python MCP server provides:

- `get_timetable(batch, day)` – retrieves scheduled classes.
- `get_fee_status(student_id)` – checks mock student fee records.
- `campus://hostel-rules` – provides the hostel rules resource.

### 4. Git Worktrees
Three separate worktrees were created:

- `feature/skill-tests`
- `feature/mcp-server`
- `bugfix/hook-path`

A deliberate merge conflict was created between the Skill and MCP branches and then resolved.

## Technologies Used

- Python
- Git and Git Worktrees
- CSV
- Model Context Protocol (MCP)
- Claude Code plugin format

## Project Structure

```text
campus-helpdesk-agent/
├── data/
├── skill/
├── plugin/
├── mcp-server/
├── documentation/
├── protected/
├── .claude-plugin/
├── part-a-claim-audit.md
└── README.md
```

## Running the Timetable Helper

From the project root:

```bash
python3 skill/timetable-helper/scripts/show_timetable.py
```

Follow the prompts to enter a batch and day.

## Running the MCP Server

Install the MCP Python SDK:

```bash
python3 -m pip install "mcp[cli]"
```

Start the server:

```bash
mcp dev mcp-server/server.py
```

Use MCP Inspector to connect and test the available tools and resource.

## Testing and Security

- Tested timetable lookup with valid and invalid inputs.
- Tested fee-status lookup with existing and missing student IDs.
- Tested the hostel rules resource.
- Simulated the hook's allow and deny decisions.
- Documented threats involving prompt injection, malicious hooks, and MCP tool poisoning.

**Verification note:** The MCP server was tested using MCP Inspector. The plugin's live installation and runtime behavior were not verified because the Claude Code CLI was unavailable in the development environment.

## Assignment Scope

This repository demonstrates practical implementation and testing of AI-agent components, along with Git collaboration workflows and basic security considerations.