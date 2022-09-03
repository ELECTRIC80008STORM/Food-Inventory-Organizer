"""
Nombre-por-Decidir
Organizador de inventario para personas foráneas.
El programa recibirá un nombre de artículo e información relacionada al mismo y lo listará.
Enviando notificaciones al usuario cuando se requiera que recuerde algo.
"""

#Bibliotecas (Si se requiere mover a un archivo aparte)


#Funciones (Mover después a un archivo aparte)


"""Programa Principal (No logré conseguir que las notificaciones funcionaran en 
la prueba externa que realicé ni logré convertir las funciones a una clase, por ahorita) """
lista_de_alimentos = []
lista_de_su_caducidad = []
alimento_numero = {}


def ingresar_alimento():
    alimento = str((input("Ingresa un alimento: ")))
    caducidad = str(input("Y su caducidad como dd/mm/aaaa: "))
    lista_de_alimentos.append(alimento.capitalize())
    numero_alimento = lista_de_alimentos.index(alimento.capitalize())
    alimento_numero[alimento.capitalize()] = numero_alimento
    lista_de_su_caducidad.append(caducidad)
    

ingresar_alimento()

def mostrar_datos_alimentos():
    print("Alimentos actuales: ")
    print(*lista_de_alimentos, sep = ", ")

def mostrar_datos_caducidad():
    print("Caducidad: ")
    print(*lista_de_su_caducidad, sep = ", ")


    
print("Alimentos actuales: ", *lista_de_alimentos, "\nCaducidad: ", *lista_de_su_caducidad)

respuesta_del_usuario_añadir_alimento = str(input("¿Quieres añadir otro alimento? "))

def respuesta(respuesta_dada_pregunta):
    if respuesta_dada_pregunta.lower() == "si" or respuesta_dada_pregunta.lower() == "sí":
        ingresar_alimento()
        mostrar_datos_alimentos()
        mostrar_datos_caducidad()
        respuesta_dada_pregunta = str(input("\n¿Quieres añadir otro alimento? "))
        respuesta(respuesta_dada_pregunta)
    elif respuesta_dada_pregunta.lower() == "no":
        print("\nEspero la app te haya sido útil ")
    else:
        print("No entendí tu respuesta", "\n¿Quieres ingresar otro alimento?")
        respuesta_dada_pregunta = input()
        respuesta(respuesta_dada_pregunta)


respuesta(respuesta_del_usuario_añadir_alimento)
