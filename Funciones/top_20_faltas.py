import pandas as pd

def top_20_faltas(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'Faltas', 'Club']].sort_values('Faltas', ascending=False).head(20)
    return top20
