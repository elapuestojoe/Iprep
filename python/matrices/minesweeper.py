def minesweeper(matrix):
    width = len(matrix[0])
    height = len(matrix)
    
    result = []
    for i in range(height):
        result.append([0]*width)
    
    for y in range(height):
        for x in range(width):
            val = 0
            left = x - 1
            if(left < 0):
                left = 0
                
            right = x + 1
            if(right >= width):
                right = width - 1
                
            up = y - 1
            
            if(up < 0):
                up = 0
            down = y + 1
            if(down >= height):
                down = height - 1
            
            for j in range(up, down+1):
                for i in range(left, right+1):
                    val += (j != y or i != x) & matrix[j][i]
            result[y][x] = val
    return result

matrix = [[True, False, False],
          [False, True, False],
          [False, False, False]]
print(minesweeper(matrix))