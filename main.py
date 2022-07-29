from tkinter import *
import random
janela = Tk()
matrizBotao=[]
matrizJogo=[]

informacao=[22,22,10,0,0,"n"]#x,y,porcentagem bombas,num bombas,spc,estado jogo(derrota('n' ou 's'))

def bomba(i,g):
    matriz = matrizBotao[informacao[1]*i+g]
    if matriz["bg"] != "#DCDCDC" and informacao[5] == "n":
        if matriz["bg"]!="#ff0000":
            matriz["bg"]="#ff0000"
            informacao[3] -= 1
            
            bombasInfo["text"] = "Bombas: " + str(informacao[3])
        else:
            matriz["bg"]="#000000"
            informacao[3] += 1
            bombasInfo["text"] = "Bombas: " + str(informacao[3])

def clicou(i,g,c):
	c.append([i,g])
	st = []
	if matrizJogo[i][g]==1 and matrizBotao[i*informacao[1]+g]["bg"]!="#ff0000" and informacao[5]=="n":
		bombasInfo["text"] = "Perdeu"
		informacao[5] = "s"
		for j in range(informacao[0]):
			for z in range(informacao[1]):
				if matrizJogo[j][z] == 1:
					matrizBotao[informacao[1]*j+z]["bg"]="#ffffff"
	elif matrizJogo[i][g]==0 and matrizBotao[i*informacao[1]+g]["bg"]!="#ff0000" and matrizBotao[informacao[1]*i+g]["bg"] != "#DCDCDC" and informacao[5]=="n":
		b=0
		for j in range(-1,2):
			v= i+j
			for z in range(-1,2):
				f = z+g
				if j!=0 or z!=0:
					if v>=0 and f>=0 and v<len(matrizJogo) and f<len(matrizJogo[0]) :
						if matrizJogo[v][f] == 1:
							b+=1
		for j in range(-1,2):
			v= i+j
			for z in range(-1,2):
				f = z+g
				if j!=0 or z!=0:
					if v>=0 and f>=0 and v<len(matrizJogo) and f<len(matrizJogo[0]) :
						if ((j == 0 and z == 1) or (j==0 and z == -1) or (j==-1 and z == 0) or (j==1 and z == 0) and (matrizJogo[i+j][g+z] == 0)or b==0):
							st = [v,f]
							l = False
							for k in range(len(c)):
								if st == c[k]:
									l = True
							if l == False and b==0:
								c.append(st)
								clicou(v,f,c)
							st = []	
                       
		matrizBotao[informacao[1]*i+g]["bg"]="#DCDCDC"
		informacao[4]-=1
		if b==0: b=""
		matrizBotao[informacao[1]*i+g]["text"] = b
		bombasInfo["text"] = "Bombas: " + str(informacao[3])
		if informacao[4] <= 0 and informacao[5]=="n":
			bombasInfo["text"] = "Ganhou!"
			informacao[5] = "s"
	return 0
    
for i in range(informacao[0]):
	matrizJogo.append([])
	for g in range(informacao[1]):
		if random.randint(1,100)<=informacao[2] :
			matrizJogo[-1].append(1)
			informacao[3] += 1
		else:
			matrizJogo[-1].append(0)
		matrizBotao.append(Button(janela,width="3",height="1"))
		matrizBotao[-1].grid(row = i,column=g+1)
		matrizBotao[-1].bind('<Button-1>', lambda a=None,i=i, g=g: clicou(i,g,[]))   
		matrizBotao[-1].bind('<Button-3>', lambda a=None,i=i, g=g: bomba(i,g))
		matrizBotao[-1]["bg"]="#000000"

informacao[4] = (informacao[0]*informacao[1])-informacao[3]

janela.title('Campo minado')
bombasInfo = Label(janela,text="Bombas: "+str(informacao[3]))
bombasInfo.grid(row=informacao[0],column=0)
janela.mainloop()
