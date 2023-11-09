def prezzo_medio(prezzi_prodotti, prodotto, giorno):
    return prezzo_medio


prezzi_prodotti = (
    ("Mele", "Lunedi", 1.0),
    ("Mele", "Martedi", 1.2),
    ("Mele", "Mercoledi", 1.1),
    ("Banana", "Lunedi", 0.8),
    ("Banana", "Martedi", 0.9),
    ("Banana", "Mercoledi", 0.7),
)
SSS
prodottoIns = input("Inserisci il prodotto che vuoi verificare: ")
giornoIns = input("Inserisci il giorno di vendita del prodotto: ")

for(nomi, giorni, prezzi) in prezzi_prodotti:
    if prodottoIns != nomi:
        prodottoIns = input("Prodotto inesistente, rinserisci il prodotto che vuoi verificare: ")
    if giornoIns != giorni:
        giornoIns = input("Giorno inesistente, inserisci il giorno di vendita del prodotto: ")
        
        #FA SCHIFO DEVO RIFARE