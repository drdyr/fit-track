import argparse
import json

def update_runs(log):
    file = open('logs/runs.json', 'r')
    data = json.load(file)
    file.close()

    data.append(log)

    file = open('logs/runs.json', 'w')
    json.dump(data, file, indent=1)
    file.close()

def update_weights(log):
    file = open('logs/weights.json', 'r')
    data = json.load(file)
    file.close()

    data.append(log)

    file = open('logs/weights.json', 'w')
    json.dump(data, file, indent=1)
    file.close()

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
            weight = currentarg[2]
            log = {"weight": weight}
            print("Recording weight of "+weight)
            update_weights(log)

        elif currentarg[1] == "-r" or currentarg[1] == "-run":
            distance, time = currentarg[2], currentarg[3]
            log = {"distance": distance, "time": time}
            print("Recording run of "+ distance + " in time " + time)
            update_runs(log)

    elif currentarg[0] == "graph":
        print("show graph")






