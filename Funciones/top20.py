import pandas as pd
# ...existing code...

# Valoración
def top_20_valoracion(csv_file):
    df = pd.read_csv(csv_file)
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    col_puntos = _find_column(df, ['Puntos', 'PTS', 'Ptos', 'Puntos Totales'])
    col_t2c = _find_column(df, ['T2C', 'Tiros de 2 Convertidos', 'T2 Convertidos'])
    col_t2i = _find_column(df, ['T2I', 'Tiros de 2 Intentados', 'T2 Intentados'])
    col_t3c = _find_column(df, ['T3C', 'Tiros de 3 Convertidos', 'T3 Convertidos'])
    col_t3i = _find_column(df, ['T3I', 'Tiros de 3 Intentados', 'T3 Intentados'])
    col_t1c = _find_column(df, ['T1C', 'Tiros Libres Convertidos', 'T1 Convertidos'])
    col_t1i = _find_column(df, ['T1I', 'Tiros Libres Intentados', 'T1 Intentados'])
    col_ast = _find_column(df, ['Asistencias', 'Asist.', 'AST', 'Asist'])
    col_perdidas = _find_column(df, ['Perdidas', 'Turnovers', 'TO', 'Pérdidas'])
    col_rec = _find_column(df, ['Recuperos', 'REC', 'Robos', 'Steals'])
    col_faltas = _find_column(df, ['Faltas', 'Fouls', 'Faltas Cometidas'])
    col_rd = _find_column(df, ['RD', 'Rebotes Defensivos', 'Defensive Rebounds'])
    col_ro = _find_column(df, ['RO', 'Rebotes Ofensivos', 'Offensive Rebounds'])
    col_rt = _find_column(df, ['RT', 'Rebotes Totales', 'Total Rebounds'])

    # Fórmula de valoración simple: Puntos + Rebotes Totales + Asistencias + Recuperos - Tiros de campo fallados - Tiros libres fallados - Perdidas - Faltas
    df['Valoracion'] = (
        df[col_puntos]
        + df[col_rt]
        + df[col_ast]
        + df[col_rec]
        - ((df[col_t2i] - df[col_t2c]) + (df[col_t3i] - df[col_t3c]))
        - (df[col_t1i] - df[col_t1c])
        - df[col_perdidas]
        - df[col_faltas]
    )
    df['Valoracion x J'] = (df['Valoracion'] / df[col_pj]).round(2)
    top20 = df.sort_values('Valoracion', ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, 'Valoracion', 'Valoracion x J']].copy().reset_index(drop=True)
    result.index += 1
    return result



#Perdidas
def top_20_perdidas(csv_file):
    df = pd.read_csv(csv_file)
    col_perdidas = _find_column(df, ['Perdidas', 'Turnovers', 'TO', 'Pérdidas'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_perdidas] / df[col_pj]).round(2)
    top20 = df.sort_values(col_perdidas, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_perdidas, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

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
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_puntos] / df[col_pj]).round(2)
    top20 = df.sort_values(col_puntos, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_puntos, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Asistidores
def top_20_asistidores(csv_file):
    df = pd.read_csv(csv_file)
    col_asist = _find_column(df, ['Asistencias', 'Asist.', 'AST', 'Asist'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_asist] / df[col_pj]).round(2)
    top20 = df.sort_values(col_asist, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_asist, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Tiros de 2 convertidos
def top_20_t2c(csv_file):
    df = pd.read_csv(csv_file)
    col_t2c = _find_column(df, ['T2C', 'Tiros de 2 Convertidos', 'T2 Convertidos'])
    col_t2i = _find_column(df, ['T2I', 'Tiros de 2 Intentados', 'T2 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['TCxJ'] = (df[col_t2c] / df[col_pj]).round(2)
    df['TIxJ'] = (df[col_t2i] / df[col_pj]).round(2)
    df['Eficiencia_val'] = (df[col_t2c] / df[col_t2i])
    df['Eficiencia'] = (df['Eficiencia_val'] * 100).round(2).astype(str) + '%'
    top20 = df.sort_values(col_t2c, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_t2c, col_t2i, 'TCxJ', 'TIxJ', 'Eficiencia']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Tiros de 3 convertidos
def top_20_t3c(csv_file):
    df = pd.read_csv(csv_file)
    col_t3c = _find_column(df, ['T3C', 'Tiros de 3 Convertidos', 'T3 Convertidos'])
    col_t3i = _find_column(df, ['T3I', 'Tiros de 3 Intentados', 'T3 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['TCxJ'] = (df[col_t3c] / df[col_pj]).round(2)
    df['TIxJ'] = (df[col_t3i] / df[col_pj]).round(2)
    df['Eficiencia_val'] = (df[col_t3c] / df[col_t3i])
    df['Eficiencia'] = (df['Eficiencia_val'] * 100).round(2).astype(str) + '%'
    top20 = df.sort_values(col_t3c, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_t3c, col_t3i, 'TCxJ', 'TIxJ', 'Eficiencia']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Tiros libres convertidos
def top_20_t1c(csv_file):
    df = pd.read_csv(csv_file)
    col_t1c = _find_column(df, ['T1C', 'Tiros Libres Convertidos', 'T1 Convertidos'])
    col_t1i = _find_column(df, ['T1I', 'Tiros Libres Intentados', 'T1 Intentados'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['TCxJ'] = (df[col_t1c] / df[col_pj]).round(2)
    df['TIxJ'] = (df[col_t1i] / df[col_pj]).round(2)
    df['Eficiencia_val'] = (df[col_t1c] / df[col_t1i])
    df['Eficiencia'] = (df['Eficiencia_val'] * 100).round(2).astype(str) + '%'
    top20 = df.sort_values(col_t1c, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_t1c, col_t1i, 'TCxJ', 'TIxJ', 'Eficiencia']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Recuperos
def top_20_recuperos(csv_file):
    df = pd.read_csv(csv_file)
    col_rec = _find_column(df, ['Recuperos', 'REC', 'Robos', 'Steals'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_rec] / df[col_pj]).round(2)
    top20 = df.sort_values(col_rec, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_rec, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Rebotes defensivos
def top_20_rd(csv_file):
    df = pd.read_csv(csv_file)
    col_rd = _find_column(df, ['RD', 'Rebotes Defensivos', 'Defensive Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_rd] / df[col_pj]).round(2)
    top20 = df.sort_values(col_rd, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_rd, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Rebotes ofensivos
def top_20_ro(csv_file):
    df = pd.read_csv(csv_file)
    col_ro = _find_column(df, ['RO', 'Rebotes Ofensivos', 'Offensive Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_ro] / df[col_pj]).round(2)
    top20 = df.sort_values(col_ro, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_ro, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Rebotes totales
def top_20_rt(csv_file):
    df = pd.read_csv(csv_file)
    col_rt = _find_column(df, ['RT', 'Rebotes Totales', 'Total Rebounds'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_rt] / df[col_pj]).round(2)
    top20 = df.sort_values(col_rt, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_rt, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result

# Faltas
def top_20_faltas(csv_file):
    df = pd.read_csv(csv_file)
    col_faltas = _find_column(df, ['Faltas', 'Fouls', 'Faltas Cometidas'])
    col_jugador = _find_column(df, ['Jugador', 'Nombre', 'Player'])
    col_club = _find_column(df, ['Club', 'Equipo', 'Team'])
    col_pj = _find_column(df, ['PJ', 'Partidos Jugados', 'Juegos', 'Games'])
    df['Prom x J'] = (df[col_faltas] / df[col_pj]).round(2)
    top20 = df.sort_values(col_faltas, ascending=False).head(20)
    result = top20[[col_jugador, col_club, col_pj, col_faltas, 'Prom x J']].copy().reset_index(drop=True)
    result.index += 1
    return result