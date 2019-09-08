def get_number_of_islands(binaryMatrix): 
    def sink(x, y):
        q = [(x, y)]
        print(x, y)
        while q:
            x, y = q.pop(0)
            binaryMatrix[x][y] = 0
            if y - 1 >= 0 and binaryMatrix[x][y-1] == 1:
                q.append((x, y-1))
            if y + 1 < len(binaryMatrix[0]) and binaryMatrix[x][y+1] == 1:
                q.append((x, y+1)) 
            if x - 1 >= 0 and binaryMatrix[x-1][y] == 1:
                q.append((x-1, y))
            if x + 1 < len(binaryMatrix) and binaryMatrix[x+1][y] == 1:
                q.append((x+1, y))



    r = len(binaryMatrix)
    c = len(binaryMatrix[0])
    islandNumber = 0

    for i in range(r):
        for j in range(c):
            if binaryMatrix[i][j] == 1:
                islandNumber += 1
                sink(i, j)
    return islandNumber


# binaryMatrix = [ [0,    1,    0,    1,    0],[0,    0,    1,    1,    1],[1,    0,    0,    1,    0],[0,    1,    1,    0,    0], [1,    0,    1,    0,    1] ]
binaryMatrix = [[1,0,1,0]]
print(get_number_of_islands(binaryMatrix))
