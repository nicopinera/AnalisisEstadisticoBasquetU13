import pandas as pd

def top_20_rt(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'RT', 'Club']].sort_values('RT', ascending=False).head(20)
    return top20
