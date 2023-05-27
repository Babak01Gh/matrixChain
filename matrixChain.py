m1 = ([
    [1,1],[2,2],[3,3]
],3,2)
m2 = ([
    [1,1,1],[2,2,2]
],2,3)
m3 = ([
    [1,1,1,1],[2,2,2,2],[3,3,3,3]
],3,4)
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
    n = len(matrixList)
    for k in range(1,n):
        for i in range(n - k):
            j = i+k
            if i==j:
                pass
            else:
                muls,kk = test(matrixList,i,j)
                w[i][j] = muls
                r[i][j] = kk
    return r[0][n-1]
                
def test(matrixList,i,j):
    oops = float('inf')
    retk = -1
    for k in range(i,j):
        newVal = w[i][k] + w[k+1][j] + matrixList[i][1]*matrixList[k][2]*matrixList[j][2]
        if newVal < oops :
            oops = newVal
            retk = k
    return (oops , retk)
        

print(matrixChain([m1,m2,m3]))