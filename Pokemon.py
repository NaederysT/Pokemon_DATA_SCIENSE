import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



"""
Ejercicios de Análisis de Datos con Pokémon (Primera Generación)
===============================================================
Archivo de datos: pokemon_primera_gen.csv
"""

"""
1. Lectura de datos
-------------------
- Carga el archivo pokemon_primera_gen.csv en un DataFrame de Pandas.
"""
tabla_Pokemon = pd.read_csv('pokemon_primera_gen.csv')
#print(tabla_Pokemon.head())
"""
2. Filtrado y selección
-----------------------
- Filtra todos los Pokémon de tipo "Fuego".
- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
"""
#Nombre,Tipo 1,Tipo 2,Ataque,Defensa,Velocidad,PS
tipo_Fuego = tabla_Pokemon.loc[tabla_Pokemon['Tipo 1'] == 'Fuego', ['Nombre', 'Tipo 1', 'Ataque', 'Velocidad']]
print(tipo_Fuego)


"""
3. Estadística descriptiva básica
---------------------------------
- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
- ¿Cuántos Pokémon tienen dos tipos?
- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
"""

# ! Calculo promedio
def promedioAtaques():
    promedios_Ataques = round(tabla_Pokemon['Ataque'].mean(),1)
    print(f'El promedio de los ataques: {promedios_Ataques}')

# ! Calculo mediana
def mediaAtaques():
    mediana_Ataques = tabla_Pokemon['Ataque'].median()
    print(f'La media de los ataques de los pokemnones son: {mediana_Ataques}')

# ! Calculo moda
def modaAtaques():
    moda_Ataques = tabla_Pokemon['Ataque'].mode().values[0]
    print(f'La moda de los ataques de los pokemnones son: {moda_Ataques}')

def pregunta3A():
    promedioAtaques()
    mediaAtaques()
    modaAtaques()
    
pregunta3A()

#  ! Nombre,Tipo 1,Tipo 2,Ataque,Defensa,Velocidad,PS
def mayorDefensa():
    pokemon_defensa_Alta = tabla_Pokemon['Defensa'].idxmax()
    print(f"El pokemon de mayor defensa es: {pokemon_defensa_Alta}")
    
def menorVelocidad():
    pokemon_menor_Velocidad = tabla_Pokemon['Velocidad'].idxmin()
    print(f"El pokemon de menor velocidad es: {pokemon_menor_Velocidad}")

def pregunta3B():
    mayorDefensa()
    menorVelocidad()
pregunta3B()


# Cantidad de pokemon con dos tipos
def cantidadDosTipos():
    dos_Tipos = tabla_Pokemon["Tipo 2"].notna() & (tabla_Pokemon["Tipo 2"] != "")
    print(f'Cantidad de pokemon de 2 tipos: {dos_Tipos.sum()}')

cantidadDosTipos()

"""
4. Visualización de datos
-------------------------
- Haz un histograma de los valores de ataque.
- Realiza un gráfico de dispersión entre ataque y velocidad.
- Haz un boxplot de los PS por tipo principal (Tipo 1).
- Grafica la distribución de la defensa usando un diagrama de violín.
"""
# ! HISTOGRAMA DEVALORES DE ATAQUE
def histogramaAtaque():
    plt.figure(figsize=(10,6))
    sns.histplot(tabla_Pokemon['Ataque'], bins=20, kde=True)
    plt.title('Histograma de Valores de Ataque')
    plt.xlabel('Valor de Ataque')
    plt.ylabel('Frecuencia')
    plt.show()
histogramaAtaque()

# !GRAFICO DE DISPERSION ENTRE ATAQUE Y VELOCIDAD
def graficoDispersion():
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=tabla_Pokemon, x='Ataque', y='Velocidad', hue='Tipo 1', palette='viridis')
    plt.title('Gráfico de Dispersión entre Ataque y Velocidad')
    plt.xlabel('Ataque')
    plt.ylabel('Velocidad')
    plt.legend(title='Tipo 1', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()
graficoDispersion()

# !BLOXPLOT DE PUNTOS DE SALUD POR TIPO PRINCIPAL (TIPO 1)
def boxplotPS():
    plt.figure(figsize=(12,8))
    sns.boxplot(data=tabla_Pokemon, x='Tipo 1', y='PS', palette='Set3')
    plt.title('Boxplot de Puntos de Salud por Tipo Principal (Tipo 1)')
    plt.xlabel('Tipo 1')
    plt.ylabel('Puntos de Salud (PS)')
    plt.xticks(rotation=45)
    plt.show()
#bloxplotPS()

# !DIAGRAMA DE VIOLIN DE LA DEFENSA
def diagramaViolinDefensa():
    plt.figure(figsize=(12,8))
    sns.violinplot(data=tabla_Pokemon, x='Tipo 1', y='Defensa', palette='Set2')
    plt.title('Diagrama de Violín de la Defensa por Tipo Principal (Tipo 1)')
    plt.xlabel('Tipo 1')
    plt.ylabel('Defensa')
    plt.xticks(rotation=45)
    plt.show()
diagramaViolinDefensa()

"""
5. Manipulación de datos
------------------------
- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
- Ordena el DataFrame por "Poder Total" de mayor a menor.
"""
# !CREACION COLUMNNA "pODER TOTAL"
def crearColumnaPoderTotal():
    tabla_Pokemon['Poder Total'] = tabla_Pokemon[['Ataque', 'Defensa', 'Velocidad', 'PS']].sum(axis=1)
    print("columna de Poder total con la suma de ataque - defensa - velocidad -ps")
    print(tabla_Pokemon.head())
crearColumnaPoderTotal()

# !ORDENAR EL DT POR PODER TOTAL DE MAYOR A MENOR
def ordenarPorPoderTotal():
    tabla_ordenada = tabla_Pokemon.sort_values(by='Poder Total', ascending=False)
    print("Tabla con orden de poder total de mayor a menor")
    print(tabla_ordenada.head())
ordenarPorPoderTotal()

"""
6. Agrupamiento y análisis por grupo
-------------------------------------
- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
- ¿Qué tipo tiene el mayor promedio de velocidad?
- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
"""

# ! Caluclo promedio de ataque por TIPO 1
def promedioAtaqueTipo1():
    promedioAtaqueTipo1 = tabla_Pokemon.groupby('Tipo 1')['Ataque'].mean().round(1)
    print(f"El promedio de ataque por tipo principal es:{promedioAtaqueTipo1}")

def medianaAtaqueTipo1():
    medianaAtaqueTipo1 = tabla_Pokemon.groupby('Tipo 1')['Ataque'].median()
    print(f"La mediana de ataque por tipo principal es: {medianaAtaqueTipo1}")

def desviacionEstandarAtaqueTipo1():
    desviacionEstandarAtaqueTipo1 = tabla_Pokemon.groupby('Tipo 1')['Ataque'].std().round(1)
    print(f"La desviacion estandar de ataque por tipo principal es : {desviacionEstandarAtaqueTipo1}")

def pregunta6A():
    promedioAtaqueTipo1()
    medianaAtaqueTipo1()
    desviacionEstandarAtaqueTipo1()
pregunta6A()

# !Tipo (Tipo 1 o 2) con MAYOR promedio de VELOCIDAD
def tipoMayorPromedioVelocidad():
    velocidadPromedio1 = round(tabla_Pokemon.groupby('Tipo 1')['Velocidad'].mean(),1)
    velocidadPromedio2 = round(tabla_Pokemon.groupby('Tipo 2')['Velocidad'].mean(),1)
    mayor_tipo1 = velocidadPromedio1.idxmax()
    mayor_tipo2 = velocidadPromedio2.idxmax()
    if velocidadPromedio1[mayor_tipo1] > velocidadPromedio2[mayor_tipo2]:
        print(f'El tipo con mayor promedio de velocidad es Tipo 1: {mayor_tipo1} con un promedio de {velocidadPromedio1[mayor_tipo1]}')
    else:
        print(f'El tipo con mayor promedio de velocidad es Tipo 2: {mayor_tipo2} con un promedio de {velocidadPromedio2[mayor_tipo2]}')
tipoMayorPromedioVelocidad()

# !Tipo 1 con MAYOR PUNTOS DE SALUD y MENOR PUNTOS DE SALUD (ps)
    
def pokemonMayorPsTipo1():
    mayor_ps_tipo1 = tabla_Pokemon.loc[tabla_Pokemon.groupby('Tipo 1')['PS'].idxmax()]
    print("Pokémon con mayor PS por Tipo 1:")
    print(mayor_ps_tipo1[['Tipo 1', 'Nombre', 'PS']])

def pokemonMenorPsTipo1():
    menor_ps_tipo1 = tabla_Pokemon.loc[tabla_Pokemon.groupby('Tipo 1')['PS'].idxmin()]
    print("Pokémon con menor PS por Tipo 1:")
    print(menor_ps_tipo1[['Tipo 1', 'Nombre', 'PS']])

def Mayor_Y_Menor_PS_Tipo1():
    pokemonMayorPsTipo1()
    pokemonMenorPsTipo1()

Mayor_Y_Menor_PS_Tipo1()

"""
7. Análisis exploratorio (EDA)
------------------------------
- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
- Identifica posibles outliers en los valores de ataque y PS usando boxplots.
"""

# !Tipos de pokemon que tienden a mayor ataque o defensa
