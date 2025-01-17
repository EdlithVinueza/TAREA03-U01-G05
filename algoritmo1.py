# -*- coding: utf-8 -*-
"""CRIPTOej1-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1f53w1-4ZffxgNPAOlLK4-060XZ-gsdpO

# Ejercicio 1
Algoritmo que escriba todas las posibles permutaciones de una palabra de longitud N sin espacios (anagrama). La palabra se ingresa al iniciar el algoritmo, el algoritmo debe mostrar el numero total de permutaciones y las 10 primeras ordenadas alfabeticamente.
"""

from itertools import permutations

# Solicitar al usuario que ingrese la palabra
palabra = input("Ingrese la palabra: ")

# Generar todas las permutaciones posibles y eliminamos duplicados (para palabras con letras repetidas)
permutaciones = sorted(set(''.join(p) for p in permutations(palabra)))

# Contar el número total de permutaciones
total_permutaciones = len(permutaciones)

# Mostrar el total de permutaciones
print(f"Total de permutaciones: {total_permutaciones}")

# Mostrar las primeras 10 permutaciones ordenadas alfabéticamente
print("Las primeras 10 permutaciones son:")
for perm in permutaciones[:10]:
    print(perm)

