'''
Titulo: Ordenamiento por shell
Descripcion: Este programa realiza el ordenamiento por shell dado el numero de elementos que el usuario desea ordenar, en este caso, los elementos se cargar a traves de un txt
Fecha: 20 de marzo del 2022
Version: 1.0
Autor: Espinoza Bautista Daniel
'''

# Importamos la libreria Numpy y Time
import numpy as np
from time import time

# Inicializamos el arreglo de numeros
numeros = []

# Solicitamos al usuario que nos diga el numero de elementos
# que quiere ordenar dentro del arreglo y a esta le restamos
# un 1 para que coincida con el arreglo
print("Numeros a ordenar")
cant = input()
cant = int(cant)

# Leemos los numeros del archivo, y lo agregamos a un arreglo
arch = np.loadtxt("D:\\Documentos\\ESCOM\\7moSemestre\\Analisis\\Practica 2\\numeros.txt", dtype="str", delimiter=" ")

# Inicializamos la variable para el ciclo
i=0

# Mediante el ciclo convertimos el arreglo a enteros para
# poder trabajar de una manera mas eficiente con el
while i<cant:
    aux = int(arch[i])
    numeros.append(aux)
    i+=1

# Inicializamos la variable tiempo_in que nos ayudara a
# contar el tiempo de ejecucion del programa
tiempo_in = time()

# Realizamos el ordenamiento del arreglo
def shell(numeros):
    n = len(numeros)
    gap = n//2
    while gap>0:
        for i in range(gap,n):
            key = numeros[i]
            while i>gap and numeros[i-gap]>key:
                numeros[i] = numeros[i-gap]
                i-=gap
            numeros[i]=key
        gap //= 2
    return numeros

# Llamamos a la funcion e imprimimos el arreglo
orde = shell(numeros)
print("Lista ordenada")

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)