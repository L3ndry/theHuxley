numeros = input() # Nível 1
numeros = numeros.split()

for i in sorted(numeros): print(int(i), end = " ")
