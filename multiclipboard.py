"""     MULTI-CLIPBOARD
    The idea behind this application is to store multiple thing in our clipboard.
   Clipboard is that where we copy and paste our data,we only have only one save slot, so when we copy something it
   overrides what we have. Here is the idea behind the application is to store multiple things from our clipboard and
   then easily load all those things in our clipboard.
"""
import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as ref:
        json.dump(data, ref)


def load_data(filepath):
    try:
        with open(filepath, "r") as ref:
            data = json.load(ref)
            return data
    except:
        return {}


if len(sys.argv) == 2:      # we are checking that there should be two command line arguments (0- file_name, 1- command)
    command = sys.argv[1]   # Then coping that command in command variable
    data = load_data(SAVED_DATA)

    if command == "save":               # we can save/replace data in existing key
        key = input(" Enter a key : ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Data saved successfully")

    elif command == "load":
        key = input(" Enter a key : ")
        if key in data:
            clipboard.copy(data[key])
            print(" Data copied to clipboard")
        else:
            print(" Key does not exist")
    elif command == "list":
        print(data)

    elif command == "delete":
        key = input(" Enter a key to delete : ")
        del data[key]
        print("Data saved deleted ")

    else:
        print(" Unknown command")
else:
    print(" Please pass exactly one command")


"""
     summary : 
        1. so, what i have done in .this project is i have imported some modules 
        2. i have created saved_data variable that has json file (clipboard.json),
        3. which is the name of the file where i have saved data of the clipboard
        4. then there are two functions which are being used to write and read the json file
        5. 
        
"""
