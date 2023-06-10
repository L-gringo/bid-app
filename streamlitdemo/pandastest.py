import streamlit as st
import pandas as pd
import numpy as np 
from bidapp.streamlitdemo.generatecsv import gencsv
from bidapp.streamlitdemo.database import insert_cred, insert_dataenchere, insert_datastock, fetch_data, update_db, update_marge, insert_marge_base
#import streamlit_pandas as sp

def load_data(path):
   # df=pd.read_csv("C:\\Users\\ma79caen\\Documents\\vscodetest\\.venv\\streamlitdemo\\Historicenchere.csv")
    df=pd.read_csv(path)
    st.dataframe(df.style.set_properties(**{'border': '1.3px blue',
                          'color': 'black'}), width=800, hide_index=True)


def dataframe_with_selections(dataframe):
    df_with_selections = dataframe.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        width=1200,
        disabled=dataframe.columns,
    )
    selected_indices = list(np.where(edited_df.Select)[0])

    return edited_df, selected_indices


def dataframe_multiple_selections(dataframe):
    df_with_selections = dataframe.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=dataframe.columns,
    )
    selected_rows = dataframe[edited_df.Select]
    return selected_rows

def openstock_csv(dataframe):
    pass

def select_affichage_func(field_Names,database,filename,path,):
     
     field_Names=field_Names
            
     datas=fetch_data(database)
     gencsv(filename,datas,field_Names)
     datasetpath=path
     df=pd.read_csv(datasetpath)
       
     # afficher le tableau avec la case selection 
     dataframe_edit= dataframe_with_selections(df)
     return dataframe_edit

def simple_affichage_func(field_Names, basename, filename, path):
    
    field_Names= field_Names
    datas=fetch_data(basename)
    gencsv(filename,datas,field_Names)
    datasetpath=path
    load_data(datasetpath)
