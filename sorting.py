## Bubble sort algorithm.

def swap(A, x, y):
    # temp = A[x]
    # A[x] = A[y]
    # A[y] = temp

    ### Alternative way
    (A[x], A[y]) = (A[y], A[x])

## Bubble Sort
# Bubble which are now values moving to start for increasing sort order 
def bubble_sort(A):
    swap = True
    for iter in range(len(A)):
        if not swap:
            return 
        swap = False
        for i in range(len(A) - iter - 1):
            if A[i] > A[i+1]:
                swap = True
                A[i], A[i+1] = A[i + 1], A[i] 

## Selection Sort       
# array = sorted_part + unsorted_part
def selection_sort(A):
    for i in range(0, len(A)-1):
        for j in range(i, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i] 


def insertion_sort(A):

    for pos in range(1,len(A)):
        i = pos - 1
        print(A)
        while A[i+1] < A[i] and i >= 0:
            (A[i+1], A[i]) = (A[i], A[i+1])
            i -= 1
        
def merge_sort(A):
    if len(A) > 1:
        m = len(A)//2
        
        L = A[:m]
        R = A[m:]

        merge_sort(L)
        merge_sort(R)

        i = j = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                A[i+j] = R[j]
                j += 1
            else:
                A[i+j] = L[i]
                i += 1
        
        while i < len(L):
            A[i + j] = L[i]
            i += 1
        
        while j < len(R):
            A[i + j] = R[j]
            j += 1


def partition(A, l, h):
    if l != h and l<h:
        pivot = A[l]
        i = l + 1 
        j = h

        while i < j:
            
            while A[i] < pivot:
                i += 1
            
            while A[j] > pivot:
                j -= 1
            if i < j:
                A[i], A[j] = A[j], A[i]
       
    
        A[l], A[j] = A[j], A[l]
        return j 


def partition(arr, l, h):
  low, high = l, h
  if l != h and l < h:
    # Choose the leftmost element as pivot
    pivot = arr[l]
    low = low+1
    # Traverse through all elements
    # compare each element with pivot
    while low <= high:
      if arr[high] < pivot and arr[low] > pivot:
        arr[high], arr[low] = arr[low], arr[high]
      if not arr[low] > pivot:
        low += 1
      if not arr[high] < pivot:
        high -= 1
  arr[l], arr[high] = arr[high], arr[l]
  # Return the position from where partition is done
  return high
  
def quick_sort(A, l, h):
    if l < h:
        p = partition(A, l, h)
        quick_sort(A,l,p-1)
        quick_sort(A,p+1,h)

# Test Cases
A = [4, 2, 5, 7, 1, 8, 10, 9, 7]
quick_sort(A, 0, 8)
print(A)

# def myFunc(e):
#     return len(e) 

# A= [4, 2, 5, 7]
# A= ["Vikas", "Vi", "V", "Vika"]
# A.sort(key=myFunc)
# print(A)
