# MCP Protocol Exchanges – Campus Helpdesk

## 1. Initialize

The `initialize` exchange is the first communication between an MCP client and the MCP server.

**Purpose:**
- Establishes the connection.
- Allows the client and server to exchange protocol version information.
- Shares supported capabilities.

**Explanation:**

The client sends an initialization request to the server. The server responds with its protocol version, server information, and supported capabilities. The client then sends an `initialized` notification to indicate that initialization is complete.

**Testing evidence:**

The MCP Inspector successfully connected to the Campus Helpdesk server using STDIO transport.

## 2. Tools List

The `tools/list` request allows the client to discover the tools provided by the MCP server.

**Available Campus Helpdesk tools:**

1. `get_timetable(batch, day)`
   - Retrieves classes for a specified batch and day.
2. `get_fee_status(student_id)`
   - Checks a student's fee payment status.

**Explanation:**

The client requests the list of available tools. The server responds with tool names, descriptions, and input schemas. The client can then understand which tools are available and what arguments they require.

## 3. Tools Call

The `tools/call` request allows the client to execute a tool provided by the server.

**Example:**

Tool: `get_timetable`

Arguments:
- batch: `CSE-A`
- day: `Monday`

**Observed result:**

Database Management System: 09:00 - 10:00, Room 101

Java Programming: 10:00 - 11:00, Room 102

**Explanation:**

The client sends a tool name and its required arguments. The server executes the requested function and returns the result to the client.

## 4. Capability Negotiation

Capability negotiation happens during initialization.

The client and server communicate which MCP features they support. This helps both sides understand which operations are available during the connection.

In this project, the server provides tools and a resource. The MCP Inspector was used to connect to the server and test these features.

## 5. Testing Summary

The Campus Helpdesk MCP server was tested using MCP Inspector.

- `get_timetable` successfully returned Monday's CSE-A classes.
- `get_fee_status` successfully returned the Pending status for STU002.
- `campus://hostel-rules` was successfully read.
- A failure test for CSE-E on Monday returned a no-classes-found message.

**Note:** The examples above describe the protocol exchanges and observed tool results. They are not verbatim JSON request/response logs.
