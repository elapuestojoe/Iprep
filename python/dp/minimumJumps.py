
# O(n^2)
def minimumJumps(arr):
    dp = [-1] * len(arr)
    dp[0] = 0
    for i in range(1, len(arr)):
        for j in range(i):
            if(i <= arr[j] + j and dp[j] != -1):
                if(dp[i] != -1):
                    dp[i] = min(dp[i], dp[j] + 1)
                else:
                    dp[i] = dp[j] + 1
                break
    return dp[-1]

# print(minimumJumps([1,3,6,1,0,9]))
# print(minimumJumps([0, 1, 1, 9]))

#Linear approach
def linearMinimumJumps(arr):
    if(len(arr) <= 1):
        return 0
    
    if(arr[0] == 0):
        return -1

    ladder = arr[0]
    stairs = arr[0]
    jumps = 1
    for level in range(1, len(arr)):
        if(level == len(arr)-1):
            return jumps
        
        if(level + arr[level] > ladder):
            ladder = level + arr[level]
        
        stairs -= 1
        if(stairs == 0):
            jumps+=1

            newStairs = ladder - level

            if(newStairs == stairs):
                return - 1
            else:
                stairs = newStairs
            
    return jumps

print(linearMinimumJumps([1,3,6,1,0,9]))
print(linearMinimumJumps([1, 1, 0, 9]))
print(linearMinimumJumps([0, 1, 1, 9]))
print(linearMinimumJumps([1,9,3,0,0,0,0]))