a = int(input("Enter the length of the list : "))
lst = []
sum = 0

for i in range(1,a+1):
    ele = int(input(f"Enter Element {i} : "))
    lst.append(ele)

print(F"Your list is {lst}")

def addList():
    for j in range (a):
        global sum
        sum += lst[j]
    return sum

print(f"The sum of your lsit is {addList()}")

