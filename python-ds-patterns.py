
#### Pattern: Slidinig window 

# Max(Avg) in subarray of size k

from collections import deque
from queue import Queue
from unittest.mock import NonCallableMagicMock


def maxavg_subarray(arr, k):    
    if k > len(arr):
        return None

    max_avg = float("-inf")
    sum = 0
    start = 0
    
    
    for end in range(0, len(arr)):
        sum += arr[end]

        if end > k-1:
            sum -= arr[start]
            max_avg = max(max_avg, sum/k)
            start += 1

    return max_avg


# time_complexity = O(n*k)  

## how to make it O(n). Summation can be changes to make it run in linear time.
   
#arr = [1,2,3,4,5,6,7,8,9]
#print(maxavg_subarray(arr, 3))


#### Pattern: Two pointer approach

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def two_sum_0(arr, target):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target and i != j:
                return (i,j)


def two_sum_1(arr, target):
    num_map = {}

    for i, num in enumerate(arr):
        if target - num in num_map:
            return [i, num_map[target - num]]
        else:
            num_map[arr[i]] = i

    return [-1, -1]


def two_sum(arr, target):
    left = 0
    right = len(arr) -1

    while arr[left] + arr[right] == target:



arr = [1,2,3,4,5,6,7,8,9]
print(two_sum(arr, 9))




#############
# fast and slower pointers.


def detect_cycle(head):

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        fast = fast.next.next
        slow = slow.next
    
    return False


# Get the node where cycle is started
def cycle_node(head):

    slow = head
    fast = head
    current = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            while current is not slow:
                slow = slow.next
                current = current.next
            return slow
    return None



## Merge intervals

# Merge the intervals which are overlapping.

def merge_intervals(A):
    
    A = A.sort(key=lambda x: x[0])

    result = []
    start = A[0][0]
    end = A[0][1]
    
    for i in range(1, len(A)):
        if A[i][0] > end:
            result.append([start, end])
            start = A[i][0]
            end = A[i][1]
        else:
            end = max(A[i][1], end)
    
    result.append([start, end])

    return result

#### Cyclic Sort
## sample run: 3,2,0,4,1

def cyclic_sort(arr):
    start = 0
    while start < len(arr):
        num = arr[start]

        if num != start and num < len(arr):
            swap(arr[num], arr[start])
        else:
            start += 1
    
    for i in range(len(arr)):
        if arr[i] != i:
            return i

    return len(arr)


### reverse linked list:

def reverse_ll_inplace(head):
    if head is None:
        return head

    curr= head
    prev = None
    
    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    head = prev
    return 

### BFS
# Level oder traversal of the binary tree.

def  level_order_traversal(root):
    if not root:
        return

    result = []    
    q = []
    q.append(root)

    while q:
        level_size = len(q)
        current_level = []
        for i in range(level_size):
            node = q.pop(0)
            current_level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        result.append(current_level)

    return result


# DFS -- Path sum (root to leaf is total )

def path_sum(root, sum):
    if root is None:
        return False

    if root.val == sum and root.left is None and root.right is None:
        return True
    
    return path_sum(root.left, sum - root.val) or path_sum(root.right, sum - root.val)
    



# Two heap
# find median in a data stream.


class Stream:

    def __init__(self) -> None:
        
        pass


    def addNum(self, num) -> None :
        pass

    def find_median(self) -> int:
        pass











        















    
