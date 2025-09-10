import pandas as pd

def top_20_t2c(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'T2C', 'Club']].sort_values('T2C', ascending=False).head(20)
    return top20
