#metodos computacionais
#metodo da bissecao
#David Turati

import math

#voce devera mudar a equacao  aqui nesta funcao 
def Funcao(x):						   #funcao que encontra o valor de f() para qualquer numero enviado como argumento (a,b ou x)
	return x**3 -x -2 #<-- muda a equacao AQUI 

#funcao realiza o calculo da bissecao
def Bissecao(a,b):
	#ATENCAO NA LINHA DE BAIXO
	er = 0.001                        #margem de erro a ser calculado, o erro deve ser mudado AQUI
	vt =[0,0,0,0,0,0,0]                #cria lista com elementos a serem calculados
	
	#["vt[0]=k","vt[1]=x","vt[2]=a","vt[3]=b","vt[4]=f(x)","vt[5]=f(a)","vt[6]=f(b)"] #apenas para auxilo visual
	
	#primeira iteracao, fora do loop
	vt[0]=1				               #valor da primeira iteracao
	vt[1]=float(a+b)/2                 #encontra o valor inicial de x
	vt[2]=float(a)		               #valor inicial de a
	vt[3]=float(b)		               #valor inicial de b
	vt[4]=float(Funcao(vt[1]))	       #valor inicial de f(x)
	vt[5]=float(Funcao(vt[2]))		   #valor inical de  f(a)
	vt[6]=float(Funcao(vt[3]))		   #valor inicial de  f(b)
	
	#loop que realiza o calculo
	while abs(vt[4]) > er:
		print(vt)                       #imprime a tabela a cada novo calculo
		if (vt[4])*vt[5] > 0:			#testa condicao entre f(x) e a
			vt[0]=vt[0]+1				#incrementa nova iteracao
			vt[2]=vt[1]					#muda valor de a
			vt[5]=float(Funcao(vt[2]))  #calcula o valor de f(a)
			vt[6]=float(Funcao(vt[3]))  #calcula o valor de f(b)
			vt[1]=float(vt[2]+vt[3])/2	#calcula novo valor de x
			vt[4]=float(Funcao(vt[1]))  #calcula o valor de f(x)
		elif (vt[4]*vt[6]) > 0:
			vt[0]=vt[0]+1				#incrementa novovalor a iteracao
			vt[3]=vt[1]					#muda valor de b
			vt[5]=float(Funcao(vt[2]))  #valor inical de  f(a)
			vt[6]=float(Funcao(vt[3]))  #valor inicial de  f(b)
			vt[1]=float(vt[2]+vt[3])/2  #calcula novo valor de x
			vt[4]=float(Funcao(vt[1]))  #valor inicial de f(x)
	print(vt)                           #imprime o ultimo calculo
	print("O valor procurado e:")
	print(vt[1]) 						#imprime valor aproximado de x
#fim da funcao bissecao

print("Entre com os intervalos:")
#a=input()
#b=input()
Bissecao(1,2)							#chama a funcao que faz calculo da bissecao

