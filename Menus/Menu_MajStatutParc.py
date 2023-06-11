import streamlit as st
from streamlitdemo.database import  update_db
from streamlitdemo.pandastest import select_affichage_func


def menu_maj_statut_parc(Options_Menu,basename,user1):
    if Options_Menu=="MAJ Statut Parc":

            #st.title("MAJ Statut Parc")

            st.markdown("<h1 style='text-align: center; color: grey;'>MAJ Statut Parc</h1>",unsafe_allow_html=True)
         #créer une fonction d'etat de session
            
            if "MAJ" not in st.session_state:
                st.session_state.MAJ=False

            def callback():
                st.session_state.MAJ=True

            # génère un fichier csv en guise de dataset pour l'affichage du tableau
            dataframe_edit=select_affichage_func(basename)

            update_button=st.button("Mettre a jour",on_click=callback)

            if update_button or st.session_state.MAJ:

                frame=dataframe_edit[0]
                indice=dataframe_edit[1][0]
                value=frame.iloc[indice]["key"]

                with st.form(key="form3"):

                    model_Manufacturer_input1=st.text_input("Entrer le nom du fabricant :",value=frame.iloc[indice]["Fabricant"])
                    model_Name_input1=st.text_input("Entrer le nom du modèle :",value=frame.iloc[indice]["Modele"])
                    modele_year_input1=st.number_input("Entrer la date de sortie du modèle :",value= frame.iloc[indice]["date sortie"], min_value=0)
                    buy_date1=st.text_input("Entrer la date d'achat",value= frame.iloc[indice]["date achat"])
                    buy_price_input1=st.number_input("Entrer le prix d'achat", value= frame.iloc[indice]["prix achat"],min_value=10000)
                    sale_price_prev_input1=st.number_input("Entrer le prix de vente prévisionnel", value= frame.iloc[indice]["prix de vente previsionnel"], min_value=10000)
                    fret_input1=st.number_input("Entrer le prix du fret", value= frame.iloc[indice]["fret"], min_value=1000)
                    town1=st.selectbox("Selectionner la ville d'origine du véhicule :",("Washington","New York","Houston"))
                    transpfees1=user1.transportfees(town1)
                    marge_input1=st.number_input("marge", min_value=0)
                    statuts_input1=st.selectbox("Satut",["En stock","Vendu","Concessionnaire","Port de depart","Bateau","Port arrivee","En location"]) 
                    sale_price_final_input1=st.number_input("Entrer le prix de vente final", min_value=10000)
                    reparations1=st.number_input("Montant des réparations",value= frame.iloc[indice]["reparations"],min_value=0)
                    val1=value
                    button=st.form_submit_button("Validez")
                    
                    if button:

                        update_db("Stock", 
                                    val1, 
                                    model_Manufacturer_input1, 
                                    model_Name_input1, 
                                    modele_year_input1,
                                    buy_date1, 
                                    transpfees1, 
                                    fret_input1,
                                    buy_price_input1,
                                    sale_price_final_input1, 
                                    sale_price_prev_input1,
                                    reparations1,
                                    marge_input1, 
                                    statuts_input1,)
                        st.write("entrée mise a jour")

                        st.session_state.MAJ=False