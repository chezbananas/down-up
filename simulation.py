import csv
import matplotlib.pyplot as plt
import random
import sys

# Runs a single game of down-up with n players, and returns the number of turns it took to complete.
def runGame(n):
    count = 0    
    while (n > 2):
        users = []
        for i in range(n):
            users.append(random.randint(0, n - 1))
            while users[i] == i:
                users[i] = random.randint(0, n - 1)
        for i in range(n):
            if i == users[users[i]]: 
                n -= 1
        count += 1
    return count

# Runs numGames down-up games with n players, and returns the average number of turns it took to complete.
def runMultiple(n, numGames):
    if n < 1:
        raise Exception("n < 1")
    count = 0
    for i in range(numGames):
        count += runGame(n)
    return count / numGames

def megaMulti(n, numGames):
    result = []
    for i in range(3, n + 1):
        result.append(runMultiple(i, numGames))
    return result


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 3:
        raise Exception("not enough arguments")
    mode = argv[1]
    n = int(argv[2])
    if mode == "multi" or mode == "megamulti":
        numGames = int(argv[3])
    if mode == "single":
        print("Game of size " + str(n) + " took " + str(runGame(n)))
    if mode == "multi":
        result = runMultiple(n, numGames)
        print("Average for size = " + str(n) + ", " + str(numGames) + " games = " + str(result))
    if mode == "megamulti":
        result = megaMulti(n, numGames)
        with open("output.csv", 'w') as file:
            writer = csv.writer(file)
            writer.writerow(["Players", "Average Length"])
            for i in range(len(result)):
                n = i + 3
                print("n = " + str(n) + ", avg length = " + str(result[i]))
                writer.writerow([n, result[i]])
        x = range(3, n + 1)
        plt.plot(x, result)
        plt.xlabel("Number of Starting Players")
        plt.ylabel("Average Number of Rounds")
        plt.title("Rounds Played vs Number of Starting Players")
        plt.show()
        plt.savefig("swag")
    if mode == "simulation":
        print("this isn't implemented yet!")
            