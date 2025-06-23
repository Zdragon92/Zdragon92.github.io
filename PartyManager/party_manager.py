import toolbox as tb
import database_manager
import character


# Translate the database record to a character or adventure class
def covert_entry(entry: dict, adv: bool):
    if adv:
        convert = character.Adventure()
        convert.spec = entry["Difficulty"]
    else:
        convert = character.Character()
        convert.spec = entry["Class"]

    convert.name = entry["Name"]
    convert.str = int(entry["Str"])
    convert.dex = int(entry["Dex"])
    convert.con = int(entry["Con"])
    convert.int = int(entry["Int"])
    convert.wis = int(entry["Wis"])
    convert.cha = int(entry["Cha"])
    convert.hp = int(entry["HP"])
    convert.ac = int(entry["AC"])
    convert.proficiency = int(entry["Proficiency"])
    convert.acrobatics = int(entry["Acrobatics"])
    convert.animal_handling = int(entry["Animal Handling"])
    convert.arcana = int(entry["Arcana"])
    convert.athletics = int(entry["Athletics"])
    convert.deception = int(entry["Deception"])
    convert.history = int(entry["History"])
    convert.insight = int(entry["Insight"])
    convert.intimidation = int(entry["Intimidation"])
    convert.investigation = int(entry["Investigation"])
    convert.medicine = int(entry["Medicine"])
    convert.nature = int(entry["Nature"])
    convert.perception = int(entry["Perception"])
    convert.performance = int(entry["Performance"])
    convert.persuasion = int(entry["Persuasion"])
    convert.religion = int(entry["Religion"])
    convert.sleight_of_hand = int(entry["Sleight of Hand"])
    convert.stealth = int(entry["Stealth"])
    convert.survival = int(entry["Survival"])

    return convert


# Output the evaluations for the user
# Takes a list of dictionaries created from party evaluation
def display_evals(evals: list[dict | dict[str, dict]]):
    # Display the stat
    stats = ["Strong", "Weak"]

    # ["Weak"][stat] & ["Strong"][stat]
    for i in range(len(stats)):
        print(stats[i]+":\n")
        # First get the Strong stats then the Weak stats
        for stat in evals[i].keys():
            # Show the highest value in the category and the characters in the category
            print(f"{stat}: Highest value: {evals[i][stat]}")
            print(f"Characters: {evals[2][stats[i]][stat]}\n")
        tb.ToolBox.enter_to_continue()


# Output the party for the user
def list_party(party: list):
    for i in range(len(party)):
        print(f"{i + 1}: {party[i].name}, Class: {party[i].spec}")


class PartyManager:

    def __init__(self):
        self.current_party = []
        self.party_evals = []
        self.current_adventure = None

    # Add a character within the party
    def add_to_party(self, database: database_manager):
        # Ask user for each of the info on a character
        prompt = "Please enter the name of the character to add to the party: "
        user_input = tb.ToolBox.get_input(prompt)
        char = self.search_char(database, user_input)
        # Check database for character
        if char:
            # Show character to user
            char.display_char()
            # Confirm if character is added to party
            prompt = f"Note: Adding character will remove current evaluations.\n" \
                     f"Do you want to add {char.name} ({char.spec}) to the party (y/n): "

            if tb.ToolBox.confirm_choice(prompt):
                # When a new character is added to the party, the old evaluations are obsolete
                print(f"Adding {char.name} to the party.\n")
                self.current_party.append(char)
                self.party_evals.clear()
            else:
                print(f"{char.name} will not be added to the party.\n")
        else:
            print(f"{user_input} was not found within the database.\n")

    # Create a character to add to the database
    def entry_creator(self, database: database_manager.DatabaseManager):
        # Nested list for menu
        choices = [["Character", "Adventure"]]
        choice = tb.ToolBox.menu_from_list(choices, False)
        adv = False

        if choice == 0:
            word = "Character"
            sheet = character.CHAR_CATEGORIES
        elif choice == 1:
            word = "Adventure"
            sheet = character.adv_categories()
            adv = True
        else:
            print("Leaving entry creator.")
            return

        print(f"Beginning {word} creation. Notes: {word} names must be original. Input exit instead of prompt to "
              "leave \n")
        tb.ToolBox.enter_to_continue()

        prompt = f"Enter the {word}'s "
        temp_entry = {}
        # Ask user for each of the info on a character/adventure
        for i in range(len(sheet)):
            if i < 2:
                while True:
                    try:
                        user_input = tb.ToolBox.get_input(prompt + sheet[i] + ": ").title()
                        temp_entry[sheet[i]] = user_input

                        # Allow player to exit at anytime
                        if user_input == "Exit":
                            print("Leaving character creator")
                            return

                        # If this is the name variable then check for duplicates
                        if i == 0:
                            if adv:
                                # If we find the adventure, Notify the user
                                if self.search_adv(database, name=user_input):
                                    print(f"There is already a adventure named {user_input} within the database.")
                                    # If the user does not want to continue, leave
                                    if not tb.ToolBox.confirm_choice("Input new name? (y/n)\n"):
                                        return
                                    else:
                                        raise ValueError
                            else:
                                # If we find the character, Notify the user
                                if self.search_char(database, name=user_input):
                                    print(f"There is already a character named {user_input} within the database.")
                                    # If the user does not want to continue, leave
                                    if not tb.ToolBox.confirm_choice("Input new name? (y/n)\n"):
                                        return
                                    else:
                                        raise ValueError
                    except ValueError:
                        print("Special characters (\\, {, }, :, $) are not allowed.")

                    else:
                        break
            else:
                # Now we only want integers for the other categories
                try:
                    user_input = tb.ToolBox.get_int((prompt + sheet[i] + " "), leave=True)
                    temp_entry[sheet[i]] = user_input
                    if user_input == -99:
                        print("Leaving character creator")
                        return
                except ValueError:
                    pass

        # All keys are accounted for
        name = temp_entry["Name"]
        # Collection for characters
        col = 0
        if adv:
            # If we're working on adventures then use the proper collection
            col = 2
        if database.insert(temp_entry, col):
            print(f"{name} has been added to the database")
        else:
            print(f"Failed to add {name} to the database")

    # Select a character to delete from the database
    def entry_deleter(self, database: database_manager.DatabaseManager):
        # Get entry from user
        # Nested list for menu
        choices = [["Character", "Adventure"]]
        choice = tb.ToolBox.menu_from_list(choices, False)
        adv = False

        if choice == 0:
            word = "Character"
        elif choice == 1:
            word = "Adventure"
            adv = True
        else:
            # If the exit option is chosen then we just leave
            return

        prompt = f"Please enter the name of the {word} to remove from the database: "
        user_input = tb.ToolBox.get_input(prompt).title()
        if adv:
            entry = self.search_adv(database, user_input)
        else:
            entry = self.search_char(database, user_input)
        if entry:
            # Show character to user
            if adv:
                entry.display_adv()
                col = 2
            else:
                entry.display_char()
                col = 0
            # Confirm if character is deleted from database
            prompt = f"Do you want to remove {entry.name} from the database? (y/n): "
            # Confirm removal
            if tb.ToolBox.confirm_choice(prompt):
                if database.remove({"Name": entry.name.title()}, col):
                    print(f"Removing {entry.name} from the database.\n")
                else:
                    print(f"Could not remove {entry.name} from the database.\n")
            else:
                print(f"{entry.name} will not be removed from the database.\n")
        else:
            print(f"{user_input} was not found in the database\n")

    def menu_display(self) -> str:
        party = ""
        adv = self.current_adventure
        # Check if there is a party
        if len(self.current_party) != 0:
            for char in self.current_party:
                # Add party member to the string
                party += f"{char.name}, "
            # Remove the ", " from the end of party
            party = party[:-2]

        # There are no party members
        else:
            party = "None"
        # If there is no adventure then set to none
        if not adv:
            adv = "None"
        else:
            adv = adv["Name"]
        return f"Party: {party}\n" \
               f"Adventure: {adv}\n"

    # Determine what the party is good or bad at and display to the user
    # Compare the skills of the party to an expected threshold (from an adventure)
    def party_eval(self, database: database_manager.DatabaseManager):
        weak_dict = {}
        strong_dict = {}
        individual_dict = {"Strong": {}, "Weak": {}}
        # Check if there are characters to evaluate
        if len(self.current_party) <= 0:
            print("There are no characters in the party to Evaluate.")
            return
        # Have user select an adventure

        # gather the stat sheet for the adventure
        self.current_adventure = self.set_adv(database)
        # Check if there is an adventure to compare the characters
        if self.current_adventure:
            # Check each of the party members
            for char in self.current_party:
                sheet = char.stat_sheet()
                for stat in sheet.keys():
                    # Ignore the name and class entries
                    if stat == "Name" or stat == "Class":
                        continue

                    # Check if the stat meets the threshold
                    if sheet[stat] >= self.current_adventure[stat]:

                        # Remove stat from weak dict if necessary
                        if stat in weak_dict:
                            weak_dict.pop(stat)

                        if stat in strong_dict:
                            # Update the stat if it's better than current top value
                            if sheet[stat] > strong_dict[stat]:
                                strong_dict[stat] = sheet[stat]

                        # Stat not yet in the strong_dict add it
                        else:
                            strong_dict[stat] = sheet[stat]

                        if stat in individual_dict["Strong"]:
                            # Update the amount of characters strong in the stat
                            individual_dict["Strong"][stat] += (", " + char.name)
                        else:
                            # Add stat to the individual_dict
                            individual_dict["Strong"][stat] = char.name

                    # Stat does not meet or exceed threshold
                    else:

                        if stat in weak_dict:
                            # Update the stat if it's better than current top value
                            if sheet[stat] > weak_dict[stat]:
                                weak_dict[stat] = sheet[stat]

                        elif stat in strong_dict:
                            # Check if the stat is already in the strong dict then skip
                            pass

                        # Stat is not yet in the weak_dict
                        else:
                            weak_dict[stat] = sheet[stat]

                        if stat in individual_dict["Weak"]:
                            # Update the amount of characters weak in the stat
                            individual_dict["Weak"][stat] += (", " + char.name)
                        else:
                            # Add stat to the individual_dict
                            individual_dict["Weak"][stat] = char.name

            # Once dictionaries are set up, update party_evals
            self.party_evals = [strong_dict, weak_dict, individual_dict]
            print("Displaying Evaluations\n")

            display_evals(self.party_evals)

            print("Evaluations finished.")
        else:
            print("There is no adventure prepared.")

    # Remove a character within the party
    def remove_char(self):
        prompt = "Note: Selecting a character will remove any evaluations." \
                 "Please select a character to remove from the party.\n" \
                 "Or enter 0 to return to menu: "
        while True:
            # Get character from user
            list_party(self.current_party)
            choice = tb.ToolBox.get_int(prompt)
            if choice == 0:
                break
            elif choice <= len(self.current_party):
                # Compensate for list starting at 1
                name = self.current_party[choice - 1].name
                print(f"Removing {name} from the party and resetting evaluations.")
                # Remove character from the party and reset the evaluations
                self.current_party.pop(choice - 1)
                self.party_evals.clear()
                break
            else:
                print(f"{choice} is an invalid selection")
            print("Returning to menu.")

    def search_adv(self, database: database_manager, name: str) -> character.Adventure():
        query = database.search({"Name": name.title()}, 2)
        if query:
            adv = covert_entry(query[0], True)
            return adv
        else:
            return None

    def search_char(self, database: database_manager, name: str) -> character.Character():
        query = database.search({"Name": name.title()}, 0)
        if query:
            char = covert_entry(query[0], False)
            return char
        else:
            return None

    def set_adv(self, database):
        adv_list = []
        # get all adventures from the database
        advs = database.search(query="", col=2, full=True)
        # Check database for adventures
        if advs:
            # get names of adventures
            for adv in advs:
                adv_list.append(adv["Name"])
            # Format the list for menu
            menu = tb.ToolBox.nest_list(adv_list)
            # Retrieve the name of the adventure from the
            pos = tb.ToolBox.menu_from_list(menu, False)
            # Ensure
            if pos >= 0:
                adv = advs[pos]
            else:
                return
            # Check if there is a name
            if adv:
                # When a new adventure is set, the old evaluations are obsolete
                print(f"Setting {adv['Name']} as the current adventure.\n")
                self.party_evals.clear()
                return adv

            else:
                print("No change in adventure.\n")
        else:
            print("No adventures found within the database.\n")
            return None
        tb.ToolBox.enter_to_continue()

    def show_party(self):
        # Display each of the current characters in the party
        for char in self.current_party:
            char.display_char()

    # Update a character and send to the database
    def update_entry(self, database: database_manager.DatabaseManager):
        # Nested list for menu
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
            print("Leaving entry editor.")
            return

        prompt = f"Enter the name of the {word} to update: "
        # Get entry from user input
        user_input = tb.ToolBox.get_input(prompt)
        if adv:
            entry = self.search_adv(database, user_input)
        else:
            entry = self.search_char(database, user_input)

        if entry:
            # Display the entry for the user and prepare dictionary
            if adv:
                entry.display_adv()
                dic_entry = entry.adv_sheet()
                tb.ToolBox.enter_to_continue()
            else:
                entry.display_char()
                dic_entry = entry.char_sheet()
                tb.ToolBox.enter_to_continue()

            query = {"Name": entry.name.title()}

        else:
            print(f"There is no {word} named with the name {user_input} in the database.\n")
            return
        # Create menu to get user's choice
        menu = tb.ToolBox.create_list_from_dict(dic_entry)
        while True:
            # Select which stat to change
            print("Editing")
            stat = tb.ToolBox.menu_from_list(menu, True)
            # Exit menu value
            if stat == -1:
                print("Exiting Character updater")
                return
            match stat:
                case "Class" | "Difficulty" | "Name":
                    try:
                        new_value = tb.ToolBox.get_input(f"Input the new value of {stat}: ")
                    except ValueError:
                        continue
                case _:
                    # All other stats use integer values
                    try:
                        new_value = tb.ToolBox.get_int(f"Input the new value of {stat}: ")
                    except ValueError:
                        continue

            # If everything is ok then we update the database
            new_values = {"$set": {stat: new_value}}
            if database.update(query, new_values, col):
                print("Update was successful.\n")
            else:
                print("Update was unsuccessful.\n")
