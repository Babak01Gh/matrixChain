# matrixChain multiplication
this algorithm gets some matrices with their dimentions
and gives the order that gives minimum multiplication number

## more information about
[matrixChain wikipedia](https://en.wikipedia.org/wiki/Matrix_chain_multiplication)

## give an example of input&output

**example input dimentions**
```
chainOfMatrices = [
    (3,3),
    (3,5),
    (5,2),
    (2,6),
    (6,3)
]
```

**output**
```
minMult(chainOfMatrices)

result order :

    ((M0(M1M2))(M3M4))

multiples matrix :

     [  0  45  48  84 102]
     [  0   0  30  66  84]
     [  0   0   0  60  66]
     [  0   0   0   0  36]
     [  0   0   0   0   0]

R matrix :

     [0 0 0 2 2]
     [0 0 1 2 2]
     [0 0 0 2 2]
     [0 0 0 0 3]
     [0 0 0 0 0]
```