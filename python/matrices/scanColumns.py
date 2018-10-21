def scanColumns(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if(matrix[j][i] == 0):
                break
            print(matrix[j][i], end="")
        print("")
matrix =    [[0,1,1,2],
             [0,5,0,6],
             [10,1,2,3]]

scanColumns(matrix)