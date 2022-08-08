def power_set(nums):
    result = [[]]
    
    for x in nums:
        print(result)
        for i in range(len(result)):
            result.append(result[i] + [x])
        
    return result

print(power_set([1,2,3]))