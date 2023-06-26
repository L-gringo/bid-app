from deta import Deta
import datetime
import streamlit as st
import streamlit_authenticator as stauth
from streamlitdemo.generatecsv import gencsv
#from streamlitdemo.pandastest import dataframe


Deta_KEY=st.secrets["DETA"]
deta=Deta("DETA_KEY")

def insert_dataenchere(basename,key, manufacturer, model, modeldate,enchere, exchangerate, currday):

    db = deta.Base(basename)
    db.put({"key":key, "Fabricant":manufacturer, "Modele":model, "Date sortie":modeldate, "Montant Enchere":enchere, "Taux de Change":exchangerate,"Date Enchere":currday})


def insert_transp_db(basename,key,town,price):
    db=deta.Base(basename)
    db.put({"key":key, "Ville":town, "Prix":price})
    


def update_transp_db(basename,city,price,keyval):
    
    db=deta.Base(basename)
    
    updates={"Ville":city,"Prix":price}

    db.update(updates, key=keyval)


def insert_datastock(basename,key, manufacturer, model, modeldate,buydate, selldate, buyprice,transp,salepriceprev,salepriceend,fret,repair,marge, exchange,statut):

    db = deta.Base(basename)
    
    db.put(
        {"key":key, 
            "Fabricant":manufacturer, 
            "Modele":model, 
            "date sortie":modeldate,
              "date achat":buydate,
              "date vente": selldate,
              "frais transport":transp,
              "fret":fret,
              "marge":marge,
              "Taux de change":exchange,
              "prix achat":buyprice, 
              "prix de vente previsionnel":salepriceprev, 
              "prix de vente final":salepriceend,
              "reparations":repair,
                "statut":statut}
         )


#def insert_marge_base(basename,key, manufacturer, model, modeldate,buydate,buyprice,salepriceend,marge):
def insert_marge_base(basename,key, manufacturer, model, modeldate, buydate, buyprice, salepriceend, marge):

    db = deta.Base(basename)
    
    db.put(
        {"key":key, 
            "Fabricant":manufacturer, 
            "Modele":model, 
            "date sortie":modeldate,
              "date achat":buydate,
              "prix achat":buyprice,
              "prix de vente final":salepriceend,
              "marge":marge,
               
              }
         )

def insert_cred(basename,username, name, password):

    hashed_pass= stauth.Hasher(password).generate() 
    db=deta.Base(basename)
    db.put({"Key":username,"Name":name,"password":hashed_pass})

def fetch_data(basename):
    db=deta.Base(basename)
    data=db.fetch()
    return data.items

def update_db(basename, keyval, fab, mod, ds, da, dv, tf, ft, pa, pvf, pvp, rp, exr, mg,stt):

    db=deta.Base(basename)
    updates={"Fabricant":fab,
            "Modele":mod, 
            "date sortie":ds,
            "date achat":da,
            "date vente": dv,
            "frais transport":tf,
            "fret":ft,
            "prix achat":pa,
            "prix de vente previsionnel":pvp,
            "prix de vente final":pvf,  
            "reparations":rp,
            "Taux de change":exr, 
            "marge":mg,         
            "statut":stt,
            }
    db.update(updates=updates, key=keyval)


def update_marge(basename, keyval,mg):

    db=deta.Base(basename)
    updates={"marge":mg}
    db.update(updates=updates,key=keyval)


def delete_items(basename, keyval):

    db=deta.Base(basename)
    db.delete(key=keyval)
    
def db_items_list(basename):

    towns=fetch_data(basename)
    transpdict={}
    for town in towns:
        transpdict[town["Ville"]]=town["Prix"]
    
    return transpdict


