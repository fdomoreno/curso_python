"""
Ejercicios:

#Ejercicio 1: Un vendedor recibe un sueldo base más un 10% extra por cada comisión de sus ventas, el vendedor desea 
saber cuánto dinero obtendrá por contecto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

#Ejercicio 2: Una tienda ofrece descuento del 15% sobre el total de una compra y un cliente desea saber
cuánto deberá pagar finalmente por su compra.

#Ejercicio 3: Un alumno desea saber cuál srá su calificación final en la materia de Algoritmos. Dicha calificación
se compone de tres exámenes parciales.

#Ejercicio 4: Un maestro desea saber sobre qué porcentaje de hombres y que porcentaje de mujeres hay en un grupo
de estudiantes.
"""
import os

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

opcion_escape = "5"
opciones = ["1","2","3","4"]

def vendedor():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Calculo Salario de Vendedor======={bold_color.END}\n")
    salario_base = float(input("Por favor ingresar el salario base: "))
    numero_ventas = int(input("Por favor ingresar el número de ventas: "))
    comision=(salario_base*0.10)*numero_ventas
    print(f"\nEl vendedor recibirá{bold_color.BOLD} {bold_color.BLUE}$ {round(comision):,.2f} MCTE COP{bold_color.END} por concepto de comisiones, y un total de {bold_color.BOLD} {bold_color.GREEN}$ {round(salario_base+comision):,.2f} MCTE COP{bold_color.END} por concepto de salario total.")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def tienda():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Calculo valor final de la compra======={bold_color.END}\n")
    valor_total=float(input("Por favor ingresar el valor total de la compra: "))
    descuento=valor_total*0.15
    print(f"\nEl descuento aplicado corresponde a{bold_color.BOLD} {bold_color.BLUE}$ {round(descuento):,.2f} MCTE COP{bold_color.END}, el valor final de la compra es de {bold_color.BOLD} {bold_color.GREEN}$ {round(valor_total-descuento):,.2f} MCTE COP{bold_color.END}.")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")


def calificaciones():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Calculo de Calificación Final======={bold_color.END}\n")
    calificacion1 = float(input("Por favor ingrese la primera calificacion: "))
    calificacion2 = float(input("Por favor ingrese la segunda calificacion: "))
    calificacion3 = float(input("Por favor ingrese la tercera calificacion: "))
    calificacion_final=round((calificacion1+calificacion2+calificacion3)/3,2)
    color = bold_color.GREEN if calificacion_final>=3 else bold_color.RED
    print(f"\nEl promedio de la calificación del estudiante es: {bold_color.BOLD}{color}{calificacion_final}{bold_color.END}")
    print(f"\n{bold_color.BOLD}========FIN ALGORITMO======={bold_color.END}\n")

def maestro():
    print(f"{bold_color.BOLD}========INICIO ALGORITMO: Porcentaje por genero======={bold_color.END}\n")
    hombres = int(input("Por favor ingrese la cantidad de personas que se identifican dentro del géneros masculino: "))
    mujeres = int(input("Por favor ingrese la cantidad de personas que se identifican dentro del géneros femenino: "))
    otros = int(input("Por favor ingrese la cantidad de personas que no se identifican dentro de estos dos géneros: "))
    total=hombres+mujeres+otros
    print(f"\nPorcentaje de Mujeres:{bold_color.BOLD} {bold_color.PURPLE}{round((mujeres*100)/total,2)}%{bold_color.END}, Porcentaje de Hombres:{bold_color.BOLD} {bold_color.GREEN}{round((hombres*100)/total,2)}%{bold_color.END}, Porcentaje de otros géneros:{bold_color.BOLD} {bold_color.BLUE}{round((otros*100)/total,2)}%{bold_color.END}")

switch_algoritmos = {
	1: vendedor,
	2: tienda,
	3: calificaciones,
	4: maestro
}

while True:
    print(f"{bold_color.BOLD}========Menú de ejercicios======={bold_color.END}")
    print("\nPor favor indique un número de ejercicio que desea ejecutar: ")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}1{bold_color.END}, para ejecutar el algoritmo del calculo de sueldo y comisiones del vendedor")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}2{bold_color.END}, para ejecutar el algoritmo de calculo del pago total de la compra en una tienda")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}3{bold_color.END}, para ejecutar el algoritmo para calcular la calificación final del alumno")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}4{bold_color.END}, para ejecutar el algoritmo para calcular el porcentaje de hombre y mujeres en un curso")
    print(f"{bold_color.BOLD}Ingrese el número: {bold_color.RED}5{bold_color.END}, para salir y terminar la ejecución.")
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