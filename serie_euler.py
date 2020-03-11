import math as m

def SerieEuler(N):
	suma = 1.0
	n = 2
	while (n <= N):
		suma += 1.0/(n*n)
		n += 1
	return suma

N = int(input("Introduce el número de sumandos a tomar: "))

suma = SerieEuler(N)

print("La estimación de pi es {}".format(m.sqrt(6*suma)))
