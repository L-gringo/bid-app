import streamlit as st
#from CalculEnchere.getexchangerate.getexchangerate import get_exchange_rate
from CalculEnchere.streamlitdemo.pandastest import select_affichage_func


def menu_recap_marges(Options_Menu,basename,filename,path):
    
    if Options_Menu=="Recap Des Marges":
                
                #st.title("Recapitulatif Des Marges Generees")

                st.markdown("<h1 style='text-align: center; color: grey;'>Recapitulatif Des Marges Generees</h1>",unsafe_allow_html=True)
                field_Names=["key",
                         "Fabricant",
                         "Modele", 
                         "date sortie",
                         "date achat",
                           "prix achat",
                               "prix de vente final",
                               "marge",
                               ]
                #récupérer les données de la base marge pour générer un dataset et l'afficher avec une colonne de selection de ligne
                dataframe_edit2=select_affichage_func(field_Names,basename,filename,path)

                show_benefits_button=st.button ("Faire la somme")

                #Si le bouton  "Faire la somme" est cliqué, les lignes sélectionnés du tableau sont récupérées puis une boucle sur l'index 
                # permet de faire la somme des valeurs de la case Marge de chaque ligne pour ensuite afficher à l'utilisateur la valeur totale
                 
                if show_benefits_button:

                    frame2=dataframe_edit2[0]
                    indice2=dataframe_edit2[1]
                    marge_tot=0
                    
                    for i in indice2:
                        line=frame2.iloc[i]
                        value2=int(frame2.iloc[i]["marge"])
                        marge_tot+=value2

                    st.write(f"Le total des marges pour les modèles selectionnes est de {marge_tot}")    

