print("=== Calculadora de Promedio de Notas ===")

nombre = input("Ingrese el nombre del estudiante: ")

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
nota5 = float(input("Ingrese la quinta nota: "))      #en esta parte se añadieron dos notas mas 

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
#aqui se añadieron las notas a la formula matematica

print("\n=== Resultado ===")
print("Estudiante:", nombre)
print("Promedio:", round(promedio, 2))

if promedio >= 70:
    print("Resultado: Aprobado")
else:
    print("Resultado: No aprobado")

print("\nFin del programa.")