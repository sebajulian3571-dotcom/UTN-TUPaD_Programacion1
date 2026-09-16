# Ejercicio 3
# PUNTO DE VENTA(Fast Food) 
# Creen un programa para gestionar los pedidos de un local de comida rápida. El programa debe tener un menú que le permita al cajero
# ir sumando productos a la cuenta de un cliente. 
# Menú principal: 1. Agregar Hamburguesa ($4500) 2. Agregar Papas Fritas ($2000) 3. Agregar Bebida ($1500) 4. Pagar el pedido (Cierra el ticket)
# 5. Cancelar pedido y salir 
# Requisitos: 
# • Cada vez que se elige la opción 1, 2 o 3, se debe sumar el precio al total y avisar por pantalla ("Hamburguesa agregada. Total actual: $...").
# • Si se elige Pagar (Opción 4), el programa debe mostrar el total a pagar y pedirle al cajero que ingrese con cuánto efectivo paga el cliente.
# • ¡Atención! Si el efectivo ingresado es menor al total, el programa debe usar un bucle while para seguir pidiendo dinero hasta que alcance o supere el total.
#      Una vez que alcanza, debe mostrar el cambio (vuelto) a devolver al cliente, reiniciar el total a $0 y volver al menú principal para el siguiente cliente. 
# • La opción 5 finaliza el programa por completo. 

hamburguesa = 4500
papasFritas = 2000
bebida = 1500
total_1 = 0
dinero = 0
deuda = 0
saldo= 0

print("Menú principal")
print("1.) Agregar Hamburguesa (4500) /  2.) Agregar Papas Fritas ($2000) /  3.) Agregar Bebida ($1500)" )
print ("4.) Pagar el pedido (Cierra el ticket) / 5.  Cancelar pedido y salir")

opcion = int(input("Ingresa la opcion: "))

match opcion:
    
    case 1:
        cantidad=input("Ingrese la cantidad: ")
        while not cantidad.isdigit():
            cantidad=input("Ingrese la cantidad: ")
        
        cantidad = int(cantidad) #Transformar
        for cont in range(cantidad + 1):
            total_1= hamburguesa * cont
            cont =+ 1
        total_1 = total_1
        
        print(f"Hamburguesa agrgada ({cantidad}) Total actual {total_1}")
        
    case 2:
        cantidad=input("Ingrese la cantidad: ")
        while not cantidad.isdigit():
            cantidad=input("Ingrese la cantidad: ")
            
        cantidad = int(cantidad) #Transformar
        for cont in range(cantidad + 1):
            total_1= papasFritas * cont
            cont =+ 1
        total_1 = total_1
            
        print(f"Papas Fritas agrgadas ({cantidad}) Total actual {total_1}")
        
    case 3:
           cantidad=input("Ingrese la cantidad: ")
           while not cantidad.isdigit():
               cantidad=input("Ingrese la cantidad: ")
           
           cantidad = int(cantidad) #Transformar
           for cont in range(cantidad + 1):
               total_1= bebida * cont
               cont =+ 1
           total_1 = total_1
           
           print(f"bebidas agrgadas ({cantidad}) Total actual {total_1}")

    case 4:
        deuda = int(input("Ingrese el monto a cobrar: "))
        dinero = int(input("Efectivo recibido: "))

        while deuda !=  dinero: 
            saldo = deuda - dinero
            print("Falta", saldo)
            
            pedirMas = int(input("pedir más dinero: "))
            dinero = dinero + pedirMas
           
        print("Deuda cancelada")
        
    case _:
        print("Pedido Cancelado.. siguiente pedido")

