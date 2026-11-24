#Mostrar el menú principal
#Se uso ia para descubrir como hacer un bucle, por eso ese "while True"
placas=[]
marcas=[]
tipos=[]
colores=[]
espacio=0
lugar=0
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
    if espacio>4:
         print(" ") 
         print("¡No hay espacio suficiente en la cochera!")
         print(" ") 
    else:
         numCar=0
         i=0
         print(" ")
         print("--//Agregar auto a la cochera//--")
         print(" ")
         placa=input("Ingresa los 5 dígitos de las palcas: "),
         marca=input("Ingresa la marca del auto: "),
         tipo=input("Ingresa el tipo del auto: "),
         color=input("Ingresa el color del auto: ")
         numCar=numCar+1
         i=i+1
         lugar=lugar+1
         espacio=espacio+1
         placas.append(placa)
         marcas.append(marca)
         tipos.append(tipo)
         colores.append(color)
         print(" ")
         print("--//Auto agregado a la cochera//--")
         print(f"Su lugar es el número:",lugar)
         print(" ")       
 elif opMenu ==2:
     print(" ")
     print("--//Mostrar los autos de la cochera//--")
     if lugar==0:
        print("¡No hay autos en la cochera!")
        print(" ")
     else:
                print(" ")
                print("Placas:",placas)
                print("Marcas:",marcas)
                print("Tipos:",tipos)
                print("Colores:",colores)
                print(" ")
 elif opMenu ==3:
     print(" ")
     print("--//Mostrar precios de tarifa//--")
     print(" ")
     print("10 min --> $10")
     print("30 min --> $30")
     print("1 hr --> $60")
     print("Por cada hr extra --> $60 + $5")
     print(" ")
 elif opMenu ==4:
     print(" ")
     print("--//Pagar tarifa//--")
     print(" ")
     buscarPlaca=input("Ingresa los 5 dígitos de la placa:")
     if buscarPlaca==placas(placa):
         tiempoMin=int(input("Ingresa la cantidad de minutos: "))
         tiempoHr=int(input("Ingresa la cantidad de horas: "))
         if tiempoHr==1:
             tarifa=(tiempoMin*1)+(tiempoHr*60)
             print(f"El costo de tarifa es de: $",tarifa)
         elif tiempoHr==0:
             tarifa=(tiempoMin*1)+(tiempoHr*60)
             print(f"El costo de tarifa es de: $",tarifa)
         else:
             tarifa=(tiempoMin*1)+(tiempoHr*60+(tiempoHr*5-5))
             print(f"El costo de tarifa es de: $",tarifa)
             print(" ")
     else:
         print("¡No hay placas registradas!")
 elif opMenu ==5:
     print("Saliendo del programa w...")
     print(" ")
     break
 else:
    print("Opción no válida, intenta de nuevo.")
    print(" ")
    

