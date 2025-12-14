# Comparativa: Programación Orientada a Objetos (POO) vs. Programación Tradicional

Ambos enfoques resuelven el problema del promedio semanal de temperatura, pero utilizan estructuras muy diferentes para organizar el código.

## 1. Programación Orientada a Objetos (POO) - (`clima_poo.py`)

| Concepto Clave | Aplicación en el Código | Ventaja |
| :--- | :--- | :--- |
| **Clase/Objeto** | Se define la Clase `ClimaSemanal` y se crea un Objeto `reporte_semanal`. | Agrupa los datos y las funciones que los manipulan en una única entidad. |
| **Encapsulamiento** | Las temperaturas (`self._temperaturas`) están protegidas y solo se acceden mediante los métodos de la clase (ej. `ingresar_temperaturas`). | Aísla y protege los datos, mejorando la seguridad y el control del código. |
| **Estructura** | El programa es una secuencia de llamadas a **métodos** del objeto. | Modelado lógico, ideal para programas grandes o que simulan entidades reales. |

## 2. Programación Tradicional (Funcional) - (`clima_tradicional.py`)

| Concepto Clave | Aplicación en el Código | Ventaja |
| :--- | :--- | :--- |
| **Funciones** | Se usan funciones independientes (`entrada_temperaturas()` y `calcular_promedio()`). | La lógica se divide en tareas pequeñas y reutilizables. |
| **Datos Flotantes** | La lista de temperaturas es creada fuera de las funciones y se pasa como **argumento**. | Los datos y la lógica de procesamiento están claramente separados. |
| **Estructura** | El programa es una secuencia de **llamadas a funciones** que se ejecutan en orden. | Más simple y directo, ideal para resolver problemas pequeños y lineales. |

---

**Conclusión:** La solución POO ofrece mejor **organización, modularidad y control de datos** gracias al encapsulamiento, haciendo el código más robusto y escalable a futuro.