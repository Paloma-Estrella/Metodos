def media(x: list[float]) -> float:
    """Calcula la media aritmética de una lista de valores.

    Args:
        x (list[float]): Lista de números reales.

    Returns:
        float: El valor promedio (media) de los elementos.
    """
    return sum(x) / len(x)


def diferencia_cuadrado(x: list[float]) -> float:
    """Calcula la sumatoria de los cuadrados de las diferencias 
    de cada elemento respecto a la media de X: Σ(X - X̄)²

    Args:
        x (list[float]): Lista de valores de la variable X.

    Returns:
        float: Suma total de cuadrados de las diferencias de X.
    """
    la_media = media(x)
    la_diferencia = 0
    for i in x:
        la_diferencia = la_diferencia + (i - la_media) * (i - la_media)
    return la_diferencia


def diferencia_xy(x: list[float], y: list[float]) -> float:
    """Calcula la sumatoria del producto cruzado de las diferencias 
    de X e Y respecto a sus respectivas medias: Σ(X - X̄)(Y - Ȳ)

    Args:
        x (list[float]): Lista de valores de la variable X.
        y (list[float]): Lista de valores de la variable Y.

    Returns:
        float: Sumatoria de los productos cruzados.
    """
    mediax = media(x)
    mediay = media(y)
    lista_xy = [(a - mediax) * (b - mediay) for a, b in zip(x, y)]
    sumatoria = sum(lista_xy)
    return sumatoria


def obtener_b1(x: list[float], y: list[float]) -> float:
    """Calcula la pendiente (b1) del modelo de regresión lineal.

    Args:
        x (list[float]): Lista de valores de la variable X.
        y (list[float]): Lista de valores de la variable Y.

    Returns:
        float: Valor de la pendiente b1.
    """
    diferencia = diferencia_xy(x, y)
    diferencia_cuadrados = diferencia_cuadrado(x)
    return diferencia / diferencia_cuadrados


def obtener_b0(x: list[float], y: list[float]) -> float:
    """Calcula la ordenada al origen (b0) del modelo de regresión lineal.

    Args:
        x (list[float]): Lista de valores de la variable X.
        y (list[float]): Lista de valores de la variable Y.

    Returns:
        float: Valor de la intersección b0.
    """
    mediay = media(y)
    mediax = media(x)
    b1 = obtener_b1(x, y)
    return mediay - (b1 * mediax)


def calcular_regresion_lineal() -> None:
    """Solicita los datos al usuario, imprime la tabla detallada paso a paso 
    y muestra el modelo de regresión lineal estimado (Ŷ = b0 + b1x).

    Args:
        None (Los datos se obtienen mediante la entrada interactiva por consola).

    Returns:
        None: Imprime en consola los resultados tabulados y la ecuación final.
    """
    print("--- Calculadora de Regresión Lineal (Ŷ = b0 + b1x) ---")
    
    # Ingresar los datos
    entrada_y = input("Ingresa los números de Y separados por espacios (ej: 6 8 9 5 4.5 9.5): ")
    entrada_x = input("Ingresa los números de X separados por espacios (ej: 3 4 6 4 2 5): ")
    
    try:
        # Convertir entradas a listas de float
        y = [float(val) for val in entrada_y.split()]
        x = [float(val) for val in entrada_x.split()]
        
        # Validar que tengan la misma cantidad de elementos y no estén vacías
        if len(x) != len(y) or not x:
            print("\nError: Las listas deben tener la misma cantidad de elementos y no pueden estar vacías.")
            return
        
        n = len(x)
        
        # Obtener medias usando las funciones modulares
        media_x = media(x)
        media_y = media(y)
        sum_x = sum(x)
        sum_y = sum(y)
        
        # 1. Imprimir encabezado de la tabla estilo reporte
        print("\n" + "="*75)
        print(f"{'Y':<10} | {'X':<10} | {'(X - X̄)²':<22} | {'(X - X̄)(Y - Ȳ)'}")
        print("="*75)
        
        # 2. Iterar fila por fila mostrando cada renglón detallado
        for i in range(n):
            yi = y[i]
            xi = x[i]
            
            dif_x = xi - media_x
            dif_y = yi - media_y
            
            cuadrado_x = dif_x ** 2
            prod_cruzado = dif_x * dif_y
            
            str_cuadrado = f"({xi:g} - {media_x:g})² = {cuadrado_x:g}"
            str_prod = f"({xi:g} - {media_x:g})({yi:g} - {media_y:g}) = {prod_cruzado:g}"
            
            print(f"{yi:<10.1f} | {xi:<10.1f} | {str_cuadrado:<22} | {str_prod}")
        
        print("="*75)
        
        # 3. Obtener sumatorias totales usando las funciones dedicadas
        suma_cuadrados_x = diferencia_cuadrado(x)
        suma_productos = diferencia_xy(x, y)
        
        # Imprimir totales al pie de la tabla
        print(f"ΣY = {sum_y:g}          | ΣX = {sum_x:g}          | Σ(X - X̄)² = {suma_cuadrados_x:g}      | Σ(X - X̄)(Y - Ȳ) = {suma_productos:g}")
        print(f"Ȳ = {sum_y:g}/{n} = {media_y:g}     | X̄ = {sum_x:g}/{n} = {media_x:g}")
        print("="*75)
        
        # Validar división entre cero antes de calcular el modelo
        if suma_cuadrados_x == 0:
            print("\nNo es posible calcular la regresión lineal: la suma de cuadrados de X es cero (todos los valores de X son idénticos).")
            return

        # 4. Cálculo de los coeficientes empleando las funciones modulares
        b1 = obtener_b1(x, y)
        b0 = obtener_b0(x, y)
        
        print("\n" + "--- MODELO DE REGRESIÓN LINEAL ---")
        print(f"Pendiente (b1) = Σ(X - X̄)(Y - Ȳ) / Σ(X - X̄)² = {suma_productos:g} / {suma_cuadrados_x:g} = {b1:.4f}")
        print(f"Intersección (b0) = Ȳ - b1(X̄) = {media_y:g} - ({b1:.4f} * {media_x:g}) = {b0:.4f}")
        print(f"\nEcuación estimada: Ŷ = {b0:.4f} + {b1:.4f}x")
        print("="*75)

    except ValueError:
        print("\nError: Asegúrate de ingresar únicamente números válidos.")


# Ejecutar el programa principal
if __name__ == "__main__":
    calcular_regresion_lineal()
