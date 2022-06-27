""" 
SCRIP DISEÑADO PARA INTRODUCIR NUEVOS REGISTROS A LA BASE DE DATOS
"""

import pandas as pd

print("Que tipo de registros quiere añadir a la base de datos? ")

tipo_delta =input("(CLIENTES / COMPRAS / GASTOS / VENTAS): ")

print("Cual es el nombre del archivo? ")

nombre_delta =input("Nombre del archivo:")

if tipo_delta == "CLIENTES":

    #Lectura de archivo delta
    clientes = pd.read_csv(nombre_delta, delimiter=";")

    #Eliminación de la columna "col10"
    clientes = clientes.drop("col10",axis=1)

    #Renombramiento de columnas X e Y
    clientes.columns = ["IdCliente","Provincia","Nombre y Apellido","Direccion","Telefono","Edad","Localidad","Longitud","Latitud"]

    #Cambio de orden de las columnas
    clientes = clientes[["IdCliente","Nombre y Apellido","Edad","Telefono","Direccion","Localidad","Provincia","Latitud","Longitud"]]

    # Eliminación/reemplazo de caracteres innecesarios 
    clientes["Telefono"] = clientes["Telefono"].replace({'-':''}, regex=True)
    clientes["Telefono"] = clientes["Telefono"].replace({' ':''}, regex=True)
    clientes["Direccion"] = clientes["Direccion"].replace({'-':''}, regex=True)
    clientes["Latitud"] = clientes["Latitud"].replace({',':'.'}, regex=True)
    clientes["Longitud"] = clientes["Longitud"].replace({',':'.'}, regex=True)

    #Normalizacion a Letra Capital
    clientes["Nombre y Apellido"] = clientes["Nombre y Apellido"].str.title()
    clientes["Direccion"] = clientes["Direccion"].str.title() 
    clientes["Localidad"] = clientes["Localidad"].str.title()
    clientes["Provincia"] = clientes["Provincia"].str.title()

    #Imputar Valores Faltantes
    clientes["Nombre y Apellido"].fillna("Sin dato", inplace=True)
    clientes["Edad"].fillna("Sin dato", inplace=True)
    clientes["Telefono"].fillna("Sin dato", inplace=True)
    clientes["Direccion"].fillna("Sin dato", inplace=True)
    clientes["Localidad"].fillna("Sin dato", inplace=True)
    clientes["Provincia"].fillna("Sin dato", inplace=True)
    clientes["Latitud"].fillna("Sin dato", inplace=True)
    clientes["Longitud"].fillna("Sin dato", inplace=True)

    #Eliminación de valores duplicados
    clientes = clientes.drop_duplicates(
        subset=['IdCliente'], keep="last")
    clientes = clientes.drop_duplicates(
        subset=['Nombre y Apellido'], keep="last")

    print("Transformación completada")

elif tipo_delta == "COMPRAS":

    #Lectura de archivo delta
    compras = pd.read_csv(nombre_delta, delimiter=",", encoding = "UTF-8")

    #Eliminación de valores duplicados
    compras = compras.drop_duplicates(
        subset=['IdCompra'], keep="last")

    print("Transformación completada")

elif tipo_delta == "GASTOS":

    #Lectura de archivo delta
    gastos = pd.read_csv(nombre_delta, delimiter=",")

    #Eliminación de valores duplicados
    gastos = gastos.drop_duplicates(
        subset=['Idgasto'], keep="last")

    print("Transformación completada")

elif tipo_delta == "VENTAS":

    #Lectura de archivo delta    
    ventas = pd.read_csv(nombre_delta, delimiter=",")

    #Eliminación de valores duplicados
    ventas = ventas.drop_duplicates(
        subset=['IdVenta'], keep="last")

    print("Transformación completada")

else:

    print("Tipo de archivo o nombre incorrecto")
