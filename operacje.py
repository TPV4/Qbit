
from math import *
from sympy import *

def mnozenie(A:list, B:list)->list:

    n=len(A)
    C=[[0 for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(n):
            x=0
            for k in range(n):
                x+=A[i][k]*B[k][j]
            C[i][j]=x

    return C

def iloczyn_tensorowy(A:list, B:list)->list:

    n=len(A)*len(B)
    C=[[0 for j in range(n)] for i in range(n)]

    for i in range(len(A)):
        for j in range(len(A[i])):
            for k in range(len(B)):
                for l in range(len(B[k])):
                    C[i*len(B)+k][j*len(B[k])+l]=A[i][j]*B[k][l]

    return C

def skladanie(obwod:list)->list:
    if len(obwod)==0:
        return [[]]
    else:
        kolumny=[[[1]] for i in range(10)]
        for i in range(10):
            for j in range(len(obwod)):
                kolumny[i]=iloczyn_tensorowy(kolumny[i], obwod[j][i])
        macierz=kolumny[0]
        for i in range(1,10):
            macierz=mnozenie(macierz, kolumny[i])
        return macierz

I=[[1,0],
   [0,1]]

X=[[0,1],
   [1,0]]

Y=[[0,-1j],
   [1j,0]]

Z=[[1,0],
   [0,-1]]

H=[[sqrt(2)/2,sqrt(2)/2],
   [sqrt(2)/2,-sqrt(2)/2]]

S=[[1,0],
   [0,1j]]

SWAP=[[1,0,0,0],
      [0,0,1,0],
      [0,1,0,0],
      [0,0,0,1]]

pSWAP=[[sqrt(2)/2,0,0,sqrt(2)/2],
       [0,(1-1j)/2,(1+1j)/2,0],
       [0,(1+1j)/2,(1-1j)/2,0],
       [sqrt(2)/2,0,0,-sqrt(2)/2]]

CNOT=mnozenie(iloczyn_tensorowy(I,H),mnozenie(pSWAP, mnozenie(iloczyn_tensorowy(X,X),mnozenie(pSWAP,iloczyn_tensorowy(I,H)))))

# print(CNOT)