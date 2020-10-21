import argparse

currentarg = [""]

while currentarg[0] != "quit":
    currentarg = input("fit-track: ").split()
    if currentarg[0] == "help":
        print("\n------ Commands & Help ------\n\n"
              "track        [-w] [-weight] [-r] [-run]\n"
              "graph        [-flags]\n")
    elif currentarg[0] == "track":
        if len(currentarg) < 3:
            print("Invalid syntax\ntrack [-w <weight>] [-r <distance> <time>]")
        elif currentarg[1] == "-w" or currentarg[1] == "-weight":
            print("Recording weight of "+currentarg[2])
        elif currentarg[1] == "-r" or currentarg[1] == "-run":
            print("Recording run of "+currentarg[2] + " in time "+currentarg[3])
    elif currentarg[0] == "graph":
        print("show graph")