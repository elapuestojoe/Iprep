'''
Given two cells on the standard chess board, determine whether they have the same color or not.

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true.

'''

def chessBoardCellColor(cell1, cell2):
    asciiUpperStart = 65
    numberStart = 48
    cell1Position = [ord(cell1[0])-asciiUpperStart+1, ord(cell1[1])-numberStart]
    cell2Position = [ord(cell2[0])-asciiUpperStart+1, ord(cell2[1])-numberStart]
    
    cell1Color = (cell1Position[0] ^ cell1Position[1]) & 1
    cell2Color = (cell2Position[0] ^ cell2Position[1]) & 1
    
    return cell1Color == cell2Color