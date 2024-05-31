def InsertTri(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    return arr



li = [int(x) for x in input().strip().split()]

# Call the kLargest function and get the result
k_largest_list = InsertTri(li)
# Output the result
for element in k_largest_list:
    print(element, end=" ")
    print('')