import streamlit as st
from streamlitdemo.database import insert_datastock
from streamlitdemo.pandastest import list_towns

def menu_ajout_nouvel_achat(Options_Menu,user1,exchangerate,ctkeystr):

    if Options_Menu=="Ajout Nouvel Achat":
           
             #st.title("Stock")
             st.markdown("<h1 style='text-align: center; color: grey;'>Stock</h1>",unsafe_allow_html=True)
             with st.form(key="form2"):
                model_Manufacturer_input=st.text_input("Entrer le nom du fabricant :")
                model_Name_input=st.text_input("Entrer le nom du modèle :")
                modele_year_input=st.number_input("Entrer l'année de sortie du modèle :", min_value=0)
                buy_date=st.date_input("Entrer la date d'achat")
                buy_price_input=st.number_input("Entrer le prix d'achat", min_value=10000)
                sale_price_prev_input=st.number_input("Entrer le prix de vente prévisionnel", min_value=10000)
                sell_date_input=st.date_input("Entrer la date de vente")
                marge_input=st.number_input("marge", min_value=0)
                exchange_input=st.number_input("Taux de change", value=exchangerate)
                fret_input=st.number_input("Entrer le prix du fret", min_value=1000)
                statuts_input=st.selectbox("Satut",["En stock","Vendu","Concessionnaire","Port de depart","Bateau","Port arrivee","En location"], index=0) 
                sale_price_final_input=st.number_input("Entrer le prix de vente final", min_value=10000)
                town=st.selectbox("Selectionner la ville d'origine du véhicule :",list_towns("Transports"))
                transpfees=user1.transportfees(town)
                reparations=st.number_input("Montant estimé de réparations",min_value=0)
                submit_button1=st.form_submit_button("Ajouter au stock")

                if submit_button1:
                     #Remplit la base de données cible avec les infos du modèles (Fabricant, nom, année de sortie), le montant de l'enchère et la date de calcul de l'enchère
                    insert_datastock("Stock", ctkeystr, 
                                      model_Manufacturer_input, 
                                      model_Name_input,
                                        modele_year_input, 
                                        buy_date.strftime("%d %B  %Y"),
                                        sell_date_input.strftime("%d %B %Y"),
                                        buy_price_input,
                                        transpfees,
                                        sale_price_prev_input,
                                        sale_price_final_input,
                                        fret_input,
                                        reparations,
                                        marge_input,
                                        exchange_input,
                                        statuts_input,
                                        )