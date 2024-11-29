def fibonacci_series(n):
    # Verificar si el número es válido
    if n <= 0:
        print("Por favor, introduce un número mayor que cero.")
        return []

    # Inicializar los dos primeros números de Fibonacci
    series = [0, 1]
    while len(series) < n:
        # Agregar el siguiente número sumando los dos anteriores
        next_number = series[-1] + series[-2]
        series.append(next_number)
    
    return series[:n]  # Devolver solo los primeros 'n' números

# Solicitar al usuario la cantidad de números de la serie
try:
    num = int(input("¿Cuántos números de la serie de Fibonacci deseas ver? "))
    resultado = fibonacci_series(num)
    print(f"La serie de Fibonacci con {num} números es: {resultado}")
except ValueError:
    print("Por favor, introduce un número entero válido.")
