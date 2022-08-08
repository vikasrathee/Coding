
#### Pattern: Slidinig window 

# Max(Avg) in subarray of size k

from collections import deque
import heapq
from locale import nl_langinfo
from multiprocessing.sharedctypes import Value
from queue import Queue
from unittest.mock import NonCallableMagicMock
from unittest.util import sorted_list_difference
from xml.dom import minicompat


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
from heapq import *

class Stream:

    def __init__(self) -> None:
        self.min_heap = [] # two half of the stream seen so far.
        self.max_heap = []

    def addNum(self, num) -> None :
        if not self.max_heap and -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, heappop(self.max_heap))
        elif len(self.max_heap) + 1 < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self) -> int:
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else: 
            return -self.max_heap[0]


#### Subsets
# Find all possible combinations or Power Set.

def power_set(nums):
    result = [[]]
    
    for x in nums:
        print(result)
        for i in range(len(result)):
            result.append(result[i] + [x])
        
    return result



def bst(nums, target):
    low = 0
    high = len(nums)

    while low < high:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
    
        elif nums[mid] > target:
            high = mid

        else:
            low = mid
    
    return -1



## Top k numbers

# Kth largest element in the array
 # Idea is to use heap to keep track of the k largest values. minheap wil do it.

def k_largest(arr, k):
    minheal = []
    count = 0

    for i in range(arr):
        if count < k:
            heappush(minheap, num[i])
            count += 1
        else:
            if minheap[0] < num[i]:
                heappop(minheap)
                heappush(minheap, num[i])
    
    return minheap[0]

#### K way merge algorithm
# Merge k sorted list:




class linkedlist:
    def __init__(self, Value) -> None:
        self.val = Value
        self.next = None

    def __lt__(self, other):
        return self.val < other.val


class Solution:

    def k_way_merge(self, list):
        min_heap = []

        for root in list:
            if root is not None:
                heappush(min_heap, root)
                
        head = min_heap[0]
        tail = min_heap[0]

        while min_heap:
            
            tail = min_heap[0].next
            heappushpop(next)
            head.next =  min_heap[0]
        
        return head


### 0/1 Knapsack
#Return type bool
#[1,5, 11, 5]

#Answer:
#[1,5,5], [11]


# find one subset which shows ad with elements = sum/2
def can_partition(arr):
    sum = 0
    for num in arr:
        sum += num
    
    if sum %2 != 0:
        return False
    
    return can_partition_recursive(arr, sum/2, 0)

def can_partition_recursive(nums, sum, current_index):
    if sum == 0:
        return True

    if len(nums) == 0 or current_index >= len(nums):
        return False

    if nums[current_index] <= sum:
        if can_partition_recursive(nums, sum - nums[current_index], current_index+1):
            return True

    return can_partition_recursive(nums, sum, current_index+1)
    
    

##### Courses:
def if_courses_possible(self, numCourses: int, preReq: list[list[int]] ) -> bool:

    graph = {i: [] for i in numCourses}
    in_degree = {i: 0 for i in numCourses}
    
    for pre in preReq:
        graph[pre[0]].append(pre[1])
        in_degree[pre[0]] += 1

    source = []
    for vertex in in_degree.keys:
        if in_degree[vertex] == 0:
            source.append(vertex)

    sorted_list = []
    while source:
        vertex = source.pop[0]
        sorted_list.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                source.append(child)
    
    return len(sorted_list) == numCourses


### Staircase
# 

