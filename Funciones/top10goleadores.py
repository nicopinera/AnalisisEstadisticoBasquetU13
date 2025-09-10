import pandas as pd


def top_20_jugadores_puntos(csv_path):
    """
    Lee el archivo CSV de resumen y retorna una tabla con los 20 jugadores con más puntos.
    Muestra: Nombre, cantidad de puntos, equipo.
    """
    # Leer el CSV
    df = pd.read_csv(csv_path)
    # Seleccionar columnas relevantes y ordenar
    top20 = (
        df[["Jugador", "Puntos", "Club"]]
        .sort_values("Puntos", ascending=False)
        .head(20)
    )
    return top20
