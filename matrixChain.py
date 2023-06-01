import numpy
def minMult(matrixChain):
    n = len(matrixChain)
    for index in range(n):
        w.append([0]*n)
        r.append([0]*n)
    for diagonal in range(1,n):
        for i in range(n - diagonal):
            j = i+diagonal
            if i==j:
                pass
            else:
                mults,kWithMin = minKgiver(matrixChain,i,j)
                w[i][j] = mults
                r[i][j] = kWithMin
    showMults(0, n-1)
    
                
def minKgiver(matrixChain,i,j):
    firstVal = float('inf')
    minimumK = -1
    for k in range(i,j):
        newVal = w[i][k] + w[k+1][j] + matrixChain[i][0]*matrixChain[k][1]*matrixChain[j][1]
        if newVal < firstVal :
            firstVal = newVal
            minimumK = k
    return (firstVal , minimumK)

def showMults(i,j):
    if i==j:
        print(f'M{i}',end='')
    else:
        k = r[i][j]
        print('(',end='')
        showMults(i, k)
        showMults(k+1, j)
        print(')',end='')
        
chainOfMatrices = [
    (3,3),
    (3,5),
    (5,2),
    (2,6),
    (6,3)
]
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

minMult(chainOfMatrices)
print('\n',numpy.array(w))
print('\n',numpy.array(r))