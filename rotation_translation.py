import numpy as np
from scipy.linalg import svd

# Number of points

def enterPoint(N=3):
    p = np.empty((N,3))
    print("Enter ",N, "point coordinate")
    for i in range(N):
        print("point ",i+1)
        p[i][0] = input("x :")
        p[i][1] = input("y :")
        p[i][2] = input("z :")

    return p

def createCentroid(M):
  return np.mean(M, axis=0)

def covarianceMatrix(A,Ca, B, Cb):
    row, col = A.shape
    sum = np.zeros(A.shape)
    for i in range(row):
        Bs = (B[i] - Cb)
        Bt = Bs.transpose()
        sum = sum + np.dot((A[i] - Ca), Bt)
    return sum

def USVt_SVD(H):
    return svd(H)

def main():



    A = enterPoint()
    Ca = createCentroid(A)

    B = enterPoint()
    Cb = createCentroid(B)

    H = covarianceMatrix(A, Ca, B,Cb)
    print("cov Matrix")


    #H= np.matrix([[1, 0, 0, 0, 2],[0, 0, 3, 0, 0],[0, 0, 0, 0, 0],[0, 2, 0, 0, 0]])
    #H = np.array([[1, 2], [3, 4], [5, 6]])
    #H = np.array([[2, 2], [-1, 1]])
    print(H)

    U, S, V = USVt_SVD(H)
    print("U", U.shape)
    print(U)
    print("S", S.shape)
    print(S)
    print("V", V.shape)
    print(V)


    #Rotation
    R  = V*U.transpose()
    print("Rotation", R)

    #Translation
    T = -1*R*Ca + Cb
    print("Transaltion", T)

if __name__ == '__main__':
    main()