import json

class Database:

    def add_data(self,name,email,password):
        with open("db.json", "r") as file:
            database = json.load(file)

        if email in database:
            return 0
        else:
            database[email] = [name,password]
            with open("db.json", "w") as file:
                json.dump(database,file)
            return 1


    def search_data(self,email,password):
        with open("db.json", "r") as file:
            database = json.load(file)
        
        if email not in database:
            return 0
        else:
            if database[email][1] == password:
                return [email,database[email][0]]
            else:
                return 0

