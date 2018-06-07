import matplotlib.pyplot as plt
import random as r
import math
import sys, traceback


def custo(ye, y):
    c = 0.0
    for i in range(len(y)):
        c += (ye[i] - y[i]) ** 2
    return c / len(y)


pot = [50, 100, 150, 230, 75, 90, 120, 200, 80, 140]
con = [12, 9, 7, 3, 11, 10, 6, 4, 11, 7]

for potencia in pot:
    print('potencia=', potencia)

r.seed(1)
custox = 100.0

m = len(con)

t0 = 30.0
t1 = -1.0

lcusto=[]

for i in range(100000):
    theta0 = 20 + 10 * r.random()
    theta1 = -r.random()
    ye = []
    for j in range(m):
        ye.append(theta0 + pot[j] * theta1)
    cc = custo(ye, con)
    if (cc <= custox):
        t0, t1 = theta0, theta1
        custox = cc
        lcusto.append(cc)
        plt.plot([0, 255], [t0, t0 + t1 * 255], color='gray')

print(custox, t0, t1)

plt.plot(pot, con, 'bo')
plt.plot([0, 255], [t0, t0 + t1 * 255], color='red')
plt.show()

for i in range(m):
    yec = t0 + pot[i] * t1
    print(i + 1, pot[i], con[i], yec, math.fabs(con[i] - yec))

lx = [i for i in range(len(lcusto))]
plt.plot(lx, lcusto, 'ro')

sys.exit(0);