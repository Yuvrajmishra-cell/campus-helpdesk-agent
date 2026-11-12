import json
import sys
from pathlib import Path

# Read information sent by Claude Code
data = json.load(sys.stdin)

# Get the file path being modified
tool_input = data.get("tool_input", {})
file_path = tool_input.get("file_path", "")

# Define the protected folder inside this project
project_root = Path(__file__).resolve().parents[3]
protected_folder = (project_root / "protected").resolve()

try:
    target_path = Path(file_path).resolve()

    # Check whether the target is inside the protected folder
    if target_path == protected_folder or protected_folder in target_path.parents:
        decision = "deny"
        reason = "Editing files inside the protected folder is not allowed."
    else:
        decision = "allow"
        reason = "File modification is allowed."

except (OSError, RuntimeError, ValueError):
    decision = "deny"
    reason = "Unable to safely verify the file path."

# Return the hook decision
print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": reason
    }
}))
