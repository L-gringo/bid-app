import streamlit as st
#from CalculEnchere.getexchangerate.getexchangerate import get_exchange_rate
from calculenchere.calculenchere import calcul_enchere
from streamlitdemo.database import  insert_dataenchere

def menu_calcul_enchere(Options_Menu,user1,exchangerate,ctkeystr,ctstr):
       
    if Options_Menu=="Calcul Enchere":          
           
            #st.title("Formulaire de calcul des encheres")
            st.markdown("<h1 style='text-align: center; color: grey;'>Calcul Des Encheres</h1>",unsafe_allow_html=True)
            with st.form(key="form1"):
                model_Manufacturer_input=st.text_input("Entrer le nom du fabricant :")
                model_Name_input=st.text_input("Entrer le nom du modèle :")
                modele_year_input=st.number_input("Entrer la date de sortie du modèle :", min_value=0)
                sale_price_input=st.number_input("Entrer le prix de vente", min_value=10000)
                exchange_input=st.number_input("Taux de change", value=exchangerate)
                fret_input=st.number_input("Entrer le prix du fret", min_value=1000)
                profits_input=st.number_input("Entrer la marge visée",min_value=0)

                #frais de réparations
                reparation=st.number_input("Montant estimé de réparations",min_value=0)
                    
                #Etat d'origine du véhicule pour le transport
                town=st.selectbox("Selectionner la ville d'origine du véhicule :",("Washington","New York","Houston"))
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
                    
                    st.markdown(f"le taux de change {currencies[0]}/{currencies[1]} est actuellement de : {exchangerate}")
                    #calcul la valeur de l'enchère e
                    value=calcul_enchere(modele.sellprice,modele.profit,transpfees,modele.fret,repfees,exchangerate)

                    st.markdown(f"la valeur maximale de cette enchère pour ce modèle {modele.name} {modele.year} est de : {value} dollars")
        
                    #Remplit la base de données cible avec les infos du modèles (Fabricant, nom, année de sortie), le montant de l'enchère et la date de calcul de l'enchère
                    insert_dataenchere("History2", ctkeystr, model_Manufacturer_input, model_Name_input, modele_year_input, value, exchange_input, ctstr)
                    
                    