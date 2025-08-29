#  Reporte de Calidad de Datos -- Estudiante C

##  Introducción

El presente informe corresponde al trabajo del **Estudiante C (Calidad
de Datos)** dentro del proyecto colaborativo *Análisis de Datos FAC --
Bienestar Familiar*.\
El objetivo principal es **evaluar la calidad de la base de datos
`JEFAB_2024.xlsx`**, identificando valores faltantes, duplicados,
problemas de plausibilidad y errores de codificación, para garantizar la
confiabilidad del análisis posterior.

------------------------------------------------------------------------

##  Metodología

Se empleó un script en Python (`calidad_datos.py`) que incluye: -
Estandarización de nombres de columnas.\
- Análisis de valores faltantes y duplicados.\
- Identificación de inconsistencias de plausibilidad (edades, hijos,
estratos).\
- Detección de outliers numéricos mediante el criterio IQR.\
- Revisión de posibles problemas de codificación en nombres de
variables.

------------------------------------------------------------------------

##  Respuestas a las preguntas asignadas

### 1. ¿Qué columnas tienen más datos faltantes?

Se detectó que las variables con mayor porcentaje de valores nulos
corresponden a información económica y familiar:\
- **INGRESO_MENSUAL**\
- **GASTO_MENSUAL**\
- **EDAD_PADRE**\
- **EDAD_MADRE**

Estas variables presentan porcentajes de ausencia superiores al promedio
de la base.

------------------------------------------------------------------------

### 2. ¿Hay registros duplicados?

El análisis muestra que **no existen registros duplicados
significativos** (el conteo fue cercano a 0).\
Esto indica un buen control en el proceso de captura de encuestas.

------------------------------------------------------------------------

### 3. ¿Qué problemas de encoding se detectan?

Se encontraron errores de codificación en nombres de variables y
categorías, con caracteres como:\
- `Ã`\
- `â`

Esto afecta a variables de texto, generando inconsistencias como
"Bogotá" vs "BogotÃ¡".\
El problema se mitiga mediante la estandarización aplicada en el código.

------------------------------------------------------------------------

##  Hallazgos adicionales

1.  **Valores faltantes significativos** en variables económicas y de
    padres.\
2.  **Inconsistencias de plausibilidad**:
    -   Edades fuera del rango 15--90 años.\
    -   Hogares donde `HIJOS_EN_HOGAR > NUMERO_HIJOS`.\
3.  **Hallazgo crítico**: Problemas de encoding en variables
    categóricas, que fragmentan las categorías y afectan el análisis.

------------------------------------------------------------------------

## Conclusiones

El análisis de calidad evidencia que, aunque la base de datos **no
presenta duplicados relevantes**, sí existen **faltantes importantes,
errores de plausibilidad y problemas de encoding**.\
Estos aspectos deben corregirse o mitigarse antes de realizar el
análisis demográfico y familiar, para asegurar la validez de los
resultados finales del proyecto.

------------------------------------------------------------------------

 **Autor:** Estudiante C -- *Calidad de Datos*
