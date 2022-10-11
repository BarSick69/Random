from random import randint as rand
def superloto():
    puncte=0
    numar=0
    lista=[]
    listamea=[]
    for i in range(0,10):
        for f in range(0,5):
            numar = rand(0,36)
            while numar in lista:
                numar = rand(0,36)
            lista.append(numar)
        for g in range(0,5):
            numar = rand(0,36)
            while numar in listamea:
                numar = rand(0,36)
            listamea.append(numar)
        print("Numerele voastre sunt: ",listamea)
        print(i+1,"Variant este:",lista)
        for n in listamea:
            if n in lista:
                puncte+=1
        if(puncte==5):
            print("Jackpot")
        elif(puncte==4):
            print("Categoria II de castig!")
        elif(puncte==3):
            print("Categoria III de castig!")
        else:
            print("Nu ati castigat nimic:(")
        print("\n")
        lista=[]
        listamea=[]
        puncte=0
superloto()