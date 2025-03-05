#notes app
import sys
print("Welcome to Notes App")
print("1. Add a note")
print("2. View a note")
mode =  input("Please select an option: ")
if mode == "1":
    print("Enter the note")
    note = input()
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added")
elif mode == "2":
    with open("notes.txt") as file:
        notes = file.readlines()
    for note in notes:
        print(note)
else:
    sys.exit("Invalid option selected")