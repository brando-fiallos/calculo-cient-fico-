# Ejercicio 5: Tienda con diccionarios
productos = {
    "manzana": 1.50,
    "banana": 0.75,
    "naranja": 1.20,
    "pan": 2.50,
    "leche": 3.00
}

print("Productos disponibles:")
for producto, precio in productos.items():
    print(f"- {producto.capitalize()}: ${precio:.2f}")

while True:
    busqueda = input("\nBuscar producto (o 'salir' para terminar): ").lower()
    if busqueda == 'salir':
        break
    if busqueda in productos:
        print(f"{busqueda.capitalize()}: ${productos[busqueda]:.2f}")
    else:
        print("Producto no encontrado.")
