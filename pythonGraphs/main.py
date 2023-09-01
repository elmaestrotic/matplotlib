import matplotlib.pyplot as plt
import numpy as np
import random

def print_barras():
    fig, xy = plt.subplots()
    xy.bar([10, 20, 30, 40, 50], [50, 40,30, 20, 10])
    plt.show()

def print_histograma():
    fig, xy = plt.subplots()
    # Generar valores aleatorios con una media de 7 y desviación estándar de 2
    x = np.random.normal(7, 2, size=1000)

    # Crear un histograma con intervalos de 1 y en el rango de 0 a 15
    xy.hist(x, np.arange(0, 16, 1))
    plt.show()

def print_gauss():
    fig, ax = plt.subplots()

    # Generar valores aleatorios con una media de 7 y desviación estándar de 2
    x = [random.gauss(7, 2) for _ in range(1000)]

    # Crear un histograma con intervalos de 1 y en el rango de 0 a 15
    ax.hist(x, bins=range(0, 16, 1))

    plt.show()

def print_sectores():
    import matplotlib.pyplot as plt

    # Datos para los sectores
    datos = [5, 4, 3, 2, 1]

    # Etiquetas para cada sector
    etiquetas = ['Categoría A', 'Categoría B', 'Categoría C', 'Categoría D', 'Categoría E']

    # Crear la figura y los ejes
    fig, ax = plt.subplots()

    # Crear el diagrama de sectores
    ax.pie(datos, labels=etiquetas, autopct='%1.1f%%', startangle=90)

    # Añadir título
    ax.set_title('Diagrama de Sectores')

    # Mostrar el gráfico
    plt.show()


if __name__ == '__main__':
    print_sectores()
    print_barras()
    print_histograma()


