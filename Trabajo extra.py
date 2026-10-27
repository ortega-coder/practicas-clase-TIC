sexo=input("Ingresa tu sexo (hombre o mujer):")
edad=int(input("Ingresa tu edad: "))
estciv=input("Ingresa tu estado civil: ")
cantHijos=int(input("Ingresa la cantidad de hijos: "))

if sexo=="mujer" and cantHijos==1 and edad<18:
    print("Eres mujer, tienes un hijo y eres menor de edad, entonces el apoyo será de $800")

elif sexo=="mujer" and cantHijos==1 and edad>=18:
    print("Eres mujer, tienes un hijo y eres mayor de edad, entonces el apoyo será de $300")

elif sexo=="mujer" and cantHijos>1 and edad<18:
    print("Eres mujer, tienes mas de un hijo y eres menor de edad, entoces el apoyo será de $1500")

elif sexo=="mujer" and cantHijos>1 and edad>=18:
    print("Eres mujer, tienes mas de un hijo y eres mayor de edad, entonces el apoyo será de $500")

elif sexo=="hombre" and cantHijos>=1 and estciv=="soltero":
    print("Eres hombre y tienes hijos, su apoyo será de $780")
else:
    print("No válido")
