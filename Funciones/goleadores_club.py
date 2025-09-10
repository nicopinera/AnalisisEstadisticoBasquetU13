import pandas as pd
import matplotlib.pyplot as plt

def goleadores_club(csv_path, club):
    """
    Muestra todos los goleadores de un club específico, ordenados por puntos.
    Genera una tabla y un gráfico de barras horizontal.
    """
    df = pd.read_csv(csv_path)
    df_club = df[df['Club'].str.lower() == club.lower()]
    if df_club.empty:
        print(f"No se encontraron jugadores para el club: {club}")
        return None
    df_club = df_club[['Jugador', 'Puntos', 'Club']].sort_values('Puntos', ascending=False)

    # Gráfico
    plt.figure(figsize=(12, max(4, 0.5*len(df_club))))
    bars = plt.barh(df_club['Jugador'][::-1], df_club['Puntos'][::-1], color='#50C878', edgecolor='black', linewidth=1.2)
    plt.xlabel('Puntos', fontsize=13, fontweight='bold')
    plt.title(f'Goleadores de {club}', fontsize=15, fontweight='bold')
    plt.grid(axis='x', linestyle='--', alpha=0.5)
    plt.gca().set_axisbelow(True)
    plt.tight_layout(rect=[0, 0, 1, 0.98])
    for bar, puntos in zip(bars, df_club['Puntos'][::-1]):
        width = bar.get_width()
        plt.text(width + max(df_club['Puntos']) * 0.01, bar.get_y() + bar.get_height()/2, int(puntos),
                 va='center', fontsize=10, fontweight='bold', color='#333')
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=10)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['left'].set_linewidth(1.1)
    plt.gca().spines['bottom'].set_linewidth(1.1)
    plt.subplots_adjust(left=0.28, right=0.98)
    plt.show()
    return df_club

# Ejemplo de uso:
# goleadores_club('resumen_estadisticas_jugadores.csv', 'Banco')
