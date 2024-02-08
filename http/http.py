import requests

def effettua_request(url):
    try:
        response = requests.get(url)  # Effettua la richiesta GET all'URL specificato
        response.raise_for_status()  # Solleva un'eccezione in caso di errore nella risposta
        #print("Risposta:", response.text)  # Stampa il contenuto della risposta
        print("OK ",url)
    except requests.exceptions.RequestException as e:
        print("Errore durante la richiesta:", e)

# Esempio di utilizzo
url = "https://www.example.com"  # URL di esempio
effettua_request(url)
siti_web = [
    'https://envato.com',
    'http://amazon.com',
    'http://facebook.com',
    'http://google.com',
    'http://google.fr',
    'http://google.es',
    'http://internet.org',
    'http://gmail.com',
    'http://stackoverflow.com',
    'http://github.com',
    'http://heroku.com',
    'http://really-cool-available-domain.com',
    'http://djangoproject.com',
    'http://rubyonrails.org',
    'http://basecamp.com',
    'http://trello.com',
    'http://yiiframework.com',
    'http://shopify.com',
    'http://another-really-interesting-domain.co',
    'http://airbnb.com',
    'http://instagram.com',
    'http://snapchat.com',
    'http://youtube.com',
    'http://baidu.com',
    'http://yahoo.com',
    'http://live.com',
    'http://linkedin.com',
    'http://yandex.ru',
    'http://netflix.com',
    'http://wordpress.com',
    'http://bing.com',
]
