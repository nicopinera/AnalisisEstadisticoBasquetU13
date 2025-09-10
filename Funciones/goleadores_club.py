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

    # Solo retornar la tabla
    return df_club

# Ejemplo de uso:
# goleadores_club('resumen_estadisticas_jugadores.csv', 'Banco')
