import argparse
import json

def update_logs(log, prefix):
    filename = 'logs/' + prefix + '.json'
    file = open(filename, 'r')
    data = json.load(file)
    file.close()

    data.append(log)

    file = open(filename, 'w')
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
            update_logs(log, "weights")

        elif currentarg[1] == "-r" or currentarg[1] == "-run":
            distance, time = currentarg[2], currentarg[3]
            log = {"distance": distance, "time": time}
            print("Recording run of "+ distance + " in time " + time)
            update_logs(log, "runs")

    elif currentarg[0] == "graph":
        print("show graph")






