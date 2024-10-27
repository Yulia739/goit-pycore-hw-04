from prettytable import PrettyTable

def add_contact(args, contacts):
    '''User adding'''
    name, phone_number = args
    contacts[name] = phone_number
    return f"Contact added."

def change_contact(args, contacts):
    '''Changing the phone number by user name'''
    name, phone_number = args
    if name in contacts:
        contacts[name] = phone_number
    else: return(f"User not found")
    return f"Contact updated."

def show_phone(args, contacts):
    '''Display user phone number by name'''
    name = args[0]
    if name in contacts:
        phone_number = contacts[name]
        return f"Your phone number is: {phone_number}"
    else: return f"User not found"

def show_all_contacts(contacts):
    '''Display information about all users'''
    table = PrettyTable()
    table.field_names = ["Name", "Phone Number"]
    for name, phone_number in contacts.items():
        table.add_row([name, phone_number])
    print(f"All users information:\n{table}")