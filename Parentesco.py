parentesco=input("¿Qué eres mio? ")
if parentesco=="hermano" or parentesco=="madre" or parentesco=="padre":
    print("Eres de mi familia")
else:
    print("No eres de mi familia")
print("_________________________________________")
edad=int(input("Ingresa tu edad: "))
prm=input("¿Tienes permiso de tus padres? ")
carnal=input("¿Vas acompañado? ")
if edad>=18 or prm=="si" or carnal=="si":
    print("Puedes entrar al concierto")
else:
    print("No puedes entrar al concierto")
print("_________________________________________")
