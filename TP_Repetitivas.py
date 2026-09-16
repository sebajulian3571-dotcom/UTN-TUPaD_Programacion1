"""TP integrador – Repetitivas- Condicionales y 
Secuenciales. 

     Ejercicio 1— “Caja del Kiosco” 

Objetivo: Simular una compra con validaciones y cálculo de total. 

Requisitos
1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while). 
2. Pedir cantidad de productos a comprar (número entero positivo, validar con 
        .isdigit() en while). 
3. Por cada producto (usar for): 
        o Pedir precio (entero, validar .isdigit()). 
        o Pedir si tiene descuento S/N (validar con while, aceptar s o n en 
        cualquier mayuscula/minuscula). 
        o Si tiene descuento: aplicar 10% al precio de ese producto. 
4. Al final mostrar: 
        o Total sin descuentos 
        o Total con descuentos 
        o Ahorro total 
        o Promedio por producto (usar float y formatear con :.2f, ejem: 
        x = 3.14159 
        print(f"{x:.2f}"))
        
        Validaciones obligatorias 
            • Sin try/except. 
            • No aceptar vacío en nombre (si queda vacío, es error). 
            • Cantidad > 0 (si ingresa 0, volver a pedir). 
    Salida esperada (ejemplo) 
Cliente: Ana 
Cantidad de productos: 3 
Producto 1 - Precio: 100  Descuento (S/N): s 
Producto 2 - Precio: 50   Descuento (S/N): n 
Producto 3 - Precio: 200  Descuento (S/N): s 

Total sin descuentos: $350 
Total con descuentos: $320.00 
Ahorro: $30.00 
Promedio por producto: $106.67 """

#)))))))))))))))))))))))))))))>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))))))))))))))))))

nombre = ""
cantidad=0
total_sin_descuento=0
total_con_descuento=0
ahorro = 0
promedio = 0
suma_con = 0
suma_sin = 0
pro_s = 0

nombre=input("Ingrese su nombre: ")
 
while not nombre.isalpha():
        print("Nombre invalido debe contener letra sin espacios")
        nombre=input("Ingrese su nombre: ")
       
cantidad = (input("Ingrese la cantidad de productos: "))
while not cantidad.isdigit() or cantidad == "0":
       print ("No puede ser cero, número negativo ó letras") 
       cantidad = (input("Ingrese la cantidad de productos"))
cantidad = int(cantidad)

for i in range(cantidad):
  producto_precio = input(f"producto {i +1} - precio: ")
  while not producto_precio.isdigit() or producto_precio == "0":
     print("Error No puede ser cero, letras o números negativos")
     producto_precio = input(f"producto {i +1} - precio: ")
     
  producto_precio = int(producto_precio)
     
  descuento = input("Tiene Descuento?(S/N): ").lower()
  
  while descuento.lower() != "s" and descuento.lower() != "n":
   print("Error debe ser (S/N)")
   descuento = input("Tiene Descuento?(S/N): ").lower()
   
  if descuento == "s":
     producto_precio = int(producto_precio)     
     suma_con += producto_precio 
     
  else:
     suma_sin += producto_precio

pro_s = suma_con - (suma_con * 0.10)
total_sin_descuento = suma_con + suma_sin
total_con_descuento= pro_s + suma_sin
ahorro= total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad


print (f"Cliente: {nombre}")
print (f"Cantidad de productos: : {cantidad}")
print (f"Total sin  descuento: {total_sin_descuento}")
print (f"Total con  descuento: {total_con_descuento:.2f}")
print(f"Ahorro: {ahorro:.2f}")
print (f"Promedio por producto: {promedio:.2f}")

#)))))))))))))))============)))))))))))))))===================))))))))))))))

"""Ejercicio 2  — “Acceso al Campus y Menú Seguro” 

Objetivo: Login con intentos + menú de acciones con validación estricta. 

Requisitos 
 1. Definir credenciales fijas en el código: 
   o usuario correcto: "alumno" 
   o clave correcta: "python123" 
 2. Permitir máximo 3 intentos para ingresar usuario y clave. 
 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 
        1. Ver estado de inscripción (mostrar “Inscripto”) 
        2. Cambiar clave (pedir nueva clave y confirmación; deben 
        coincidir) 
        3. Mostrar mensaje motivacional (1 frase) 
        4. Salir 
 5. Validación del menú: 
   o Debe ser número (.isdigit()) 
   o Debe estar entre 1 y 4 
Cambio de clave 
        • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, 
        rechazar. 
Salida esperada  
Intento 1/3 - Usuario: alumno 
Clave: xxx 
Error: credenciales inválidas. 
Intento 2/3 - Usuario: alumno 
Clave: python123 
Acceso concedido. 
1) Estado  2) Cambiar clave  3) Mensaje  4) Salir 
Opción: a 
Error: ingrese un número válido. 
Opción: 5 
Error: opción fuera de rango. 
Opción: 2 
Nueva clave: 123 
Error: mínimo 6 caracteres."""

#)))))))))))))))))))))))))))))>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))))))))))))))))))

#Ejercicio 2
print (" ======Acceso al Campus====== ")
usuario_correcto= "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

while intentos < 3:
   print(f"\nIntento {intentos + 1}/3")
   usuario = input("Usuario: ").strip()
   clave = input("Clave: ").strip()
   
   if usuario == usuario_correcto and clave == clave_correcta:
      acceso = True
      print("Acceso concedido.")
      break
   else:
      print("Error: credenciales inválidas.")
      intentos += 1

if not acceso:
   print("Cuenta bloqueada.")
else:
   while True:

      print("\n1) Estado")
      print("2) Cambiar clave")
      print("3) Mensaje")
      print("4) Salir")
      
      opcion = input("Opción: ").strip()

      if not opcion.isdigit():
         print("Error: ingrese un número válido.")
         continue
      opcion = int(opcion)
      if opcion < 1 or opcion > 4:
           print("Error: opción fuera de rango.")
           continue
      if opcion == 1:
         print("Inscripto")
      elif opcion == 2:
         nueva_clave = input("Nueva clave: ").strip()

         if len(nueva_clave) < 6:
            print("Error: mínimo 6 caracteres.")
         else:
            confirmar = input("Confirme la nueva clave: ").strip()

            if nueva_clave == confirmar:
               clave_correcta = nueva_clave
               print("Clave actualizada correctamente.")
            else:
               print("Error: las claves no coinciden.")

      elif opcion == 3:
         print("¡Sigue practicando, cada línea de código te acerca a tu meta!")

      elif opcion == 4:
         print("Hasta luego.")
         break
      
#)))))))))))))))============)))))))))))))))===================))))))))))))))

"""Ejercicio 3 (Alta) — “Agenda de Turnos con 
Nombres (sin listas)” 
Contexto 
Hay 2 días de atención: Lunes y Martes. 
Cada día tiene cupos fijos: 
• Lunes: 4 turnos 
• Martes: 3 turnos 
Reglas 
1. Pedir nombre del operador (solo letras). 
2. Menú repetitivo hasta salir: 
1. Reservar turno 
2. Cancelar turno (por nombre) 
3. Ver agenda del día 
4. Ver resumen general 
5. Cerrar sistema 
3. Reservar: 
o Elegir día (1=Lunes, 2=Martes). 
o Pedir nombre del paciente (solo letras). 
o Verificar que no esté repetido en ese día (comparando con las variables 
ya cargadas). 
o Guardar en el primer espacio libre (ej. lunes1, lunes2…). 
4. Cancelar: 
o Elegir día. 
o Pedir nombre del paciente (solo letras). 
o Si existe, cancelar y dejar el espacio vacío (""). 
5. Ver agenda del día:   
o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si 
está vacío. 
6. Resumen general: 
o Turnos ocupados y disponibles por día. 
o Día con más turnos (o empate). 
Restricciones 
• ❌ No listas, no diccionarios, no sets, no tuplas. 
• ✅ Se permite usar "" como “vacío”. 
• ✅ Validaciones con .isalpha() y .isdigit() (sin try/except). """
 
#)))))))))))))))))))))))))))))>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))))))))))))))))))

# Ejercicio 3 - Agenda de Turnos sin listas

# Operador
operador = ""
while operador == "":
    operador = input("Ingrese nombre del operador: ").strip()
    if not operador.isalpha():
        print("Solo letras.")
        operador = ""

print(f"\nBienvenido/a {operador}!\n")

# Cupos - "" significa libre
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != "5":
    print("\n--- MENU ---")
    print("1. Reservar turno")
    print("2. Cancelar turno (por nombre)")
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    
    opcion = input("Elija opcion: ").strip()

    if not opcion.isdigit():
        print("Ingrese solo numeros 1-5")
        continue

    # 1. RESERVAR
    if opcion == "1":
        dia = input("Dia 1=Lunes / 2=Martes: ").strip()
        if dia != "1" and dia != "2":
            print("Dia invalido.")
            continue

        nombre = input("Nombre del paciente: ").strip()
        if not nombre.isalpha():
            print("Nombre solo letras.")
            continue

        # Verificar repetido en ese dia
        repetido = False
        if dia == "1":
            if nombre.lower() == lunes1.lower() or nombre.lower() == lunes2.lower() or nombre.lower() == lunes3.lower() or nombre.lower() == lunes4.lower():
                repetido = True
        else:
            if nombre.lower() == martes1.lower() or nombre.lower() == martes2.lower() or nombre.lower() == martes3.lower():
                repetido = True
        
        if repetido:
            print(f"{nombre} ya tiene turno ese dia.")
            continue

        # Guardar en primer libre
        guardado = False
        if dia == "1":
            if lunes1 == "":
                lunes1 = nombre
                guardado = True
            elif lunes2 == "":
                lunes2 = nombre
                guardado = True
            elif lunes3 == "":
                lunes3 = nombre
                guardado = True
            elif lunes4 == "":
                lunes4 = nombre
                guardado = True
        else:
            if martes1 == "":
                martes1 = nombre
                guardado = True
            elif martes2 == "":
                martes2 = nombre
                guardado = True
            elif martes3 == "":
                martes3 = nombre
                guardado = True

        if guardado:
            print(f"Turno reservado para {nombre}.")
        else:
            print("No hay cupos disponibles ese dia.")

    # 2. CANCELAR
    elif opcion == "2":
        dia = input("Dia 1=Lunes / 2=Martes: ").strip()
        if dia != "1" and dia != "2":
            print("Dia invalido.")
            continue
        
        nombre = input("Nombre a cancelar: ").strip()
        if not nombre.isalpha():
            print("Nombre solo letras.")
            continue

        borrado = False
        if dia == "1":
            if nombre.lower() == lunes1.lower() and lunes1 != "":
                lunes1 = ""
                borrado = True
            elif nombre.lower() == lunes2.lower() and lunes2 != "":
                lunes2 = ""
                borrado = True
            elif nombre.lower() == lunes3.lower() and lunes3 != "":
                lunes3 = ""
                borrado = True
            elif nombre.lower() == lunes4.lower() and lunes4 != "":
                lunes4 = ""
                borrado = True
        else:
            if nombre.lower() == martes1.lower() and martes1 != "":
                martes1 = ""
                borrado = True
            elif nombre.lower() == martes2.lower() and martes2 != "":
                martes2 = ""
                borrado = True
            elif nombre.lower() == martes3.lower() and martes3 != "":
                martes3 = ""
                borrado = True
        
        if borrado:
            print(f"Turno de {nombre} cancelado.")
        else:
            print("No se encontro ese nombre ese dia.")

    # 3. VER AGENDA DEL DIA
    elif opcion == "3":
        dia = input("Dia 1=Lunes / 2=Martes: ").strip()
        if dia == "1":
            print("\n--- LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print("\n--- MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
        else:
            print("Dia invalido.")

    # 4. RESUMEN GENERAL
    elif opcion == "4":
        # Contar ocupados
        ocup_lunes = 0
        if lunes1 != "": ocup_lunes = ocup_lunes + 1
        if lunes2 != "": ocup_lunes = ocup_lunes + 1
        if lunes3 != "": ocup_lunes = ocup_lunes + 1
        if lunes4 != "": ocup_lunes = ocup_lunes + 1

        ocup_martes = 0
        if martes1 != "": ocup_martes = ocup_martes + 1
        if martes2 != "": ocup_martes = ocup_martes + 1
        if martes3 != "": ocup_martes = ocup_martes + 1

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes: {ocup_lunes} ocupados / {4 - ocup_lunes} libres")
        print(f"Martes: {ocup_martes} ocupados / {3 - ocup_martes} libres")

        if ocup_lunes > ocup_martes:
            print("Dia con mas turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Dia con mas turnos: Martes")
        else:
            print("Empate en cantidad de turnos.")

    elif opcion == "5":
        print(f"\nSistema cerrado por {operador}. Chau!")
    else:
        print("Opcion invalida. 1-5")

#)))))))))))))))============)))))))))))))))===================))))))))))))))

"""Ejercicio 4  — “Escape Room: La Bóveda” 
Historia 
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo 
limitados. 
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. 
Variables iniciales (NO se piden por teclado) 
• energia = 100 
• tiempo = 12 
• cerraduras_abiertas = 0 
• alarma = False 
• codigo_parcial = "" 
Validaciones obligatorias 
• No usar try/except. 
• Pedir nombre del agente y validar con .isalpha() en un while. 
• Validar opciones del menú y cualquier número pedido con .isdigit() en un 
while. 
• El juego debe funcionar con estructuras secuenciales, condicionales y 
repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), 
formateo, etc.). 
Regla anti-spam (muy importante) 
Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al 
iniciar: 
✅ Si el jugador elige Forzar cerradura (opción 1) 3 veces seguidas, entonces: 
• se cobra el costo normal (-20 energía, -2 tiempo), 
• NO abre cerradura, y 
• se activa la alarma automáticamente (alarma = True) porque “la cerradura se 
trabó”. 
Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”. 
Menú de acciones (se repite mientras el juego siga) 
El juego continúa mientras: 
• energia > 0, tiempo > 0, cerraduras_abiertas < 3 
• y no esté bloqueado por alarma. 
En cada turno mostrar el estado y el siguiente menú: 
1. Forzar cerradura (costo: -20 energía, -2 tiempo) 
o Si la energía está por debajo de 40, hay “riesgo de alarma”: 
▪ pedir un número 1-3 (validado). Si elige 3 → alarma=True. 
o Si no hay alarma, abre 1 cerradura. 
o Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y 
no abre. 
2. Hackear panel (costo: -10 energía, -3 tiempo) 
o Debe usar un for de 4 pasos mostrando progreso. 
o En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). 
o Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si 
todavía faltan. 
3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 
energía extra) 
Regla de bloqueo por alarma 
• Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema 
se bloquea y se pierde. 
Condiciones de fin 
• Si cerraduras_abiertas == 3 → VICTORIA 
• Si energia <= 0 o tiempo <= 0 → DERROTA 
• Si se bloquea por alarma → DERROTA (bloqueo)"""

#)))))))))))))))))))))))))))))>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))))))))))))))))))

# Ejercicio 4 - Escape Room: La Boveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente = ""
while agente == "":
    agente = input("Nombre del agente: ").strip()
    if not agente.isalpha():
        print("Solo letras.")
        agente = ""

print(f"\nAgente {agente}, la boveda tiene 3 cerraduras. ¡Suerte!\n")

# Para anti-spam
forzar_seguidas = 0

# Juego mientras tenga recursos y no gane
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    # Regla de bloqueo por alarma
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n[ALARMA ACTIVA] Tiempo critico! Sistema bloqueado.")
        break

    print(f"\n--- ESTADO ---")
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma} | Codigo: {codigo_parcial}")
    print("\n1. Forzar cerradura (-20 energia, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3 tiempo)")
    print("3. Descansar (+15 energia, -1 tiempo)")

    opcion = input("Accion: ").strip()
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        print("Opcion invalida. Use 1, 2 o 3.")
        opcion = input("Accion: ").strip()

    # 1. FORZAR
    if opcion == "1":
        forzar_seguidas = forzar_seguidas + 1

        # Anti-spam: 3 veces seguidas
        if forzar_seguidas == 3:
            print("\n[ANTI-SPAM] Forzaste 3 veces seguidas! La cerradura se trabo.")
            energia = energia - 20
            tiempo = tiempo - 2
            alarma = True
            print("Se activo la alarma y NO abriste cerradura.")
            continue # no abre

        # Costo normal
        energia = energia - 20
        tiempo = tiempo - 2

        # Riesgo de alarma si energia < 40
        if energia < 40:
            print("\n[RIESGO] Energia baja! Riesgo de alarma.")
            num = ""
            while not num.isdigit() or num not in ["1","2","3"]:
                num = input("Elegi un numero 1-3 para estabilizar: ").strip()
                if not num.isdigit() or num not in ["1","2","3"]:
                    print("Debe ser 1, 2 o 3.")
            
            if num == "3":
                alarma = True
                print("Fallaste! Alarma activada.")
            else:
                print("Zafaste del riesgo.")

        if alarma == False:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print(f"Cerradura forzada! Van {cerraduras_abiertas}/3")
        else:
            print("Con alarma activa no pudiste abrir.")

    # 2. HACKEAR
    elif opcion == "2":
        forzar_seguidas = 0 # corta racha

        energia = energia - 10
        tiempo = tiempo - 3

        print("\nHackeando panel...")
        for i in range(1, 5):
            print(f"Paso {i}/4...")
            codigo_parcial = codigo_parcial + "A"
            print(f"Codigo actual: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas = cerraduras_abiertas + 1
            print(f"\nCodigo completo! Se abrio 1 cerradura automaticamente. Van {cerraduras_abiertas}/3")

    # 3. DESCANSAR
    elif opcion == "3":
        forzar_seguidas = 0 # corta racha

        tiempo = tiempo - 1
        energia = energia + 15
        if energia > 100:
            energia = 100

        if alarma == True:
            energia = energia - 10
            print("\nDescansas con alarma ON, -10 energia extra por stress.")

        print(f"\nDescansaste. Energia: {energia}")

# FIN DEL JUEGO
print("\n--- FIN ---")
if cerraduras_abiertas == 3:
    print(f"VICTORIA! Agente {agente} abriste la boveda!")
elif energia <= 0:
    print("DERROTA: Te quedaste sin energia.")
elif tiempo <= 0:
    print("DERROTA: Te quedaste sin tiempo.")
else:
    print("DERROTA: Bloqueo por alarma.")
    
#)))))))))))))))============)))))))))))))))===================))))))))))))))    
    
"""Ejercicio 5  — “Escape Room:"La Arena del 
Gladiador"  
1. Descripción del Escenario  
Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un 
usuario (Gladiador) contra un oponente controlado por la computadora (Enemigo). El 
objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo.  
Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de 
control (if/elif/else), ciclos (while y for) y validación de datos estricta.  
2. Requerimientos Técnicos  
A. Tipos de Datos  
Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego:  
• • String: Para el nombre del jugador.  
• • Int: Para los Puntos de Vida (HP) y cantidad de pociones.  
• • Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5). • Boolean: Para controlar si el juego sigue activo o quién tiene el turno.  
B. Reglas de Validación (¡Importante!)  
• • No está permitido usar bloques try / except.  
• • Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.  
• • Para validar números, debes usar el método .isdigit() dentro de un ciclo 
while.  
3. Flujo del Programa  
Paso 1: Configuración del Personaje  
El programa inicia pidiendo el nombre del Gladiador.  
• • Validación: El nombre solo puede contener letras. Si el usuario ingresa números, 
símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a 
preguntar hasta que sea válido.  
Paso 2: Inicialización de Estadísticas  El programa debe definir las variables iniciales (sin preguntar al usuario):  
• • Vida del Gladiador: 100 (int)  
• • Vida del Enemigo: 100 (int)  
• • Pociones de Vida: 3 (int)  
• • Daño base "Ataque Pesado": 15 (int)  
• • Daño base del enemigo: 12 (int)  
• • Turno Gladiador : True (booleano)  
Paso 3: El Ciclo de Combate  
El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 
puntos de vida.  
Turno del Jugador:  
Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 
opciones:  
1. Ataque Pesado  
2. Ráfaga Veloz (Requiere uso de for)  
3. Curar  
• Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo 
ingresado sea un número (.isdigit()).  
2. Verificar que el número sea 1, 2 o 3.  
o Si falla alguna validación, mostrar mensaje de error y volver a pedir.  
Lógica de las Acciones:  
Acción A: Ataque Pesado (Opción 1)  
• • Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador 
realiza un "Golpe Crítico" multiplicando su daño base por 1.5 (resultado float).  
• • Resta el daño a la vida del enemigo.  
• • Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"  
Acción B: Ráfaga Veloz (Opción 2)  
• • Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for.  
• • El bucle debe repetirse 3 veces (usando range).  
• • Dentro del bucle, en cada repetición: 1. Resta 5 puntos de daño a la vida del enemigo.  
• 2. Muestra el mensaje: " > Golpe conectado por 5 de daño".  
•  • Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción.  
• • Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el 
enemigo ataca igual).  
Turno del Enemigo:  
Justo después de tu acción, el enemigo ataca automáticamente.  
• • Resta el daño base del enemigo (12) a tu vida.  
• • Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"  
Paso 4: Fin del Juego  
Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
• • Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
• • Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."  
4. Ejemplo de Ejecución (Consola)  
Plaintext  --- BIENVENIDO A LA ARENA ---  
Nombre del Gladiador: Leonidas1  
Error: Solo se permiten letras.  
Nombre del Gladiador: Leonidas  
=== INICIO DEL COMBATE ===  
Leonidas (HP: 100) vs Enemigo (HP: 100) | Pociones: 3  
Elige acción:  
1. Ataque Pesado  
2. Ráfaga Veloz  
3. Curar  
Opción: A  
Error: Ingrese un número válido.  
Opción: 2  
>> ¡Inicias una ráfaga de golpes!  
> Golpe conectado por 5 de daño  
> Golpe conectado por 5 de daño  
> Golpe conectado por 5 de daño  
>> ¡El enemigo contraataca por 12 puntos!  
=== NUEVO TURNO ===  
Leonidas (HP: 88) vs Enemigo (HP: 85) | Pociones: 3
Acción C: Curar (Opción 3)"""

#)))))))))))))))))))))))))))))>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>))))))))))))))))))))))

# Ejercicio 5 - La Arena del Gladiador - UTN

# Paso 2: Inicializacion
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
turno_gladiador = True # Boolean obligatorio
juego_activo = True # Boolean para controlar

# Paso 1: Configuracion
print("--- BIENVENIDO A LA ARENA ---")
nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

print("\n=== INICIO DEL COMBATE ===")

# Paso 3: Ciclo de Combate
while vida_gladiador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    opcion = input("Opcion: ").strip()
    # B. Validacion con isdigit
    while not opcion.isdigit() or (opcion != "1" and opcion != "2" and opcion != "3"):
        if not opcion.isdigit():
            print("Error: Ingrese un numero valido.")
        else:
            print("Error: Opcion debe ser 1, 2 o 3.")
        opcion = input("Opcion: ").strip()

    # Accion A: Ataque Pesado
    if opcion == "1":
        if vida_enemigo < 20:
            # Float obligatorio por critico
            dano_final = float(dano_pesado * 1.5)
            print(f"¡GOLPE CRITICO! por {dano_final}!")
        else:
            dano_final = float(dano_pesado)
        
        vida_enemigo = vida_enemigo - int(dano_final)
        print(f"¡Atacaste al enemigo por {int(dano_final)} puntos de daño!")

    # Accion B: Rafaga Veloz - REQUIERE FOR
    elif opcion == "2":
        print(">> ¡Inicias una rafaga de golpes!")
        for i in range(3):
            vida_enemigo = vida_enemigo - 5
            print(" > Golpe conectado por 5 de daño")
            if vida_enemigo < 0:
                vida_enemigo = 0

    # Accion C: Curar
    elif opcion == "3":
        if pociones > 0:
            vida_gladiador = vida_gladiador + 30
            if vida_gladiador > 100:
                vida_gladiador = 100
            pociones = pociones - 1
            print(f"Te curaste +30 HP. Vida actual: {vida_gladiador}. Pociones restantes: {pociones}")
        else:
            print("¡No quedan pociones!")
            print("Pierdes el turno!")

    # Turno del Enemigo
    if vida_enemigo > 0:
        vida_gladiador = vida_gladiador - dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos!")

    if vida_gladiador > 0 and vida_enemigo > 0:
        print("\n=== NUEVO TURNO ===")

# Paso 4: Fin del Juego
print("\n--- FIN DEL COMBATE ---")
if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
