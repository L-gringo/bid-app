import streamlit as st
import pandas as pd
import numpy as np 
from streamlitdemo.database import fetch_data
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


def select_affichage_func(database):
            
     datas=fetch_data(database)
     df=pd.DataFrame(datas)
       
     # afficher le tableau avec la case selection 
     dataframe_edit= dataframe_with_selections(df)
     return dataframe_edit

def simple_affichage_func(basename):
    
    datas=fetch_data(basename)
    df=pd.DataFrame(datas)
    st.dataframe(df)


def dataframe(basename):
     db=fetch_data(basename)
     df=pd.DataFrame(db)
     return df


