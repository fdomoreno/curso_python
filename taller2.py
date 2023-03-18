"""
Ejercicios:

#Ejercicio 1: Un vendedor recibe un sueldo base más un 10% extra por cada comisión de sus ventas, el vendedor desea 
saber cuánto dinero obtendrá por contecto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

#Ejercicio 2: Un vendedor recibe un sueldo base más un 10% extra por cada comisión de sus ventas, el vendedor desea 
saber cuánto dinero obtendrá por contecto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

#Ejercicio 3: Un vendedor recibe un sueldo base más un 10% extra por cada comisión de sus ventas, el vendedor desea 
saber cuánto dinero obtendrá por contecto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

#Ejercicio 4: Un vendedor recibe un sueldo base más un 10% extra por cada comisión de sus ventas, el vendedor desea 
saber cuánto dinero obtendrá por contecto de comisiones por las tres ventas que realiza en el mes y el total 
que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

"""
import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

opcion_escape = "4"
opciones = ["1","2","3"]
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

while True:
    print("========Menú de ejercicios=======")
    print("\nPor favor indique un número de ejercicio que desea ejecutar: ")
    print(f"{bold_color.BOLD}Ingrese le número: {bold_color.RED}1{bold_color.END}, para ejecutar el algoritmo del calculo de sueldo y comisiones del vendedor")
    print(f"{bold_color.BOLD}Ingrese le número: {bold_color.RED}2{bold_color.END}, para realizar el calculo de sueldo y comisiones de vendedor")
    print(f"{bold_color.BOLD}Ingrese le número: {bold_color.RED}3{bold_color.END}, para realizar el calculo de sueldo y comisiones de vendedor")
    print(f"{bold_color.BOLD}Ingrese le número: {bold_color.RED}4{bold_color.END}, para salir y terminar la ejecución.")
    palabra = input("\nIngresa opción: ")
    clear()
    if palabra == opcion_escape:
        break
    else:
        if palabra in opciones:
            print("Opción valida")
        else:
            print(f"{bold_color.BOLD}{bold_color.RED}La opción ingresada no corresponde a una opción valida, por favor ingresar la opción correcta.{bold_color.END}\n")

print(f"{bold_color.BOLD}Adios!{bold_color.END}")