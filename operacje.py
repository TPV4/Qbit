
# from math import *
# from sympy import *
from cmath import sqrt, cos, sin, exp, pi
# import numpy as np

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
        # macierz=[[1]]
        # wiersze=[I for n in range(len(obwod))]
        # for i in range(len(obwod)):
        #     for j in range(10):
        #         wiersze[i]=mnozenie(wiersze[i],obwod[i][j])
        # for i in range(len(obwod)):
        #     macierz=iloczyn_tensorowy(macierz, wiersze[i])
        kolumny=[[[1]] for i in range(10)]
        for i in range(10):
            j=0
            while j<len(obwod):
                kolumny[i]=iloczyn_tensorowy(kolumny[i], obwod[j][i])
                if len(obwod[j][i])==4:
                    j+=2
                else:
                    j+=1
        macierz=kolumny[0]
        for i in range(1,10):
            macierz=mnozenie(macierz, kolumny[i])
        for i in range(len(macierz)):
            for j in range(len(macierz[i])):
                if type(macierz[i][j])==complex:
                    if macierz[i][j].imag==0:
                        macierz[i][j]=round(macierz[i][j].real,2)
                    else:
                        macierz[i][j]=complex(round(macierz[i][j].real,2),round(macierz[i][j].imag,2))
                else:
                    macierz[i][j]=round(macierz[i][j],2)
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

SX=[[(1+1j)/2,(1-1j)/2],
    [(1-1j)/2,(1+1j)/2]]

Rx=[[cos(pi/4), -1j*sin(pi/4)],
    [-1j*sin(pi/4), cos(pi/4)]]

Ry=[[cos(pi/4), -sin(pi/4)],
    [sin(pi/4), cos(pi/4)]]

Rz=[[exp(-1j*pi/4), 0],
    [0, exp(1j*pi/4)]]

SWAP=[[1,0,0,0],
      [0,0,1,0],
      [0,1,0,0],
      [0,0,0,1]]

iSWAP=[[1,0,0,0],
      [0,0,1j,0],
      [0,1j,0,0],
      [0,0,0,1]]

pSWAP=[[sqrt(2)/2,0,0,sqrt(2)/2],
       [0,(1-1j)/2,(1+1j)/2,0],
       [0,(1+1j)/2,(1-1j)/2,0],
       [sqrt(2)/2,0,0,-sqrt(2)/2]]

pSWAP2=[[1,0],[0,1]]

CNOT=[[1,0,0,0],
      [0,1,0,0],
      [0,0,0,1],
      [0,0,1,0]]

rCNOT=[[1,0,0,0],
      [0,0,0,1],
      [0,0,1,0],
      [0,1,0,0]]
# pSWAP1=[[sqrt(2)/2,0],
#         [0,(1-1j)/2]]
# pSWAP2=[[0,sqrt(2)/2],
#         [(1+1j)/2,0]]
# pSWAP3=[[0,(1+1j)/2],
#         [sqrt(2)/2,0]]
# pSWAP4=[[(1-1j)/2,0],
#         [0,-sqrt(2)/2]]



# CNOT=mnozenie(iloczyn_tensorowy(I,H),mnozenie(pSWAP, mnozenie(iloczyn_tensorowy(X,X),mnozenie(pSWAP,iloczyn_tensorowy(I,H)))))

# print(CNOT)