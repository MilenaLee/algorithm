
def binarySearch(inputList, target):
    if not inputList:
        return -1

    start = 0
    end = len(inputList) - 1

    while start <= end:
        mid = (start+end)//2

        if inputList[mid] == target:
            return mid
        elif inputList[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1


binarySearch([0,0,2,6,7,8,10,15,18,20,26], 15)
