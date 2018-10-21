def financialCrisis(roadRegister):
    solutions = []
    for s in range(len(roadRegister)):
        solution = []
        for y in range(len(roadRegister)):
            solutionRow = []
            if(y != s):
                for x in range(len(roadRegister[0])):
                    if(x != s):
                        solutionRow.append(roadRegister[y][x])
                solution.append(solutionRow)
        solutions.append(solution)
    return solutions


roadRegister = [[False, True,  True,  False],
                [True,  False, True,  False],
                [True,  True,  False, True ],
                [False, False, True,  False]]

# print(financialCrisis(roadRegister))
for solution in financialCrisis(roadRegister):
    print(solution)