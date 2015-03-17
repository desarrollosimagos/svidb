#import random
#indice = 0
resultados=[]
contador=0
 
inicio = 10
fin = 20
 
#genera las tiradas
while inicio < fin:
                inicio=inicio + 1
                contador = contador +1
                resultados[contador]=inicio
                

#imprime los resultados
for x in range(len(resultados)-1,-1,-1):
	print resultados[x]
