import locale
locale.setlocale(locale.LC_ALL, '')
SMMLV=1160000

def derecho_paseo(estado,hijos):
    if (estado.upper()=="CASADO") and (hijos>0):
        print("El empleado tiene derecho a paseo en diciembre")
    else:
        print("El empleado NO tiene derecho a paseo en diciembre")
        
def bono_pre_pension(edad, sueldo_b):
    if edad>=55:
        derecho_bono_prepension=sueldo_b*0.05
    else:
        derecho_bono_prepension=0
    print(f"El empleado recibe: ${round(derecho_bono_prepension,2):,.2f} COP por concepto de bono de prepensión")
    return derecho_bono_prepension

def comision(sueldo_b):
    if(sueldo_b>=1000000 and sueldo_b<=1500000):
        derecho_comision=sueldo_b*0.02
    elif(sueldo_b>1500000 and sueldo_b<=2000000):
        derecho_comision=sueldo_b*0.05
    else:
        derecho_comision=0
    print(f"El empleado recibe: ${round(derecho_comision,2):,.2f} COP por concepto de comisión")
    return derecho_comision

def derecho_bono_alimento(dias_lab,sueldo_b):
    if(dias_lab>20 and sueldo_b<1000000):
        bono=SMMLV*1.5
    else:
        bono=0
    print(f"El empleado recibe: ${round(bono,2):,.2f} COP por concepto de bono de alimentación")
    return bono

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
print("Estatura: ",estatura,"cm")
print("Fecha de contratación: ", fecha_contratacion)
print("Sueldo básico: ", locale.format_string('%.2f', float(sueldo_basico), grouping=True, monetary=True), "COP")
print("Días laborados: ",dias_laborados)
derecho_paseo(estado_civil,numero_hijos)
bono_prepension=bono_pre_pension(edad,sueldo_basico)
derecho_a_comision=comision(sueldo_basico)
bono_alimentacion=derecho_bono_alimento(dias_laborados, sueldo_basico)
print(f"El empleado devenga en total: ${round(sueldo_basico+bono_alimentacion+derecho_a_comision+bono_prepension,2):,.2f} COP")