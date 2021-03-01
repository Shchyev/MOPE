from random import randrange
from time import perf_counter

startProgram = perf_counter()

# Змінні

genLimitMin = 0
genLimitMax = 20

a0 = 1
a1 = 2
a2 = 3
a3 = 4

x = []
normalizedX = []

y = []
refY = 0

x0 = []
x1 = []
x2 = []
x3 = []
dx = []
x1norm = []
x2norm = []
x3norm = []

separatedX = [x1, x2, x3]
maxY = 0
result = []

# Матриця 8х3
for i in range(0, 8):
    x.append([])
    for j in range(0, 3):
        x[i].append(randrange(genLimitMin, genLimitMax))

# Значення функції відгуків та всі значення окремих факторів
for i in range(len(x)):
    y.append(a0 + a1 * x[i][0] + a2 * x[i][1] + a3 * x[i][2])
    x1.append(x[i][0])
    x2.append(x[i][1])
    x3.append(x[i][2])

# Нульові рівні факторів та значення відгуків для них
for i in range(len(separatedX)):
    x0.append((max(separatedX[i]) + min(separatedX[i])) / 2)
    dx.append((x0[i] - min(separatedX[i])))

# Нормування факторів та всі значення нормованих факторів окремо
for i in range(len(x)):
    normalizedX.append([])
    for j in range(len(x[i])):
        normalizedX[i].append(round(((x[i][j] - x0[j]) / dx[j]), 3))

for i in range(len(normalizedX)):
    x1norm.append(normalizedX[i][0])
    x2norm.append(normalizedX[i][1])
    x3norm.append(normalizedX[i][2])

# Еталонне Y
refY = a0 + a1 * x0[0] + a2 * x0[1] + a3 * x0[2]

# Точка, що задовольняє критерію(max(Y))
maxY = max(y)

# Формування та відображення результату
for i in range(len(separatedX)):
    result.append(separatedX[i])

result.append(y)
result.append(x1norm)
result.append(x2norm)
result.append(x3norm)

print("\n" + "- "*26)
print(" {:^6} {:^6} {:^6} {:^6} {:^7} {:^6} {:^6}".format("x1", "x2", "x3", "y", "x1нрм", "x2нрм", "x3нрм"))

for i in range(8):
    for j in range(7):
        print("{:>6.1f}".format(result[j][i]), end=" ")
    print("\t")

print("- "*26)
print("Еталонний Y: " + str(refY))
print(("Y, що задовольняє критерій: " + str(maxY)))
print("Час виконання програми(секунди): " + str((perf_counter() - startProgram)) + "s")
