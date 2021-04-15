nums = [100,3,4,2,42,35,1350,4,3536,235]

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index
def selection_sort(listNum):
    newArr = []

    for i in range(len(listNum)):
        smallest = findSmallest(listNum)
        newArr.append(listNum.pop(smallest))
    return newArr
print(nums)
print(selection_sort(nums))