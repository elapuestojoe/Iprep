def cutSticks(lengths):
    results = []
    while(len(lengths) > 0):
        results.append(len(lengths))
        temp = []
        # find min O(n)
        minStick = lengths[0]
        for i in range(1, len(lengths)):
            if lengths[i] < minStick:
                minStick = lengths[i]
        #Remove min sticks and substrack from remaining ones O(n)
        for i in range(len(lengths)):
            tempStick = lengths[i] - minStick
            if(tempStick > 0):
                temp.append(tempStick)
        
        lengths = temp
    return results

print(cutSticks([5, 4, 4, 2, 2, 8]))