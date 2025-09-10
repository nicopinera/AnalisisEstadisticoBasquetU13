import pandas as pd

def top_20_ro(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'RO', 'Club']].sort_values('RO', ascending=False).head(20)
    return top20
