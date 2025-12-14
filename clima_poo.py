# =========================================================
# PROGRAMACIÓN ORIENTADA A OBJETOS (POO): CÁLCULO DE PROMEDIO
# =========================================================

class ClimaSemanal:
    """
    Clase que representa el registro del clima semanal
    y encapsula las temperaturas y los métodos para su gestión.
    """
    
    def __init__(self):
        # 1. ENCAPSULAMIENTO: El atributo _temperaturas está "protegido" 
        self._temperaturas = []
        self._dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
    # ---------------------------------------------------------
    # 2. MÉTODO PARA INGRESAR DATOS
    # ---------------------------------------------------------
    def ingresar_temperaturas(self):
        """
        Permite ingresar las temperaturas diarias, modificando el atributo _temperaturas.
        """
        print("--- Ingreso de Temperaturas Diarias (POO) ---")
        for dia in self._dias:
            while True:
                try:
                    temp = float(input(f"Temperatura del {dia}: "))
                    self._temperaturas.append(temp) 
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")
                    
    # ---------------------------------------------------------
    # 3. MÉTODO PARA CALCULAR PROMEDIO
    # ---------------------------------------------------------
    def calcular_promedio(self):
        """
        Calcula el promedio de las temperaturas encapsuladas.
        """
        if not self._temperaturas:
            return 0.0
        
        suma = sum(self._temperaturas)
        return suma / len(self._temperaturas)

    # ---------------------------------------------------------
    # 4. MÉTODO PARA MOSTRAR INFORMACIÓN
    # ---------------------------------------------------------
    def mostrar_info(self):
        """
        Muestra la información relevante (temperaturas y promedio).
        """
        promedio = self.calcular_promedio()
        print("\n=============================================")
        print("Reporte del Clima Semanal (POO):")
        print(f"Temperaturas registradas: {self._temperaturas}")
        print(f"El promedio semanal del clima es: {promedio:.2f} °C")
        print("=============================================")

# ---------------------------------------------------------
# PROGRAMA PRINCIPAL (Instanciación y uso del Objeto)
# ---------------------------------------------------------
if __name__ == "__main__":
    reporte_semanal = ClimaSemanal()
    reporte_semanal.ingresar_temperaturas()
    reporte_semanal.mostrar_info()