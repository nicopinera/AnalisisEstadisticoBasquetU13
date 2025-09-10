import os
import pandas as pd

# Carpeta con los archivos de partidos (ajustar el nombre de la carpeta)
FOLDER = 'Estasdisticas'

# Inicializar lista para todos los partidos
all_data = []

total_bloques = 0
for file in os.listdir(FOLDER):
    if file.endswith('.xlsx'):
        path = os.path.join(FOLDER, file)
        try:
            df_full = pd.read_excel(path, header=None)
            bloques_en_archivo = 0
            nombre_idxs = [i for i, row in df_full.iterrows() if str(row[1]).strip().upper() == 'NOMBRE']
            for h, header_row in enumerate(nombre_idxs):
                club_name = 'Desconocido'
                for cidx in range(header_row-1, -1, -1):
                    val = str(df_full.iloc[cidx, 1]).strip()
                    if val and val.upper() != 'ESTADISTICAS' and val.upper() != 'CONFEDERACIÓN ARGENTINA DE BASQUETBOL':
                        club_name = val
                        break
                data_start = header_row + 1
                if h+1 < len(nombre_idxs):
                    data_end = nombre_idxs[h+1]
                else:
                    data_end = min(50, len(df_full))
                if data_end > data_start:
                    df_team = pd.read_excel(path, header=header_row, nrows=data_end - data_start)
                    cols_idx = [1, 3, 4, 6, 8, 10, 11, 12, 13, 14, 15, 18]
                    col_names = ['Jugador', 'Puntos', 'T2', 'T3', 'T1', 'RD', 'RO', 'RT', 'AST', 'Perdidas', 'Recuperos', 'Faltas']
                    df_team = df_team.iloc[:, cols_idx]
                    df_team.columns = col_names
                    for tiro, conv, intent in [('T2', 'T2C', 'T2I'), ('T3', 'T3C', 'T3I'), ('T1', 'T1C', 'T1I')]:
                        split = df_team[tiro].astype(str).str.split('/', expand=True)
                        df_team[conv] = pd.to_numeric(split[0], errors='coerce').fillna(0)
                        df_team[intent] = pd.to_numeric(split[1], errors='coerce').fillna(0)
                    df_team = df_team.drop(columns=['T2', 'T3', 'T1'])
                    df_team['Club'] = club_name
                    all_data.append(df_team)
                    bloques_en_archivo += 1
            total_bloques += bloques_en_archivo
        except Exception as e:
            print(f'Error leyendo {file}: {e}')

if not all_data:
    print('No se encontraron datos.')
    exit()

 # Unir todos los datos
data = pd.concat(all_data, ignore_index=True)
# Eliminar filas donde el jugador es 'TOTALES'
if 'Jugador' in data.columns:
    data = data[data['Jugador'].str.upper() != 'TOTALES']
    data = data[data['Jugador'].notna()]

def find_and_rename(col_candidates, new_name):
    for col in data.columns:
        if all(c.lower() in col.lower() for c in col_candidates):
            data.rename(columns={col: new_name}, inplace=True)
            return col
    return None

find_and_rename(['nombre'], 'Jugador')
find_and_rename(['min'], 'Minutos')
find_and_rename(['pts'], 'Puntos')
find_and_rename(['as'], 'AST')
find_and_rename(['rec'], 'Recuperos')
find_and_rename(['pér'], 'Perdidas')
find_and_rename(['tap'], 'Tapones')
find_and_rename(['fal'], 'Faltas')
find_and_rename(['def'], 'RD')
find_and_rename(['ofe'], 'RO')
find_and_rename(['tot'], 'RT')
find_and_rename(['tc 2p', 'a/i'], 'T2L')
find_and_rename(['tc 3p', 'a/i'], 'T3L')
find_and_rename(['tl', 'a/i'], 'T1L')

columnas_numericas = ['T2C', 'T2I', 'T3C', 'T3I', 'T1C', 'T1I', 'RD', 'RO', 'RT', 'AST', 'Perdidas', 'Recuperos', 'Tapones', 'Faltas', 'Puntos']
for col in columnas_numericas:
    if col in data.columns:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)

if 'Puntos' not in data.columns and 'PTS' in data.columns:
    data['Puntos'] = pd.to_numeric(data['PTS'], errors='coerce')

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

for col in ['T2C', 'T2I', 'T3C', 'T3I', 'T1C', 'T1I', 'RD', 'RO', 'RT']:
    if col not in data.columns:
        data[col] = 0

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
}
agg_dict = {k: v for k, v in agg_dict.items() if k in data.columns}

resumen = data.groupby(group_cols).agg(agg_dict)

partidos_jugados = data.groupby(group_cols).size().reset_index(name='Partidos Jugados')
if 'Jugador' not in resumen.columns and 'Jugador' in resumen.index.names:
    resumen = resumen.reset_index()
resumen = pd.merge(resumen, partidos_jugados, on=group_cols, how='left')

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

try:
    lista_buena_fe = pd.read_excel('ListaBuenaFe/Lista_buena_fe.xlsx')
    lista_buena_fe = lista_buena_fe.rename(columns={"Nombre": "Jugador", "Equipo": "Club"})
    resumen = resumen.drop(columns=["Club"], errors='ignore')
    resumen = pd.merge(resumen, lista_buena_fe[["Jugador", "Club"]], on="Jugador", how="left")
    resumen["Club"] = resumen["Club"].fillna("Desconocido")
except Exception as e:
    print(f"No se pudo cruzar con la lista de buena fe: {e}")

resumen.to_csv('EstadisticasGlobales.csv', encoding='utf-8-sig', index=False)
