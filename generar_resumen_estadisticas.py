import os
import pandas as pd

# python generar_resumen_estadisticas.py
# .venv\Scripts\Activate

# Carpeta con los archivos de partidos
FOLDER = 'Estadisticas_2025'

# Columnas esperadas (ajustar si los archivos tienen otros nombres)
COLUMNS = {
    'Jugador': 'Jugador',
    'Club': 'Club',
    'Puntos': 'Puntos',
    'T2C': 'T2 Convertidos',
    'T2L': 'T2 Lanzados',
    'T1C': 'T1 Convertidos',
    'T1L': 'T1 Lanzados',
    'T3C': 'T3 Convertidos',
    'T3L': 'T3 Lanzados',
    'RD': 'Rebotes Defensivos',
    'RO': 'Rebotes Ofensivos',
    'Perdidas': 'Perdidas',
    'Recuperos': 'Recuperos',
    'Asistencias': 'Asistencias',
    'Tapones': 'Tapones',
    'Minutos': 'Minutos',
}

# Inicializar lista para todos los partidos
all_data = []


print(f"Procesando archivos en la carpeta: {FOLDER}")
total_bloques = 0
for file in os.listdir(FOLDER):
    if file.endswith('.xlsx'):
        path = os.path.join(FOLDER, file)
        try:
            # print(f"\nArchivo: {file}")
            df_full = pd.read_excel(path, header=None)
            bloques_en_archivo = 0
            # Buscar todos los encabezados 'NOMBRE' y procesar cada bloque
            nombre_idxs = [i for i, row in df_full.iterrows() if str(row[1]).strip().upper() == 'NOMBRE']
            for h, header_row in enumerate(nombre_idxs):
                club_name = 'Desconocido'
                for cidx in range(header_row-1, -1, -1):
                    val = str(df_full.iloc[cidx, 1]).strip()
                    if val and val.upper() != 'ESTADISTICAS' and val.upper() != 'CONFEDERACIÓN ARGENTINA DE BASQUETBOL':
                        club_name = val
                        break
                data_start = header_row + 1
                # El bloque termina en la fila 50 (o el final del archivo si es menor)
                if h+1 < len(nombre_idxs):
                    data_end = nombre_idxs[h+1]
                else:
                    data_end = min(50, len(df_full))
                if data_end > data_start:
                    # Leer bloque con header adecuado
                    df_team = pd.read_excel(path, header=header_row, nrows=data_end - data_start)
                    # Seleccionar columnas por posición (A=0, B=1, ..., S=18)
                    cols_idx = [1, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 18]  # B, D, E, G, I, K, L, M, N, O, P, S
                    col_names = ['Jugador', 'Puntos', 'T2', 'T3', 'T1', 'RD', 'RO', 'RT', 'AST', 'Perdidas', 'Recuperos', 'Faltas']
                    df_team = df_team.iloc[:, cols_idx]
                    df_team.columns = col_names
                    # Split de tiros
                    for tiro, conv, intent in [('T2', 'T2C', 'T2I'), ('T3', 'T3C', 'T3I'), ('T1', 'T1C', 'T1I')]:
                        split = df_team[tiro].astype(str).str.split('/', expand=True)
                        df_team[conv] = pd.to_numeric(split[0], errors='coerce').fillna(0)
                        df_team[intent] = pd.to_numeric(split[1], errors='coerce').fillna(0)
                    # Eliminar columnas originales de tiros
                    df_team = df_team.drop(columns=['T2', 'T3', 'T1'])
                    # Asignar club
                    df_team['Club'] = club_name
                    all_data.append(df_team)
                    # print(f"  Bloque equipo: {club_name} | Jugadores: {len(df_team)} (filas) filas {data_start}-{data_end-1}")
                    bloques_en_archivo += 1
            # print(f"  Total bloques en archivo: {bloques_en_archivo}")
            total_bloques += bloques_en_archivo
        except Exception as e:
            print(f'Error leyendo {file}: {e}')
 # print(f"\nTotal archivos procesados: {len([f for f in os.listdir(FOLDER) if f.endswith('.xlsx')])}")
 # print(f"Total bloques de equipos procesados: {total_bloques}")


if not all_data:
    print('No se encontraron datos.')
    exit()



# Unir todos los datos
data = pd.concat(all_data, ignore_index=True)
# No eliminar duplicados por jugador: cada aparición es un partido jugado




# Buscar y renombrar columnas relevantes por coincidencia parcial
def find_and_rename(col_candidates, new_name):
    for col in data.columns:
        if all(c.lower() in col.lower() for c in col_candidates):
            data.rename(columns={col: new_name}, inplace=True)
            return col
    return None

# Nombre del jugador
find_and_rename(['nombre'], 'Jugador')
# Minutos
find_and_rename(['min'], 'Minutos')
# Puntos
find_and_rename(['pts'], 'Puntos')
# Asistencias
find_and_rename(['as'], 'AST')
# Recuperos
find_and_rename(['rec'], 'Recuperos')
# Perdidas
find_and_rename(['pér'], 'Perdidas')
# Tapones
find_and_rename(['tap'], 'Tapones')
# Faltas
find_and_rename(['fal'], 'Faltas')
# Rebotes Defensivos
find_and_rename(['def'], 'RD')
# Rebotes Ofensivos
find_and_rename(['ofe'], 'RO')
# Rebotes Totales
find_and_rename(['tot'], 'RT')

# Tiros
find_and_rename(['tc 2p', 'a/i'], 'T2L')
find_and_rename(['tc 3p', 'a/i'], 'T3L')
find_and_rename(['tl', 'a/i'], 'T1L')

 # print('Columnas después del renombrado:')
 # print(list(data.columns))


# Asegurar que las columnas relevantes sean numéricas después del renombrado
columnas_numericas = ['T2C', 'T2I', 'T3C', 'T3I', 'T1C', 'T1I', 'RD', 'RO', 'RT', 'AST', 'Perdidas', 'Recuperos', 'Tapones', 'Faltas', 'Puntos']
for col in columnas_numericas:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

# Calcular puntos si no está
if 'Puntos' not in data.columns and 'PTS' in data.columns:
    data['Puntos'] = pd.to_numeric(data['PTS'], errors='coerce')

# Calcular rebotes totales si no está
if 'RD' in data.columns and 'RO' in data.columns and 'RT' not in data.columns:
    data['RT'] = pd.to_numeric(data['RD'], errors='coerce') + pd.to_numeric(data['RO'], errors='coerce')

def minutos_a_segundos(val):
    if pd.isna(val):
        return 0
    if isinstance(val, (int, float)):
        return int(val)
    partes = str(val).split(':')
    if len(partes) == 2:
        try:
            return int(partes[0])*60 + int(partes[1])
        except:
            return 0
    return 0

if 'Minutos' in data.columns:
    data['Minutos_seg'] = data['Minutos'].apply(minutos_a_segundos)


# Asegurar que todas las columnas estadísticas estén presentes aunque no existan en todos los archivos
for col in ['T2C', 'T2I', 'T3C', 'T3I', 'T1C', 'T1I', 'RD', 'RO', 'RT']:
    if col not in data.columns:
        data[col] = 0

# Agrupar por jugador y club
group_cols = ['Jugador', 'Club'] if 'Club' in data.columns else ['Jugador']


agg_dict = {
    'T2C': 'sum',
    'T2I': 'sum',
    'T1C': 'sum',
    'T1I': 'sum',
    'T3C': 'sum',
    'T3I': 'sum',
    'AST': 'sum',
    'Perdidas': 'sum',
    'Recuperos': 'sum',
    'Tapones': 'sum',
    'Faltas': 'sum',
    'RD': 'sum',
    'RO': 'sum',
    'RT': 'sum',
    'Puntos': 'sum',
    # 'Minutos_seg': 'sum',
    # 'Minutos': 'sum',
}

# Solo usar columnas presentes
agg_dict = {k: v for k, v in agg_dict.items() if k in data.columns}

resumen = data.groupby(group_cols).agg(agg_dict)



 # Calcular partidos jugados: cantidad de veces que aparece un jugador (y club) en todos los archivos
partidos_jugados = data.groupby(group_cols).size().reset_index(name='Partidos Jugados')
if 'Jugador' not in resumen.columns and 'Jugador' in resumen.index.names:
    resumen = resumen.reset_index()
resumen = pd.merge(resumen, partidos_jugados, on=group_cols, how='left')

# Reordenar columnas según pedido
cols_order = [
    'Jugador',
    'Partidos Jugados',
    'T2C', 'T2I', 'T3C', 'T3I', 'T1C', 'T1I',
    'AST', 'Perdidas', 'Recuperos', 'Tapones', 'Faltas',
    'RD', 'RO', 'RT',
    'Puntos',
    'Club',
]
resumen = resumen[[c for c in cols_order if c in resumen.columns]]

# Cruzar con la lista de buena fe para asignar el club correcto
try:
    lista_buena_fe = pd.read_excel('ListaBuenaFe/Lista_buena_fe.xlsx')
    lista_buena_fe = lista_buena_fe.rename(columns={"Nombre": "Jugador", "Equipo": "Club"})
    resumen = resumen.drop(columns=["Club"], errors='ignore')
    resumen = pd.merge(resumen, lista_buena_fe[["Jugador", "Club"]], on="Jugador", how="left")
    resumen["Club"] = resumen["Club"].fillna("Desconocido")
except Exception as e:
    print(f"No se pudo cruzar con la lista de buena fe: {e}")

# Guardar a CSV
resumen.to_csv('resumen_estadisticas_jugadores.csv', encoding='utf-8-sig', index=False)
 # print('Resumen generado en resumen_estadisticas_jugadores.csv (sin columna Minutos)')
