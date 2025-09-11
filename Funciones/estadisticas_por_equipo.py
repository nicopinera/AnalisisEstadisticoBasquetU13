import matplotlib.pyplot as plt
import pandas as pd


def _find_column(df, posibles):
    for col in posibles:
        if col in df.columns:
            return col
    raise KeyError(
        f"Ninguna de las columnas {posibles} fue encontrada en el archivo. Las columnas disponibles son: {list(df.columns)}"
    )


def resumen_tiros_por_equipo(csv_file):
    df = pd.read_csv(csv_file)
    col_club = _find_column(df, ["Club", "Equipo", "Team"])
    col_pj = _find_column(df, ["PJ", "Partidos Jugados", "Juegos", "Games"])
    col_t2c = _find_column(df, ["T2C", "Tiros de 2 Convertidos", "T2 Convertidos"])
    col_t2i = _find_column(df, ["T2I", "Tiros de 2 Intentados", "T2 Intentados"])
    col_t3c = _find_column(df, ["T3C", "Tiros de 3 Convertidos", "T3 Convertidos"])
    col_t3i = _find_column(df, ["T3I", "Tiros de 3 Intentados", "T3 Intentados"])
    col_t1c = _find_column(df, ["T1C", "Tiros Libres Convertidos", "T1 Convertidos"])
    col_t1i = _find_column(df, ["T1I", "Tiros Libres Intentados", "T1 Intentados"])

    # Filtrar equipos desconocidos
    df = df[~df[col_club].str.lower().str.contains("desconocido", na=False)]

    equipos = []
    t2c, t2i, t3c, t3i, t1c, t1i = [], [], [], [], [], []
    pj = []
    t2c_pj, t2i_pj, t3c_pj, t3i_pj, t1c_pj, t1i_pj = [], [], [], [], [], []
    t2ef, t3ef, t1ef = [], [], []

    for equipo, grupo in df.groupby(col_club):
        sum_t2c = grupo[col_t2c].sum()
        sum_t2i = grupo[col_t2i].sum()
        sum_t3c = grupo[col_t3c].sum()
        sum_t3i = grupo[col_t3i].sum()
        sum_t1c = grupo[col_t1c].sum()
        sum_t1i = grupo[col_t1i].sum()
        max_pj = grupo[col_pj].max()

        equipos.append(equipo)
        t2c.append(sum_t2c)
        t2i.append(sum_t2i)
        t3c.append(sum_t3c)
        t3i.append(sum_t3i)
        t1c.append(sum_t1c)
        t1i.append(sum_t1i)
        pj.append(max_pj)

        t2c_pj.append(round(sum_t2c / max_pj, 2) if max_pj > 0 else 0)
        t2i_pj.append(round(sum_t2i / max_pj, 2) if max_pj > 0 else 0)
        t3c_pj.append(round(sum_t3c / max_pj, 2) if max_pj > 0 else 0)
        t3i_pj.append(round(sum_t3i / max_pj, 2) if max_pj > 0 else 0)
        t1c_pj.append(round(sum_t1c / max_pj, 2) if max_pj > 0 else 0)
        t1i_pj.append(round(sum_t1i / max_pj, 2) if max_pj > 0 else 0)

        t2ef.append(f"{round(100*sum_t2c/sum_t2i,2)}%" if sum_t2i > 0 else "-")
        t3ef.append(f"{round(100*sum_t3c/sum_t3i,2)}%" if sum_t3i > 0 else "-")
        t1ef.append(f"{round(100*sum_t1c/sum_t1i,2)}%" if sum_t1i > 0 else "-")

    result = pd.DataFrame(
        {
            "Equipo": equipos,
            "PJ": pj,
            "T2C": t2c,
            "T2I": t2i,
            "T2C/PJ": t2c_pj,
            "T2I/PJ": t2i_pj,
            "Efic2P": t2ef,
            "T3C": t3c,
            "T3I": t3i,
            "T3C/PJ": t3c_pj,
            "T3I/PJ": t3i_pj,
            "Efic3P": t3ef,
            "T1C": t1c,
            "T1I": t1i,
            "T1C/PJ": t1c_pj,
            "T1I/PJ": t1i_pj,
            "Efic1P": t1ef,
        }
    )
    result = result.sort_values("Equipo").reset_index(drop=True)
    result.index += 1

    # --- Graficos de eficiencia ---
    # Convertir eficiencias a float para graficar
    result_plot = result.copy()
    result_plot = result_plot[result_plot["Efic2P"] != "-"]
    result_plot = result_plot[result_plot["Efic3P"] != "-"]
    result_plot = result_plot[result_plot["Efic1P"] != "-"]
    result_plot["Efic2P_float"] = (
        result_plot["Efic2P"].str.replace("%", "").astype(float)
    )
    result_plot["Efic3P_float"] = (
        result_plot["Efic3P"].str.replace("%", "").astype(float)
    )
    result_plot["Efic1P_float"] = (
        result_plot["Efic1P"].str.replace("%", "").astype(float)
    )

    # Gráfico de eficiencia 2P
    plt.figure(figsize=(10, 5))
    bars = plt.bar(
        result_plot["Equipo"],
        result_plot["Efic2P_float"],
        color="#4A90E2",
        edgecolor="black",
    )
    plt.ylabel("Eficiencia 2P (%)")
    plt.title("Eficiencia de Tiros de 2 por Equipo")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 100)
    # Etiquetas de porcentaje sobre cada barra
    for bar, val in zip(bars, result_plot["Efic2P_float"]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{val:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    plt.tight_layout()
    plt.show()

    # Gráfico de eficiencia 3P
    plt.figure(figsize=(10, 5))
    bars = plt.bar(
        result_plot["Equipo"],
        result_plot["Efic3P_float"],
        color="#E24A4A",
        edgecolor="black",
    )
    plt.ylabel("Eficiencia 3P (%)")
    plt.title("Eficiencia de Tiros de 3 por Equipo")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 100)
    for bar, val in zip(bars, result_plot["Efic3P_float"]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{val:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    plt.tight_layout()
    plt.show()

    # Gráfico de eficiencia 1P
    plt.figure(figsize=(10, 5))
    bars = plt.bar(
        result_plot["Equipo"],
        result_plot["Efic1P_float"],
        color="#4AE26B",
        edgecolor="black",
    )
    plt.ylabel("Eficiencia 1P (%)")
    plt.title("Eficiencia de Tiros Libres por Equipo")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 100)
    for bar, val in zip(bars, result_plot["Efic1P_float"]):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{val:.1f}%",
            ha="center",
            va="bottom",
            fontsize=9,
        )
    plt.tight_layout()
    plt.show()
    return result


def puntos_por_equipo(csv_file):
    df = pd.read_csv(csv_file)
    col_club = _find_column(df, ["Club", "Equipo", "Team"])
    col_puntos = _find_column(df, ["Puntos", "PTS", "Ptos", "Puntos Totales"])
    col_pj = _find_column(df, ["PJ", "Partidos Jugados", "Juegos", "Games"])

    # Filtrar equipos desconocidos
    df = df[~df[col_club].str.lower().str.contains("desconocido", na=False)]

    equipos = []
    puntos_totales = []
    partidos_maximos = []
    promedio_puntos = []

    for equipo, grupo in df.groupby(col_club):
        total_puntos = grupo[col_puntos].sum()
        max_pj = grupo[col_pj].max()
        prom_puntos = round(total_puntos / max_pj, 2) if max_pj > 0 else 0
        equipos.append(equipo)
        puntos_totales.append(total_puntos)
        partidos_maximos.append(max_pj)
        promedio_puntos.append(prom_puntos)

    result = pd.DataFrame(
        {
            "Equipo": equipos,
            "Puntos": puntos_totales,
            "Pj": partidos_maximos,
            "Prom Pts": promedio_puntos,
        }
    )
    result = result.sort_values("Prom Pts", ascending=False).reset_index(drop=True)
    result.index += 1

    # Calcular promedios generales
    prom_total = (
        round(result["Puntos"].sum() / len(result), 2) if len(result) > 0 else 0
    )
    prom_por_juego = (
        round(result["Prom Pts"].sum() / len(result), 2) if len(result) > 0 else 0
    )

    # Fila resumen de promedios
    resumen = pd.DataFrame(
        {
            "Equipo": ["PROMEDIO"],
            "Puntos": [prom_total],
            "Pj": ["-"],
            "Prom Pts": [prom_por_juego],
        }
    )
    result = pd.concat([result, resumen], ignore_index=True)
    return result
