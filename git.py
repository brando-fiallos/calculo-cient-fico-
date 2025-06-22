# Ejercicio 4: Frecuencia de palabras
texto = input("Ingrese una línea de texto: ").lower().split()
frecuencia = {}

for palabra in texto:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, count in frecuencia.items():
    print(f"{palabra}: {count}")