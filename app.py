import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de proyectos de agua potable y alcantarillado")

# Intentar cargar el archivo Excel y mostrar errores si hay problemas
try:
    df = pd.read_excel("Presupuesto PNSU.xlsx")
    st.write("Datos cargados correctamente:")
    st.dataframe(df.head())  # Muestra las primeras filas para confirmar carga
except Exception as e:
    st.error(f"No se pudo cargar el archivo Excel: {e}")
    st.stop()

# Lista de columnas para seleccionar, se verifica que existan
columnas_disponibles = df.columns.tolist()
opciones = ["AVNCE (%)", "DEVENGADO", "PIM", "COSTO DEL PROYECTO"]

# Filtramos las opciones para mostrar solo las que existen en el DataFrame
opciones_validas = [col for col in opciones if col in columnas_disponibles]

if not opciones_validas:
    st.error("Ninguna de las métricas esperadas está en el archivo Excel.")
    st.stop()

selected = st.selectbox("Selecciona una métrica", opciones_validas)

# Crear la gráfica solo si la columna seleccionada está en el DataFrame
if selected in df.columns:
    fig = px.bar(df.sort_values(selected, ascending=True),
                 x=selected,
                 y="PROYECTO",
                 orientation="h",
                 title=f"{selected} por proyecto")
    st.plotly_chart(fig)
else:
    st.warning(f"La columna {selected} no se encontró en los datos.")