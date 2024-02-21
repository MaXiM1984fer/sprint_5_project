import pandas as pd
import plotly.express as px
import streamlit as st
        
st.header('Anuncios de Autos Usados US')

st.write('Análisis exploratorio del mercado de autos usados de los Estados Unidos de America')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_check = st.checkbox('Construir histograma') # crear un botón
        
if hist_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



scatter_check = st.checkbox('Construir gráfico de dispersión') # crear un botón
        
if scatter_check: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión del precio de los anuncios de venta de coches')
            
    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)