"""
Food Inventory Organizer
Organizador de Alimentos para la despensa.
El objetivo del programa es ayudar a tener una mejor organización y control sobre nuestros alimentos,
pudiendo tener en un solo lugar su fecha como caducidad, la categoría que le ponemos y cuando creemos que se puede acabar.
"""

#Biblioteca
from time import sleep
import classes_and_functions 

#Listas Auxiliares
lista_alimentos = []

#Código Principal
def inicio_app():
    """
    Realiza las acciones iniciales al momento de empezar la app.
    No poseé ningún parámetro.
    No regresa ningún valor.
    """
    print("\nBienvenido!!!", "\nPruebe a ingresar su primer alimento:")
    sleep(1)
    classes_and_functions.crear_alimento(lista_alimentos)
    classes_and_functions.mostrar_alimentos(lista_alimentos)
    sleep(1.5)
    classes_and_functions.opciones(lista_alimentos)

inicio_app()
