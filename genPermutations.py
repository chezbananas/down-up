import csv
from itertools import product
import random
import sys

def pure(n):
    prods = []
    for roll in product([i for i in range(n)], repeat=n):
        trash = False
        for i in range(n):
            if roll[i] == i:
                trash = True
        if trash:
            continue
        prods.append(roll)
    count = 0
    countsArr = [0 for i in range(n // 2 + 1)]
    probArr = [0 for i in range(n // 2 + 1)]
    average = 0
    realCount = 0
    numPerms = (n - 1) ** n
    for arr in prods:
        flag = False
        curr = 0
        for i in range(n):
            if i == arr[arr[i]]: 
                flag = True
                realCount += 0.5
                curr += 0.5
                average += 1 / numPerms / n
        if flag:
            count += 1
        curr = int(curr)
        countsArr[curr] += 1
        probArr[curr] += 1 / numPerms
    print("percentage of trials with 1 or more pairs: " + str(count / numPerms))  # percentage of trials with 1 or more pairs
    print("weighted number of pairs: " + str(realCount / numPerms))  # average number of pairs
    print("number of possible permutations = " + str(numPerms))
    print(countsArr)
    print(probArr)
    print("average probability of a number finding a pair: " + str(average))  # for any given number, probability that it found a pair
    # with open("permutations.csv", 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Number of Matches", "Probability"])
    #     for i in range(len(probArr)):
    #         writer.writerow([i, probArr[i]]
    for i in range(len(probArr)):
        probArr[i] = round(probArr[i], 5)
    probArr.insert(0, n)
    return probArr

def estimate(n, numTrials):
    count = 0   
    countsArr = [0 for i in range(n // 2 + 1)]
    probArr = [0 for i in range(n // 2 + 1)]
    average = 0
    realCount = 0
    numPerms = (n - 1) ** n
    for j in range(numTrials):
        flag = False
        users = []
        curr = 0
        for i in range(n):
            users.append(random.randint(0, n - 1))
            while users[i] == i:
                users[i] = random.randint(0, n - 1)
        for i in range(n):
            if i == users[users[i]]: 
                flag = True
                realCount += 0.5
                curr += 0.5
                average += 1 / numTrials / n
        if flag:
            count += 1
        curr = int(curr)
        countsArr[curr] += 1 / numTrials * numPerms
        probArr[curr] += 1 / numTrials
    print("percentage of trials with 1 or more pairs: " + str(count / numTrials))  # percentage of trials with 1 or more pairs
    print("weighted number of pairs: " + str(realCount / numTrials))  # average number of pairs
    print(countsArr)
    print(probArr)
    print("average probability of a number finding a pair: " + str(average))  # for any given number, probability that it found a pair
    # with open("permutations.csv", 'w') as file:
    #     writer = csv.writer(file)
    #     writer.writerow(["Number of Matches", "Probability"])
    #     for i in range(len(probArr)):
    #         writer.writerow([i, probArr[i]])
    for i in range(len(probArr)):
        probArr[i] = round(probArr[i], 5)
    probArr.insert(0, n)
    return probArr

def writeLine(arr, maxNum):
    # for i in range(maxNum  + 1 - len(arr)):
    #     arr.append(0)
    arr = arr[:maxNum + 2]
    with open("permutations.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow(arr)

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == "single":
        n = int(sys.argv[2])
        label = "actual"
        if (n > 8):
            numTrials = 500000
            label = "ESTIMATE"
        print("n = " + str(n) + ", " + label)
        if (n <= 8):
            result = pure(n)
            writeLine(result, 10)
        else:
            estimate(n, numTrials)
    if mode == "multi":
        n = int(sys.argv[2])
        maxNum = int(sys.argv[3])        
        numTrials = 500000
        with open("permutations.csv", 'w') as file:
            writer = csv.writer(file)
            arr = [i for i in range(maxNum + 1)]
            arr.insert(0, "n")
            writer.writerow(arr)
        for i in range(3, n + 1):
            if i < 8:
                writeLine(pure(i), maxNum)
            else:
                writeLine(estimate(i, numTrials), maxNum)
