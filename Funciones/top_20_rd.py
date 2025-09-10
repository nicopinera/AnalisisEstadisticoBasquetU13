import pandas as pd

def top_20_rd(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'RD', 'Club']].sort_values('RD', ascending=False).head(20)
    return top20
