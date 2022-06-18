numeroPrincipal = int(input()); # Nível 1
numeros = list();

for i in range(20): 
	numero = int(input());
	if numero == -1: break
	else: numeros.append(numero);

quantidadeNumerosPrincipal = numeros.count(numeroPrincipal);

print(f"{numeroPrincipal} aparece {quantidadeNumerosPrincipal} vezes");
	