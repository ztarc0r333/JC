import json


# open the json file and save the data into the database
def code_storage(code):
    if code:
        with open("database/codes_db.json", "w") as f:
            json.dump(code, f)
    else:
        print("No code to store")
