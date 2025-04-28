# A notes application with file storage

import os
from datetime import datetime

# File to store notes
NOTES_FILE = "notes.txt"

def show_menu():
    """Display the main menu"""
    print("\nWeclome To My Notes Application")
    print("----------------------")
    print("1. Create a new note")
    print("2. View all notes")
    print("3. Search notes")
    print("4. Exit")
    return input("Choose an option (1-4): ")

def create_note():
    """Create a new note and save it to file"""
    title = input("Enter note title: ")
    content = input("Enter note content: ")

    # Get current timestamp (Try without strftime)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the note
    note = f"--- {title} ({timestamp}) ---\n{content}\n\n"

    # Append to the notes file
    try:
        with open(NOTES_FILE, "a") as file:
            file.write(note)
        print("Note saved successfully!")
    except Exception as e:
        print(f"Error saving note: {e}")

def view_notes(): #Display all saved notes

    try:
        if not os.path.exists(NOTES_FILE):
            print("No notes found.")
            return

        with open(NOTES_FILE, "r") as file:
            notes = file.read()

        if notes.strip():
            print("\n=== Your Notes ===")
            print(notes)
        else:
            print("No notes found.")
    except Exception as e:
        print(f"Error reading notes: {e}")

def search_notes(): #Search for notes containing a keyword
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return

    keyword = input("Enter search term: ")

    try:
        with open(NOTES_FILE, "r") as file:
            lines = file.readlines()

        found = False
        current_note = []
        displaying = False

        for line in lines:
            if line.startswith("--- "):  # Start of a note
                # If we were displaying a note, print it
                if displaying:
                    print("".join(current_note))

                # Check if this new note matches
                if keyword.lower() in line.lower():
                    displaying = True
                    found = True
                    current_note = [line]
                else:
                    displaying = False
                    current_note = []
            elif displaying:
                current_note.append(line)

        # Display last note if it matched
        if displaying:
            print("".join(current_note))

        if not found:
            print(f"No notes found containing '{keyword}'.")
    except Exception as e:
        print(f"Error searching notes: {e}")

# Main application loop
print("Welcome to the Notes App!")
while True:
    choice = show_menu()

    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        print("Thank you for using the Notes App. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
