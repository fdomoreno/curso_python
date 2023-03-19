import locale
locale.setlocale(locale.LC_ALL, '')

#UNIR TALLER 2 y TALLER 3 en este con funciones y ciclos

SMMLV=1160000
print("====BIENVENIDO AL FORMULARIO DE DATOS BÁSICOS DEL CURSO DE FUNDAMENTOS DE PROGRAMACIÓN EN PYTHON====")
identificacion= input("Por favor ingresar el número de identificacion: ")
nombres= input("Por favor ingresar el nombre: ")
apellidos= input("Por favor ingresar los apellidos: ")
direccion= input("Por favor ingresar la dirección: ")
telefono= input("Por favor ingresar el número de teléfono: ")
edad= input("Por favor ingresar la edad en años: ")
estado_civil= input("Por favor ingresar el estado civil: ")
numero_hijos= input("Por favor ingresar número de hijos: ")
estatura= input("Por favor ingresar la estatura en centimetros: ")
fecha_contratacion= input("Por favor ingresar la fecha de contratación en el formato: DD/MM/AAAA: ")
sueldo_basico= input("Por favor ingresar el sueldo básico en COP, sin puntuación: ")
dias_laborados= input("Por favor ingresar los días laborados: ")
edad= int(edad)
sueldo_basico= float(sueldo_basico)
numero_hijos=int(numero_hijos)
dias_laborados=int(dias_laborados)
print("====LOS DATOS INGRESADOS FUERON: =========")
print("Número de identificacion: ", identificacion)
print("Nombre completo: ", nombres, apellidos)
print("Dirección: ", direccion)
print("Teléfono: ", telefono)
print("Edad: ",edad,"años")
print("Estado civil: ", estado_civil)
print("Número de hijos: ", numero_hijos)
if (estado_civil.upper()=="CASADO") and (numero_hijos>0):
    print("El empleado tiene derecho a paseo en diciembre")
print("Estatura: ",estatura,"cm")
print("Fecha de contratación: ", fecha_contratacion)
print("Sueldo básico: ", locale.format_string('%.2f', float(sueldo_basico), grouping=True, monetary=True), "COP")
print("Días laborados: ",dias_laborados)
if edad>=55:
    bono_prepension=sueldo_basico*0.05
    print(f"El empleado recibe: ${round(bono_prepension,2):,.2f} COP por concepto de bono de prepensión")
else:
    bono_prepension=0
if(sueldo_basico>=1000000 and sueldo_basico<=1500000):
    comision=sueldo_basico*0.02
    print(f"El empleado recibe: ${round(comision,2):,.2f} COP por concepto de comisión")
elif(sueldo_basico>1500000 and sueldo_basico<=2000000):
    comision=sueldo_basico*0.05
    print(f"El empleado recibe: ${round(comision,2):,.2f} COP por concepto de comisión")
else:
    comision=0
if(dias_laborados>20 and sueldo_basico<1000000):
    bono_alimentacion=SMMLV*1.5
    print(f"El empleado recibe: ${round(bono_alimentacion,2):,.2f} COP por concepto de bono de alimentación")
else:
    bono_alimentacion=0
print(f"El empleado devenga en total: ${round(sueldo_basico+bono_alimentacion+comision+bono_prepension,2):,.2f} COP")