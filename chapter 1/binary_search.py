guesses = 1     
def binary_search(target, listNum, start, end):
    global guesses 
    guesses += 1
    if start > end:
        return -1
    mid = (start + end)//2
    element = listNum[mid]

    if target == element:
        print(guesses)
        return mid

    
    if target < element :
        return binary_search(target, listNum,start, mid - 1)
    else:
        return binary_search(target, listNum, mid + 1, end)

tmp = []
for i in range(1,240000 + 1):
    tmp.append(i)



print(binary_search(1,tmp,0, len(tmp) - 1))
