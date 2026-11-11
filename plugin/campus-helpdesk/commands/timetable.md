---
description: Get timetable information for a college student
argument-hint: "[day] [batch]"
---

# Timetable Command

Help the student find their college timetable.

Follow the instructions in the timetable-helper Skill.

When the student provides a day and batch:

1. Read the available timetable CSV data.
2. Find all matching classes.
3. Display the subject, start time, end time, and room.
4. Arrange classes in time order.
5. If no matching classes exist, clearly say so.
6. Never invent subjects, timings, rooms, or other information.

If the day or batch is missing, ask the student for the missing information.
