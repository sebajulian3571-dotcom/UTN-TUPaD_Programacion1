# Ejercicio 2 
# El Cajero Automático Desarrollen un simulador de cajero automático.

#El usuario comenzará con un saldo inicial de $50,000. El programa debe mostrar un menú
#  que se repita hasta que el usuario decida salir: 1. Consultar saldo. 2. Ingresar dinero. 3.
#  Retirar dinero. 4. Salir. Reglas de negocio: • No se pueden ingresar cantidades negativas. 
# • No se puede retirar más dinero del que hay en el saldo, ni cantidades negativas. 
# Si el usuario intenta retirar de más, mostrar un mensaje de "Fondos insuficientes". 
# • Usar match-case para manejar las opciones del menú.

saldoInicial = 50000
saldoFinal= 0
cantidad= 0

print("1.Consultar saldo. 2. Ingresar dinero. 3. Retirar dinero. 4. Salir.")
opcion=int(input("Ingrese una opción "))

match opcion: 
    case 1: 
        print(f"Su saldo es Saldo {saldoInicial}")

    case 2: 
        print("Ingresar dinero.")
        cantidad= input("Ingrese la cantidad: ")
        while not cantidad.isdigit():
            cantidad=(input("Ingrese la cantidad:"))

        cantidad = int(cantidad)#Transformar
        saldoFinal= saldoInicial + cantidad
        print(f"Su Saldo es {saldoFinal}")

    case 3:
        print("Retirar dinero.")
        cantidad= input("Ingrese la cantidad:") 
        while not cantidad.isdigit():
            cantidad= (input("Ingrese la cantidad:"))

        cantidad = int(cantidad)#Transformar
        if cantidad > saldoInicial:
            print("Saldo Insuficiente")
            print(f"Su actual es {saldoInicial}")
        elif cantidad < saldoInicial:
                saldoFinal = saldoInicial - cantidad
                print(f"Su Saldo es {saldoFinal}")  

    case 4:
        print("Salir")
