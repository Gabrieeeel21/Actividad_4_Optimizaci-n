import matplotlib.pyplot as plt
import numpy as np

# --- ⚠️ REEMPLAZA ESTOS VALORES CON TUS TIEMPOS REGISTRADOS ⚠️ ---
# Ejemplo: 55.45 segundos para el original (el tuyo será diferente y lento)
tiempo_original = 55.45  
# Ejemplo: 0.1009 segundos para el optimizado (el que registraste antes)
tiempo_optimizado = 0.1009 

# --- Configuración del Gráfico ---
tiempos = [tiempo_original, tiempo_optimizado]
versiones = ['Original', 'Optimizado']
colores = ['#FF6347', '#3CB371'] # Rojo para el lento, verde para el rápido

# Crear la figura y los ejes del gráfico
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(versiones, tiempos, color=colores, width=0.5)

# Títulos y Etiquetas
ax.set_title('Comparación de Tiempos de Ejecución: Código Original vs. Optimizado', fontsize=14, fontweight='bold')
ax.set_ylabel('Tiempo de Ejecución (segundos)', fontsize=12)

# Añadir etiquetas de valor en las barras
for bar in bars:
    yval = bar.get_height()
    # Formateo condicional: mostrar más decimales si el tiempo es muy pequeño
    if yval < 1:
        label = f'{yval:.4f} s'
    else:
        label = f'{yval:.2f} s'
        
    # Añadir la etiqueta sobre la barra. Ajustamos la posición vertical
    # para que las etiquetas no se superpongan si hay mucha diferencia
    ax.text(bar.get_x() + bar.get_width()/2.0, yval + (yval * 0.05), label, 
            ha='center', va='bottom', fontsize=11, fontweight='semibold')

# Ajustar el límite superior del eje Y para que se vea bien la barra original
ax.set_ylim(0, max(tiempos) * 1.15) 

# Mostrar el gráfico (o guardarlo)
plt.show()

# Opcional: Si quieres guardar la imagen directamente para el informe:
# plt.savefig('comparativa_tiempos.png')

print("Gráfico generado con éxito. ¡Asegúrate de tomar una captura de pantalla!")