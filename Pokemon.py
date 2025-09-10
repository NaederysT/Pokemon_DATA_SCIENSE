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
    moda_Ataques = tabla_Pokemon['Ataque'].mode()
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

