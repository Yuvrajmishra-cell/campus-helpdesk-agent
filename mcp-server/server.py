from mcp.server import MCPServer

# Create our MCP server
mcp = MCPServer("Campus Helpdesk Server")


# Tool 1: Get timetable information
@mcp.tool()
def get_timetable(batch: str, day: str) -> str:
    """
    Find all scheduled classes for a given batch and day.
    Uses the college timetable CSV as its source.
    """
    import csv
    from pathlib import Path

    # Locate the timetable CSV file in the repository
    csv_path = Path(__file__).parent.parent / "data" / "timetable.csv"

    results = []

    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if (
                row["Batch"].strip().lower() == batch.strip().lower()
                and row["Day"].strip().lower() == day.strip().lower()
            ):
                results.append(
                    f"{row['Subject']}: {row['StartTime']} - "
                    f"{row['EndTime']}, {row['Room']}"
                )

    if not results:
        return f"No classes found for batch {batch} on {day}."

    return "\n".join(results)


# Tool 2: Check student fee status
@mcp.tool()
def get_fee_status(student_id: str) -> str:
    """
    Check the fee payment status of a student using their student ID.
    Uses mock student fee records.
    """

    fee_records = {
        "STU001": "Paid",
        "STU002": "Pending",
        "STU003": "Paid"
    }

    status = fee_records.get(student_id.strip().upper())

    if status is None:
        return f"No fee record found for student ID {student_id}."

    return f"Fee status for {student_id}: {status}"

# Resource: College hostel rules
@mcp.resource("campus://hostel-rules")
def get_hostel_rules() -> str:
    """
    Provides the college hostel rules document.
    """

    from pathlib import Path

    rules_path = Path(__file__).parent / "hostel-rules.md"

    return rules_path.read_text(encoding="utf-8")

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")
