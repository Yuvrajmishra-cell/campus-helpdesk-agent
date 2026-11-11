import csv
from pathlib import Path

# Locate the timetable CSV inside this Skill's folder
skill_folder = Path(__file__).resolve().parents[1]
csv_path = skill_folder / "data" / "timetable.csv"

# Open the timetable CSV file
with open(csv_path, "r", newline="", encoding="utf-8") as file:
    timetable = csv.DictReader(file)

    day = input("Enter the day: ").strip()
    batch = input("Enter your batch: ").strip()

    found = False

    for row in timetable:
        if row["Day"].lower() == day.lower() and row["Batch"].lower() == batch.lower():
            print("\nSubject:", row["Subject"])
            print("Time:", row["StartTime"], "-", row["EndTime"])
            print("Room:", row["Room"])
            found = True

    if not found:
        print("No classes found for this day and batch.")
