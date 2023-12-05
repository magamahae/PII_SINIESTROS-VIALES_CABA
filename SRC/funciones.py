import pandas as pd
#from textblob import TextBlob
import re

def verificar_tipo_datos(df):
    diccionario = {"Columna": [], "Tipo": [], "NO_nulos_%": [], "Nulos_%": [], "Nulos": []}

    for columna in df.columns:
        porcentaje_no_nulos = (df[columna].count() / len(df)) * 100
        diccionario["Columna"].append(columna)
        diccionario["Tipo"].append(df[columna].apply(type).unique())
        diccionario["NO_nulos_%"].append(round(porcentaje_no_nulos, 2))
        diccionario["Nulos_%"].append(round(100-porcentaje_no_nulos, 2))
        diccionario["Nulos"].append(df[columna].isnull().sum())

    df_info = pd.DataFrame(diccionario)
        
    return df_info