lst = []

n = int(input("Enter the number of elements : "))

count = 1
for i in range (0,n):
    element = int(input(f"input the {count} number in the list : "))
    lst.append(element)
    count += 1
print(lst)
num_to_find = int(input("Give the number to find : "))

def search (lst,n,num_to_find):
    for num in range (0,n):
        if (lst[num] == num_to_find):
            return num
    return -1

ind = search(lst, n, num_to_find)


if ind == -1:
    print("Number is not in the list")
else:
    print(f"The number is found at the posiion number {ind+1}")
input()