import streamlit as st
#from CalculEnchere.getexchangerate.getexchangerate import get_exchange_rate
from bidapp.streamlitdemo.pandastest import select_affichage_func
from bidapp.streamlitdemo.database import delete_items

def menu_stock_parc(Options_Menu,basename,field_Names1,filename,path):
    if Options_Menu=="Stock Parc":
            #st.title("Stock Parc")
            st.markdown("<h1 style='text-align: center; color: grey;'>Stock Parc</h1>",unsafe_allow_html=True)
            # génère un fichier csv en guise de dataset pour l'affichage du tableau
            dataframe_edit=select_affichage_func(field_Names1,basename,filename,path)
            
            supp_button= st.button("Supprimer")

            if supp_button:
                
                frame=dataframe_edit[0]
                indice=dataframe_edit[1]
                
                for i in indice:
                     
                    value=frame.iloc[i]["key"]
                    delete_items(basename,value)
                
                st.write("entrée(s) supprimée(s)")


