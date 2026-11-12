# Campus Helpdesk MCP Server

## Overview
This project implements an MCP server using the official Python MCP SDK.

## Features

### Tools

1. **get_timetable(batch, day)**
   - Finds classes using the student's batch and day.
   - Reads information from `data/timetable.csv`.

2. **get_fee_status(student_id)**
   - Checks a student's fee payment status.
   - Uses sample mock data.

### Resource

**campus://hostel-rules**
- Provides the college hostel rules document.
- Reads information from `hostel-rules.md`.

## Technology Used
- Python
- Model Context Protocol (MCP)
- Official MCP Python SDK

## Run the Server

Install the SDK:

```bash
python3 -m pip install "mcp[cli]"
```

Start the server:

```bash
python3 mcp-server/server.py
```

The server uses standard input/output (stdio) transport.

## Data Sources
- Timetable: `data/timetable.csv`
- Fee records: Mock data inside `server.py`
- Hostel rules: `mcp-server/hostel-rules.md`



## Testing

The MCP server was tested using MCP Inspector and direct Python function calls.

The following tests were completed:

1. `get_timetable` – Successfully returned Monday's classes for batch CSE-A.
2. `get_timetable` – Correctly rejected an empty batch input.
3. `get_fee_status` – Successfully returned Pending for student STU002.
4. `get_fee_status` – Correctly rejected an empty student ID.
5. Hostel rules resource – Successfully returned the contents of `hostel-rules.md`.
6. Failure test – Correctly returned a no-classes-found message for batch CSE-E on Monday.

The server successfully connected using STDIO transport through MCP Inspector.

**Note:** Direct Python function calls were used for input validation tests.


The assignment asked us to verify whether `@nimbus/mcp-skill-bridge` version `2.3` exists.

**Finding:** Unverified. No reliable evidence confirming the exact package and version was found during the search.

**Decision:** The package was not installed or used because its existence could not be verified.

**Date accessed:** 11 November 2026.

