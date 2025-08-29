# Análisis datos Fac

# Proyecto  Análisis de Datos FAC 



##  Descripción

Este proyecto corresponde a un **análisis exploratorio de datos** de la encuesta de bienestar familiar aplicada al personal de la **Fuerza Aérea Colombiana (FAC)** en 2024.  



El objetivo principal es **explorar, analizar y documentar patrones demográficos, familiares y de calidad de datos**, trabajando en equipo con control de versiones en Git/GitHub.



##  Organización del Equipo

El proyecto se desarrolla en grupos de **3 estudiantes**, con responsabilidades específicas:



- **Estudiante A – Demografía**  

&nbsp; Análisis de edad, género y rango.  

&nbsp; Genera el reporte `demografia\_basica.md`.



- **Estudiante B – Análisis Familiar**  

&nbsp; Estudia estado civil, hijos, convivencia y patrones familiares.  

&nbsp; Genera el reporte `analisis\_familiar.md`.



- **Estudiante C – Calidad de Datos**  

&nbsp; Revisa datos faltantes, duplicados y errores de encoding.  

&nbsp; Genera el reporte `calidad\_datos.md`.



##  Estructura del Repositorio



analisis-datos-fac



├── 📄 README.md # descripción general del proyecto

├── 📄 datos\_exploracion.py # script principal que integra A+B+C

├── 📄 demografia\_basica.py # parte A

├── 📄 analisis\_familiar.py # parte B

├── 📄 calidad\_datos.py # parte C

├── 📁 datos/

│ └── 📄 JEFAB\_2024.xlsx # base de datos original

└── 📁 reportes/

├── 📄 demografia\_basica.md

├── 📄 analisis\_familiar.md

└── 📄 calidad\_datos.md





##  Metodología

1. **Lectura y exploración de datos**   

2. **Visualización básica**  

3. **División de tareas** según las preguntas guía:  



&nbsp;  - **A (Demografía):** ¿Cuál es el rango de edad más común? ¿Hay diferencias por género? ¿Cuál es el grado militar más frecuente?  

&nbsp;  - **B (Familiar):** ¿Qué porcentaje del personal está casado? ¿Cuántos tienen hijos y cuántos viven con ellos? ¿Hay relación entre edad y estado civil?  

&nbsp;  - **C (Calidad de Datos):** ¿Qué columnas tienen más faltantes? ¿Hay duplicados? ¿Se detectan problemas de encoding o plausibilidad?  



##  Resultados esperados

- **Gráficos**: histogramas de edad, distribuciones por género, barras de estado civil, convivencia con hijos, heatmaps de calidad de datos.  

- **Tablas resumen**: conteo de categorías, porcentajes de casados, proporción de convivencia con hijos, métricas de datos faltantes.  

- **Reportes Markdown**: cada estudiante genera un reporte con sus hallazgos principales.  



##  Flujo de trabajo colaborativo

- Cada estudiante desarrolla su parte (A, B, C) en un script individual.  

- Se integran todos en `datos\_exploracion.py`.  

- Se documentan hallazgos en `reportes/`.  

- Se usa **GitHub** para control de versiones: `clone`, `commit`, `push`, `pull`.



##  Competencias trabajadas

- Lectura y análisis de datos con `pandas`.  

- Visualización de información en `matplotlib/seaborn`.  

- Identificación de problemas de calidad de datos.  

- Trabajo colaborativo con Git/GitHub.  

- Redacción técnica y estructuración de reportes.



---



**Julian Mendez, Camila Infante y Diego Gomez **  

Proyecto académico de análisis de datos, 2025.  



