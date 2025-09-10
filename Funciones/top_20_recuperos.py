import pandas as pd

def top_20_recuperos(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'Recuperos', 'Club']].sort_values('Recuperos', ascending=False).head(20)
    return top20
