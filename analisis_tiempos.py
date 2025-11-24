import matplotlib.pyplot as plt
import numpy as np

# ----------------------------------------------------------------------
# --- ⚠️ REEMPLAZAMOS VALORES  TIEMPOS REGISTRADOS ⚠️ ---
# ----------------------------------------------------------------------

# El tiempo que obtuvo
tiempo_original = 48.50  
# El tiempo de ejecución 
tiempo_optimizado = 0.1345 

# --- Configuración del Gráfico ---
tiempos = [tiempo_original, tiempo_optimizado]
versiones = ['Original', 'Optimizado']
colores = ['#FF6347', '#3CB371'] # Rojo para el lento, verde para el rápido

# Crear la figura y los ejes del gráfico
# Usamos una escala logarítmica si la diferencia es demasiado grande para visualizar la optimizada
if tiempo_original / tiempo_optimizado > 100:
    fig, ax = plt.subplots(figsize=(10, 7))
    bars = ax.bar(versiones, tiempos, color=colores, width=0.5)
    ax.set_yscale('log')
    ax.set_title('Comparación de Tiempos (Escala Logarítmica)', fontsize=14, fontweight='bold')
    ax.set_ylabel('Tiempo de Ejecución (segundos, Escala Logarítmica)', fontsize=12)
else:
    # Si la diferencia es menor, usamos escala lineal normal
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(versiones, tiempos, color=colores, width=0.5)
    ax.set_title('Comparación de Tiempos de Ejecución', fontsize=14, fontweight='bold')
    ax.set_ylabel('Tiempo de Ejecución (segundos)', fontsize=12)


# Añadir etiquetas de valor en las barras
for bar in bars:
    yval = bar.get_height()
    # Formateo condicional: mostrar más decimales si el tiempo es muy pequeño
    if yval < 1:
        label = f'{yval:.4f} s'
    else:
        label = f'{yval:.2f} s'
        
    # Ajustar la posición vertical para las etiquetas
    if ax.get_yscale() == 'log':
        ax.text(bar.get_x() + bar.get_width()/2.0, yval, label, 
                ha='center', va='bottom', fontsize=11, fontweight='semibold')
    else:
        ax.text(bar.get_x() + bar.get_width()/2.0, yval + (max(tiempos) * 0.03), label, 
                ha='center', va='bottom', fontsize=11, fontweight='semibold')


# Mostrar el gráfico (o guardarlo)
plt.tight_layout()
plt.show()

