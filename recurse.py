import csv
import sys

arr = [0, 0, 0]  # base cases for n=0, 1, 2 (0 is needed in case everyone matches in one go)

# i say recursion but this is just memoization
def recurse(filename):
    with open(filename) as file:
        for line in file:
            if line[0] == 'n':
                continue
            line = line.strip()
            lst = line.split(',')
            n = int(lst[0])
            const = 0
            for i in range(2, len(lst)):
                const += float(lst[i]) * (1 + arr[n - 2 * (i - 1)])  # getting the constant terms from matches
            const += float(lst[1])  # add P(no matches)
            result = const / (1 - float(lst[1]))
            arr.append(result)
    print(arr)
    with open("recursion.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Number of Players", "Expected Rounds"])
        for i in range(3, len(arr)):
            writer.writerow([i, round(arr[i], 3)])



if __name__ == '__main__':
    filename = "500k,3-30.csv"
    recurse(filename)