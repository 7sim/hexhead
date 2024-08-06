import os
from datetime import datetime
import random
import webbrowser

def email_checker(database):
    username = input("Enter username to search: ").lower()
    clear_screen()

    found = False
    for line in database:
        user_data = line.strip().split(':')
        if user_data[0].lower() == username:
            if len(user_data) >= 3:
                email = user_data[2]
                print(f"Email found: {email}")
                found = True
            else:
                print("Email not found for this user.")
            break

    if not found:
        print("Username not found in the database.")

    input("Press Enter to continue...")

def pg_finder():
    keyword = input("Enter keyword to search: ").lower()
    clear_screen()

    found = False
    matching_usernames = []
    with open('usernames.txt', 'r') as file:
        for line in file:
            if keyword in line.lower():
                matching_usernames.append(line.strip())
                found = True

    if found:
        print("Matching usernames:")
        for username in matching_usernames:
            print(username)
    else:
        print("No usernames found containing the keyword.")

    input("Press Enter to continue...")

def pgbable_accounts():
    clear_screen()

    random_number = random.randint(1, 1000000)
    link = "https://www.roblox.com/users/" + str(random_number)
    print("Generated link:", link)
    open_link_in_browser(link)

    input("Press Enter to continue...")

def owners_list():
    clear_screen()

    directory = "ownerlists"
    txt_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.txt')]

    if not txt_files:
        print("No .txt files found in the 'ownerlists' directory.")
        input("Press Enter to continue...")
        return

    print("Options:")
    for index, file in enumerate(txt_files, start=1):
        print(f"{index}. {os.path.splitext(os.path.basename(file))[0]}")

    choice = input("Enter the option number to view its contents: ")

    try:
        choice_index = int(choice) - 1
        selected_file = txt_files[choice_index]
        with open(selected_file, 'r') as file:
            print(f"Contents of {selected_file}:")
            print(file.read())
    except (ValueError, IndexError):
        print("Invalid option.")

    input("Press Enter to continue...")

def save_results(keyword, matching_usernames):
    if not os.path.exists('results'):
        os.makedirs('results')

    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"results/{keyword}_search_{current_time}.txt"

    with open(file_name, 'w') as file:
        for username in matching_usernames:
            file.write(username + '\n')

    return file_name

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_link_in_browser(link):
    webbrowser.open(link)

def main():
    with open('database.txt', 'r') as file:
        database = file.readlines()

    while True:
        clear_screen()
        
        print("\033[91m██░ ██ ▓█████ ▒██   ██▒ ██░ ██ ▓█████ ▄▄▄      ▓█████▄ ")
        print("▓██░ ██▒▓█   ▀ ▒▒ █ █ ▒░▓██░ ██▒▓█   ▀▒████▄    ▒██▀ ██▌")
        print("▒██▀▀██░▒███   ░░  █   ░▒██▀▀██░▒███  ▒██  ▀█▄  ░██   █▌")
        print("░▓█ ░██ ▒▓█  ▄  ░ █ █ ▒ ░▓█ ░██ ▒▓█  ▄░██▄▄▄▄██ ░▓█▄   ▌")
        print("░▓█▒░██▓░▒████▒▒██▒ ▒██▒░▓█▒░██▓░▒████▒▓█   ▓██▒░▒████▓ ")
        print(" ▒ ░░▒░▒░░ ▒░ ░▒▒ ░ ░▓ ░ ▒ ░░▒░▒░░ ▒░ ░▒▒   ▓▒█░ ▒▒▓  ▒ ")
        print(" ▒ ░▒░ ░ ░ ░  ░░░   ░▒ ░ ▒ ░▒░ ░ ░ ░  ░ ▒   ▒▒ ░ ░ ▒  ▒ ")
        print(" ░  ░░ ░   ░    ░    ░   ░  ░░ ░   ░    ░   ▒    ░ ░  ░ ")
        print(" ░  ░  ░   ░  ░ ░    ░   ░  ░  ░   ░  ░     ░  ░   ░    ")
        print("                                                 ░      \033[0m")

        print("Options:")
        print("1. Email Finder")
        print("2. Username Scraper")
        print("3. Pgable Accs")
        print("4. Owners List")
        print("5. Exit")
        choice = input("Enter your choice: ")

        clear_screen()

        if choice == '1':
            email_checker(database)
        elif choice == '2':
            pg_finder()
        elif choice == '3':
            pgbable_accounts()
        elif choice == '4':
            owners_list()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
