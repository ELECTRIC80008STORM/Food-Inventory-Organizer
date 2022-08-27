"""
Nombre-por-Decidir
Organizador de inventario para personas foráneas.
El programa recibirá un nombre de artículo e información relacionada al mismo y lo listará.
Enviando notificaciones al usuario cuando se requiera que recuerde algo.
"""

#Bibliotecas (Si se requiere mover a un archivo aparte)


#Funciones (Mover después a un archivo aparte)

#Convertir en clase en algún futuro
alimento = str((input("Ingresa un alimento: ")))
lista_de_alimentos = []
lista_de_alimentos.append(alimento.capitalize())

print("Alimentos actuales: ", *lista_de_alimentos)

respuesta_del_usuario_añadir_alimento = str(input("¿Quieres añadir otro alimento? "))

def respuesta(respuesta_dada_pregunta):
    if respuesta_dada_pregunta.lower() == "si" or respuesta_dada_pregunta.lower() == "sí":
        alimento = str((input("\nIngresa otro alimento: ")))
        lista_de_alimentos.append(alimento.capitalize())
        print("\nAlimentos actuales: ")
        print(*lista_de_alimentos, sep = ", ")
        respuesta_dada_pregunta = str(input("\n¿Quieres añadir otro alimento? "))
        respuesta(respuesta_dada_pregunta)
    if respuesta_dada_pregunta.lower() == "no":
        print("\nEspero la app te haya sido útil ")
    else:
        print("No entendí tu respuesta", "\n¿Quieres ingresar otro alimento?")
        respuesta_dada_pregunta = input()
        respuesta(respuesta_dada_pregunta)


respuesta(respuesta_del_usuario_añadir_alimento)