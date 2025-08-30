### **ESTUDIANTE A: Análisis Demográfico**

**Responsabilidades:**
  - Explorar las columnas básicas de demografía
  - Crear visualizaciones simples de edad, género, rango
  - Documentar hallazgos principales



```python
# demografia_basica.py
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel("C:/Users/aleja/OneDrive/Documentos/Python_para_Analitica_y_Mineria_de_Datos/analisis-datos-fac-equipo-Nose/datos/JEFAB_2024.xlsx")

print("Cargue de los datos")
```

    Cargue de los datos
    

## **Importancia de los datos de la Encuesta de Bienestar Familiar del personal FAC**

El uso de datos provenientes de la encuesta de Bienestar Familiar del personal de la Fuerza Aérea Colombiana (FAC) es fundamental para garantizar que los análisis reflejen las condiciones y necesidades actuales del personal. Estas fuentes permiten identificar de manera objetiva aspectos sociodemográficos, condiciones de vida y características del entorno familiar, brindando insumos clave para orientar políticas y programas de bienestar institucional.

En este caso, la base de datos contiene variables relevantes como Edad, Género, Estado civil, Número de hijos, Nivel educativo, y Estrato socioeconómico, las cuales proporcionan una visión integral sobre la composición de la población encuestada. Estas variables son especialmente útiles para identificar tendencias, segmentar grupos de interés y establecer comparaciones que apoyen la toma de decisiones estratégicas dentro de la FAC.  

---

#### **Cantidad de registros a analizar:**



```python
# Explorar estructura básica
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")
```

    === INFORMACIÓN GENERAL ===
    Total de registros: 6423
    Total de columnas: 231
    

#### **Análisis de edad**


```python
# Análisis de edad
print("\n=== ANÁLISIS DE EDAD ===")
print(f"Edad promedio: {df['EDAD2'].mean():.1f} años")
print(f"Edad mínima: {df['EDAD2'].min()} años")
print(f"Edad máxima: {df['EDAD2'].max()} años")
```

    
    === ANÁLISIS DE EDAD ===
    Edad promedio: 36.7 años
    Edad mínima: 18.0 años
    Edad máxima: 69.0 años
    

#### **Gráfico de edades**


```python
plt.figure(figsize=(10, 6))
plt.hist(df['EDAD2'], bins=20, edgecolor='black')
plt.title('Distribución de Edades del Personal FAC')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Personal')
plt.show()

```


    
![png](demografia_basica_files/demografia_basica_7_0.png)
    


#### **Análisis de género**


```python
# Análisis de género
print("\n=== ANÁLISIS DE GÉNERO ===")
print(df['GENERO'].value_counts())
```

    
    === ANÁLISIS DE GÉNERO ===
    GENERO
    MASCULINO     4451
    FEMENINO      1955
    OTRO            15
    NO BINARIO       2
    Name: count, dtype: int64
    

#### **Grafico de Genero**


```python
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
```


    
![png](demografia_basica_files/demografia_basica_11_0.png)
    


## **Preguntas a responder:**

**1. ¿Cuál es el rango de edad más común?**
 



```python
# Respuesta Primera Pregunta
edad_counts = df["EDAD_RANGO"].value_counts().sort_index() # conteo por rango 
print("\nDistribución por rangos de edad:")
print(edad_counts)
# Contar valores faltantes en EDAD_RANGO
faltantes = df["EDAD_RANGO"].isna().sum()
print("Número de valores faltantes en EDAD_RANGO:", faltantes)

```

    
    Distribución por rangos de edad:
    EDAD_RANGO
    18-22     309
    23-27     958
    28-32    1211
    33-37    1254
    38-42    1012
    43-47     601
    48-52     470
    53-57     371
    58-62     194
    63-67      26
    68-72       4
    Name: count, dtype: int64
    Número de valores faltantes en EDAD_RANGO: 13
    


```python
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

```


    
![png](demografia_basica_files/demografia_basica_14_0.png)
    


#### **Respuesta**

Los Rangos de Edades mas comunes son de los 28 a los 37 años, cabe resaltar que se omitieron los 13 valores faltantes encontrados en esta variable.

**2. ¿Hay diferencias en la distribución por género?**
 


```python

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

```

    GENERO      FEMENINO  MASCULINO
    EDAD_RANGO                     
    18-22             81        228
    23-27            251        706
    28-32            299        909
    33-37            331        922
    38-42            290        720
    43-47            234        362
    48-52            229        237
    53-57            153        217
    58-62             76        118
    63-67              4         22
    68-72              3          1
    Total general (hombres + mujeres): 6393
    


```python
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

```


    
![png](demografia_basica_files/demografia_basica_18_0.png)
    


#### **Respuesta**

En la encuesta de bienestar familiar del personal de la Fuerza Aérea Colombiana (FAC) se observa una marcada predominancia del género masculino, que representa el 69,3% de los participantes y sobre todo entre los 28 y 37 años. En contraste, el género femenino corresponde al 30,4% con una fuerte conservacion poblacional de este genero desde los 32 hasta los 42 años. Adicionalmente, se registraron 15 casos clasificados como 'otros' y 2 casos identificados como 'no binarios'.


**3. ¿Cuál es el grado militar más frecuente?**


```python
# Análisis de género
print("\n=== ANÁLISIS DE GRADO Militar ===")
print(df['GRADO'].value_counts())
print(df['CATEGORIA'].value_counts())


```

    
    === ANÁLISIS DE GRADO Militar ===
    GRADO
    NO RESPONDE    1929
    T3              622
    T2              621
    T1              491
    CT              483
    AT              453
    TE              416
    ST              406
    MY              343
    T4              319
    TC              140
    TS               72
    TJ               61
    CR               48
    TJC              11
    BG                5
    MG                2
    GR                1
    Name: count, dtype: int64
    CATEGORIA
    SUBOFICIAL    2650
    CIVIL         1929
    OFICIAL       1844
    Name: count, dtype: int64
    


```python
import plotly.express as px

# Agrupar por categoría y contar
categoria_counts = df['GRADO'].value_counts().reset_index()
categoria_counts.columns = ['GRADO', 'COUNT']

# Crear treemap
fig = px.treemap(
    categoria_counts,
    path=['GRADO'],   # Nivel jerárquico
    values='COUNT',       # Tamaño por conteo
    color='COUNT',        # Colorear según el conteo
    color_continuous_scale='Blues',  # Escala de color
    title="Treemap de Categorías"
)

fig.show()

```


<div>                            <div id="858bff35-25cc-4ff0-bff7-58001635f563" class="plotly-graph-div" style="height:525px; width:100%;"></div>            <script type="text/javascript">                require(["plotly"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById("858bff35-25cc-4ff0-bff7-58001635f563")) {                    Plotly.newPlot(                        "858bff35-25cc-4ff0-bff7-58001635f563",                        [{"branchvalues":"total","customdata":[[453.0],[5.0],[48.0],[483.0],[1.0],[2.0],[343.0],[1929.0],[406.0],[491.0],[621.0],[622.0],[319.0],[140.0],[416.0],[61.0],[11.0],[72.0]],"domain":{"x":[0.0,1.0],"y":[0.0,1.0]},"hovertemplate":"labels=%{label}\u003cbr\u003eCOUNT_sum=%{value}\u003cbr\u003eparent=%{parent}\u003cbr\u003eid=%{id}\u003cbr\u003eCOUNT=%{color}\u003cextra\u003e\u003c\u002fextra\u003e","ids":["AT","BG","CR","CT","GR","MG","MY","NO RESPONDE","ST","T1","T2","T3","T4","TC","TE","TJ","TJC","TS"],"labels":["AT","BG","CR","CT","GR","MG","MY","NO RESPONDE","ST","T1","T2","T3","T4","TC","TE","TJ","TJC","TS"],"marker":{"coloraxis":"coloraxis","colors":[453.0,5.0,48.0,483.0,1.0,2.0,343.0,1929.0,406.0,491.0,621.0,622.0,319.0,140.0,416.0,61.0,11.0,72.0]},"name":"","parents":["","","","","","","","","","","","","","","","","",""],"values":[453,5,48,483,1,2,343,1929,406,491,621,622,319,140,416,61,11,72],"type":"treemap"}],                        {"template":{"data":{"histogram2dcontour":[{"type":"histogram2dcontour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"choropleth":[{"type":"choropleth","colorbar":{"outlinewidth":0,"ticks":""}}],"histogram2d":[{"type":"histogram2d","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmap":[{"type":"heatmap","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"heatmapgl":[{"type":"heatmapgl","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"contourcarpet":[{"type":"contourcarpet","colorbar":{"outlinewidth":0,"ticks":""}}],"contour":[{"type":"contour","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"surface":[{"type":"surface","colorbar":{"outlinewidth":0,"ticks":""},"colorscale":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]]}],"mesh3d":[{"type":"mesh3d","colorbar":{"outlinewidth":0,"ticks":""}}],"scatter":[{"fillpattern":{"fillmode":"overlay","size":10,"solidity":0.2},"type":"scatter"}],"parcoords":[{"type":"parcoords","line":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolargl":[{"type":"scatterpolargl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"bar":[{"error_x":{"color":"#2a3f5f"},"error_y":{"color":"#2a3f5f"},"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"bar"}],"scattergeo":[{"type":"scattergeo","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterpolar":[{"type":"scatterpolar","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"histogram":[{"marker":{"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"histogram"}],"scattergl":[{"type":"scattergl","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatter3d":[{"type":"scatter3d","line":{"colorbar":{"outlinewidth":0,"ticks":""}},"marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattermapbox":[{"type":"scattermapbox","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scatterternary":[{"type":"scatterternary","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"scattercarpet":[{"type":"scattercarpet","marker":{"colorbar":{"outlinewidth":0,"ticks":""}}}],"carpet":[{"aaxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"baxis":{"endlinecolor":"#2a3f5f","gridcolor":"white","linecolor":"white","minorgridcolor":"white","startlinecolor":"#2a3f5f"},"type":"carpet"}],"table":[{"cells":{"fill":{"color":"#EBF0F8"},"line":{"color":"white"}},"header":{"fill":{"color":"#C8D4E3"},"line":{"color":"white"}},"type":"table"}],"barpolar":[{"marker":{"line":{"color":"#E5ECF6","width":0.5},"pattern":{"fillmode":"overlay","size":10,"solidity":0.2}},"type":"barpolar"}],"pie":[{"automargin":true,"type":"pie"}]},"layout":{"autotypenumbers":"strict","colorway":["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],"font":{"color":"#2a3f5f"},"hovermode":"closest","hoverlabel":{"align":"left"},"paper_bgcolor":"white","plot_bgcolor":"#E5ECF6","polar":{"bgcolor":"#E5ECF6","angularaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"radialaxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"ternary":{"bgcolor":"#E5ECF6","aaxis":{"gridcolor":"white","linecolor":"white","ticks":""},"baxis":{"gridcolor":"white","linecolor":"white","ticks":""},"caxis":{"gridcolor":"white","linecolor":"white","ticks":""}},"coloraxis":{"colorbar":{"outlinewidth":0,"ticks":""}},"colorscale":{"sequential":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"sequentialminus":[[0.0,"#0d0887"],[0.1111111111111111,"#46039f"],[0.2222222222222222,"#7201a8"],[0.3333333333333333,"#9c179e"],[0.4444444444444444,"#bd3786"],[0.5555555555555556,"#d8576b"],[0.6666666666666666,"#ed7953"],[0.7777777777777778,"#fb9f3a"],[0.8888888888888888,"#fdca26"],[1.0,"#f0f921"]],"diverging":[[0,"#8e0152"],[0.1,"#c51b7d"],[0.2,"#de77ae"],[0.3,"#f1b6da"],[0.4,"#fde0ef"],[0.5,"#f7f7f7"],[0.6,"#e6f5d0"],[0.7,"#b8e186"],[0.8,"#7fbc41"],[0.9,"#4d9221"],[1,"#276419"]]},"xaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"yaxis":{"gridcolor":"white","linecolor":"white","ticks":"","title":{"standoff":15},"zerolinecolor":"white","automargin":true,"zerolinewidth":2},"scene":{"xaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"yaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2},"zaxis":{"backgroundcolor":"#E5ECF6","gridcolor":"white","linecolor":"white","showbackground":true,"ticks":"","zerolinecolor":"white","gridwidth":2}},"shapedefaults":{"line":{"color":"#2a3f5f"}},"annotationdefaults":{"arrowcolor":"#2a3f5f","arrowhead":0,"arrowwidth":1},"geo":{"bgcolor":"white","landcolor":"#E5ECF6","subunitcolor":"white","showland":true,"showlakes":true,"lakecolor":"white"},"title":{"x":0.05},"mapbox":{"style":"light"}}},"coloraxis":{"colorbar":{"title":{"text":"COUNT"}},"colorscale":[[0.0,"rgb(247,251,255)"],[0.125,"rgb(222,235,247)"],[0.25,"rgb(198,219,239)"],[0.375,"rgb(158,202,225)"],[0.5,"rgb(107,174,214)"],[0.625,"rgb(66,146,198)"],[0.75,"rgb(33,113,181)"],[0.875,"rgb(8,81,156)"],[1.0,"rgb(8,48,107)"]]},"legend":{"tracegroupgap":0},"title":{"text":"Treemap de Categor\u00edas"}},                        {"responsive": true}                    ).then(function(){

var gd = document.getElementById('858bff35-25cc-4ff0-bff7-58001635f563');
var x = new MutationObserver(function (mutations, observer) {{
        var display = window.getComputedStyle(gd).display;
        if (!display || display === 'none') {{
            console.log([gd, 'removed!']);
            Plotly.purge(gd);
            observer.disconnect();
        }}
}});

// Listen for the removal of the full notebook cells
var notebookContainer = gd.closest('#notebook-container');
if (notebookContainer) {{
    x.observe(notebookContainer, {childList: true});
}}

// Listen for the clearing of the current output cell
var outputEl = gd.closest('.output');
if (outputEl) {{
    x.observe(outputEl, {childList: true});
}}

                        })                };                });            </script>        </div>


#### **Respuesta**

En la encuesta de bienestar familiar del personal de la FAC, la mayoría de los participantes se concentran en el grado de Suboficial (2.650), seguido por Civiles (1.929) y Oficiales (1.844). Dentro de los grados específicos, el mayor número de respuestas se encuentra en 'No responde' (1.929), y entre los grados militares destacan T3 (622), T2 (621) y T1 (491).


```python
!jupyter nbconvert --to markdown "demografia_basica.ipynb" --output-dir="C:/Users/aleja/OneDrive/Documentos/Python_para_Analitica_y_Mineria_de_Datos/analisis-datos-fac-equipo-Nose/Reportes"

```

    [NbConvertApp] Converting notebook demografia_basica.ipynb to markdown
    [NbConvertApp] Support files will be in demografia_basica_files\
    [NbConvertApp] Writing 4578327 bytes to C:\Users\aleja\OneDrive\Documentos\Python_para_Analitica_y_Mineria_de_Datos\analisis-datos-fac-equipo-Nose\Reportes\demografia_basica.md
    


```python
!jupyter nbconvert --to script "demografia_basica.ipynb" --output-dir="C:/Users/aleja/OneDrive/Documentos/Python_para_Analitica_y_Mineria_de_Datos/analisis-datos-fac-equipo-Nose/Codigo Python"

```

    [NbConvertApp] Converting notebook demografia_basica.ipynb to script
    [NbConvertApp] Writing 7078 bytes to C:\Users\aleja\OneDrive\Documentos\Python_para_Analitica_y_Mineria_de_Datos\analisis-datos-fac-equipo-Nose\Codigo Python\demografia_basica.py
    
