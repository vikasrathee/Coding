# import requests
# import mysql.connector
# import pandas as pd

# Roblox collects lots of time-series data.  Here is some represented by an array of integers, where the index indicates the time point (eg: minute 0 => value is 8):

# [ 8, 9, 10, 11, 12 (lp), 10, 9, 8, 7, 8 (lp), 6 ]

# Please write a method or function that takes in time series data like above and returns all local peaks.  A local peak is defined as any time the line is trending upwards, and begins trending downwards.  In the above example index 4 (value 12) is a peak and index 9 (value 8) is a peak.

# (2) There is a case where the data comes up to a plateau, meaning a peak value across consecutive data points (eg 1,2,3,4,4,4,3,2,1).  Plateaus should be handled by returning one value or index to represent the peak in the plateau (eg 4 from above example).  If returning the index, any index along the plateau is valid (leading edge, trailing edge, somewhere in the middle if you want to make things very difficult; this should be left to the candidate to decide).


def get_local_peak(A):
    if len(A) == 0:
        return []
    if len(A) == 1:
        return [0]
        
    res = []
    
    if A[0] > A[1]:
        res.append(0)
    
   
    for i in range(1, len(A)-1):
        if A[i] > A[i-1] and A[i] > A[i+1]:
            res.append(i)
    
    if A[len(A)-1 ] > A[len(A)-2]:
        res.append(len(A)-1) 
        
    return res
    
def get_local_peak_hanle_plateau(A):
    if len(A) == 0:
        return []
    if len(A) == 1:
        return [0]
        
    res = []
    start = False
    
    for i in range(1, len(A)):

        if A[i] > A[i-1]:
            start = True
            peak_index = i
        elif A[i] < A[i-1] and start == True:
            start = False
            res.append(peak_index)
        
    return res
    
    
    
print(get_local_peak_hanle_plateau([10, 8, 9, 10, 11, 12, 12, 12, 10, 9, 8, 7, 8, 6 ]))
#print(get_local_peak([ 10, 9, 10, 11, 12, 10, 9, 8, 7, 8, 9 ]))