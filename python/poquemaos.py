quantidadeDoces = int(input()) # Nível 2
poquemaos = [int(input()) for indice in range(3)]
poquemaosEvoluidos = 0
	
for valor in sorted(poquemaos):
	quantidadeDoces -= valor
	if (quantidadeDoces >= 0): poquemaosEvoluidos += 1 		
		
print(poquemaosEvoluidos)
