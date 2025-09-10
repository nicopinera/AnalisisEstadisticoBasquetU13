import pandas as pd
import matplotlib.pyplot as plt


def top_20_jugadores_puntos(csv_path):
    """
    Lee el archivo CSV de resumen y genera una tabla y gráfico de los 10 jugadores con más puntos.
    Muestra: Nombre, cantidad de puntos, equipo.
    """

    # Leer el CSV
    df = pd.read_csv(csv_path)


    # Seleccionar columnas relevantes y ordenar
    top20 = df[['Jugador', 'Puntos', 'Club']].sort_values('Puntos', ascending=False).head(20) # modificar para tomar mas jugadores




    # Gráfico: barras horizontales, nombres a la izquierda, puntos y club sobre cada barra
    # Ajustar el alto de la figura según la cantidad de jugadores
    fig_height = max(7, 0.6 * len(top20))
    plt.figure(figsize=(14, fig_height))
    # Combinar nombre y club para el eje Y
    jugadores_labels = [f"{row['Jugador']}\n({row['Club']})" for _, row in top20[::-1].iterrows()]
    bars = plt.barh(jugadores_labels, top20['Puntos'][::-1], color='#4A90E2', edgecolor='black', linewidth=1.2)
    plt.xlabel('Puntos', fontsize=13, fontweight='bold')
    plt.title('Top 20 jugadores con más puntos', fontsize=16, fontweight='bold', pad=20)
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.gca().set_axisbelow(True)
    plt.tight_layout(rect=[0, 0, 1, 0.98])

    # Agregar los valores de puntos al final de cada barra
    for bar, puntos in zip(bars, top20['Puntos'][::-1]):
        width = bar.get_width()
        plt.text(width + max(top20['Puntos']) * 0.01, bar.get_y() + bar.get_height()/2, int(puntos),
                 va='center', fontsize=10, fontweight='bold', color='#333')

    # Mejorar fuente y estética
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=10)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_linewidth(1.1)
    plt.gca().spines['bottom'].set_linewidth(1.1)
    plt.subplots_adjust(left=0.28, right=0.98)

    plt.show()

    return top20
