alumnos=["Juanito","Angelito"]
alumno1={
    "nombre":"Juanito",
    "edad":15,
    "promedio":8.2
}
alumno2={
    "nombre":"Angelito",
    "edad":18,
    "promedio":10
}
print("Nombre:",alumno1.get("nombre"))
print("Nombre:",alumno1.get("nombre"))
alumno1["nombre"]="Pedrito"
print("Nombre:", alumno1.get("nombre"))
for clave, valor in alumno1.items():
    print(clave, ":", valor)