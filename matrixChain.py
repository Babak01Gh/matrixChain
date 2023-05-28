m1 = (20,2)
m2 = (2,30)
m3 = (30,12)
m4 = (12,8)
w,r = [],[]

def matrixChain(matrixList):
    n = len(matrixList)
    for i in range(n):
        w.append([0]*n)
        r.append([0]*n)
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
        newVal = w[i][k] + w[k+1][j] + matrixList[i][0]*matrixList[k][1]*matrixList[j][1]
        if newVal < oops :
            oops = newVal
            retk = k
    return (oops , retk)

matrixChain([m1,m2,m3,m4])

def showHow(i,j):
    if i==j:
        print(f'M{i}',end='')
    else:
        k = r[i][j]
        print('(',end='')
        showHow(i, k)
        showHow(k+1, j)
        print(')',end='')

showHow(0, 3)