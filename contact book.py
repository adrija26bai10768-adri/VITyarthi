import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    if name in contacts:
        print("Contact already exists! Use update instead.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts saved yet.")
        return
    print("\n--- All Contacts ---")
    for name, details in contacts.items():
        print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")
    print()


def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        details = contacts[name]
        print(f"Name: {name} | Phone: {details['phone']} | Email: {details['email']}")
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()
    if name not in contacts:
        print("Contact not found.")
        return
    phone = input(f"New phone (leave blank to keep '{contacts[name]['phone']}'): ").strip()
    email = input(f"New email (leave blank to keep '{contacts[name]['email']}'): ").strip()
    if phone:
        contacts[name]["phone"] = phone
    if email:
        contacts[name]["email"] = email
    save_contacts(contacts)
    print(f"Contact '{name}' updated.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted.")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    menu = """
--- Contact Book ---
1. Add Contact
2. View All Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()