import streamlit as st
from sklearn.datasets import fetch_california_housing
import pandas as pd

# Cargar el dataset California Housing
california = fetch_california_housing(as_frame=True)
df = california.frame

st.title('Dataset de California Housing')

st.markdown("""
El conjunto de datos de California Housing contiene información sobre viviendas en California y sus características, utilizado frecuentemente en aprendizaje automático y estadística.

**Características principales:**
- **MedInc**: Ingreso medio en el bloque (en decenas de miles de dólares)
- **HouseAge**: Edad promedio de las casas en el bloque
- **AveRooms**: Promedio de habitaciones por vivienda
- **AveBedrms**: Promedio de dormitorios por vivienda
- **Population**: Población del bloque
- **AveOccup**: Promedio de ocupantes por vivienda
- **Latitude**: Latitud
- **Longitude**: Longitud
- **MedHouseVal**: Valor medio de las viviendas (objetivo)

**Tipo de análisis posibles:**
- Análisis exploratorio de datos (EDA)
- Correlación entre variables
- Modelos de regresión para predecir el precio de las casas
- Visualización de distribuciones y relaciones
""")

st.subheader('Primeras filas del dataset')
st.dataframe(df.head())

st.subheader('Descripción estadística')
st.write(df.describe())

st.subheader('Variables del dataset')
st.write(list(df.columns))

# Visualización del dataset Soils
st.header('Dataset Soils (carData de R)')
try:
    soils_df = pd.read_csv('soils.csv')
    st.markdown("""
    El dataset **Soils** contiene mediciones de suelos agrupadas por diferentes factores experimentales. Las variables incluidas son:
    - **Group**: Grupo experimental
    - **Contour**: Contorno
    - **Depth**: Profundidad
    - **Block**: Bloque
    - **pH**: Nivel de pH
    - **N**: Nitrógeno
    - **Dens**: Densidad
    - **P**: Fósforo
    - **Ca**: Calcio
    - **Mg**: Magnesio
    - **K**: Potasio
    - **Na**: Sodio
    - **Conduc**: Conductividad

    **Análisis posibles:**
    - Comparación de grupos y bloques
    - Análisis de la relación entre variables químicas
    - Visualización de distribuciones y correlaciones
    """)
    st.subheader('Primeras filas del dataset Soils')
    st.dataframe(soils_df.head())
    st.subheader('Descripción estadística Soils')
    st.write(soils_df.describe())
    st.subheader('Variables del dataset Soils')
    st.write(list(soils_df.columns))
except Exception as e:
    st.error(f"No se pudo cargar soils.csv: {e}")
