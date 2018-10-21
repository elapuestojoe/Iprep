def solution(S, K):
    solution = list()
    tempK = K
    for i in range(len(S)-1, -1, -1):
        character = S[i]
        if(tempK==0):
            tempK = K
            solution.append("-")
        if(character != "-"):
            solution.append(character.upper())
            tempK -= 1
    return "".join(solution[::-1])

print(solution("2-4A0r7-4k", 4))