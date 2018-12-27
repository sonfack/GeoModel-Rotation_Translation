import numpy as np

# Number of points

def enterPoint(N=4):
    p = np.empty((N,3))

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
    row, col = M.shape

    for i in range(row):
        sumx = sumx + M[i][0]
        sumy = sumy + M[i][1]
        sumz = sumz + M[i][2]
    return sumx/row, sumy/row, sumz/row


def main():
    A = enterPoint()
    print(createCentroid(A))


if __name__ == '__main__':
    main()