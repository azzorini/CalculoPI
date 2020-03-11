import math as m

# Método de integración
# Integra la función f entre x0 y xf
def IntegralSimpsonCompuesto(f, x0, xf, N):
	if (N <= 0):
		return 0
	elif (N % 2 != 0):
		N += 1 # Necesitamos un N par por lo que si no lo es recurrimos al siguiente N

	h, suma_par, suma_impar = float(xf - x0) / N, .0, .0
	for i in range(2, N, 2):
		suma_impar += f(x0 + (i - 1) * h)
		suma_par += f(x0 + i * h)

	suma_impar = 4 * (suma_impar + f(x0 + (N - 1) * h))
	suma_par *= 2

	return (h / 3) * (f(x0) + f(xf) + suma_par + suma_impar)

# Función a integrar (la de la circunferencia en los dos primeros cuadrantes)
def f(x):
	return m.sqrt(1-x*x)

N = int(input("Introduce el número de puntos a tomar: "))

print("La estimación de pi es {}".format(4.0*IntegralSimpsonCompuesto(f, 0, 1, N)))
