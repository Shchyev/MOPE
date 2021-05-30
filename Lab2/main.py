from random import randrange
import math as mt
import numpy as np
m = 5
X = [[-1, 1, -1], [-1, -1, 1]]
Y = []

minX1 = -20
maxX1 = 15

minX2 = -15
maxX2 = 35

minY1 = -40
maxY1 = 60

# Generating Y
for i in range(5):
    Y.append([])
    for j in range(3):
        Y[i].append(randrange(minY1, maxY1+1))

# Full table
table = []
for i in range(3):
    table.append([X[0][i], X[1][i], Y[0][i], Y[1][i], Y[2][i], Y[3][i], Y[4][i]])

print("- "*29)
print(" {:^5} {} {:^5} {} {:^5} {} {:^5} {} {:^5} {} {:^5} {} {:^5} {}".format("X1", "|", "X2", "|", "Y1", "|", "Y2", "|", "Y3", "|", "Y4", "|", "Y5", "|"))

for i in range(3):
    for j in range(7):
        print("{:>6.1f}".format(table[i][j]), end=" |")
    print("\t")

# Average Y
avgY1 = sum([elem[0] for elem in Y])/5
avgY2 = sum([elem[1] for elem in Y])/5
avgY3 = sum([elem[2] for elem in Y])/5

# Dispersion
dis1 = sum([((elem[0] - avgY1) ** 2) for elem in Y])/5
dis2 = sum([((elem[1] - avgY2) ** 2) for elem in Y])/5
dis3 = sum([((elem[2] - avgY3) ** 2) for elem in Y])/5

# Deviation
deviation = mt.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))


fuv1 = dis1/dis2 if dis1 >= dis2 else dis2/dis1
fuv2 = dis3/dis1 if dis3 >= dis1 else dis1/dis3
fuv3 = dis3/dis2 if dis3 >= dis2 else dis2/dis3

sigmaUv1 = ((m - 2) / m) * fuv1
sigmaUv2 = ((m - 2) / m) * fuv2
sigmaUv3 = ((m - 2) / m) * fuv3

ruv1 = abs(sigmaUv1 - 1) / deviation
ruv2 = abs(sigmaUv2 - 1) / deviation
ruv3 = abs(sigmaUv3 - 1) / deviation

print("\n" + "- "*29)
print("Average Y1: {}\nAverage Y2: {}\nAverage Y3: {}".format(avgY1, avgY2, avgY3))

print("\n" + "- "*29)
print("Dispersion 1: {}\nDispersion 2: {}\nDispersion 3: {}".format(dis1, dis2, dis3))

print("\n" + "- "*29)
print("Deviation: {}".format(deviation))

print("\n" + "- "*29)
print("Fuv 1: {}\nfuv 2: {}\nfuv 3: {}".format(fuv1, fuv2, fuv3))

print("\n" + "- "*29)
print("Sigma 1: {}\nSigma 2: {}\nSigma 3: {}".format(sigmaUv1, sigmaUv2, sigmaUv3))

print("\n" + "- "*29)
print("Ruv 1: {}\nRuv 2: {}\nRuv 3: {}".format(ruv1, ruv2, ruv3))

print("\n" + "- "*29)
print("Check of dispersion`s uniformity is..")
if ruv1 <= 2 and ruv2 <= 2 and ruv3 <= 2:
    print("Successful")
else:
    print("Failed")

mx1 = sum(X[0])/3
mx2 = sum(X[1])/3
my = (avgY1 + avgY2 + avgY3)/3
a1 = sum([elem ** 2 for elem in X[0]])/3
a2 = ((X[0][0] * X[1][0]) + (X[0][1] * X[1][1]) + (X[0][2] * X[1][2]))/3
a3 = sum([elem ** 2 for elem in X[1]])/3
a11 = (X[0][0] * avgY1 + X[0][1] * avgY2 + X[0][2] * avgY3)/3
a22 = (X[1][0] * avgY1 + X[1][1] * avgY2 + X[1][2] * avgY3)/3

# Determinants
b0 = np.linalg.det([[my, mx1, mx2], [a11, a1, a2], [a22, a2, a3]])/np.linalg.det(
    [[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])
b1 = np.linalg.det([[1, my, mx2], [mx1, a11, a2], [mx2, a22, a3]])/np.linalg.det(
    [[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])
b2 = np.linalg.det([[1, mx1, my], [mx1, a1, a11], [mx2, a2, a22]])/np.linalg.det(
    [[1, mx1, mx2], [mx1, a1, a2], [mx2, a2, a3]])

print("\n" + "- "*29)
print("Normalized regression equation: y = {:.1f} + {:.1f}x1 + {:.1f}x2".format(b0, b1, b2))

dx1 = abs(maxX1 - minX1)/2
dx2 = abs(maxX2 - minX2)/2
x10 = (maxX1 + minX1)/2
x20 = (maxX2 + minX2)/2
a0 = b0 - b1 * (x10 / dx1) - b2 * (x20/dx2)
a1 = b1/dx1
a2 = b2/dx2

print("\n" + "- "*29)
print("Naturalized regression equation: y = {:.1f} + {:.1f}x1 + {:.1f}x2".format(a0, a1, a2))
