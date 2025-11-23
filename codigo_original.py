import time

def es_primo(n):
    """Verifica si un número n es primo usando el enfoque simple."""
    if n <= 1:
        return False
    # Itera desde 2 hasta n-1. Esta es la parte a optimizar.
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# --- Parámetros de la Tarea ---
LIMITE_SUPERIOR = 100000

# --- Medición de Tiempo ---
print(f"Buscando números primos hasta {LIMITE_SUPERIOR}...")
tiempo_inicio = time.time()

numeros_primos = []
for numero in range(1, LIMITE_SUPERIOR + 1):
    if es_primo(numero):
        numeros_primos.append(numero)

tiempo_fin = time.time()
tiempo_ejecucion = tiempo_fin - tiempo_inicio

# --- Resultados ---
# print(f"Lista de primos (primero 10): {numeros_primos[:10]}") # Comentado para no saturar la salida
print(f"Total de números primos encontrados: {len(numeros_primos)}")
print(f"Tiempo de ejecución (sin optimizar): {tiempo_ejecucion:.4f} segundos")