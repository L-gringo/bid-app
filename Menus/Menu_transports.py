import streamlit as st
from streamlitdemo.database import  insert_transp_db, update_transp_db, delete_items
from streamlitdemo.pandastest import select_affichage_func

def menu_transports(Options_menu, basename,ctkeystr):
    
    if Options_menu=="Frais Transport":

        st.markdown("<h1 style='text-align: center; color: grey;'>Frais de Transport</h1>",unsafe_allow_html=True)

        
        if "MAJT" not in st.session_state:
            st.session_state.MAJT=False

        if "MODT" not in st.session_state:
            st.session_state.MODT=False
        
        if "SUPPT" not in st.session_state:
            st.session_state.SUPPT=False
        


        def callback():
            st.session_state.MAJT=True

        def callback1():
            st.session_state.MODT=True
        
        def callback2():
            st.session_state.SUPPT=True

        dataframe_edit=select_affichage_func(basename)

        col1,col2,col3=st.columns([1,1,1])

        with col1:
            add_button=st.button("Ajouter une ville", on_click=callback)

        with col2:
            modif_button=st.button("Modifier", on_click=callback1)

        with col3:
            supp_button=st.button("Supprimer", on_click=callback2)



        if add_button or st.session_state.MAJT:

                with st.form(key="transpform"):
                    city_input=st.text_input("Entrer la ville")
                    transprice=st.number_input("Entrer le prix")
                    submit_button=st.form_submit_button("Ajouter")

                if submit_button:
                    insert_transp_db(basename,ctkeystr,city_input,transprice)
                    st.session_state.MAJT=False
                    st.write("Ville ajoutée")
        

        if modif_button or st.session_state.MODT:


            frame=dataframe_edit[0]
            indice=dataframe_edit[1][0]
            value=frame.iloc[indice]["key"]

            st.write(value)
        
            with st.form(key="transpform1"):
               city_input=st.text_input("Entrer le nom du modèle :",value=frame.iloc[indice]["Ville"])
               transprice=st.number_input("Entrer le prix")
               submit_button=st.form_submit_button("Modifier")
                
            if submit_button:
                update_transp_db(basename,city_input,transprice,keyval=value)
                st.write("Entrée mise à jour")
                st.session_state.MODT=False


        if supp_button or st.session_state.SUPPT:
            
            frame=dataframe_edit[0]
            indice=dataframe_edit[1]

            for i in indice:
                line=frame.iloc[i]
                key=line["key"]
                delete_items(basename,keyval=key)
                st.write("Entrée supprimée")
                st.session_state.SUPPT=False
