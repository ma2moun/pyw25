# Initialize an empty contact book
contacts = {}

def show_menu():
    """Display the menu options"""
    print("\nContact Book Application")
    print("------------------------")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search for contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    return input("Choose an option (1-6): ")

def add_contact():
    """Add a new contact to the book"""
    name = input("Enter name: ")

    if name in contacts:
        print(f"Contact '{name}' already exists!")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    """Display all contacts"""
    if not contacts: #check if it's empty
        print("Contact book is empty.")
        return

    print("\nAll Contacts:")
    print("-------------")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print(f"Address: {info['address']}")
        print("-------------")

def search_contact():
    """Search for a contact by name"""
    if not contacts: #check if it is empty
        print("Contact book is empty.")
        return

    """
    to search by name (this can be imrpoved to ask the user
    to choose to search based on what)
    """
    search_term = input("Enter name to search: ")

    # Check for exact match
    if search_term in contacts:
        print(f"\nContact found:")
        print(f"Name: {search_term}")
        print(f"Phone: {contacts[search_term]['phone']}")
        print(f"Email: {contacts[search_term]['email']}")
        print(f"Address: {contacts[search_term]['address']}")
        return

    # Check for partial matches
    found = False
    for name in contacts:
        if search_term.lower() in name.lower():
            if not found:
                print("\nPartial matches found:")
                found = True
            print(f"- {name}")

    if not found:
        print("No contacts found matching that name.")

def update_contact():
    """Update an existing contact"""
    if not contacts:
        print("Contact book is empty.")
        return

    name = input("Enter name of contact to update: ")

    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return

    print(f"\nUpdating contact: {name}")
    print("Enter new information (leave blank to keep current value)")

    # Get current values
    current = contacts[name]

    # Get new values or keep current ones if blank
    phone = input(f"Phone [{current['phone']}]: ") or current['phone']
    email = input(f"Email [{current['email']}]: ") or current['email']
    address = input(f"Address [{current['address']}]: ") or current['address']

    # Update the contact
    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    print(f"Contact '{name}' updated successfully!")

def delete_contact():
    """Delete a contact"""
    if not contacts:
        print("Contact book is empty.")
        return

    name = input("Enter name of contact to delete: ")

    if name in contacts:
        confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ")
        if confirm.lower() == "yes":
            del contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print(f"Contact '{name}' not found!")

# Main application loop
print("Welcome to the Contact Book!")
while True:
    choice = show_menu() #function call

    if choice == "1":
        add_contact() #function call
    elif choice == "2":
        view_contacts() #function call
    elif choice == "3":
        search_contact() #function call
    elif choice == "4":
        update_contact() #function call
    elif choice == "5":
        delete_contact() #function call
    elif choice == "6":
        print("Thank you for using the Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
