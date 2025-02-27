

contacts = {}

def main():
    print("Welcome to the assistant bot!")
    commands = {
        "hello": greet,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "close": goodbye,
        "exit": goodbye
    }
    while True: 
        user_input = input("Enter a command: ")
        try:
            cmd, *args = parse_input(user_input)
            if cmd in commands:
                print(commands[cmd](*args))
                if cmd == "close" or cmd == "exit":
                    break
            else:
                print("Invalid command.", "Available commands: ", ", ".join(commands.keys()))
        except Exception as e:
            print(f"Error: {e}")



def parse_input(input):
    cmd, *args = input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(*args):
    name, phone = args
    if name in contacts:
        return "Contact already exists."
    else:
        contacts[name] = phone
        return "Contact added."


def change_contact(*args):
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    else:
        contacts[name] = phone
        return "Contact updated."

def show_phone(*args):
    name = args[0]
    if name not in contacts:
        return "Contact not found."
    else:
        return contacts[name]


def show_all():
    return "\n".join([f"{name} - {phone}" for name, phone in contacts.items()])


def greet():
    return "How can I help you?"


def goodbye():
    return "Goodbye!"
    

if __name__ == "__main__":
    main()