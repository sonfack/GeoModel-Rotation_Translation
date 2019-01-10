import numpy as np
import math
from scipy.linalg import svd
from scipy.spatial import distance


# Number of points

def enterPoint(N=3):
    p = np.empty((N,3))
    print("Enter ",N, "point coordinate")
    for i in range(N):
        print("point ",i+1)
        p[i][0] = input("x :")
        p[i][1] = input("y :")
        p[i][2] = input("z :")

    return np.asmatrix(np.array(p)).transpose()

def createCentroid(M):
  return np.mean(M, axis=1)

def covMatrix(A,Ca, B, Cb):
    row, col = A.shape
    H = np.zeros((row, col))
    for j in range(col):
        print("=========================================")
        print((A[:,j] - Ca)*(B[:,j]- Cb).transpose())
        print("=========================================")
        H = H + ((A[:,j] - Ca)*(B[:,j]- Cb).transpose())
    return H

def error(T, R, A, B):
    row, col = A.shape
    err = 0
    center = np.zeros((row,1))
    for j in range(col):
        V = R*A[:, j] + T - B[:, j]
        err = err + math.pow(distance.euclidean(center, V), 2)
    return err

def USVt_SVD(H):
    return svd(H)

def main():
    A = enterPoint()
    print('matrix', A)
    Ca = createCentroid(A)
    print('matrix Ca', Ca)
    print("\n")
    B = enterPoint()
    print('matrix', B)
    Cb = createCentroid(B)
    print('matrix Cb', Cb)
    print("\n")
    print("cov Matrix")
    H = covMatrix(A, Ca, B,Cb)
    print(H)
    print("\n")
    U, S, V = USVt_SVD(H)
    print("U", U.shape)
    print(U)
    print("\n")
    print("S", S.shape)
    print(S)
    print("\n")
    print("V", V.shape)
    print(V)
    print("\n")
    #Rotation
    R  = V*U.transpose()
    print("Rotation", R)
    print("\n")
    #Translation
    T = -1*R*Ca + Cb
    print("Transaltion", T)
    print("\n")
    #erreur
    err = error(T, R, A, B)
    print("Erreur : ", err)
if __name__ == '__main__':
    main()