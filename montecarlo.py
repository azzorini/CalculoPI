import random as rd

def PuntoAleatorio(x_min, x_max):
	return (rd.uniform(x_min, x_max), rd.uniform(x_min, x_max))

N = int(input("Introduce el número de puntos a tirar: "))

n, N_dentro = 0, 0
while (n < N):
	p = PuntoAleatorio(0, 1)
	if (p[0]*p[0] + p[1]*p[1] < 1):
		N_dentro += 1
	n += 1

print("La estimación de pi es {}".format(4.0*N_dentro/N))
