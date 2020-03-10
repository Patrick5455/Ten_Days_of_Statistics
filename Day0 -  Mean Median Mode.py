# Enter your code here. Read input from STDIN. Print output to STDOUT

# read input from file/user
import sys

userInput = sys.stdin.readlines()
# print(userInput)
arr = [];
arra = []

arrayLen = int(userInput[0])
# print(arrayLen)

for i in range(1, len(userInput)):
    arr.append(userInput[i])

for i in arr:
    x = i.split()

for i in x:
    arra.append(int(i))

# perform summary statistics
if len(arra) == arrayLen:
    # mean
    mean = sum(arra) / arrayLen

    # median
    arra.sort()
    if arrayLen % 2 != 0:
        median = arra[arrayLen // 2]
        print(arra)
    else:
        medianIndex = arrayLen // 2
        median = (arra[medianIndex] + arra[medianIndex - 1]) / 2

    # mode
    dico = {}
    low_mode = 0

    # gather frequency
    for i in range(arrayLen):
        total = 0
        for num in arra:
            # if num equals my current index value
            if num == arra[i]:
                total += 1
                dico[num] = total

    # check for modal key
    for k, v in dico.items():
        if v > low_mode:
            low_mode = v
            modal = k
    if low_mode == 1:
        mode = arra[0]
    else:
        mode = modal

print("{0:.1f}".format(mean))
print("{0:.1f}".format(median))
print(mode)