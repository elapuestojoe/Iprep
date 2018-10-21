import itertools

print(list(itertools.permutations([1,2,3])))
print(list(itertools.combinations([1,2,3], 1)))

a = list(itertools.combinations([1,2,3],1))

print((a[0][0]))
