import math

def sudokuVerifier(solution):
    for i in range(9):
        if dupesExist(solution, i, i, 0, 8):
            return False
    for i in range(9):
        if dupesExist(solution, 0, 8, i, i):
            return False
    for i in range(3):
        for j in range(3):
            if dupesExist(solution, 3*i, 3*(i+1), 3*j, 3*(j+1)):
                return False
    return True

def dupesExist(solution, rowStart, rowEnd, colStart, colEnd):
    used = [False for x in range(10)]
    for i in range(rowStart, rowEnd):
        for j in range(colStart, colEnd):
            if used[solution[i][j]]:
                if solution[i][j] > 0:
                    return True
            used[solution[i][j]] = True
    return False

def getSpiralOrdering(arr):
    print(arr)
    numSpirals = int(len(arr[0]) / 2)
    spiralOrdering = []
    for i in range(numSpirals):
        spiralOrdering = getOneSpiral(arr, i, spiralOrdering)
    if len(arr[0]) % 2 == 1:
        spiralOrdering.append(arr[numSpirals][numSpirals])
    print(spiralOrdering)

def getOneSpiral(arr, offset, spiralArr):
    length = len(arr[0]) - offset
    for i in range(offset, length-1):
        #print(arr[offset][i])
        spiralArr.append(arr[offset][i])
    for i in range(offset, length-1):
        #print(arr[i][length-1])
        spiralArr.append(arr[i][length-1])
    for i in range(length - 1, offset, -1):
        #print(arr[length-1][i])
        spiralArr.append(arr[length-1][i])
    for i in range(length - 1, offset, -1):
        #print(arr[i][offset])
        spiralArr.append(arr[i][offset])
    return spiralArr

def generateSpiral(d):
    arr = [][]
    for y in range(d):
        for x in range(d):
            arr[y][x] = 0

def generateOneSpiral(offset, spiralArr):
    length = len(spiralArr[0]) - offset
    for i in range
                
spiral1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
spiral2 = [[1,2,3],[4,5,6],[7,8,9]]

getSpiralOrdering(spiral1)
getSpiralOrdering(spiral2)

sudoku1 = [[3,5,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

sudoku2 = [[3,5,3,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

#print(str(sudokuVerifier(sudoku1)))
#print(str(sudokuVerifier(sudoku2)))




