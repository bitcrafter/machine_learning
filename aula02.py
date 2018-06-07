# Gradient Descent
# 1. Derivada
# 2. Maximos e Minimos da função (funcoes convexas, apenas um minimo)
# 3. Vetor Gradiente (funcoes com n vaiaveis)

import matplotlib.pyplot as mpl


def f(x):
    return (x ** 2) - (3 * x) + 2


def df(x):
    return 2 * x - 3


x = 3
n = 100
step = 0.1

lx = [x]
lf = [f(x)]
ldf = [df(x)]

for i in range(n):
    x = x - step * df(x)
    lx.append(x)
    lf.append(f(x))
    ldf.append(df(x))

print('x que minimiza f é: ', x)

mpl.plot(lx, lf, 'bo')
mpl.plot(lx, ldf, 'r+')
mpl.show()
