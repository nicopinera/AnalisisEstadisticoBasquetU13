import pandas as pd

def top_20_asistidores(csv_path):
    df = pd.read_csv(csv_path)
    top20 = df[['Jugador', 'AST', 'Club']].sort_values('AST', ascending=False).head(20)
    return top20
