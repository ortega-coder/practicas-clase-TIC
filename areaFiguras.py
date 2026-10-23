#Programa para calcular áreas
#Área cuadrado; ladoxlado
lado=float(input("Ingresa el lado del cuadrado: "))
areaCuadrado=lado*lado
print(f"El área es: {areaCuadrado}")
#Área de un triangulo
print("-----------------------")
base=float(input("Ingresa la base del triangulo: "))
altura=float(input("Ingresa la altura del triangulo: "))
areaTriangulo=base*altura/2
print(f"El área del triangulo es: {areaTriangulo} ")
#Área de un trapecio
print("-----------------------")
base1=float(input("Ingresa la primera base del trapecio: "))
base2=float(input("Ingresa la segunda base del trapecio: "))
alt=float(input("Ingresa la altura del trapecio: "))
areaTrapecio=(base1+base2)*alt/2
print(f"El área del trapecio es: {areaTrapecio}")
print("-----------------------")
#Área de un círculo
radio=float(input("Ingresa el radio del círculo: "))
pi=3.1416
areaCirculo=pi*(radio*radio)
print(f"El área del círculo es: {areaCirculo}")
print("-----------------------")
#Área del pentágono
lado1=float(input("Ingresa un lado del pentágono: "))
perimetro=lado1*5
apotema=float(input("Ingresa el apotema del pentágono: "))
areaPentagono=perimetro*apotema/2
print(f"El área del pentágono es: {areaPentagono}")
print("-----------------------")