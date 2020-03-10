num =int(input())
arr = input().split()
arr2  = input().split()

array=[];array2 =[]

for i in arr:
    array.append(int(i))

for i in arr2:
    array2.append(int(i))

# print(num,'\n', array, '\n', array2)

add = 0

for i in range(num):
    add+=array[i]*array2[i]

wm = add/sum(array2)

print(round(wm,1))
