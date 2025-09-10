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




    # Solo retornar la tabla
    return top20