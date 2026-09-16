# Ejercio 1
# VENTAS ORDENADAS POR MES: 
# Se necesita un prog. para cargar las ventas ordenadas por mes  del año 2024. 
# El ingreso de ventas cambia de mes cuando se ingresa (0).La cant. de ingresos 
# de ventas no son las mismas de cada mes.Al final deñl prog. se debe mostrar el
# total de las ventas del todo los meses

ventas_acumuladas = 0 
ventas = 0
for i in range (12):
    print ("Mes", i +1)
    ventas = int(input("Ingrese el importe de venta: "))
    while ventas != 0:
        ventas_acumuladas += ventas
        ventas = int(input("Ingrese el importe de venta: "))
print(f"Total de ventas acumuladas: {ventas_acumuladas}")

