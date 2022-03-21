'''
Titulo: Ordenamiento por mezcla
Descripcion: Este programa realiza el ordenamiento por mezcla dado el numero de elementos que el usuario desea ordenar, en este caso, los elementos se cargar a traves de un txt
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
def mezcla(numeros):
    if len(numeros)>1:
        mid = len(numeros)//2
        left = numeros[:mid] # Creamos un nuevo arreglo solo con
                             # la mitad de la izquierda
        right = numeros[mid:] # Creamos un nuevo arreglo solo con
                              # la mitad de la derecha

        mezcla(left)
        mezcla(right)

        # Iteradores que pasaran por las mitades
        i=0
        j=0

        # Iterador para la lista principal
        k=0

        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                numeros[k]=left[i]
                i+=1
            else:
                numeros[k]=right[j]
                j+=1
            k+=1

        while i<len(left):
            numeros[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            numeros[k]=right[j]
            j+=1
            k+=1
    return numeros

# Llamamos a la funcion e imprimimos el arreglo
orde = mezcla(numeros)
print("Lista ordenada ")

# Calculamos el tiempo que tardo en encontrarlo
# y lo imprimimos
tiempo_fin = time() - tiempo_in
print("\nTiempo de ejecucion: %.10f segundos." % tiempo_fin)