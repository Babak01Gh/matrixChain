chainOfMatrices = []
numberOfMatrices = int(input('Enter the number of matrices : '))
while numberOfMatrices:
    try:
        dimInput = input(f'dimention of matrix like 3*2 : ')
        dim = dimInput.split('*')
        chainOfMatrices.append(tuple([int(dim[0]),int(dim[1])]))
        numberOfMatrices-=1
    except:
        print('There is an error in your input...')
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

def showHow(i,j):
    if i==j:
        print(f'M{i}',end='')
    else:
        k = r[i][j]
        print('(',end='')
        showHow(i, k)
        showHow(k+1, j)
        print(')',end='')