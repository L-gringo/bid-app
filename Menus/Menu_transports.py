import streamlit as st
from streamlitdemo.database import  insert_transp_db, update_transp_db
from streamlitdemo.pandastest import select_affichage_func

def menu_transports(Options_menu, basename,ctkeystr):
    
    if Options_menu=="Frais Transport":

        dataframe_edit=select_affichage_func(basename)
        

        if "MAJT" not in st.session_state:
            st.session_state.MAJT=False
        
        def callback():
            st.session_state.MAJT=True
        
        add_button=st.button("Ajouter une ville", on_click=callback)

        modif_button=st.button("Modifier", on_click=callback)

        if add_button or st.session_state.MAJT:

                with st.form("transpform"):
                    city_input=st.text_input("Entrer la ville")
                    transprice=st.number_input("Entrer le prix")
                    submit_button=st.form_submit_button("Ajouter")

                if submit_button:
                    insert_transp_db(basename,ctkeystr,city_input,transprice)
        st.session_state.MAJT=False
        

        if modif_button or st.session_state.MAJT:

            frame=dataframe_edit[0]
            indice=dataframe_edit[1]

            for i in indice:
                
                with st.form("transpform"):
                    city_input=st.text_input("Ville:",str(value=frame.iloc[i]["Ville"]))
                    transprice=st.number_input("Entrer le prix")
                    submit_button=st.form_submit_button("Modifier")
                
                if (submit_button):
                    update_transp_db(basename,transprice,key=frame.iloc[i]["key"])

