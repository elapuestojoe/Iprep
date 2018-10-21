''' You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to set all bits between i and j in N equal to M
(e.g., M becomes a substring of N located at i and starting at j)
'''

def twobit(N, M, i, j):
    for x in range(i, j + 1):
        b = M & 1
        M = M >> 1
        N = N | (b << x)
    return N

N = 1024
M = 21
print(bin(N))
print(bin(M))
print(bin(twobit(N, M, 2, 6)))

print(-3 & (1))