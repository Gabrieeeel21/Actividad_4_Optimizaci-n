# 📄 Actividad Autónoma 4: Buenas Prácticas en Programación para Ciencia de Datos

<<<<<<< HEAD
**Nombres:** Gabriel Alejandro Niama Martínez
**Fecha:** 23/11/2025
**Carrera:** Ciencia de Datos e Inteligencia Artificial
=======
**Nombres:** Gabriel Alejandro Niama Martínez.

**Fecha:** 23/11/2025

**Carrera:** Ciencia de datos e Inteligencia artificial.

>>>>>>> ee188ca21a6c2fb885b6c9c0583b902520930962
**Periodo académico:** 2025 - 2S

**Semestre:** Tercero

**Repositorio GitHub:** [PEGAR AQUÍ EL ENLACE COMPLETO DE TU REPOSITORIO]

---

## 1. Introducción: Contexto y Problema Inicial

El presente informe documenta la aplicación de principios de **buenas prácticas de programación** y técnicas de **optimización algorítmica** sobre un código Python inicialmente ineficiente. El objetivo del script es identificar números primos en un rango de 1 a 100,000.

La versión original del código (`codigo_original.py`) utilizaba una estrategia de **fuerza bruta** para la comprobación de primalidad, iterando sobre todos los posibles divisores. Esta aproximación fue altamente ineficiente, consumiendo un tiempo de ejecución de **37.6650 segundos**.

El propósito de esta actividad es transformar este código ineficiente y cuantificar la mejora del rendimiento lograda mediante el análisis de tiempos y profiling.

---

## 2. Estrategias de Optimización Aplicadas

La optimización se centró en reducir la **complejidad algorítmica** (el principal cuello de botella) y en adoptar mejores prácticas para la manipulación de datos.

### 2.1. Optimización Algorítmica: Raíz Cuadrada

La mejora de rendimiento más significativa se obtuvo al modificar la lógica de la función `es_primo(n)`. Se aplicó el teorema matemático que establece que, si un número $n$ tiene un divisor, al menos uno de ellos debe ser menor o igual a la **raíz cuadrada de $n$** ($\sqrt{n}$).

Al reducir el rango de iteración del bucle, la complejidad del algoritmo se redujo de $O(n)$ a $O(\sqrt{n})$, disminuyendo de forma exponencial el número total de cálculos requeridos.

### 2.2. Uso de Comprensión de Listas (*List Comprehensions*)

Se sustituyó el bucle `for` tradicional por una **List Comprehension** para construir la lista final de números primos. Esta sintaxis es más rápida y concisa en Python, ya que su ejecución está optimizada a nivel de C, mejorando la eficiencia en la creación de estructuras de datos.

### 2.3. Incorporación de NumPy para Ciencia de Datos

Se incorporó la librería **NumPy** (`import numpy as np`) para manejar el arreglo final de números primos. Esta es una **buena práctica fundamental** en el desarrollo de Ciencia de Datos, ya que, aunque su impacto en el tiempo de la primalidad es menor, prepara el código para futuras operaciones vectorizadas de alto rendimiento.

---

## 3. Resultados y Análisis de Rendimiento

### 3.1. Comparativa de Tiempos de Ejecución

La implementación de las estrategias de optimización resultó en una mejora de rendimiento masiva:

| Versión del Código | Tiempo de Ejecución Registrado (s) | Primos Encontrados |
| :--- | :--- | :--- |
| **Original** | 37.6650 | 9592 |
| **Optimizado** | **0.1041** | 9592 |


#### Gráfico de Comparación
![alt text](Analisis%20Tiempos.png)

### 3.2. Análisis Cuantitativo de la Optimización

Utilizando los tiempos registrados, la mejora de rendimiento se cuantifica de la siguiente manera:

1.  **Reducción Absoluta de Tiempo:**
    $$\text{Tiempo de Reducción} = 37.6650 \text{ s} - 0.1041 \text{ s} = \mathbf{37.5609 \text{ s}}$$

2.  **Factor de Aceleración (*Speedup*):**
    El código optimizado es $\mathbf{361.81}$ veces más rápido.
    $$\text{Factor de Aceleración} = \frac{37.6650}{0.1041} \approx 361.81$$

3.  **Porcentaje de Mejora:**
    Se logró una mejora del $\mathbf{99.72\%}$ en el tiempo de ejecución.
    $$\text{Porcentaje de Mejora} = \left( 1 - \frac{0.1041}{37.6650} \right) \times 100\% \approx 99.72\%$$

### 3.3. Análisis de Profiling con cProfile

Se utilizó la herramienta `cProfile` para analizar la versión optimizada y validar que el tiempo de ejecución se concentra en la función crítica, confirmando su eficiencia.


**Captura de Pantalla del Resultado de cProfile**

**Interpretación:**
El resultado de `cProfile` valida la optimización. La función **`es_primo_optimizado`** es, como se esperaba, la más llamada (100,000 veces) y donde se concentra el tiempo propio (`tottime`). Sin embargo, su tiempo por llamada (`percall`) es extremadamente bajo (aprox. $0.000001$ segundos), demostrando la altísima eficiencia lograda por la optimización algorítmica.

---

## 4. Conclusiones y Aplicación de Buenas Prácticas

### Conclusiones

La actividad logró un objetivo contundente: la optimización redujo el cuello de botella del código original (la función de comprobación de primalidad) de manera drástica.

La **drástica mejora del $99.72\%$** en el rendimiento, confirmada por un factor de aceleración de $\mathbf{361.81}$ veces, valida que la **mejora de la complejidad algorítmica** es la técnica más potente para mejorar el rendimiento. El código optimizado evita trabajo innecesario al limitar el rango de divisores a verificar hasta la raíz cuadrada del número, tal como lo predijo y verificó el profiling con `cProfile`.

### Buenas Prácticas y Recomendaciones

<<<<<<< HEAD
1.  **Profiling:** El uso de herramientas de profiling (`cProfile`) es esencial para la gestión del rendimiento, asegurando que los esfuerzos de optimización se dirijan al punto exacto donde se consume el tiempo.
2.  **Control de Versiones:** La documentación y el registro de cambios en el repositorio de **GitHub** garantiza la trazabilidad del desarrollo y facilita la colaboración.
3.  **Algoritmos Avanzados:** Para futuros proyectos con mayores volúmenes de datos, se recomienda explorar algoritmos de cribado de eficiencia superior, como el **Cribado de Eratóstenes**, para maximizar la velocidad.
=======
* Para futuros proyectos de Ciencia de Datos con grandes volúmenes de números, se recomienda usar el **cribado de Eratóstenes** o el uso de librerías altamente optimizadas (como SciPy) para lograr una eficiencia aún mayor que la obtenida.
* Mantener el control de versiones con Git y la documentación en Markdown facilita la colaboración y la revisión del código.
>>>>>>> ee188ca21a6c2fb885b6c9c0583b902520930962
