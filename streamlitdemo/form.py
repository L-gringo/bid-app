import streamlit as st
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

def options_menu(menu_title, options, icons,default_index,orientation):

    option_menu(menu_title,
                options, 
                icons, 
                default_index,
                orientation )
    
    #return Options_Menu

def dataframe_with_selections1(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )
    selected_indices = list(np.where(edited_df.Select)[0])
    selected_rows = df[edited_df.Select]
    return {"selected_rows_indices": selected_indices, "selected_rows": selected_rows}
    #return selected_rows

def dataframe_with_selections(dataframe):
    df_with_selections = dataframe.copy()
    df_with_selections.insert(0, "Select", False)
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=dataframe.columns,
    )
    selected_indices = list(np.where(edited_df.Select)[0])

    return edited_df, selected_indices


