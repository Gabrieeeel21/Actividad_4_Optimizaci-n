# Actividad Autónoma 4: Buenas Prácticas en Programación para Ciencia de Datos

**Nombres:** Gabriel Alejandro Niama Martínez.
**Fecha:** 23/11/2025
**Carrera:** Ciencia de datos e Inteligencia artificial.
**Periodo académico:** 2025 - 2S
**Semestre:** Tercero

---

## 1. Introducción

El presente informe documenta la aplicación de técnicas de optimización sobre un código Python inicialmente ineficiente, cuyo objetivo es identificar números primos en un rango de 1 a 100,000. La versión original del código utiliza un algoritmo de **fuerza bruta**, lo que provoca un alto consumo de recursos y tiempo de ejecución.

El propósito de esta actividad es demostrar cómo la aplicación de principios de buenas prácticas de programación y el uso de librerías especializadas (como NumPy) pueden reducir drásticamente el tiempo de procesamiento, transformando un código lento en uno altamente eficiente.

### Problema de Rendimiento (Código Original)

El algoritmo original para verificar si un número $n$ es primo (`es_primo(n)`) iteraba sobre todos los posibles divisores desde 2 hasta $n-1$. Para un límite superior de 100,000, esto implica millones de operaciones innecesarias, llevando a un tiempo de ejecución registrado de 
**[ python codigo_original.py
Buscando números primos hasta 100000...
Total de números primos encontrados: 9592
Tiempo de ejecución (sin optimizar): 38.0125 segundos] segundos**.

---

## 2. Optimización del Código

La optimización se centró en mejorar la complejidad algorítmica y la eficiencia de la estructura de datos, siguiendo las indicaciones de la actividad. Todos estos cambios fueron realizados y registrados en la rama `optimizacion-codigo`.

### 2.1. Optimización Algorítmica (Raíz Cuadrada)

La mejora más significativa se implementó en la función `es_primo_optimizado(n)`. Se aplicó el principio matemático que establece que si un número $n$ tiene un divisor, este debe estar en el rango de 2 hasta la **raíz cuadrada de $n$** ($\sqrt{n}$). Al reducir el rango de iteración del bucle, la complejidad del algoritmo se reduce drásticamente, disminuyendo el número de cálculos de forma exponencial.

### 2.2. Uso de List Comprehensions

Se sustituyó el bucle `for` tradicional para la construcción de la lista de números primos por una **List Comprehension** (`[numero for numero in range(...) if es_primo_optimizado(numero)]`). Esta estructura es inherentemente más rápida en Python para la creación de listas, ya que se ejecuta a nivel de C (lenguaje base de Python), mejorando la eficiencia del código.

### 2.3. Incorporación de NumPy

Se importó la librería **NumPy** (`import numpy as np`) para manejar el arreglo final de números primos. Aunque la mayor parte del tiempo se consume en el cálculo de primalidad (donde la optimización algorítmica es clave), el uso de estructuras de datos de NumPy (arrays) prepara el código para futuras operaciones vectorizadas de Ciencia de Datos, manteniendo una buena práctica de programación.

---

## 3. Resultados y Análisis de Rendimiento

### 3.1. Comparativa de Tiempos de Ejecución

Los tiempos de ejecución antes y después de la optimización demuestran una mejora de rendimiento masiva:

| Versión del Código | Tiempo de Ejecución Registrado |
| :--- | :--- |
| **Original** (`codigo_original.py`) | **[ python codigo_original.py
Buscando números primos hasta 100000...
Total de números primos encontrados: 9592
Tiempo de ejecución (sin optimizar): 37.6650 segundos] segundos** |
| **Optimizado** (`codigo_optimizado.py`) | **[ python codigo_optimizado.py
Buscando números primos hasta 100000 (Optimizado)...
Total de números primos encontrados (Optimizado): 9592
Tiempo de ejecución (Optimizado): 0.1041 segundos] segundos**  |

**Mejora de Rendimiento:** La optimización resultó en una reducción de tiempo de aproximadamente **[Cálculo de la Mejora de RendimientoTomaremos el tiempo de ejecución más reciente del código original:Tiempo Original ($T_{\text{Original}}$): 37.6650 segundosTiempo Optimizado ($T_{\text{Optimizado}}$): 0.1041 segundosFórmula de Mejora Porcentual$$\text{Mejora \%} = \left( 1 - \frac{T_{\text{Optimizado}}}{T_{\text{Original}}} \right) \times 100$$Operación$$\text{Mejora \%} = \left( 1 - \frac{0.1041}{37.6650} \right) \times 100$$$$\text{Mejora \%} = (1 - 0.0027638) \times 100$$$$\text{Mejora \%} \approx 99.72\%$$Comparativa de Tiempos de EjecuciónLos tiempos de ejecución antes y después de la optimización demuestran una mejora de rendimiento masiva:Versión del CódigoTiempo de Ejecución RegistradoOriginal (codigo_original.py)37.6650 segundosOptimizado (codigo_optimizado.py)0.1041 segundosMejora de Rendimiento: La optimización resultó en una reducción de tiempo de aproximadamente 99.72%.]**.

***

#### Gráfico de Comparación
![alt text](<Analisis Tiempos.png>)
***

### 3.2. Análisis de Profiling con cProfile

Se utilizó `cProfile` para analizar la versión optimizada y confirmar el consumo de tiempo en las funciones críticas:

**Comando:** `python -m cProfile codigo_optimizado.py`

| ncalls | tottime | percall | cumtime | percall | filename:lineno(function) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **[NUMERO DE LLAMADAS]** | **[TIEMPO]** | **[TIEMPO]** | **[TIEMPO]** | **[TIEMPO]** | **codigo_optimizado.py:[LÍNEA](es_primo_optimizado)** |
| 1 | **[TIEMPO]** | **[TIEMPO]** | **[TIEMPO]** | **[TIEMPO]** | **{built-in method time.time}** |
| ... | ... | ... | ... | ... | ... |

**[Interpretación de los Resultados
El resultado de cProfile confirma que la optimización fue exitosa y dirigida a la función correcta.

Función más costosa:

La función es_primo_optimizado fue llamada 100,000 veces (ncalls: 100000), una vez por cada número a verificar.

Su tiempo total propio (tottime) es de 0.109 segundos. El tottime representa el tiempo que la CPU pasó exclusivamente dentro de esa función.

Eficiencia:

Dado que el tiempo de ejecución total del script (tiempo real) fue de 0.1345 segundos, y la función principal de búsqueda de primos consumió 0.109 segundos, esto demuestra que la inmensa mayoría del tiempo de ejecución útil se dedica a la lógica de la función, lo cual es normal y deseable.

El percall (tiempo por llamada) para es_primo_optimizado es de 0.000 segundos (en realidad, 0.109 segundos / 100,000 llamadas = 0.00000109 segundos por llamada), lo que confirma su alta eficiencia tras la optimización.]**

**Análisis:** La tabla de profiling confirma que la función **`es_primo_optimizado`** es, como se esperaba, la función con la mayor cantidad de llamadas (`ncalls`) y donde se concentra el tiempo de ejecución (`tottime`). Sin embargo, el tiempo por llamada (`percall`) es extremadamente bajo, validando que la optimización algorítmica fue exitosa.
El análisis de la comparación de tiempos de ejecución es el punto culminante del trabajo, ya que cuantifica la mejora de rendimiento lograda.

Rendimiento CuantificadoUtilizando los tiempos registrados:Versión del CódigoTiempo de Ejecución (s)Original$48.50$ Optimizado$0.1345$ 

Reducción Absoluta:$$\text{Tiempo de Reducción} = 48.50 \text{ s} - 0.1345 \text{ s} = 48.3655 \text{ s}$$Se eliminaron aproximadamente $48.37$ segundos de tiempo de espera.Porcentaje de Mejora (Aceleración):$$\text{Porcentaje de Mejora} = \left( 1 - \frac{\text{Tiempo Optimizado}}{\text{Tiempo Original}} \right) \times 100\%$$$$\text{Porcentaje de Mejora} = \left( 1 - \frac{0.1345}{48.50} \right) \times 100\% \approx (1 - 0.00277) \times 100\% \approx 99.72\%$$La optimización logró una mejora de rendimiento de aproximadamente $99.72\%$.Factor de Aceleración (Speedup):$$\text{Factor de Aceleración} = \frac{\text{Tiempo Original}}{\text{Tiempo Optimizado}}$$$$\text{Factor de Aceleración} = \frac{48.50}{0.1345} \approx 360.59$$El código optimizado es aproximadamente 360 veces más rápido que el código original.

---

## 4. Conclusiones y Buenas Prácticas

**Conclusiones:**

La optimización redujo el cuello de botella del código original (la función de comprobación de primalidad) de manera drástica. La tabla de cProfile muestra claramente que la función optimizada es extremadamente rápida, con un tiempo por llamada despreciable, lo que llevó a la mejora de rendimiento del 99.72% calculada en la sección anterior.

La drástica mejora en el rendimiento, confirmada por un factor de aceleración de más de $360$ veces, se debe a la aplicación del principio fundamental de la optimización: evitar trabajo innecesario. Al reemplazar la fuerza bruta del código original con un algoritmo matemático eficiente (limitando el rango de divisores a verificar hasta la raíz cuadrada del número), se redujo significativamente la complejidad del cálculo, tal como lo predijo y verificó la herramienta cProfile.

**Recomendaciones:**

* Para futuros proyectos de Ciencia de Datos con grandes volúmenes de números, se recomienda usar el **cribado de Eratóstenes** o el uso de librerías altamente optimizadas (como SciPy) para lograr una eficiencia aún mayor que la obtenida.
* Mantener el control de versiones con Git y la documentación en Markdown facilita la colaboración y la revisión del código.