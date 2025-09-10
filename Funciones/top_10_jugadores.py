import pandas as pd
import matplotlib.pyplot as plt


def top_10_jugadores_puntos(csv_path):
    """
    Lee el archivo CSV de resumen y genera una tabla y gráfico de los 10 jugadores con más puntos.
    Muestra: Nombre, cantidad de puntos, equipo.
    """

    # Leer el CSV
    df = pd.read_csv(csv_path)

    # Filtrar la fila de totales si existe
    df = df[df['Jugador'].str.upper() != 'TOTALES']

    # Seleccionar columnas relevantes y ordenar
    top10 = df[['Jugador', 'Puntos', 'Club']].sort_values('Puntos', ascending=False).head(10)

    print("Top 10 jugadores con más puntos:")
    print(top10)


    # Gráfico: barras horizontales, nombres a la izquierda, puntos sobre cada barra
    plt.figure(figsize=(10,6))
    bars = plt.barh(top10['Jugador'][::-1], top10['Puntos'][::-1], color='skyblue')
    plt.xlabel('Puntos')
    plt.title('Top 10 jugadores con más puntos')
    plt.tight_layout()

    # Agregar los valores de puntos al final de cada barra
    for bar in bars:
        width = bar.get_width()
        plt.text(width + max(top10['Puntos']) * 0.01, bar.get_y() + bar.get_height()/2, int(width), va='center', fontsize=10, fontweight='bold')

    plt.show()

    return top10

# Ejemplo de uso:
top_10_jugadores_puntos('resumen_estadisticas_jugadores.csv')
