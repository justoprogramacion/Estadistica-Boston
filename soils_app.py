import streamlit as st
import statsmodels.api as sm
import pandas as pd

st.title("Visualización del Dataset Soils (carData de R)")

# Cargar el dataset Soils desde R
soils = sm.datasets.get_rdataset("Soils", package="carData").data

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

st.subheader("Primeras filas del dataset Soils")
st.dataframe(soils.head())

st.subheader("Descripción estadística Soils")
st.write(soils.describe())

st.subheader("Variables del dataset Soils")
st.write(list(soils.columns))
