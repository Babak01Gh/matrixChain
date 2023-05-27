m1 = ([
    [1,1,1],[2,2,2],[3,3,3]
],3,3)
m2 = ([
    [1,1,1],[2,2,2]
],2,3)
m3 = ([
    [1,1,1,1],[2,2,2,2],[3,3,3,3]
],4,4)
w = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
r = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def matrixChain(matrixList):
    for i in range(len(matrixList)):
        for j in range(len(matrixList)):
            if i==j:
                pass
            else:
                muls,k = test(matrixList,i,j)
                
                
def test(matrixList,i,j):
    oops = float('inf')
    retk = -1
    for k in range(i,j):
        newVal = w[i,k] + w[k+1,j] + matrixList[i][1]*matrixList[k][1]*matrixList[j][2]
        if newVal < oops :
            oops = newVal
            retk = k
        

test(2,2)