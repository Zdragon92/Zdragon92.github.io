import pymongo
import csv


class DatabaseManager:
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    dblist = my_client.list_database_names()
    party_db = my_client["Party"]
    collections = ["characters", "users", "adventures"]

    # Adds an item to the database given a dictionary entry,and collection number
    def add_to_database(self, entry: dict, col: int):
        entry = self.party_db[self.collections[col]].insert_one(entry)
        print(entry.inserted_id)

    # Compiles characters in the database to csv file
    def database_export(self):
        for item in self.collections:
            entry_list = []
            field_names = []
            # We do not want to export the users collection
            if item == "users":
                continue
            col = self.party_db[item]
            # Add all characters to a list
            # We do not want the id key
            for entry in col.find({}, {"_id": 0}):
                entry_list.append(entry)

            # Get keys from the given dictionary
            for key in entry_list[0].keys():
                field_names.append(key)

            # Creates csv file with the name of the collection
            with open("csv\\" + item + ".csv", mode="w", newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=field_names)
                writer.writeheader()
                writer.writerows(entry_list)

    # Import the database from a csv file if no collection is present
    def database_import(self):
        # Gather list of existing collections.
        check_list = self.party_db.list_collection_names()

        for col in self.collections:
            # if the collection does not exist then we create it
            if col not in check_list:
                collection_list = []
                data_list = []
                # check if collection already exists
                collection = self.party_db[col]
                # Using with open to handle file closing
                file = "csv\\" + col.title() + ".csv"
                # Use csv file to fill database
                try:
                    with open(file, mode='r') as data_file:
                        csv_file = csv.reader(data_file)
                        for line in csv_file:
                            if ";" in line[0]:
                                # split the lines to create proper lists
                                data_list.append(line[0].split(";"))
                            else:
                                data_list.append(line[0])
                        # For each list minus the first which will be used for dictionary keys
                        try:
                            for i in range(len(data_list) - 1):
                                # reset the dictionary
                                collection_dict = {}
                                for j in range(len(data_list[0])):
                                    # Create dictionary of entries using the first list as keys
                                    # Check if we need to convert a string entry to an int entry
                                    if data_list[i + 1][j].isdigit():
                                        collection_dict.update({data_list[0][j]: int(data_list[i + 1][j])})
                                    else:
                                        collection_dict.update({data_list[0][j]: data_list[i + 1][j]})
                                # Add entry to list to be sent to database
                                collection_list.append(collection_dict)
                            # Once all entries are added to the list, send to the database
                            x = collection.insert_many(collection_list)
                            # show the id field to prove the insert was properly conducted
                            print(x.inserted_ids)
                        except IndexError:
                            pass
                except FileNotFoundError:
                    print(f"File {file} does not exist")

    def insert(self, vals: dict, col: int):
        doc = self.party_db[self.collections[col]].insert_one(vals)
        if doc.inserted_id:
            return True
        else:
            return False

    # searches the database given a query and collection and possibly a list
    def search(self, query: dict, col: int, sort: list = None, full: bool = None):
        if sort:
            doc = self.party_db[self.collections[col]].find(query, {"_id": 0}).sort(sort[0], sort[1])
        elif full:
            doc = self.party_db[self.collections[col]].find()
        else:
            doc = self.party_db[self.collections[col]].find(query, {"_id": 0})
        results = list(doc)
        if len(results) == 0:
            return False
        else:
            return results

    # removes an item from the database given a query and collection
    def remove(self, query: dict, col: int) -> bool:
        doc = self.party_db[self.collections[col]].delete_one(query)
        # Check if the document was deleted
        if doc.deleted_count == 1:
            return True
        else:
            return False

    def update(self, query: dict, new_vals: dict, col):
        doc = self.party_db[self.collections[col]].update_one(query, new_vals)
        if doc.modified_count == 1:
            return True
        else:
            return False
