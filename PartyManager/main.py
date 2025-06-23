# Party Manager program that allows to add to and select from an existing database of characters.
# Once characters are selected, they can be edited or added to a list. Once added to the list characters can be removed
# or the whole list (party) can be evaluated to see how well they would fare in certain situations.
import toolbox as tb
import database_manager as db
import party_manager as pm

MENU = "Party Manager System Menu.\n" \
         "[1] Register/Login an account.\n" \
         "[2] Add entry to database. (Login needed)\n" \
         "[3] Remove entry from database. (Login needed)\n" \
         "[4] Update entry from database. (Login needed)\n" \
         "[5] Search database for a entry.\n" \
         "[6] Display Names of entries in the database.\n" \
         "[7] Add character to party from the Database.\n" \
         "[8] Remove character from party.\n" \
         "[9] Evaluate Party. \n" \
         "[10] Convert database to csv file.\n"  \
         "[0] Exit Application. \n"

USER_CATEGORIES = ["Username", "Email", "Password"]

# Current active account
logged_in = False


# Prompt the user to create an account
def account_creation():
    temp_user = {}
    for key in USER_CATEGORIES:
        prompt = f"Note: Enter 'exit' to return to menu.\n" \
                 f"Enter your {key}: "
        while True:
            try:
                user_data = tb.ToolBox.get_input(prompt)
                # Check if the user is trying to exit
                print(f"{key}: {user_data}")
                if user_data.lower() == "exit":
                    print("Leaving account creator.")
                    return
                # If the user already exists
                elif key == "Username" and database.search({key: user_data}, 1):
                    print(f"User {user_data} already exists.\n")
                    raise ValueError
            except ValueError:
                pass
            else:
                temp_user[key] = user_data
                break
    # All pairs have been entered, insert data into the database
    username = temp_user["Username"]
    # Confirm user has been added to the database
    if database.insert(temp_user, 1):
        print(f"{username} has been added to the database")
    else:
        print(f"Failed to add {username} to the database")
    # Set to ensure that account_menu does not return True accidentally
    return False


# Have user attempt to log in
def account_login() -> bool:
    keys = ["Username", "Password"]
    inputs = []

    print("Beginning account login. Notes: Input exit instead of prompt to leave \n")
    tb.ToolBox.enter_to_continue()
    for key in keys:
        prompt = f"Enter 'exit' to return to menu.\n"\
                 f"Enter your {key}: "

        # Ensure user enters the prompts or leaves on their own
        while True:
            try:
                user_data = tb.ToolBox.get_input(prompt)
                if user_data.lower() == "exit":
                    print("Leaving account login.")
                    return False
            except ValueError:
                pass
            else:
                inputs.append(user_data)
                break

    # Setup query to search the database
    query = {"$and": [{keys[0]:inputs[0]}, {keys[1]:inputs[1]}]}
    if database.search(query, 1):
        print("login Succeeded.")
        return True
    else:
        print("login Failed.")
        return False


def account_menu():
    choices = [["Login", "Register"]]
    choice = tb.ToolBox.menu_from_list(choices, False)

    if choice == 0:
        # Log into account
        return account_login()

    elif choice == 1:
        # Register account
        account_creation()
    else:
        print("Leaving account screen.")
        return


# Search the database for all characters and display their names and class
def display_entries():
    choices = [["Character", "Adventure"]]
    choice = tb.ToolBox.menu_from_list(choices, False)
    adv = False

    if choice == 0:
        word = "Character"
        col = 0
    elif choice == 1:
        word = "Adventure"
        adv = True
        col = 2
    else:
        print("Leaving entry display.")
        return
    results = database.search(query={}, col=col, full=True)
    if results:
        for i in range(len(results)):
            # Output based on the correct collection
            if adv:
                print(f"[{i}]: {results[i]['Name']} - {results[i]['Difficulty']}")
            else:
                print(f"[{i}]: {results[i]['Name']} - {results[i]['Class']}")

    # If no entries are found
    else:
        print(f"No {word}s found in the database.")


# Search the database for a character using the user's input
def search():
    choices = [["Character", "Adventure"]]
    choice = tb.ToolBox.menu_from_list(choices, False)
    adv = False

    if choice == 0:
        word = "Character"
    elif choice == 1:
        word = "Adventure"
        adv = True
    else:
        print("Leaving entry editor.")
        return

    prompt = f"Enter the name of the name of the {word} to search: "
    try:
        # Set to title case to match
        user_input = tb.ToolBox.get_input(prompt).title()
        if adv:
            entry = party.search_adv(database, user_input)
        else:
            entry = party.search_char(database, user_input)

        # Check if this is an adventure or a character and display entry
        if entry and adv:
            print(entry.display_adv())
        elif entry:
            print(entry.display_char())
        else:
            print(f"The {word} {user_input} does not exist in the database")
    except ValueError:
        pass


if __name__ == '__main__':
    menu_loop = True
    database = db.DatabaseManager()
    party = pm.PartyManager()
    # Set up database if there is none
    database.database_import()
    print("Welcome to the Party Manager Application!\n")
    while menu_loop:
        # Clear the screen at the beginning of the loop for readability
        tb.ToolBox.clear_screen()
        option = tb.ToolBox.get_int(MENU + party.menu_display())
        match option:
            case 1:
                print("Account Screen.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                logged_in = account_menu()

                tb.ToolBox.enter_to_continue()

            case 2:
                print("Adding a new entry to database.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                if logged_in:
                    party.entry_creator(database)
                else:
                    print("User must be logged in to use this feature.\n")

                tb.ToolBox.enter_to_continue()

            case 3:
                print("Searching for an entry to remove from database.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                if logged_in:
                    party.entry_deleter(database)
                else:
                    print("User must be logged in to use this feature.\n")

                tb.ToolBox.enter_to_continue()

            case 4:
                print("Updating entry from the database.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                if logged_in:
                    party.update_entry(database)
                else:
                    print("User must be logged in to use this feature.\n")

                tb.ToolBox.enter_to_continue()

            case 5:
                print("Searching by entry name in the database.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                search()

                tb.ToolBox.enter_to_continue()

            case 6:
                print("Displaying entries in the database.\n")
                tb.ToolBox.clear_screen()

                display_entries()

                tb.ToolBox.enter_to_continue()

            case 7:
                print("Add a character to party.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                party.add_to_party(database)

                tb.ToolBox.enter_to_continue()

            case 8:
                print("Selecting character to remove from party.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                party.remove_char()

                tb.ToolBox.enter_to_continue()

            case 9:
                print("Evaluating party.\n")
                tb.ToolBox.enter_to_continue()
                tb.ToolBox.clear_screen()

                party.party_eval(database)

                tb.ToolBox.enter_to_continue()

            case 10:
                print("Writing Characters and Adventures collections to csv files.")
                database.database_export()
                tb.ToolBox.enter_to_continue()

            case 0:
                menu_loop = False
                print("Exiting Application.\n")

            # Default case
            case _:
                print("Invalid option.\n")
                tb.ToolBox.enter_to_continue()
