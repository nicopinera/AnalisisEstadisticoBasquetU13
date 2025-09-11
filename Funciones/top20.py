
import pandas as pd

#Perdidas
def top_20_perdidas(csv_file):
    df = pd.read_csv(csv_file)
    col_perdidas = _find_column(df, ['Perdidas', 'Turnovers', 'TO', 'Pérdidas'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_perdidas, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_perdidas]].reset_index(drop=True)

def _find_column(df, posibles):
    for col in posibles:
        if col in df.columns:
            return col
    raise KeyError(f'Ninguna de las columnas {posibles} fue encontrada en el archivo. Las columnas disponibles son: {list(df.columns)}')
# Este archivo contiene todas las funciones top 20 unificadas


# Goleadores
def top_20_jugadores_puntos(csv_file):
    df = pd.read_csv(csv_file)
    col_puntos = _find_column(df, ['Puntos', 'PTS', 'Ptos', 'Puntos Totales'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_puntos, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_puntos]].reset_index(drop=True)

# Asistidores
def top_20_asistidores(csv_file):
    df = pd.read_csv(csv_file)
    col_asist = _find_column(df, ['Asistencias', 'Asist.', 'AST', 'Asist'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_asist, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_asist]].reset_index(drop=True)

# Tiros de 2 convertidos
def top_20_t2c(csv_file):
    df = pd.read_csv(csv_file)
    col_t2c = _find_column(df, ['T2C', 'Tiros de 2 Convertidos', 'T2 Convertidos'])
    col_t2i = _find_column(df, ['T2I', 'Tiros de 2 Intentados', 'T2 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_t2c, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_t2c, col_t2i]].reset_index(drop=True)

# Tiros de 3 convertidos
def top_20_t3c(csv_file):
    df = pd.read_csv(csv_file)
    col_t3c = _find_column(df, ['T3C', 'Tiros de 3 Convertidos', 'T3 Convertidos'])
    col_t3i = _find_column(df, ['T3I', 'Tiros de 3 Intentados', 'T3 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_t3c, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_t3c, col_t3i]].reset_index(drop=True)

# Tiros libres convertidos
def top_20_t1c(csv_file):
    df = pd.read_csv(csv_file)
    col_t1c = _find_column(df, ['T1C', 'Tiros Libres Convertidos', 'T1 Convertidos'])
    col_t1i = _find_column(df, ['T1I', 'Tiros Libres Intentados', 'T1 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_t1c, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_t1c, col_t1i]].reset_index(drop=True)

# Recuperos
def top_20_recuperos(csv_file):
    df = pd.read_csv(csv_file)
    col_rec = _find_column(df, ['Recuperos', 'REC', 'Robos', 'Steals'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_rec, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_rec]].reset_index(drop=True)

# Rebotes defensivos
def top_20_rd(csv_file):
    df = pd.read_csv(csv_file)
    col_rd = _find_column(df, ['RD', 'Rebotes Defensivos', 'Defensive Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_rd, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_rd]].reset_index(drop=True)

# Rebotes ofensivos
def top_20_ro(csv_file):
    df = pd.read_csv(csv_file)
    col_ro = _find_column(df, ['RO', 'Rebotes Ofensivos', 'Offensive Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_ro, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_ro]].reset_index(drop=True)

# Rebotes totales
def top_20_rt(csv_file):
    df = pd.read_csv(csv_file)
    col_rt = _find_column(df, ['RT', 'Rebotes Totales', 'Total Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_rt, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_rt]].reset_index(drop=True)

# Faltas
def top_20_faltas(csv_file):
    df = pd.read_csv(csv_file)
    col_faltas = _find_column(df, ['Faltas', 'Fouls', 'Faltas Cometidas'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    top20 = df.sort_values(col_faltas, ascending=False).head(20)
    return top20[[col_jugador, col_club, col_faltas]].reset_index(drop=True)