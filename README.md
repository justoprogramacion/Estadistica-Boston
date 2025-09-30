# Estadística de Viviendas (California Housing y Soils)

Este proyecto utiliza datasets clásicos para el análisis estadístico y visualización de datos de viviendas y suelos, empleando Streamlit para una interfaz web interactiva.

## Tipos de análisis posibles

### California Housing
- Análisis exploratorio de datos (EDA)
- Visualización de distribuciones y correlaciones
- Modelos de regresión para predecir el valor de las viviendas
- Análisis de variables geográficas y socioeconómicas
- Detección de outliers y patrones

### Soils
- Comparación de grupos y bloques experimentales
- Análisis de la relación entre variables químicas y físicas del suelo
- Visualización de distribuciones y correlaciones
- Análisis de varianza (ANOVA) entre grupos
- Identificación de factores que afectan la calidad del suelo

## Datasets utilizados

### 1. California Housing
- **Fuente:** scikit-learn (`fetch_california_housing`)
- **Descripción:** Contiene información sobre viviendas en California, incluyendo variables como ingreso medio, edad promedio de las casas, número de habitaciones, población, latitud, longitud y el valor medio de las viviendas.
- **Variables principales:**
  - MedInc: Ingreso medio
  - HouseAge: Edad promedio de las casas
  - AveRooms: Promedio de habitaciones
  - AveBedrms: Promedio de dormitorios
  - Population: Población
  - AveOccup: Promedio de ocupantes
  - Latitude, Longitude: Ubicación geográfica
  - MedHouseVal: Valor medio de las viviendas (objetivo)
- **Aplicaciones:**
  - Análisis exploratorio de datos
  - Modelos de regresión para predicción de precios
  - Visualización de correlaciones y distribuciones

### 2. Soils (carData de R)
- **Fuente:** `statsmodels.api.datasets.get_rdataset` (paquete `carData` de R)
- **Descripción:** Mediciones de suelos agrupadas por factores experimentales como grupo, contorno, profundidad y bloque. Incluye variables químicas y físicas del suelo.
- **Variables principales:** Group, Contour, Depth, Block, pH, N, Dens, P, Ca, Mg, K, Na, Conduc
- **Aplicaciones:**
  - Comparación de grupos y bloques
  - Análisis de relaciones entre variables químicas
  - Visualización de distribuciones

## Consideraciones éticas

El dataset original de las casas de Boston fue eliminado de scikit-learn por problemas éticos relacionados con variables racistas y su uso inapropiado. Por ello, este proyecto utiliza el dataset California Housing como alternativa ética y moderna para el análisis de precios de viviendas.

## Requisitos
- Python 3.8+
- Streamlit
- pandas
- statsmodels
- scikit-learn

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

## Ejecución
Para iniciar la aplicación web ejecuta:
```bash
streamlit run app.py
```
O para el análisis de suelos:
```bash
streamlit run soils_app.py
```

## Autor
- justoprogramacion
