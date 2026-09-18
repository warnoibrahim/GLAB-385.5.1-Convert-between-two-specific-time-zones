# Event Handling Application
import datetime
import json
from pathlib import Path


# Create the path to the data folder and JSON file
DATA_FOLDER = Path(__file__).parent / "data"
DATA_FILE = DATA_FOLDER / "events.json"


def load_events():
    """Load existing events from events.json."""

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return {}


# Load saved events into the dictionary when the program starts
db = load_events()


def save_events():
    """Save the db dictionary inside events.json."""

    # Create the data folder if it does not already exist
    DATA_FOLDER.mkdir(exist_ok=True)

    # "w" creates events.json or replaces its existing contents
    with open(DATA_FILE, "w") as file:
        json.dump(db, file, indent=4)


def add_event():
    event_name = input("Enter the event name: ")
    date_input = input("Enter the event date (YYYY-MM-DD): ")

    try:
        # Verify that the user entered a valid date
        datetime.datetime.strptime(date_input, "%Y-%m-%d")

    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")
        return

    # Add the event to the Python dictionary
    db[event_name] = date_input

    # Copy the dictionary into data/events.json
    save_events()

    print("Event added successfully!")


def list_events():
    if not db:
        print("No events found.")
        return

    print("\nSaved Events:")

    for event_name, event_date in db.items():
        print(f"{event_name}: {event_date}")


def main():
    while True:
        print("\nEvent Management System")
        print("1 Add Event")
        print("2 List Events")
        print("3 Quit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            add_event()

        elif choice == "2":
            list_events()

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()