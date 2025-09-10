import pandas as pd

def top_20_t3c(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'T3C', 'Club']].sort_values('T3C', ascending=False).head(20)
    return top20
