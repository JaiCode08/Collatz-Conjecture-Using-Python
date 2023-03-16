import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

cor = []
x = []
y = []

num = int(input("Enter a number: "))
orig = num
iter = 0
count = 0
isOne = 0
while(isOne == 0):
    if (num % 2 == 0):
        num /= 2
    else:
        num = (num * 3) + 1

    cor.append([iter, num])
    x.append(iter)
    y.append(num)

    if (num == 1):
        isOne = 1
    
    iter += 1

max = cor[0][1]

for i in range(0, len(cor)):
    if(cor[i][1] > max):
        max = cor[i][1]

if(cor[0][1] % 2 == 0):
    plt.axis([0, iter - 1, 0, max])
else:
    plt.axis([0, iter - 1, 0, max])

pointX = np.array(x)
pointY = np.array(y)

fig.suptitle('Collatz\'s Conjecture', fontsize=20)

plt.plot(pointX, pointY)
plt.show()