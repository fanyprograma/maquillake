def pascal_triangle(n):
    # Verificar si el número es válido
    if n <= 0:
        print("Por favor, introduce un número mayor que cero.")
        return

    triangle = [[1]]  # Inicia el triángulo con la primera fila

    for i in range(1, n):
        # Generar la fila actual basándose en la fila anterior
        prev_row = triangle[-1]
        current_row = [1]  # El primer elemento siempre es 1
        for j in range(1, len(prev_row)):
            current_row.append(prev_row[j - 1] + prev_row[j])  # Sumar los elementos adyacentes
        current_row.append(1)  # El último elemento siempre es 1
        triangle.append(current_row)

    # Imprimir el triángulo
    for row in triangle:
        print(" " * (n - len(row)), end="")  # Espacios para alinear
        print(" ".join(map(str, row)))

# Solicitar al usuario la cantidad de filas del triángulo de Pascal
try:
    num = int(input("¿Cuántas filas del triángulo de Pascal deseas ver? "))
    pascal_triangle(num)
except ValueError:
    print("Por favor, introduce un número entero válido.")
