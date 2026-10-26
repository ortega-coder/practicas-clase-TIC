nombre=input("Ingresa el nombre del empleado: ")
pagoxhora=int(input("Ingresa el pago por hora: "))
horastr=int(input("Ingresa las horas trabajadas del mes: "))
sueldo=pagoxhora*horastr
print(f"Su sueldo es de: {sueldo} pesos")
if sueldo>=100 and sueldo<=300:
    sueldof=sueldo+500
    print(f"Su sueldo con bonos es de: {sueldof} pesos")
elif sueldo>300 and sueldo<=1500:
    sueldof1=sueldo+1700
    print(f"Su sueldo con bonos es de: {sueldof1} pesos")
elif sueldo>1500 and sueldo<=3000:
    sueldof2=sueldo+3500
    print(f"Su sueldo con bonos es de: {sueldof2} pesos")
elif sueldo>3000 and sueldo<=8000:
    sueldof3=sueldo+8500
    print(f"Su sueldo con bonos es de: {sueldof3} pesos")
elif sueldo>8000:
    sueldof4=sueldo+10000
    print(f"Su sueldo con bonos es de: {sueldof4} pesos")
else:
    print("No válido")
