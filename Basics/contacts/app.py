
def display(contact_list):

    for i, (name, email) in enumerate(contact_list, start=1):
        print(f"{i}: Name: {name} -- Email: {email}")

    #counter = 1
    #for contact in contact_list:
        #print(f"{counter}: Name: {contact[0]} -- Email: {contact[1]}")
        #counter+=1


def add_contact (name, email, contact_list):
    contact_list.append((name, email))

def delete_contact(index, contact_list):
    contact_list.pop(index - 1)


def main():
    contacts = []

    while True:

        try:
            user_choice = int(input("\nEnter '1' to create a new contact. Enter '2' to view the current contacts. Enter '3' to quit. Enter 4 to delete a contact: " ))

            if user_choice not in [1,2,3,4]:
                raise ValueError("User choice is not 1 or 2")
            
            print(f"You selected {user_choice}")
        except ValueError:
            print("Invalid selection. Please enter 1 or 2")
            continue

        if user_choice == 1:
            
            user_name = input("Enter the contact's name: ")
            user_email = input("Enter the contact's email address: ")

            add_contact(user_name, user_email, contacts)

            continue

        elif user_choice == 2:
            display(contacts)
            continue

        elif user_choice == 3:
            break

        elif user_choice == 4:

            display(contacts)

            try:
                user_del = int(input("Enter the index of the contact you would like to delete: "))
                delete_contact(user_del, contacts) 
                print("Contact deleted")
            except (ValueError, IndexError):
                print("Invalid selection. No contacts were deleted")
                continue


if __name__ == "__main__":


    main()

