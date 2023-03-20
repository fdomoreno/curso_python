"""
Ejercicios:

#Ejercicio 1: Crear un bucle que cuente todos los números pares hasta el 100 (ciclo for).

#Ejercicio 2: Haz una tabla de multiplicar utilizando el ciclo for (ciclo for).

#Ejercicio 3: Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
que ha cumplido (desde 1 hasta su edad) (ciclo for).

#Ejercicio 4: Escribir un programa que pida al usuario un número entero positivo y muestre en pantalla
todos los números impares desde 1 hasta ese número separados por comas.

#Ejercicio 5: Encuentra la suma de todos los números pares del 1 al 100 (ciclo for).
"""
import os
import locale

locale.setlocale(locale.LC_ALL, '')
SMMLV=1160000
class bold_color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

opcion_escape = "6"
opciones = ["1","2","3","4","5"]

def contar_pares_a_cien():
    print(f"{bold_color.BOLD}====INICIO ALGORITMO: Números pares hasta 100===={bold_color.END}\n")
    cantidad_pares=0
    for i in range(1,101,1):
        if i % 2 == 0:
            cantidad_pares+=1
        #print(f"{cantidad_pares} en {i}")
    print(f"Cantidad de números pares de 1 a 100= {bold_color.BOLD}{bold_color.RED}{cantidad_pares}{bold_color.END}")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def tabla_multiplicar():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Tabla de multiplicar======={bold_color.END}\n")
    numero = input("Ingrese el número del cual quiere mostrar la tabla de multiplicar: ")
    numero = int(numero)
    for i in range(1,11,1):
        print(f"{i} x {numero} = {bold_color.BOLD}{bold_color.RED}{i*numero}{bold_color.END}")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def anios_cumplidos():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Años cumplidos======={bold_color.END}\n")
    edad = input("Ingrese su edad: ")
    edad = int(edad)
    anio_actual=2023
    anio_inicial=anio_actual-edad
    for i in range(anio_inicial,anio_actual+1):
        print(f"En el año {bold_color.BOLD}{bold_color.RED}{i}{bold_color.END} usted cumplió {bold_color.BOLD}{bold_color.RED}{(i-anio_inicial)+1}{bold_color.END}")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def numeros_impares():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Presentación de números impares======={bold_color.END}\n")
    numero = input("Ingrese un número entero positivo: ")
    numero = int(numero)
    for i in range(1,numero+1,2):
        if i < numero:
            print(i, end=",")
        else:
            print(i)
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def suma_pares():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Suma números pares hasta 100======={bold_color.END}\n")
    suma_pares=0
    for i in range(1,101,1):
        if i % 2 == 0:
            suma_pares+=i
        #print(f"{cantidad_pares} en {i}")
    print(f"Total de la suma de números pares de 1 a 100= {bold_color.BOLD}{bold_color.RED}{suma_pares}{bold_color.END}")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

switch_algoritmos = {
    1: contar_pares_a_cien,
	2: tabla_multiplicar,
	3: anios_cumplidos,
	4: numeros_impares,
	5: suma_pares,
}

while True:
    print(f"{bold_color.BOLD}========Menú de ejercicios======={bold_color.END}")
    print("\nPor favor indique un número de ejercicio que desea ejecutar: ")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}1{bold_color.END}, para ejecutar el algoritmo para calcular los números pares hasta 100")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}2{bold_color.END}, para ejecutar el algoritmo para mostrar la tabla de multiplicar")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}3{bold_color.END}, para ejecutar el algoritmo para escribir años cumplidos")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}4{bold_color.END}, para ejecutar el algoritmo para escribir números impares de 1 al número ingresado")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}5{bold_color.END}, para ejecutar el algoritmo para calcular suma de números pares de 1 al 100")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}6{bold_color.END}, para salir y terminar la ejecución.")
    opcion = input("\nIngresa opción: ")
    clear()
    if opcion == opcion_escape:
        break
    else:
        if opcion in opciones:
            switch_algoritmos.get(int(opcion))()
        else:
            print(f"{bold_color.BOLD}{bold_color.RED}La opción ingresada no corresponde a una opción valida, por favor ingresar la opción correcta.{bold_color.END}\n")

print(f"{bold_color.BOLD}{bold_color.RED}Adios!{bold_color.END}")