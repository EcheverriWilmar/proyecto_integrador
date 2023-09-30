import pandas as pd 
import plotly.express as px 
import streamlit as st 

st.title('Aplicacion 2 ') 
st.subheader('Reporte de Ventas')
st.markdown('##') 
                   
archivo_excel = 'Reporte de Ventas.xlsx' 
hoja_excel = 'BASE DE DATOS' 

df = pd.read_excel(archivo_excel,
                   sheet_name = hoja_excel,
                   usecols = 'A:P')
                   #header = 0



st.sidebar.header("Opciones a filtrar:") 
vendedor = st.sidebar.multiselect(
    "Seleccione el Vendedor:",
    options = df['Vendedor'].unique(),
    default = df['Vendedor'].unique() 
)

status_factura = st.sidebar.multiselect(
    "Factura Pagada (?):",
    options = df['Pagada'].unique(),
    default = df['Pagada'].unique() 
)

ciudad = st.sidebar.multiselect(
    "Seleccione Ciudad:",
    options = df['Ciudad'].unique(),
    default = df['Ciudad'].unique() 
)

industria = st.sidebar.multiselect(
    "Seleccione Industria:",
    options = df['Industria'].unique(),
    default = df['Industria'].unique() 
)

cliente = st.sidebar.multiselect(
    "Seleccione Cliente:",
    options = df['Cliente'].unique(),
    default = df['Cliente'].unique() 
)

plazo = st.sidebar.multiselect(
    "Seleccione plazo:",
    options = df['Términos'].unique(),
    default = df['Términos'].unique() 
)






df_seleccion = df.query("Vendedor == @vendedor  & Ciudad == @ciudad & Pagada ==@status_factura & Industria ==@industria & Cliente ==@cliente & Términos ==@plazo " ) 



total_ventas = int(df_seleccion['Valor'].sum())

total_facturas = int(df_seleccion['Valor'].count())

left_column, right_column = st.columns(2)

with left_column:
    st.subheader("Ventas Totales:")
    st.subheader(f"US $ {total_ventas:,}")

with right_column:
    st.subheader('Facturas:')
    st.subheader(f" {total_facturas}")
            
 
st.markdown("---") 

st.dataframe(df_seleccion) 

ventas_por_cliente = (
    df_seleccion.groupby(by=['Cliente'])[['Valor']].sum()).sort_values(by='Valor')



fig_ventas_cliente = px.bar(
    ventas_por_cliente,
    x = 'Valor',
    y=ventas_por_cliente.index, 
    orientation= "h",
    title = "<b>Ventas por Cliente</b>", 
    color_discrete_sequence = ["#00008B"] * len(ventas_por_cliente),
    template='plotly_white',

)

fig_ventas_cliente.update_layout(
    plot_bgcolor = "rgba(0,0,0,0)",
    xaxis=(dict(showgrid = False))
    
)

ventas_por_vendedor = (
    df_seleccion.groupby(by=['Vendedor'])[['Valor']].sum()).sort_values(by='Valor')




fig_ventas_por_vendedor = px.bar(
    ventas_por_vendedor,
    x=ventas_por_vendedor.index,
    y='Valor',
    title = '<b>Ventas por Vendedor</b>',
    color_discrete_sequence = ["#00008B"]*len(ventas_por_vendedor),
    template = 'plotly_white',
)

fig_ventas_por_vendedor.update_layout(
    xaxis=dict(tickmode='linear'),
    plot_bgcolor='rgba(0,0,0,0)',
    yaxis=(dict(showgrid=False)),
   
)    

## QUIERO PONER LAS DOS GRAFICAS A CADA LADO, UNA AL LADO DE LA OTRA

left_column, right_column = st.columns(2)

left_column.plotly_chart(fig_ventas_por_vendedor, use_container_width = True) 
right_column.plotly_chart(fig_ventas_cliente, use_container_width = True)




