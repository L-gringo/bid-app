#fonction qui récupère le taux de change
import requests
from forex_python.converter import CurrencyRates
from dotenv import load_dotenv
import os
import streamlit as st


def get_exchange(base_currency, target_currency):
    c = CurrencyRates()
    try:
        exchange_rate = c.get_rate(base_currency, target_currency)
    except Exception as error:
        print("le taux de change de la paire demandée n'est pas disponible.. Merci d'indiquer une paire valide")
        raise error
    return exchange_rate

def get_exchange_rate(target_currency):

    load_dotenv()
    key=st.secrets["api"]
    currencies=target_currency
    endpoint="live"
    
    #response=requests.get(f"https://api.currencylayer.com/{endpoint}?access_key={os.getenv('api_key')}&currencies={currencies}")
    response=requests.get(f"https://api.currencylayer.com/{endpoint}?access_key={key}&currencies={currencies}")    
    data=response.json()
    return data["quotes"]["USDXOF"]
    