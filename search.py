# binary serach

def binary_search(A, l, h, value):
    if l > h:
        return -1
    # run binary search for valid case
    else:
        mid = (h + l)//2
        
        if A[mid] == value:
            return mid

        elif A[mid] > value:
            return binary_search(A, l , mid - 1, value)

        else:
            return binary_search(A, mid + 1 , h, value)


A = [1,2,3,5,6,7,8,9]

print(binary_search(A, 0, 7, 4))