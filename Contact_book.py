# A script that allows you to create a contact, add a contact to a contact list, find, update and remove a contact.
import re
contact_list = []
# Validation functions
def validate_number(message):
    while True:
        number = input(message)
        if number == "":
            return ""
        pattern = r"^(?:080|081|070|090|091)\d{8}$"
        if re.fullmatch(pattern, number):
            return number
        else:
            print("Enter a valid Nigerian number!")

def validate_email(message):
    while True:
        email = input(message)
        if email == "":
            return ""
        if re.fullmatch(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
            return email
        else:
            print("Enter a valid email!")

def add_contact():
    while True:
        name = input("Enter contact's name: ").title()
        number = validate_number("Enter contact's number: ")
        email = validate_email("Enter contact's email: ")
        contact = {'Name': name, 'Number': number, 'Email': email}
        contact_list.append(contact)
        print(f"{contact['Name']}'s contact has been added!")

        again = input("Do you want to add another contact? (yes/no): ")
        if again == 'no':
            break

def view_contact_list():
    if contact_list:
        print("\nYour Contacts:")
        for i, contact in enumerate(contact_list, start=1):
            print(f"{i}. {contact}")
    else:
        print("No contacts saved yet!")

def find_contact():
    search_name = input("Enter the name of the contact you want to find: ").title()
    found = False
    for contact in contact_list:
        if contact['Name'] == search_name:
            print(f"Contact found:\n{contact}")
            found = True
            break
    if not found:
        print(f"{search_name} is not in the contact list.")

def update_contact():
    update_contact = input("Enter the name of the contact you want to update: ").title()
    for contact in contact_list:
        if contact['Name'] == update_contact:
            print(f"You are about to update this contact:\n{contact}")
            new_number = validate_number("Enter new number (press enter to skip): ")
            new_email = validate_email("Enter new email (press enter to skip): ")

            if new_number:
                contact['Number'] = new_number
            if new_email:
                contact['Email'] = new_email
                
            print(f"Here is your updated contact:\n{contact}")
        else:
            print("Contact not found")

def delete_contact():
    delete_contact = input("Enter the name of the contact you want to delete: ").title()
    for contact in contact_list:
        if contact['Name'] == delete_contact:
            answer = input("Are you sure you want to delete this contact? (yes/no): ").lower()
            if answer == 'yes':
                contact_list.remove(contact)
                print(f"{delete_contact} deleted successfully")
                break
    else:
        print("Contact not found")
   

def main():

    print("----------------------------------------------------\n")
    print("Welcome to Alo's Contact Book Application\n")
    print("----------------------------------------------------\n")
    while True:
        print("\nOptions: ")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Find contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")
        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contact_list()

        elif choice == '3':
            find_contact()

        elif choice == '4':
            update_contact()

        elif choice == '5':
            delete_contact()

        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!Enter a number between 1-6.")
main()














    

