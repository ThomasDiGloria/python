def media_globale(tupla_vendite):
    cont=0
    prezzi=[]
    for reparto, prodotto, in tupla_vendite:
        print(prodotto)
        for prodotto, prezzo in prodotto:
            print(prezzo)
            for tipo, prezzo in prezzo:    
                print(prezzo)
                prezzi[cont].append(prezzo)
                print(prezzi)
                cont+=1
    sommaM=sum(prezzi)
    if cont==0:
        return 0
    media=sommaM / cont
    return media

tupla_vendite = (
                (("RepartoA","Informatica"),("Prodotto A", ("contanti",1000))),
                (("RepartoA","Informatica"),("Prodotto B", ("carta di credito",1500))),
                (("RepartoA","Informatica"),("Prodotto C", ("carta di credito",1200))),
                (("RepartoA","Informatica"),("Prodotto D", ("contanti",200))),
                (("RepartoA","Informatica"),("Prodotto E", ("contanti",800))),
                (("RepartoA","Informatica"),("Prodotto F", ("N/D",200))),
                (("RepartoB","Elettronica"),("Prodotto A", ("contanti",1500))),
                (("RepartoB","Elettronica"),("Prodotto B", ("carta di credito",900)))
                )

print("la media globale è: ", media_globale(tupla_vendite))
