import numpy as np

# Number of points

def enterPoint(N=3):
    p = np.empty((3,N))
    print("Enter ",N, "point coordinate")
    for i in range(N):
        print("point ",i+1)
        p[i][0] = input("x :")
        p[i][1] = input("y :")
        p[i][2] = input("z :")

    return p

def createCentroid(M):
    sumx = 0
    sumy = 0
    sumz = 0
    N, M = M.shape()
    for i in range(N):
        sumx = sumx + M[i][0]
        sumy = sumy + M[i][1]
        sumz = sumz + M[i][2]
    return sumx/N, sumy/N, sumz/N


def main():
    enterPoint()
    print(createCentroid(4))


if __name__ == '__main__':
    main()