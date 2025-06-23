from os import system

exception_list = ["\\", "{", "}", ":", "$", "(", ")", "*", "&", "^", "#"]


class ToolBox:

    # Method to pause screen to allow user to read output
    @staticmethod
    def enter_to_continue():
        input("Press enter to continue.")

    # Method to clear terminal for better readability
    @staticmethod
    def clear_screen():
        system("cls")

    # Ensures that user inputs an integer when prompted
    @staticmethod
    def get_int(prompt: str, leave: bool = None) -> int:
        user_input = ""
        if leave and user_input.lower() == "exit":
            return -99
        while not isinstance(user_input, int):
            try:
                user_input = int(input(prompt))
            except ValueError:
                print("Input must be a whole number.\n")
            else:
                return user_input

    # Ensures that users have provided input when prompted and checks for special characters
    @staticmethod
    def get_input(prompt: str) -> str:
        user_input = ""
        while user_input.strip() == "":
            user_input = input(prompt)
            if user_input.strip() == "":
                print("Input must not be blank.\n")
                continue
            for exception in exception_list:
                if exception in user_input:
                    # Handle the exception here so that we can show user the invalid characters
                    print(exception_list)
                    print("\nPlease do not put any above special characters when answering prompts.\n")
                    raise ValueError
            else:
                return user_input

    # Gets yes or no answer from the user
    @staticmethod
    def confirm_choice(prompt: str) -> bool:
        while True:
            choice = ToolBox.get_input(prompt)
            match choice.lower():
                case 'y':
                    return True
                case 'n':
                    return False
                case _:
                    print("Invalid option\n")

    # Output the different choices for the user using a dictionary
    @staticmethod
    def create_list_from_dict(choices: dict) -> list:
        i = 0
        selections = []
        select = []
        if choices:
            for key, val in choices.items():
                select.append(f"{key}: {val}")
                i += 1
                # gather 5 items at a time
                if i == 6:
                    selections.append(list(select))
                    select.clear()
                    # Reset to get the next five
                    i = 0
                    continue
            # check if there are any missing items
            if len(select) > 0:
                selections.append(select)
        return selections

    @staticmethod
    def nest_list(choices: list) -> list:
        selections = []
        select = []
        for i in range(len(choices)):
            select.append(f"{choices[i]}")
            # gather 5 items at a time
            if (i+1) % 5 == 0:
                selections.append(list(select))
                # Reset to get the next five
                select.clear()
            elif i == len(choices)-1:
                # If at the end of the loop we have leftovers
                selections.append(select)
        return selections

    # Creates a menu for the user using a nested list
    @staticmethod
    def menu_from_list(items: list, key: bool):
        prompt = "\nEnter 'exit' to leave menu.\n" \
                 "Enter 'next' to see more choices\n" \
                 "Enter 'back' return to previous choices\n" \
                 "Enter the adjacent number to select an option: "
        list_pos = 0
        while True:
            ToolBox.clear_screen()
            print("\n")
            # Display each item in a nested list
            for i in range(len(items[list_pos])):
                print(f"[{i+1}]: {items[list_pos][i]}")
            try:
                # Get user input
                user_input = ToolBox.get_input(prompt)
                if user_input == "exit":
                    print("Leaving menu.")
                    return -1

                # If the user attempts to go to the next page
                elif user_input == "next":
                    if list_pos < len(items)-1:
                        list_pos += 1
                        print(f"Moving to page {list_pos}.")
                    else:
                        print("You are on the last page.")

                # If the user attempts to go to the previous page
                elif user_input == "back":
                    if list_pos > 0:
                        list_pos -= 1
                        print(f"Moving to page {list_pos}.")
                    else:
                        print("You are on the first page.")

                # If the user enters one of the numbers associated with a value
                elif len(items[list_pos]) >= int(user_input) > 0:
                    print(f"Selecting {items[list_pos][int(user_input)-1]}")

                    # If we need the string itself
                    if key:
                        item = items[list_pos][int(user_input) - 1].split(":", 1)
                        return item[0]
                    # return the where integer where the item is in the list
                    return (5 * list_pos) + int(user_input)-1
                else:
                    print("Invalid option.\n")

            except ValueError:
                pass
            except IndexError:
                print("Value not present.")
            ToolBox.enter_to_continue()
