import time
import numpy as np

def es_primo_optimizado(n):
    """
    Verifica si un número n es primo, iterando solo hasta la raíz cuadrada.
    Esta es la optimización algorítmica más importante.
    """
    if n <= 1:
        return False
    # Si n es par y mayor que 2, no es primo
    if n % 2 == 0 and n > 2:
        return False
    
    # La optimización clave: solo necesitamos verificar divisores impares hasta la raíz cuadrada de n.
    # Usamos int(n**0.5) + 1 para incluir la raíz cuadrada si es un entero.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# --- Parámetros de la Tarea ---
LIMITE_SUPERIOR = 100000

# --- Medición de Tiempo ---
print(f"Buscando números primos hasta {LIMITE_SUPERIOR} (Optimizado)...")
tiempo_inicio = time.time()

# Aplicando List Comprehensions (eficiencia)
# Y usando np.array para el manejo de los resultados (NumPy)
numeros_primos_list = [
    numero for numero in range(1, LIMITE_SUPERIOR + 1) if es_primo_optimizado(numero)
]
# Convertir a NumPy array
numeros_primos_array = np.array(numeros_primos_list)


tiempo_fin = time.time()
tiempo_ejecucion_optimizado = tiempo_fin - tiempo_inicio

# --- Resultados ---
print(f"Total de números primos encontrados (Optimizado): {len(numeros_primos_array)}")
print(f"Tiempo de ejecución (Optimizado): {tiempo_ejecucion_optimizado:.4f} segundos")

# Guardar el tiempo para comparativa
print(f"\n¡No olvides registrar este tiempo para la Parte 3!")