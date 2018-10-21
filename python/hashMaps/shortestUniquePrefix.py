
def shortestUniquePrefix(array):
    indexArray = [1]*len(array)

    solved = False
    while(not solved):
        dictionary = {}
        conflicts = {}

        for i in range(len(array)):
            word = array[i]
            prefix = word[:indexArray[i]]
            
            if(prefix not in dictionary):
                dictionary[prefix] = [i]
            else:
                dictionary[prefix].append(i)
                conflicts[prefix] = True
        
        if(len(conflicts.keys()) == 0):
            solved = True
        else:
            for key in conflicts.keys():
                for i in dictionary[key]:
                    indexArray[i] += 1
    
    words = []
    for i in range(len(array)):
        words.append(array[i][:indexArray[i]])
    print(words)
shortestUniquePrefix(["zebra", "dog", "duck", "dove"])

# This can be optimized by using a trie