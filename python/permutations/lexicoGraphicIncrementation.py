'''
Finds next lexicographic word with the given characters
'''

def incrementLexicoGraphic(word):

    # Step 1: Find from left to right decreasing point
    right = len(word)-1
    while(right > 0 and word[right] <= word[right-1]):
        right -= 1
    
    if(right == 0):
        # Word is decreased sorted, there is no lexicographic increment
        return False
    
    #Step 2: Reverse right part
    i = right
    end = len(word)-1
    while(i < end):
        word[i], word[end] = word[end], word[i]
        i+=1
        end-=1
    
    #Step 3: swap left and first biggest number from right
    left = right - 1
    for i in range(right, len(word)):
        if(word[i] > word[left]):
            word[left], word[i] = word[i], word[left]
            break
    
    #Step 4: reverse right part
    i = right
    end = len(word)-1
    while(i < end):
        word[i], word[end] = word[end], word[i]
        i+=1
        end-=1
    return True

word = [3, 5, 4, 2, 1]
# Expected result = [4,1,2,3,5]
decrease = [5,4,3,2,1]
increase = [1,2,3,4,5]
print(incrementLexicoGraphic(word))
print(incrementLexicoGraphic(decrease))
print(incrementLexicoGraphic(increase))

# Use this to generate all permutations

print("GeneratePermutations")
def generatePermutations(objects):
    objects.sort()
    print(objects)
    while(incrementLexicoGraphic(objects)):
        print(objects)
        

generatePermutations([4,3,2,1])
generatePermutations(["q", "q"])