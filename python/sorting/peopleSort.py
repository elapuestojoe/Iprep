def merge(l, r):
    i = 0
    j = 0
    result = []
    while(i < len(l) and j < len(r)):
        if(l[i] < r[j]):
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    
    while(i < len(l)):
        result.append(l[i])
        i+=1
    while(j < len(r)):
        result.append(r[j])
        j+=1
    return result

def mergeSort(a):
    if(len(a) < 2):
        return a
    else:
        midPoint = len(a)//2
        left = mergeSort(a[:midPoint])
        right = mergeSort(a[midPoint:])
        return merge(left,right)
    
def sortByHeight(a):
    people = []
    for i in range(len(a)):
        if(a[i] != -1):
            people.append(a[i])
    
    people = mergeSort(people)
    peopleIndex = 0
    for i in range(len(a)):
        if(a[i] != -1):
            a[i] = people[peopleIndex]
            peopleIndex+=1
    
    return a

print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]))
