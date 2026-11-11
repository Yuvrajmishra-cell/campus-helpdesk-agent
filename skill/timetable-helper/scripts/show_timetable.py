import csv

# Open the timetable CSV file
with open("data/timetable.csv", "r") as file:
    timetable = csv.DictReader(file)

    # Ask the user for a day and batch
    day = input("Enter the day: ").strip()
    batch = input("Enter your batch: ").strip()

    found = False

    # Search for matching classes
    for row in timetable:
        if row["Day"].lower() == day.lower() and row["Batch"].lower() == batch.lower():
            print("\nSubject:", row["Subject"])
            print("Time:", row["StartTime"], "-", row["EndTime"])
            print("Room:", row["Room"])
            found = True

    # Show a message if no class is found
    if not found:
        print("No classes found for this day and batch.")

