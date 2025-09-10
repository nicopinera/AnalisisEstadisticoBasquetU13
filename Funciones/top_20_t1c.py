import pandas as pd

def top_20_t1c(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'T1C', 'Club']].sort_values('T1C', ascending=False).head(20)
    return top20
