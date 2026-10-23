#Progrma que me indique como me fue
calif=float(input("A ver w, ingresa tu calificación: "))
if calif==10:
    print("Te la rifaste w, Excelente")
elif calif==9:
    print("Muy bien w")
elif calif==8:
    print("Pos bien w")
elif calif==7:
    print("Regular, echale ganas w")
elif calif==6:
    print("Pos apenas w, puedes mejorar")
else:
    print("Lo unico que tenías que hacer y repruebas angel manuel")
print("______________________________________________")
#Solicitar temperatura
temp=float(input("Ingresa la temperatura de tu zona: "))
if temp>=40:
    print("Hace mucho calor")
elif temp>=30 and temp<40:
    print("Pos esta templado")
elif temp >=20 and temp<30:
    print("Esta fresco el clima")
elif temp <20:
    print("Hace frio")
else:
    print("No valido")
print("______________________________________________")
sexo=input("Ingresa tu sexo: ")
edad=int(input("Ingresa tu edad: "))
if sexo=="hombre" and edad>=18:
    print("Puedes sacar la cartilla militar")
else:
    print("No puedes")



