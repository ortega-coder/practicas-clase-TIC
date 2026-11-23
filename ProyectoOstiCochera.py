#Mostrar el menú principal
#Se uso ia para descubrir como hacer un bucle, por eso ese "while True"
placas=[]
marcas=[]
tipos=[]
colores=[]
while True:
 print("BIENVENIDOS A LA OSTICOCHERA")
 print("---//Menú Principal//---")
 print(" ")
 print("1. Agregar auto a la cochera")
 print("2. Mostrar los autos de la cochera")
 print("3. Mostrar precios de tarifa")
 print("4. Pagar tarifa")
 print("5. Salir del programa")
 print(" ")
#Permitir al usuario elegir una opción
 opMenu=int(input("Ingresa una opción por su número: "))
 if opMenu ==1:
    numCar=0
    i=0
    print("--//Agregar auto a la cochera//--")
    print(" ")
    placa=input("Ingresa los 5 dígitos de las palcas: ")
    marca=input("Ingresa la marca del auto: ")
    tipo=input("Ingresa el tipo del auto: ")
    color=input("Ingresa el color del auto: ")
    numCar=numCar+1
    placas.append(placa)
    marcas.append(marca)
    tipos.append(tipo)
    colores.append(color)
    print(" ")
    print("--//Auto agregado a la cochera//--")
    print(" ")
 elif opMenu ==2:
     print("--//Mostrar los autos de la cochera//--")
     if numCar<0:
        print("¡No hay autos en la cochera!")
     else:
                print(" ")
                print("Placas:",placas)
                print("Marcas:",marcas)
                print("Tipos:",tipos)
                print("Colores:",colores)
                print(" ")
 elif opMenu ==3:
     print("Opción 3 w")
     print(" ")
 elif opMenu ==4:
     print("Opción 4 w")
     print(" ")
 elif opMenu ==5:
     print("Saliendo del programa w...")
     print(" ")
     break
 else:
     print("Opción no válida, intenta de nuevo.")
     print(" ")




