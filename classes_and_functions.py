#Biblioteca
from time import sleep

#Clases
class Alimento:
    """Guarda el nombre del alimento, su caducidad, la fecha estimada para que se acabe y su categoría.
       Propiedades:
            nombre: Guarda como string el nombre del alimento.
            caducidad: Guarda como string la fecha de caducidad del alimento.
            fecha_estimada_a_acabarse: Guarda como string la fecha estimada para que se acabe el alimento.
            categoria: Guarda como string la categoria que posea el alimento
        Métodos:
        __str_:
        Da en la pantalla el mensaje 
        "Alimento: {self.nombre}
        Caducará el {self.caducidad}
        Se acabará aproximadamente el {self.fecha_estimada_a_acabarse}
        Su categoría es: {self.categoria}" 
        cuando el objeto es puesto en print()
        """
    def __init__(self,nombre,caducidad,fecha_estimada,categoria):
        self.nombre = str(nombre).lower()
        self.nombre = self.nombre.capitalize()
        self.caducidad = str(caducidad)
        self.fecha_estimada_a_acabarse = str(fecha_estimada)
        self.categoria = str(categoria)
    
    def __str__(self):
        return f"\nAlimento: {self.nombre}\nCaducará el {self.caducidad}\
            \nSe acabará aproximadamente el {self.fecha_estimada_a_acabarse}\nSu categoría es: {self.categoria}"

#Listas Auxiliares
categorias_predeterminadas = ["Verduras Y Hierbas Frescas", "Frutas", "Nueces, Semillas Y Graneles",\
     "Lácteos Y Huevos", "Carne, Pollo Y Pescados", "Salchichoneria", "Despensa", "Botanas Y Snacks",\
         "Congelados", "Dulces Y Chocolates", "Bebidas", "Cerveza, Vinos Y Licores\n"]
categorias_creadas = []

#Funciones Principales
def crear_alimento(lista):
    """
    Crea un objeto “alimento” al que le da un nombre, caducidad, fecha para acabarse y categoría tras pedir al usuario esta información.
    Parámetros: 
    lista: list
    No regresa ningún valor.
    """
    nombre_del_alimento = str(input("\nIngresa el alimento a listar: "))
    nombre_del_alimento = nombre_del_alimento.lower()

    caducidad = caducidad_del_alimento()

    fecha_estimada = fecha_estimada_a_acabarse()

    categoriaseleccionada = categoria()

    nombre_del_alimento = Alimento(nombre_del_alimento,caducidad,fecha_estimada,categoriaseleccionada)
    lista.append(nombre_del_alimento)

def mostrar_alimentos(lista):
    """
    Checa si hay alimentos actuales y los muestra en pantalla, de lo contrario muestra “No tiene alimentos actuales”.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    print("\nSus alimentos actuales son:")
    if(len(lista) == 0):
        print("\nNo tiene alimentos actuales")
    else:
        for alimento in lista:
            print(alimento.nombre)

def buscar_alimento(lista):
    """
    Checa si el alimento que se busca está guardado y da su información, de lo contrario muestra “El alimento no se encontró en la lista”.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    print("\n¿Qué alimento desea buscar?: ")
    alimento_a_buscar = str(input()).capitalize()

    acum = 0
    for item in lista:
        if alimento_a_buscar == item.nombre:
            acum = acum + 1
            alimento = item

    if(acum > 0):
        print("\nEl alimento se encuentra guardado")
        print(alimento)
    else:
        print("\nEl alimento no se encontró en la lista")

def editar_info_alimento(lista):
    """
    Checa si el alimento que se desea editar está guardado y da a elegir al usuario que desea editar, después guarda la nueva propiedad en el objeto seleccionado.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    alimento = str(input("\n¿Qué alimento desea editar?: ")).capitalize()
   
    acum = 0
    for item in lista:
        if alimento == item.nombre:
            acum = acum + 1
            alimento = item
   
    if(acum <= 0): print("\nEl alimento no se encuentra en la lista")
    
    else:
        print("\n¿Qué desea editar?","\n1. Caducidad","\n2. Fecha Estimada para Acabarse","\n3. Categoría")
        print("Tip: Puede ingresar solo el número de la opción\n")
        respuesta = str(input())
        
        while(respuesta != "1" and respuesta != "2" and respuesta != "3"\
            and respuesta.lower() != "caducidad" and respuesta.lower() != "fecha estimada para acabarse"\
            and respuesta.lower() != "categoría" and respuesta.lower() != "categoria"):
            print("\nNo entendí su respuesta. Por favor ingresala de nuevo")
            respuesta = str(input())
       
        if(respuesta == "1" or respuesta.lower() == "caducidad"):
            alimento.caducidad = caducidad_del_alimento()
        
        elif(respuesta == "2" or respuesta.lower() == "fecha estimada para acabarse"):
            alimento.fecha_estimada_a_acabarse = fecha_estimada_a_acabarse()

        elif(respuesta == "3" or respuesta.lower() == "categoría" or respuesta.lower() == "categoria"):
            alimento.categoria = categoria()

def borrar_alimento(lista):
    """
    Checa si el alimento (objeto) que deseas borrar está guardado y lo elimina tras preguntar.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    alimento = str(input("\n¿Qué alimento desea borrar?: ")).capitalize()
   
    acum = 0
    for item in lista:
        if alimento == item.nombre:
            acum = acum + 1
            alimento = item
   
    if(acum <= 0): print("\nEl alimento no se encuentra en la lista")
    
    else:
        respuesta = str(input("\n¿Está seguro que desea borrar este alimento y su información?\
            \nEsta acción no se podrá revertir\n"))
       
        while(respuesta.lower() != "si" and respuesta.lower() != "sí" and respuesta.lower() != "no"):
            print("\nNo entendí tu respuesta. Por favor ingresala de nuevo")
            respuesta = str(input())
       
        if(respuesta.lower() == "si" or respuesta.lower() == "sí"):
            lista.remove(alimento)
            del alimento
            sleep(1)
            print("\nEl alimento y su información han sido eliminados exitosamente")
            sleep(1.5)
            mostrar_alimentos(lista)

def salir_app():
    """
    Permité salir de la app.
    No poseé ningún parámetro.
    No regresa ningún valor.
    """
    sleep(1.5)
    print("\nHa salido de la app. \nVuelva pronto!!!\n")

def opciones(lista):
    """
    Le da opciones al usuario para decidir su siguiente acción.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    print("\n¿Qué desea hacer ahora?")
    print("Tip: Puede ingresar solo el número de la opción\n")
    print("1. Añadir un alimento")
    print("2. Mostrar los alimentos actuales")
    print("3. Buscar un alimento específico junto con su información")
    print("4. Editar la información de algún alimento")
    print("5. Borrar un alimento junto con su información")
    print("6. Salir de la app\n")
    respuesta = str(input())
    
    while(respuesta != "1" and respuesta != "2" and respuesta != "3" and respuesta != "4"\
        and respuesta != "5" and respuesta != "6"\
        and respuesta.lower() != "añadir un alimento" and respuesta.lower() != "mostrar los alimentos actuales"\
        and respuesta.lower() != "buscar un alimento específico junto con su información"\
        and respuesta.lower() != "editar la información de algún alimento"\
        and respuesta.lower() != "borrar un alimento junto con su información" and respuesta.lower() != "salir de la app"):
        print("\nNo entendí su respuesta. Por favor ingresala de nuevo:")
        respuesta = str(input())

    if(respuesta == "1" or respuesta.lower() == "añadir un alimento"):
        crear_alimento(lista)
        desea_continuar(lista)
    elif(respuesta == "2" or respuesta.lower() == "mostrar los alimentos actuales"):
        mostrar_alimentos(lista)
        desea_continuar(lista)
    elif(respuesta == "3" or respuesta.lower() == "buscar un alimento específico junto con su información"):
        buscar_alimento(lista)
        desea_continuar(lista)
    elif(respuesta == "4" or respuesta.lower() == "editar la información de algún alimento"):
        editar_info_alimento(lista)
        desea_continuar(lista)
    elif(respuesta == "5" or respuesta.lower() == "borrar un alimento junto con su información"):
        borrar_alimento(lista)
        desea_continuar(lista)
    elif(respuesta == "6" or respuesta.lower() == "salir de la app"):
        salir_app()

#Funciones Auxiliares
def caducidad_del_alimento():
    """
    Produce una fecha en formato de string para la caducidad después de obtener el año, mes y día por el usuario, limitando el meter valores incorrectos.
    No poseé ningún parámetro.
    Devuelve “Día/Mes/Año”
    """
    anno = input("\nIntroduce el año de caducidad: ")
    while(isinstance(anno,int) == False or len(str(anno)) != 4):
        if(isinstance(anno,int) == False):
            if(anno.isdigit()):
                anno = int(anno)
            else:
                print("Ingresé el año como un número de 4 dígitos: ")
                anno = input()
        elif(len(str(anno)) != 4):
            print("Ingresé el año como un número de 4 dígitos: ")
            anno = input()
        
        
    mes = input("Introduce el mes de caducidad: ")
    while(isinstance(mes,int) == False or mes <= 0 or mes > 12):
        if(isinstance(mes,int) == False):
            if(mes.isdigit()):
                mes = int(mes)
            else:
                print("Ingresé el mes como un número adecuado: ")
                mes = input() 
        elif(mes <= 0 or mes > 12):
            print("Ingresé el mes como un número adecuado: ")
            mes = input()
    

    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        cantidad_de_dias = 31
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        cantidad_de_dias = 30
    else:
        cantidad_de_dias = 29


    dia = input("Introduce el día de caducidad: ")
    while(isinstance(dia,int) == False or dia <= 0 or dia > cantidad_de_dias):
        if(isinstance(dia,int) == False):
            if(dia.isdigit()):
                dia = int(dia)
            else:
                print("\nIngresé el día como un número adecuado de acuerdo al mes que seleccionó: ")
                dia = input() 
        elif(dia <= 0 or dia > cantidad_de_dias):
            print("\nIngresé el día como un número adecuado de acuerdo al mes que seleccionó: ")
            dia = input()


    caducidad = "{}/{}/{}"
    return caducidad.format(dia,mes,anno)

def fecha_estimada_a_acabarse():
    """
    Produce una fecha en formato de string para la fecha estimada a acabarse después de obtener
    el año, mes y día por el usuario, limitando el meter valores incorrectos.
    No poseé ningún parámetro.
    Devuelve “Día/Mes/Año”
    """
    anno = input("\nIntroduce el año cuando consideras que podría acabarse: ")
    while(isinstance(anno,int) == False or len(str(anno)) != 4):
        if(isinstance(anno,int) == False):
            if(anno.isdigit()):
                anno = int(anno)
            else:
                print("Ingresé el año como un número de 4 dígitos: ")
                anno = input()
        elif(len(str(anno)) != 4):
            print("Ingresé el año como un número de 4 dígitos: ")
            anno = input()
        
        
    mes = input("Introduce el mes cuando consideras que podría acabarse: ")
    while(isinstance(mes,int) == False or mes <= 0 or mes > 12):
        if(isinstance(mes,int) == False):
            if(mes.isdigit()):
                mes = int(mes)
            else:
                print("Ingresé el mes como un número adecuado: ")
                mes = input() 
        elif(mes <= 0 or mes > 12):
            print("Ingresé el mes como un número adecuado: ")
            mes = input()
    

    if(mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        cantidad_de_dias = 31
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        cantidad_de_dias = 30
    else:
        cantidad_de_dias = 29


    dia = input("Introduce el día cuando consideras que podría acabarse: ")
    while(isinstance(dia,int) == False or dia <= 0 or dia > cantidad_de_dias):
        if(isinstance(dia,int) == False):
            if(dia.isdigit()):
                dia = int(dia)
            else:
                print("\nIngresé el día como un número adecuado de acuerdo al mes que seleccionó: ")
                dia = input() 
        elif(dia <= 0 or dia > cantidad_de_dias):
            print("\nIngresé el día como un número adecuado de acuerdo al mes que seleccionó: ")
            dia = input()


    fecha_estimada = "{}/{}/{}"
    return fecha_estimada.format(dia,mes,anno)

def categoria():
    """
    Permite seleccionar una categoría predeterminada o crear una y guardarla.
    No poseé ningún parámetro.
    Devuelve la categoría seleccionada como string.
    """
    print("\nSeleccióne una categoría o cree una nueva escribiendo \"Crear\"\n")
    sleep(2.5)
    print("Categorías Predeterminadas:")
    for categoria in categorias_predeterminadas:
        print(categoria)
    
    sleep(3.5)
   
    if(len(categorias_creadas) != 0):
        print("Categorías Creadas:")
        for categoria in categorias_creadas:
            print(categoria)
        print("\n")
    
    respuesta = str(input()).lower()
    
    acum = 0
    while(acum == 0):
        for categoria in categorias_predeterminadas:
            if(respuesta == categoria.lower()):
                respuesta = respuesta.title()
                acum = acum + 1
                return respuesta
        for categoria in categorias_creadas:
            if(respuesta == categoria.lower()):
                respuesta = respuesta.title()
                acum = acum + 1
                return respuesta
        if(respuesta == "crear"):
            categoria = str(input("\nAñada su Categoría: "))
            categoria = categoria.title()
            categorias_creadas.append(categoria)
            acum = acum + 1
            return categoria
        print("\nNo entendí su respuesta. Por favor ingresala de nuevo:")
        print("Tip: Recuerda seleccionar una categoría predeterminada o escribir \"Crear\" para hacer la tuya\n")
        respuesta = str(input()).lower()

def desea_continuar(lista):
    """
    Da la opción al usuario de continuar con otra opción o salirse del programa.
    Parámetro:
    lista: list
    No regresa ningún valor.
    """
    respuesta = str(input("\n¿Desea hacer algo más?: "))
    
    while(respuesta.lower() != "si" and respuesta.lower() != "sí" and respuesta.lower() != "no"):
        print("\nNo entendí tu respuesta. Por favor ingresala de nuevo")
        print("Tip: Contesta un sí o un no")
        respuesta = str(input())
    
    if(respuesta.lower() == "si" or respuesta.lower() == "sí"):
        opciones(lista)
    else:
        salir_app()
