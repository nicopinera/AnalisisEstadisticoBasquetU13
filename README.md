# Análisis Estadístico Básquet

Este repositorio contiene todo lo necesario para analizar estadísticas de básquet de cualquier categoría usando Python y Jupyter Notebook. Está pensado para entrenadores y usuarios sin experiencia técnica. Incluye ejemplos y guías visuales.

---

## 🚦 Instalación rápida y entorno

### 1. Descargar el repositorio

- Opción fácil: Ir al link del repositorio, botón verde `<> Code` → `Download ZIP`.
  ![Imagen De descarga ZIP](/img/zip.png)

- Opción recomendada (si sabés usar git):

  ```bash
  git clone <URL-del-repo>
  cd "Estudio de estadisticas"
  ```

### 2. Instalar Python

- Descargar desde [python.org](https://www.python.org/downloads/)
  ![Imagen descarga Python](/img/python.png)
- Instalar con las opciones por defecto (siguiente, siguiente, aceptar).
- Si necesitás ayuda, mirá este tutorial: [Video instalación Python](https://www.youtube.com/watch?v=xd_0RN2SyfI)

### 3. Instalar Visual Studio Code y extensiones

- Descargar VS Code: [Visual Studio Code](https://code.visualstudio.com/)
- Instalar las extensiones de Python y Jupyter Notebook (ver imagen):
  ![Extensiones Jupyter](/img/jupyter.png)
- Si necesitás ayuda, mirá este tutorial: [Video instalación VS Code](https://www.youtube.com/watch?v=gp9psTESnQE)

### 4. (Opcional) Crear un entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate  # En Windows
```

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 📁 Estructura del Proyecto

El análisis se organiza en tres notebooks principales:

- **analisis2025.ipynb**: Estadísticas del torneo 2025.
- **analisisGlobal.ipynb**: Comparativo y acumulado de 2024 y 2025.
- **analisisUniversitario.ipynb**: Análisis de un club particular.

---

## 🧩 Requisitos y dependencias

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

## 📊 Formato de los datos

Para que el análisis funcione, los archivos Excel deben tener al menos estas columnas (pueden tener otros nombres, el sistema los detecta automáticamente):

- **Club** o **Equipo**
- **PJ** (Partidos Jugados)
- **Puntos**
- **T2C** (Tiros de 2 Convertidos), **T2I** (Intentados)
- **T3C** (Tiros de 3 Convertidos), **T3I** (Intentados)
- **T1C** (Tiros Libres Convertidos), **T1I** (Intentados)

> ⚠️ Si tenés dudas sobre cómo armar los archivos, consultá los ejemplos en la carpeta de datos o pedí ayuda.

---

## 🏀 Ejemplo de uso de funciones

Podés usar las funciones desde un notebook o script. Ejemplo en Jupyter Notebook:

```python
import sys
sys.path.append('./Funciones')
import estadisticas_por_equipo

# Mostrar tabla y gráficos de eficiencia de tiro por equipo
estadisticas_por_equipo.resumen_tiros_por_equipo('resumen_estadisticas_jugadores.csv')
```

---

## 📝 Uso paso a paso

1. **Prepará las carpetas:**
   - `Estadisticas_<año>`: Guardá aquí los Excel de cada año.
   - `Estadisticas`: Todos los Excel de todos los años.
   - `ListaBuenaFe`: Un Excel con columnas `Nombre` y `Equipo`.
2. **Generá los archivos .csv** ejecutando los scripts de Python incluidos.
3. **Abrí y ejecutá los notebooks** para ver los análisis y gráficos.

---

## 💡 Consejos para entrenadores

- No necesitás saber programar: solo seguí los pasos y ejecutá los notebooks.
- Si algo no funciona, revisá que los nombres de las columnas sean correctos y que los archivos estén en las carpetas indicadas.
- Los gráficos y tablas se generan automáticamente.
- Si ves un error, volvé a leer los pasos o consultá a alguien con experiencia.

---

## 📚 Glosario rápido

- **Notebook**: Archivo interactivo donde podés ver y ejecutar análisis paso a paso.
- **Script**: Archivo de código que realiza tareas automáticas.
- **Dependencia**: Programa o librería que tu código necesita para funcionar.
- **CSV**: Archivo de texto separado por comas, usado para datos.

---

## 👤 Créditos

Desarrollado por Nico Piñera.

---

## 📝 Licencia

Uso libre para fines educativos y deportivos. Si lo usás o lo mejorás, ¡avisame!
