import numpy as np
import matplotlib.pyplot as plt
import math

# definimos nossa tolerância e o máximo que o programa vai procurar
E = 1e-6
MAX_ITER = 100

# matriz para armazenar os valores durante a bisseção
matriz = np.zeros((MAX_ITER, 6))


def f(x, function):
    return eval(function)


def bissecao(a, b, m, function):
    i = 0
    while i < MAX_ITER:
        c = (a + b) / 2
        m[i, 0] = i
        m[i, 1] = a
        m[i, 2] = b
        m[i, 3] = c
        m[i, 4] = f(c, function)
        if f(c, function) == 0.0 or (b - a) / 2 < E:
            m[i, 5] = m[i, 3] - m[i - 1, 3] if i > 0 else 0.0
            m[0, 5] = 0.0
            if f(c, function) == 0.0:
                print(
                    f"A raiz exata foi encontrada em X {i}, e seu valor é {round(c, 5)}"
                )
            else:
                print(
                    f"A raiz aproximada foi encontrada em X {i}, e seu valor é {round(c, 5)}"
                )
            return c, i + 1
        elif f(a, function) * f(c, function) < 0:
            m[i, 5] = math.fabs(b - c)
            b = c
        else:
            m[i, 5] = math.fabs(a - c)
            a = c
        i += 1


# Solicita ao usuário a função
function = input("Digite a função (em termos de 'x'): ")

# Solicita ao usuário o intervalo desejado
a = float(input("Digite o limite inferior do intervalo: "))
b = float(input("Digite o limite superior do intervalo: "))

# Realiza a bisseção
root, rows_filled = bissecao(a, b, matriz, function)
xn, xn2 = bissecao(a, b, matriz, function)
# Imprime a matriz
print("n       An      Bn      Xn      F(Xn)   E")
for row in matriz[:rows_filled]:
    print(" ".join(f"{val:.5f}" for val in row))

# Gerar valores para o eixo x
x = np.linspace(a, b, 100)
# Calcular os valores da função no intervalo
y = f(x, function)

# Plotar o gráfico da função
plt.plot(x, y, label='f(x) = x^2 - 4')
# Plotar o último ponto de iteração
plt.scatter(xn,
            f(xn, function),
            color='red',
            label='Ponto Aproximado ou exato')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função com o último ponto de aproximação')
plt.legend()
plt.grid(True)
plt.show()
