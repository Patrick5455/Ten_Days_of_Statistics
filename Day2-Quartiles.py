# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
arr = input().split()
arra = []

for i in arr:
    arra.append(int(i))
arra.sort()

lent = len(arra)
midIndex = lent // 2

if lent % 2 == 0:
    median = (arra[midIndex] + arra[midIndex - 1]) // 2

    q1Range = arra[0:midIndex]
    q3Range = arra[midIndex:lent]

    qlent = len(q1Range)

    # print(q1Range)

    # print(q3Range)

    if qlent % 2 == 0:
        q1 = (q1Range[len(q1Range) // 2] + q1Range[(len(q1Range) // 2) - 1]) // 2

        q3 = (q3Range[len(q3Range) // 2] + q3Range[len(q3Range) // 2 - 1]) // 2

    else:
        q1 = q1Range[len(q1Range) // 2]
        q3 = q3Range[len(q3Range) // 2]

    # print(q1Range[len(q1Range)*0.25])
    # print(q3Range[len(q3Range)*0.75])

    print(q1, end='\n')
    print(median, end='\n')
    print(q3, end='\n')

if lent % 2 != 0:

    median = arra[midIndex]

    q1Range = arra[0:midIndex]
    q3Range = arra[midIndex + 1:lent]

    qlent = len(q1Range)

    if qlent % 2 == 0:
        q1 = (q1Range[len(q1Range) // 2] + q1Range[(len(q1Range) // 2) - 1]) // 2
        q3 = (q3Range[len(q3Range) // 2] + q3Range[len(q3Range) // 2 - 1]) // 2

    else:
        q1 = q1Range[len(q1Range) // 2]
        q3 = q3Range[len(q3Range) // 2]

    print(q1, end='\n')
    print(median, end='\n')
    print(q3, end='\n')




