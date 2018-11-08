#Teste Phyton
cedulas = range(0,1000)
notas=0
notasList = []
vNota = 0

while (notas!=-1):
	notas = int(input("Digite a cedula a ser acrescentada (entre 1 e 1000) "))
	notasList.append(cedulas[int(notas)])
	print(notasList)
	notasList.sort(reverse=True)
	print(notasList)

#tratamento de inconsistência da entrada do valor
while True:
	try:
		valor = int(input("Digite o valor a ser calculado: "))
		break
	except ValueError:
		print("Digite um valor numérico!")

#for que percorre a lista e calcula as notas necessárias para chegar ao valor informado
for item in notasList:
	  
	while (valor>=item):
		vNota+=1
		valor-=item
	else:
		if (vNota > 0):
			print("Emitidas %s nota(s) de %s" % (vNota, str(item)))
		vNota = 0


