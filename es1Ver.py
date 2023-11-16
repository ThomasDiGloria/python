tupla_valori = (
    ("Milano", [("gennaio", 10),("febbraio", 9),("marzo", 11),("aprile", 7),("maggio", 0),("giugno", 11)]),
    ("Bergamo", [("gennaio", 11),("febbraio", 10),("marzo", 11),("aprile", 5),("maggio", 2),("giugno", 0)])
)

def valori_medi(citta):
    sommaM=0
    cont_media=0
    min=10000
    max=0
    mesi_max= []
    mesi_min = []
    
    #spacchetto tupla
    for cit, *resto in tupla_valori:
        #spacchetto  "resto"
        for resto, *mesi in resto:
            #salvo i valori di "mesi" in mesi2
            mesi2=mesi
            #spacchetto "mesi"
            for mesi , valori in mesi:
                #se la citta inserita è uguale alla citta presente nella tupla
                if citta == cit:
                    #se il valore è diverso da 0
                    if valori != 0:
                        #sommo i valori
                        sommaM += valori
                        #aumento il contatore
                        cont_media += 1
                    #se "valori" è minore di min
                    if valori <= min:
                        #do a min il valore di "valori"
                        min=valori
                    #se "valori" è maggiore di max
                    if valori >= max:
                        #do a max il valore di "valori"
                        max=valori

            if citta == cit:
                #spacchetto mesi2
                for mesi , valori in mesi2:
                    #se il valore min è uguale a "valori"
                    if min == valori:
                            #salvo il mese
                            mesi_min.append(mesi)
                    #stessa cosa di prima ma con max
                    if max == valori:
                            mesi_max.append(mesi)
    #per evitare divisioni /0
    if cont_media == 0:
        return "Citta inesistente"
    
    #assegno a valore_min e valore_max i valori di min e max
    valore_min=min
    valore_max=max

    #calcolo media
    media = sommaM / cont_media
    #creo la tupla
    tupla_risultati=(media, (valore_max, mesi_max), (valore_min, mesi_min))
    
    return tupla_risultati


citta=input("Inserisci la citta che vuoi analizzare:")

print(valori_medi(citta))