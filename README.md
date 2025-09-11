# Análisis Estadístico Básquet U13

Este repositorio permite analizar y visualizar estadísticas de básquet U13 (división A1) de los torneos 2024 y 2025. Está pensado para entrenadores y usuarios sin experiencia técnica.

---

## Instalación rápida

1. **Descargá o cloná el repositorio:**

   ```bash
   git clone <URL-del-repo>
   cd Estudio\ de\ estadisticas
   ```

2. **(Opcional) Creá un entorno virtual:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   ```

3. **Instalá las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

---

## Estructura del Proyecto

El análisis se organiza en tres notebooks principales:

1. **analisis2025.ipynb**: Estadísticas del torneo 2025.
2. **analisisGlobal.ipynb**: Comparativo y acumulado de 2024 y 2025.
3. **analisisUniversitario.ipynb**: Análisis de un club particular.

---

## Requisitos y dependencias

- Python 3.8 o superior
- pandas
- matplotlib

El archivo `requirements.txt` ya incluye todo lo necesario:

```txt
pandas
matplotlib
pre-commit
flake8
flake8-bugbear
yamllint
```

---

## Formato de los datos

Para que el análisis funcione, los archivos Excel deben tener al menos estas columnas (pueden tener otros nombres, el sistema los detecta automáticamente):

- **Club** o **Equipo**
- **PJ** (Partidos Jugados)
- **Puntos**
- **T2C** (Tiros de 2 Convertidos), **T2I** (Intentados)
- **T3C** (Tiros de 3 Convertidos), **T3I** (Intentados)
- **T1C** (Tiros Libres Convertidos), **T1I** (Intentados)

Si tenés dudas sobre cómo armar los archivos, consultá los ejemplos en la carpeta de datos.

---

## Ejemplo de uso de funciones

Podés usar las funciones desde un notebook o script. Ejemplo en Jupyter Notebook:

```python
import sys
sys.path.append('./Funciones')
import estadisticas_por_equipo

# Mostrar tabla y gráficos de eficiencia de tiro por equipo
estadisticas_por_equipo.resumen_tiros_por_equipo('resumen_estadisticas_jugadores.csv')
```

---

## Uso paso a paso

1. **Prepará las carpetas:**
   - `Estadisticas_<año>`: Guardá aquí los Excel de cada año.
   - `Estadisticas`: Todos los Excel de todos los años.
   - `ListaBuenaFe`: Un Excel con columnas `Nombre` y `Equipo`.
2. **Generá los archivos .csv** ejecutando los scripts de Python incluidos.
3. **Abrí y ejecutá los notebooks** para ver los análisis y gráficos.

---

## Consejos para entrenadores

- No necesitás saber programar: solo seguí los pasos y ejecutá los notebooks.
- Si algo no funciona, revisá que los nombres de las columnas sean correctos y que los archivos estén en las carpetas indicadas.
- Los gráficos y tablas se generan automáticamente.

---

## Créditos

Desarrollado por Nico Piñera.

---

## Licencia

Uso libre para fines educativos y deportivos. Si lo usás o lo mejorás, ¡avisame!
