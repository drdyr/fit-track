import argparse

currentarg = [""]

while currentarg[0] != "quit":
    currentarg = input("fit-track: ").split()
    if currentarg[0] == "help":
        print("HELP COMMANDS HERE !!!")
    elif currentarg[0] == "track":
        if len(currentarg) < 3:
            print("Invalid syntax")
        elif currentarg[1] == "-w":
            print("Recording weight of "+currentarg[2])
        elif currentarg[1] == "-o":
            print("Recording run of "+currentarg[2] + " in time "+currentarg[3])
    elif currentarg[0] == "graph":
        print("show graph")