#fonction qui récupère le taux de change
from forex_python.converter import CurrencyRates

def get_exchange_rate(base_currency, target_currency):
    c = CurrencyRates()
    try:
        exchange_rate = c.get_rate(base_currency, target_currency)
    except Exception as error:
        print("le taux de change de la paire demandée n'est pas disponible.. Merci d'indiquer une paire valide")
        raise error
    return exchange_rate

