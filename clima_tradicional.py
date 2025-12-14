# =========================================================
# PROGRAMACIÓN TRADICIONAL: CÁLCULO DE PROMEDIO DE TEMPERATURA
# =========================================================

# ---------------------------------------------------------
# 1. FUNCIÓN PARA ENTRADA DE DATOS
# ---------------------------------------------------------
def entrada_temperaturas():
    """
    Solicita al usuario las temperaturas de los 7 días de la semana.
    Retorna una lista de temperaturas (números flotantes).
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("--- Ingreso de Temperaturas Diarias (Grados Celsius) ---")
    
    for dia in dias_semana:
        while True:
            try:
                # La función input() es parte de la entrada de datos
                temp = float(input(f"Temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                # Manejo de errores si el usuario no ingresa un número
                print("Entrada no válida. Por favor, ingrese un número.")
                
    return temperaturas

# ---------------------------------------------------------
# 2. FUNCIÓN PARA EL CÁLCULO DEL PROMEDIO
# ---------------------------------------------------------
def calcular_promedio(datos_temperatura):
    """
    Calcula el promedio de una lista de temperaturas.
    """
    if not datos_temperatura:
        return 0
        
    # El resultado del cálculo es la suma dividida entre la cantidad de elementos
    suma = sum(datos_temperatura)
    promedio = suma / len(datos_temperatura)
    return promedio

# ---------------------------------------------------------
# 3. PROGRAMA PRINCIPAL (Llamada a las funciones)
# ---------------------------------------------------------
if __name__ == "__main__":
    # a. Obtener la lista de temperaturas usando la función de entrada
    temps_semanales = entrada_temperaturas() 
    
    # b. Calcular el promedio usando la función de cálculo
    promedio_clima = calcular_promedio(temps_semanales)
    
    # c. Mostrar el resultado
    print("\n=============================================")
    print(f"Temperaturas registradas: {temps_semanales}")
    print(f"El promedio semanal del clima es: {promedio_clima:.2f} °C")
    print("=============================================")