#!/usr/bin/env python
# coding: utf-8

# ### **ESTUDIANTE A: Análisis Demográfico**
# 
# **Responsabilidades:**
#   - Explorar las columnas básicas de demografía
#   - Crear visualizaciones simples de edad, género, rango
#   - Documentar hallazgos principales
# 

# In[1]:


# demografia_basica.py
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:/Users/aleja/OneDrive/Documentos/Python_para_Analitica_y_Mineria_de_Datos/analisis-datos-fac-equipo-Nose/datos/JEFAB_2024.xlsx")

print("Cargue de los datos")


# ## **Importancia de los datos de la Encuesta de Bienestar Familiar del personal FAC**
# 
# El uso de datos provenientes de la encuesta de Bienestar Familiar del personal de la Fuerza Aérea Colombiana (FAC) es fundamental para garantizar que los análisis reflejen las condiciones y necesidades actuales del personal. Estas fuentes permiten identificar de manera objetiva aspectos sociodemográficos, condiciones de vida y características del entorno familiar, brindando insumos clave para orientar políticas y programas de bienestar institucional.
# 
# En este caso, la base de datos contiene variables relevantes como Edad, Género, Estado civil, Número de hijos, Nivel educativo, y Estrato socioeconómico, las cuales proporcionan una visión integral sobre la composición de la población encuestada. Estas variables son especialmente útiles para identificar tendencias, segmentar grupos de interés y establecer comparaciones que apoyen la toma de decisiones estratégicas dentro de la FAC.  
# 
# ---
# 
# #### **Cantidad de registros a analizar:**
# 

# In[2]:


# Explorar estructura básica
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")


# #### **Análisis de edad**

# In[3]:


# Análisis de edad
print("\n=== ANÁLISIS DE EDAD ===")
print(f"Edad promedio: {df['EDAD2'].mean():.1f} años")
print(f"Edad mínima: {df['EDAD2'].min()} años")
print(f"Edad máxima: {df['EDAD2'].max()} años")


# #### **Gráfico de edades**

# In[8]:


plt.figure(figsize=(10, 6))
plt.hist(df['EDAD2'], bins=20, edgecolor='black')
plt.title('Distribución de Edades del Personal FAC')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Personal')
plt.show()


# #### **Análisis de género**

# In[4]:


# Análisis de género
print("\n=== ANÁLISIS DE GÉNERO ===")
print(df['GENERO'].value_counts())


# #### **Grafico de Genero**

# In[6]:


counts = df['GENERO'].value_counts() # conteo de la base
labels = list(counts.index)   
sizes = list(counts.values) # parametros en lista para la funcion a continuacion 

# Función para mostrar % solo en Masculino y Femenino
def autopct_func(pct, all_vals):
    absolute = int(round(pct/100.*sum(all_vals)))
    if absolute >= 100:  # Solo muestra porcentaje si es un grupo grande
        return f"{pct:.1f}%"
    else:
        return ""  # No mostrar nada en los pequeños

# Gráfico
plt.figure(figsize=(6,6)) # Tamaño
plt.pie(
    sizes,
    autopct=lambda pct: autopct_func(pct, sizes),
    startangle=90
) # dibuja la torta con las proporciones de genero
  # y hace cumplir la funcion para que solo se vean los porcentajes altos 
plt.legend(
    [f"{label}: {value}" for label, value in counts.items()], # Construye una lista de textos para la leyenda.
    loc="center left",
    bbox_to_anchor=(1, 0.5)
)
plt.title("Distribución por Género")
plt.show()


# ## **Preguntas a responder:**
# 
# **1. ¿Cuál es el rango de edad más común?**
#  
# 

# In[16]:


# Respuesta Primera Pregunta
edad_counts = df["EDAD_RANGO"].value_counts().sort_index() # conteo por rango 
print("\nDistribución por rangos de edad:")
print(edad_counts)
# Contar valores faltantes en EDAD_RANGO
faltantes = df["EDAD_RANGO"].isna().sum()
print("Número de valores faltantes en EDAD_RANGO:", faltantes)


# In[8]:


import matplotlib.pyplot as plt

# --- Visualización en barras ---
plt.figure(figsize=(10,6))
plt.bar(edad_counts.index, edad_counts.values, color=plt.cm.Set3.colors)  # paleta de colores variados

# Etiquetas
plt.title("Distribución por rangos de edad")
plt.xlabel("Rangos de edad")
plt.ylabel("Número de personas")

# Mostrar valores encima de las barras
for i, v in enumerate(edad_counts.values):
    plt.text(i, v + 20, str(v), ha="center", va="bottom", fontsize=9)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# #### **Respuesta**
# 
# Los Rangos de Edades mas comunes son de los 28 a los 37 años, cabe resaltar que se omitieron los 13 valores faltantes encontrados en esta variable.

# **2. ¿Hay diferencias en la distribución por género?**
#  

# In[14]:


df_genero = df[df["GENERO"].isin(["MASCULINO", "FEMENINO"])]

# Tabla cruzada: conteo por rango de edad y género
tabla = pd.crosstab(df_genero["EDAD_RANGO"], df_genero["GENERO"])

# Asegurar que los rangos salgan ordenados como los tienes
rangos_ordenados = ["18-22","23-27","28-32","33-37","38-42",
                    "43-47","48-52","53-57","58-62","63-67","68-72"]
tabla = tabla.reindex(rangos_ordenados, fill_value=0)

print(tabla)
total_general = tabla["FEMENINO"].sum() + tabla["MASCULINO"].sum()
print("Total general (hombres + mujeres):", total_general)


# In[10]:


fem = -tabla["FEMENINO"]
masc = tabla["MASCULINO"]

plt.figure(figsize=(10,6))
plt.barh(tabla.index, fem, color="pink", label="Femenino")
plt.barh(tabla.index, masc, color="skyblue", label="Masculino")
plt.title("Pirámide poblacional por género y rango de edad")
plt.xlabel("Número de personas")
plt.ylabel("Rangos de edad")
plt.legend()

# Mostrar valores en las barras
for i, (f, m) in enumerate(zip(fem, masc)):
    plt.text(f - 30, i, str(abs(f)), va="center", ha="right", fontsize=8)
    plt.text(m + 30, i, str(m), va="center", ha="left", fontsize=8)

plt.tight_layout()
plt.show()


# #### **Respuesta**
# 
# En la encuesta de bienestar familiar del personal de la Fuerza Aérea Colombiana (FAC) se observa una marcada predominancia del género masculino, que representa el 69,3% de los participantes y sobre todo entre los 28 y 37 años. En contraste, el género femenino corresponde al 30,4% con una fuerte conservacion poblacional de este genero desde los 32 hasta los 42 años. Adicionalmente, se registraron 15 casos clasificados como 'otros' y 2 casos identificados como 'no binarios'.
# 

# **3. ¿Cuál es el grado militar más frecuente?**

# In[38]:


# Análisis de género
print("\n=== ANÁLISIS DE GRADO Militar ===")
print(df['GRADO'].value_counts())
print(df['CATEGORIA'].value_counts())



# #### **Respuesta**
# 
# En la encuesta de bienestar familiar del personal de la FAC, la mayoría de los participantes se concentran en el grado de Suboficial (2.650), seguido por Civiles (1.929) y Oficiales (1.844). Dentro de los grados específicos, el mayor número de respuestas se encuentra en 'No responde' (1.929), y entre los grados militares destacan T3 (622), T2 (621) y T1 (491).

# In[17]:


get_ipython().system('jupyter nbconvert --to markdown "demografia_basica.ipynb" --output-dir="C:/Users/aleja/OneDrive/Documentos/Python_para_Analitica_y_Mineria_de_Datos/analisis-datos-fac-equipo-Nose/Reportes"')

