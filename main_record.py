import streamlit_authenticator as stauth
import streamlit as st
from CalculEnchere.user.user import user
from CalculEnchere.manufacturer.manufacturer import manufacturer
from CalculEnchere.getexchangerate.getexchangerate import get_exchange_rate
from CalculEnchere.calculenchere.calculenchere import calcul_enchere
from CalculEnchere.Connector.connector import connect
import datetime
from streamlitdemo.database import insert_cred, insert_data, fetch_data
from streamlitdemo.generatecsv import gencsv
from streamlitdemo.pandastest import load_data

def main():
     
    ct=datetime.datetime.now()
    ctkeystr=ct.strftime("%Y-%m-%d-%H-%M-%S")
    ctstr=ct.strftime("%d %B  %Y") 
    credentials= connect()
    
    #authenticator= stauth.Authenticate(names,usernames,hashed_passwords, "cookies", "abcdef", cookie_expiry_days=7)
    authenticator= stauth.Authenticate(credentials, "cookies", "abcdef", cookie_expiry_days=7)

    name, authentication_status, username = authenticator.login("login","main")

    if authentication_status==False:
         st.error("Username/password is incorrect")

    if authentication_status==None:
         st.warning("Please enter your username and password")
    
    if authentication_status:

        authenticator.logout("Logout", "sidebar")
        #st.sidebar.title(f"Bienvenue {name}")
        dict_manufacturer={"Toyota":{"Rav4":2007, "Avencis":2014}, "Ford":{"Mondeo":2008, "Mustang":1992}}
        list_man=[]
        list_mod=[]
        
        for value in dict_manufacturer:
            list_man.append(manufacturer(value,dict_manufacturer[value]))
            for mod in dict_manufacturer[value]:
                list_mod.append(dict_manufacturer[value])

        #Logging
        user1=user(username)
        
        #Informations sur le prix de vente final, le fret, la marge visée, le nom du modèle, la date de sortie 
        st.title(":green[RECAP DES ENCHERES]")

        with st.sidebar:
            st.header (f"Bienvenue {name}")       
            with st.form(key="form1"):
                model_Manufacturer_input=st.text_input("Entrer le nom du fabricant :")
                model_Name_input=st.text_input("Entrer le nom du modèle :")
                modele_year_input=st.number_input("Entrer la date de sortie du modèle :", min_value=0)
                sale_price_input=st.number_input("Entrer le prix de vente", min_value=10000)
                fret_input=st.number_input("Entrer le prix du fret", min_value=1000)
                profits_input=st.number_input("Entrer la marge visée",min_value=0)

            #frais de réparations
                reparation=st.number_input("Montant estimé de réparations",min_value=0)
                
            #Etat d'origine du véhicule pour le transport
                town=st.selectbox("Selectionner la ville d'origine du véhicule :",("Washington","New York","Texas"))
                transpfees=user1.transportfees(town)

            #Devises cibles pour le change  
                currencies=user1.currencies("USD","EUR")

            #Bouton de validation du formulaire 
                submit_button=st.form_submit_button("valider")
            
                 
            #Actions si validation
            if submit_button:

                # crée un modèle et instancie le montant des réparations 
                modele=user1.setfees(sale_price_input,fret_input,profits_input,{model_Name_input:modele_year_input})
                repfees=modele.repmount(reparation)
                
                #récupère le taux de change des devises indiquées
               #exchangerate=get_exchange_rate(currencies[0], currencies[1])
                exchangerate=0.932
                st.markdown(f"le taux de change {currencies[0]}/{currencies[1]} est actuellement de : {exchangerate}")
                #calcul la valeur de l'enchère e
                value=calcul_enchere(modele.sellprice,modele.profit,transpfees,modele.fret,repfees,exchangerate)

                st.markdown(f"la valeur maximale de cette enchère pour ce modèle {modele.name} {modele.year} est de : {value} dollars")
    
                #Remplit la base de données cible avec les infos du modèles (Fabricant, nom, année de sortie), le montant de l'enchère et la date de calcul de l'enchère
                insert_data("History2", ctkeystr, model_Manufacturer_input, model_Name_input, modele_year_input, value, ctstr)
                
                # génère un fichier csv en guise de dataset pour l'affichage du tableau
                field_Names=["key","Fabricant","Date Enchere", "Date sortie", "Modele", "Montant Enchere"]
                datas=fetch_data("History2")
                gencsv("Historicdataset.csv",datas,field_Names)

            #Actions bouton table_button
            table_button=st.button("Tableau Encheres")
        if table_button:
            datasetpath="C:\\Users\\ma79caen\\Documents\\vscodetest\\.venv\\streamlitdemo\\Historicdataset.csv"
            load_data(datasetpath)


        #Affiche dans la section principale de la page la valeur du taux de change actuel des devises indiquées ainsi que le montant calculé de l'enchère
        
        


       
        
if __name__=="__main__":
        main()