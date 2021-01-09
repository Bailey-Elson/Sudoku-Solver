matrix = list(input("enter numbers: "))
count = 0
hor = []
matrix2 = []
remaining = []

def displayGrid(matrix2):
    print('\n')
    for j in range(0,len(matrix2)):
        print(matrix2[j])

def generateGrid(matrix):
    count = 0
    hor = []
    for i in range(0,81):
        if count != 9:
            hor.append(matrix[i])
            count = count+1
        else:
            matrix2.append(hor)
            hor = []
            count=1
            hor.append(matrix[i])
    matrix2.append(hor)
    displayGrid(matrix2)

def emptyCells(remaining):
    for i in range(1,82):
        remaining.append(i)
    for i in range(81,0,-1):
        row = (i-1)//9
        col = (i-1)%9
        if matrix2[row][col] != '-':
            remaining.pop(row*9 + col)
    

def squareGrid(row,col,):
    rowpos = row%3
    colpos = col%3
    if rowpos == 0:
        rowarr = [1,2]
    elif rowpos == 1:
        rowarr = [-1,1]
    else:
        rowarr = [-1,-2]
    if colpos == 0:
        colarr = [1,2]
    elif colpos == 1:
        colarr = [-1,1]
    else:
        colarr = [-1,-2]
    squarenums = []
    squarearr = [[row,col],[row,col+colarr[0]],[row,col+colarr[1]],[row+rowarr[0],col+colarr[0]],[row+rowarr[0],col+colarr[1]],[row+rowarr[1],col+colarr[0]],[row+rowarr[1],col+colarr[1]],[row+rowarr[0],col],[row+rowarr[1],col]]
    return squarearr, squarenums

def checkNums(matrix2, potentialNums, exisitingNums ):
    for j in range(0,9):
        for k in range(len(potentialNums)-1,-1,-1):
            if exisitingNums[j]==potentialNums[k]:
                potentialNums.pop(k)

def solve(matrix2, remaining):
    generateGrid(matrix)
    emptyCells(remaining)
    while (len(remaining)!=0):
        for i in range(len(remaining),-1,-1):
            if len(remaining)!=0:
                row = ((remaining[i-1])-1)//9
                col = ((remaining[i-1])-1)%9
                fullrow = matrix2[row]
                fullcol=[]
                for j in range(0,9):
                    fullcol.append(matrix2[j][col])
                potentialNums = ['1','2','3','4','5','6','7','8','9']
                checkNums(matrix2, potentialNums, fullrow )
                checkNums(matrix2, potentialNums, fullcol )        
                squarearr, squarenums = squareGrid(row,col)
                for j in range(0,9):
                    squarenums.append(matrix2[squarearr[j][0]][squarearr[j][1]])
                checkNums(matrix2, potentialNums, squarenums )                  
                if len(potentialNums) == 1 and len(remaining)!=0:
                    matrix2[row][col] = potentialNums[0]
                    remaining.pop(i-1)
    displayGrid(matrix2)

solve(matrix2, remaining)
            
    
