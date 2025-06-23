CHAR_CATEGORIES = ["Name", "Class", "Str", "Dex", "Con", "Int", "Wis", "Cha",
                   "HP", "AC", "Proficiency", "Acrobatics", "Animal Handling", "Arcana",
                   "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation",
                   "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion",
                   "Sleight of Hand", "Stealth", "Survival"]


# Create list for adventures
def adv_categories() -> list:
    # Copy from character list
    new_list = CHAR_CATEGORIES
    # Replace Class for Difficulty
    new_list[1] = "Difficulty"
    return new_list


class Stats:
    def __init__(self):
        self._name = ""
        # Core stats' modifier Strength, Dexterity, Constitution, Intelligence, Wisdom, and Charisma
        self._str = 0
        self._dex = 0
        self._con = 0
        self._int = 0
        self._wis = 0
        self._cha = 0
        # Defensive stats, hit points and armor class
        self._hp = 0
        self._ac = 0
        # Skills
        self._proficiency = 0
        self._acrobatics = 0
        self._animal_handling = 0
        self._arcana = 0
        self._athletics = 0
        self._deception = 0
        self._history = 0
        self._insight = 0
        self._intimidation = 0
        self._investigation = 0
        self._medicine = 0
        self._nature = 0
        self._perception = 0
        self._performance = 0
        self._persuasion = 0
        self._religion = 0
        self._sleight_of_hand = 0
        self._stealth = 0
        self._survival = 0

    # Output stats for the user
    def display(self, key: str, pair: str) -> str:
        stats = f"Name: {self._name} {key}:{pair}\n" \
                f"Str: {self._str} Dex: {self._dex} Con: {self._con}\n" \
                f"Int: {self._int} Wis: {self._wis} Cha: {self._cha}\n" \
                f"HP: {self._hp} AC: {self._ac} Prof: {self._proficiency}\n" \
                f"Acrobatics: {self._acrobatics} Animal Handling: {self._animal_handling} Arcana: {self._arcana}\n" \
                f"Athletics: {self._athletics} Deception: {self._deception} History: {self._history}\n" \
                f"Insight: {self._insight} Intimidation: {self._intimidation} Investigation: {self._investigation}\n" \
                f"Medicine: {self._medicine} Nature: {self._nature} Perception: {self._perception}\n" \
                f"Performance: {self._performance} Persuasion: {self._persuasion} Religion: {self._religion}\n" \
                f"Sleight Of Hand: {self._acrobatics} Stealth: {self._animal_handling} Survival: {self._arcana}\n"
        return stats

    # "Getters" and "Setters"
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value: int):
        self._str = value

    @property
    def dex(self):
        return self._dex

    @dex.setter
    def dex(self, value: int):
        self._dex = value

    @property
    def con(self):
        return self._con

    @con.setter
    def con(self, value: int):
        self._con = value

    @property
    def int(self):
        return self._int

    @int.setter
    def int(self, value: int):
        self._int = value

    @property
    def wis(self):
        return self._wis

    @wis.setter
    def wis(self, value: int):
        self._wis = value

    @property
    def cha(self):
        return self._cha

    @cha.setter
    def cha(self, value: int):
        self._cha = value

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value: int):
        self._hp = value

    @property
    def ac(self):
        return self._ac

    @ac.setter
    def ac(self, value: int):
        self._ac = value

    @property
    def proficiency(self):
        return self._proficiency

    @proficiency.setter
    def proficiency(self, value: int):
        self._proficiency = value

    @property
    def acrobatics(self):
        return self._acrobatics

    @acrobatics.setter
    def acrobatics(self, value: int):
        self._acrobatics = value

    @property
    def animal_handling(self):
        return self._animal_handling

    @animal_handling.setter
    def animal_handling(self, value: int):
        self._animal_handling = value

    @property
    def arcana(self):
        return self._arcana

    @arcana.setter
    def arcana(self, value: int):
        self._arcana = value

    @property
    def athletics(self):
        return self._athletics

    @athletics.setter
    def athletics(self, value: int):
        self._athletics = value

    @property
    def deception(self):
        return self._deception

    @deception.setter
    def deception(self, value: int):
        self._deception = value

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value: int):
        self._history = value

    @property
    def insight(self):
        return self._insight

    @insight.setter
    def insight(self, value: int):
        self._insight = value

    @property
    def intimidation(self):
        return self._intimidation

    @intimidation.setter
    def intimidation(self, value: int):
        self._intimidation = value

    @property
    def investigation(self):
        return self._investigation

    @investigation.setter
    def investigation(self, value: int):
        self._investigation = value

    @property
    def medicine(self):
        return self._medicine

    @medicine.setter
    def medicine(self, value: int):
        self._medicine = value

    @property
    def nature(self):
        return self._nature

    @nature.setter
    def nature(self, value: int):
        self._nature = value

    @property
    def perception(self):
        return self._perception

    @perception.setter
    def perception(self, value: int):
        self._perception = value

    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value: int):
        self._performance = value

    @property
    def persuasion(self):
        return self._persuasion

    @persuasion.setter
    def persuasion(self, value: int):
        self._persuasion = value

    @property
    def religion(self):
        return self._religion

    @religion.setter
    def religion(self, value: int):
        self._religion = value

    @property
    def sleight_of_hand(self):
        return self._sleight_of_hand

    @sleight_of_hand.setter
    def sleight_of_hand(self, value: int):
        self._sleight_of_hand = value

    @property
    def stealth(self):
        return self._stealth

    @stealth.setter
    def stealth(self, value: int):
        self._stealth = value

    @property
    def survival(self):
        return self._survival

    @survival.setter
    def survival(self, value: int):
        self._survival = value

    # creates and returns a dictionary of the character's stats
    def stat_sheet(self):
        sheet = {
            "Name": self._name,
            "Str": self._str,
            "Dex": self._dex,
            "Con": self._con,
            "Int": self._int,
            "Wis": self._wis,
            "Cha": self._cha,
            "HP": self._hp,
            "AC": self._ac,
            "Proficiency": self._proficiency,
            "Acrobatics": self._acrobatics,
            "Animal Handling": self._animal_handling,
            "Arcana": self._arcana,
            "Athletics": self._athletics,
            "Deception": self._deception,
            "History": self._history,
            "Insight": self._insight,
            "Intimidation": self._intimidation,
            "Investigation": self._investigation,
            "Medicine": self._medicine,
            "Nature": self._nature,
            "Perception": self._perception,
            "Performance": self._performance,
            "Persuasion": self._persuasion,
            "Religion": self._religion,
            "Sleight of Hand": self._sleight_of_hand,
            "Stealth": self._stealth,
            "Survival": self._survival,
        }
        return sheet


# Individual characters that go on adventures
class Character(Stats):
    def __init__(self):
        # Add the character's class, short for specialization
        super().__init__()
        self._spec = ""

    # Create a character sheet and add the class
    def char_sheet(self):
        sheet = self.stat_sheet()
        sheet["Class"] = self._spec
        return sheet

    def display_char(self):
        return self.display(key="Class", pair=self._spec)

    # Getter and setter for Spec
    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value: str):
        self._spec = value


# The adventure that holds the benchmarks values to test characters against
class Adventure(Stats):
    def __init__(self):
        # Add the adventure's difficulty
        super().__init__()
        self._diff = ""

    # Create an adventure sheet and add the difficulty
    def adv_sheet(self):
        sheet = self.stat_sheet()
        sheet["Difficulty"] = self._diff
        return sheet

    def display_adv(self):
        return self.display(key="Difficulty", pair=self._diff)

    # Getter and setter for Spec
    @property
    def diff(self):
        return self._diff

    @diff.setter
    def diff(self, value: str):
        self._diff = value

