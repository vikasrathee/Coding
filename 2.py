def power_set(nums):
    result = [[]]
    
    for x in nums:
        print(result)
        for i in range(len(result)):
            result.append(result[i] + [x])
        
    return result

#print(power_set([1,2,3]))

def LCS(X, Y):
    m = len(X)
    n = len(Y)

    # Cahce for DP solution
    T = [[None] * (n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                T[i][j] = 0
            elif X[i-1] == Y[j-1]:
                T[i][j] = 1 + T[i-1][j-1]
            else:
                T[i][j] = max(T[i-1][j], T[i][j-1])
                
    return T[m][n]      

X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", LCS(X, Y))




def LIS(X):
    dp = [1] * len(X)
    
    for i in range(len(X)):
        for j in range(0 , i):
            if X[i] > X[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    res = -1

    for i in range(len(dp)):
        res = max(res, dp[i])
    return res

print(LIS([1,2,1]))






### Transactional Key value Store




