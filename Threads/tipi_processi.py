from multiprocessing import Process

"""
multiprocessing è una librearia per la creazione, la comunicazione e la sincroninazzione 
tra processi nella programmazione parallela e concorrente Process è una classe per 
creare processi eseguendo una funzione (o metodo) specificata come target.
"""

def process_function(data):
    #moltiplica il valore per due
    result = data * 2
    #visualizza il risultato
    print(result)

#se 
if __name__ == "__main__":
    #creo un array con all'interno i valori
    data_list = [1, 2, 3, 4]
    processes = []

    for data in data_list:
        #crea nuovo processo dove il target (funzione da cui far partire) è la funzione prima scritta e il contenuto sono i dati (data)
        p = Process(target=process_function, args=(data,))
        #aggiunge p(il processo) al vettore dei processi
        processes.append(p)
        p.start() #Avvia l'esecuzione del processo separato
    
    for p in processes:
        p.join() #Blocca il processo principale fino a quando il processo separato non termina