#bubble sort= its remain greater number at last in sorting
list = [65, 83, 49, 27, 34, 12, 75]
temp = 0
for i in range(len(list)-1, 0, -1):
    for j in range(i):
        if list[j] > list[j+1]:
            temp = list[j+1]
            list[j+1] = list[j]
            list[j] = temp


print(f"bubble sort{list}")

#selection sort= its remain lesser number at start in sorting(more efficiet than bubble sort)

list1 = [55, 88, 44, 22, 33, 11, 77]
for a in range(6):
    min = a
    for b in range(a,7):
        if list1[b]<list1[min]:
            min = b

    temp = list1[a]
    list1[a] = list1[min]
    list1[min] = temp

    print(list1)

print("this is selection sort")
