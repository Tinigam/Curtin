#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A

def insertionSort(A):
    for i in range(1, len(A)):
        ptr = A[i]
        j = i - 1
        while j >= 0 and A[j] > ptr:
            A[j + 1] = A[j]
            j -= 1
            A[j + 1] = ptr
    return A

def selectionSort(A):
    for i in range(len(A)):
        minIdx = i
        for j in range(i + 1, len(A)):
            if A[minIdx] > A[j]:
                minIdx = j
        temp = A[minIdx]
        A[minIdx] = A[i]
        A[i] = temp
    return A

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...

testArray = [180, 0 ,234, 12, 490, 23, 32321]
# print(bubbleSort(testArray))
# print(insertionSort(testArray))
# print(selectionSort(testArray))