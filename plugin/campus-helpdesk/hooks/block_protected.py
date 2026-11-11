import json
import sys
from pathlib import Path

# Read information sent by Claude Code
data = json.load(sys.stdin)

# Get the file path being modified
tool_input = data.get("tool_input", {})
file_path = tool_input.get("file_path", "")

# Check whether the file is inside the protected folder
path = Path(file_path)

if "protected" in path.parts:
    print(
        json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": "Editing files inside the protected folder is not allowed."
            }
        })
    )
else:
    # Allow other file modifications
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow"
        }
    }))
