import streamlit as st
#from CalculEnchere.getexchangerate.getexchangerate import get_exchange_rate
from calculenchere.calculenchere import calcul_marge
from streamlitdemo.database import  update_marge, insert_marge_base
from streamlitdemo.pandastest import  select_affichage_func

def menu_generer_marge(Options_Menu,basename,exchangerate):
    if Options_Menu=="Generer Marge":
            
            #st.title("Calcul de marge")
            st.markdown("<h1 style='text-align: center; color: grey;'>Calcul de marge</h1>",unsafe_allow_html=True)
           
           # if "marge" not in st.session_state:
             #   st.session_state.marge=False

            #def callback():
              #  st.session_state.marge=True
            
            dataframe_edit1=select_affichage_func(basename)

            marge_button =st.button("Calculer la marge")

            if marge_button:
            
            #récupérer le dataframe edite dans la variable frame et la liste des indices des lignes selectionnées dans indice
                frame1=dataframe_edit1[0]
                indice1=dataframe_edit1[1]

            #boucle sur les valeurs d'indices pour calculer la marge sur chaque ligne et rajouter les entrées dans les bases de données de Stock et de Marges 
            #la base stock est simplement mise à jour au niveau de l'entrée Marge tandis que la base Marge est complétée d'une nouvelle ligne après chaque génération
            
                for i in indice1:

                    line=frame1.iloc[i]
                    value1=frame1.iloc[i]["key"]
                    marge= calcul_marge(line["prix de vente final"],line["frais transport"],line["fret"],line["reparations"], exchangerate)
                    update_marge("Stock",value1,marge)

                    insert_marge_base("Marges", value1, str(line["Fabricant"]), str(line["Modele"]), str(line["date sortie"]), str(line["date achat"]), int(line["prix achat"]), int(line["prix de vente final"]), marge)

                st.write("Consulter la rubrique RECAP DES MARGES pour voir le tableau recapitulatif des marges generees")
        