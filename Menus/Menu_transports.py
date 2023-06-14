import streamlit as st
from streamlitdemo.database import  insert_transp_db, update_transp_db
from streamlitdemo.pandastest import select_affichage_func

def menu_transports(Options_menu, basename,ctkeystr):
    
    if Options_menu=="Frais Transport":

        dataframe_edit=select_affichage_func(basename)
        

        if "MAJT" not in st.session_state:
            st.session_state.MAJT=False
        
        if "MODT" not in st.session_state:
            st.session_state.MODT=False
        
        def callback():
            st.session_state.MAJT=True

        def callback1():
            st.session_state.MODT=True
        
        add_button=st.button("Ajouter une ville", on_click=callback)

        modif_button=st.button("Modifier", on_click=callback1)

        if add_button or st.session_state.MAJT:

                with st.form(key="transpform"):
                    city_input=st.text_input("Entrer la ville")
                    transprice=st.number_input("Entrer le prix")
                    submit_button=st.form_submit_button("Ajouter")

                if submit_button:
                    insert_transp_db(basename,ctkeystr,city_input,transprice)
        
                    st.session_state.MAJT=False
        

        if modif_button or st.session_state.MODT:

            frame=dataframe_edit[0]
            indice=dataframe_edit[1]
            line=frame.iloc[indice]
            with st.form(key="transpform1"):
               city_input=st.text_input("Ville:",value=str(line["Ville"]))
               transprice=st.number_input("Entrer le prix")
               submit_button=st.form_submit_button("Modifier")
                
            if submit_button:
                update_transp_db(basename,city_input,transprice,key=frame.iloc[indice]["key"])
                st.session_state.MODT=False
