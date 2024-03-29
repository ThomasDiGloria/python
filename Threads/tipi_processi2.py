from multiprocessing import os,Queue,Process, current_process
"""
--Queue: classe che rappresenta una codsa condivisa tra processi.
È utilizzata per consentire la comunicazione tra processi,
consentendo loro di scambiarsi dati in modo sicuro.
put(item): Aggiunge un elemento alla coda.
get(): Rimuove e restituisce un elemento dalla coda.
empty(): Restituisce True se la coda è vuota, altrimenti restituisce False.
full(): Restituisce True se la coda è piena, altrimenti restituisceFalse.
qsize(): Restituisce il numero di elementi presenti nella coda.
close(): Chiude la coda.
-- current_process: funzione che restituisce un oggetto Process che rappresenta
il processo in esecuzione.
"""

def process_id():
    #visualizza il server, il nome del processo e il pid
    print(f"Server PID: {os.getpid()}, Process Name: { current_process().name}, Process PID: {current_process().pid}")

def process_function(data,result_queue):
    process_id()
    print("Elabora: ",data)
    result = data*2
    #aggiunge il risultato alla coda
    result_queue.put(result)

if __name__ == "__main__":
    data_list = [1,2,3,4]
    result_queue = Queue()
    processes = []

    for data in data_list:
        #creo un processo con gli stesso metodo precedente
        p=Process(target=process_function, args=(data, result_queue))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("Il main stampa i risultati")
    #finchè result_queue non è vuoto
    while not result_queue.empty():
        #rimuovi e restituisce un elemento dalla coda
        result = result_queue.get()
        print(result)