class Alimento:
    def __init__(self,nombre,caducidad,fecha_estimada):
        self.nombre = str(nombre).capitalize()
        self.caducidad = str(caducidad)
        self.fecha_estimada_a_acabarse = str(fecha_estimada)
    
    def __str__(self):
        return f"\nAlimento: {self.nombre}\nCaducará el {self.caducidad}\nSe acabará aproximadamente el { self.fecha_estimada_a_acabarse}"

def caducidad_del_alimento():
    año = input("\nIntroduce el año de caducidad: ")
    while(isinstance(año,int) == False or len(str(año)) != 4):
        if(isinstance(año,int) == False):
            if(año.isdigit()):
                año = int(año)
            else:
                print("Ingresé el año como un número de 4 dígitos: ")
                año = input()
        elif(len(str(año)) != 4):
            print("Ingresé el año como un número de 4 dígitos: ")
            año = input()
        
        
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
    return caducidad.format(dia,mes,año)

def fecha_estimada_a_acabarse():
    año = input("\nIntroduce el año cuando consideras que podría acabarse: ")
    while(isinstance(año,int) == False or len(str(año)) != 4):
        if(isinstance(año,int) == False):
            if(año.isdigit()):
                año = int(año)
            else:
                print("Ingresé el año como un número de 4 dígitos: ")
                año = input()
        elif(len(str(año)) != 4):
            print("Ingresé el año como un número de 4 dígitos: ")
            año = input()
        
        
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
    return fecha_estimada.format(dia,mes,año)

def crearAlimento(lista):
    nombre_del_alimento = str(input("\nIngresa el alimento a listar: "))
    nombre_del_alimento = nombre_del_alimento.lower()

    caducidad = caducidad_del_alimento()

    fecha_estimada = fecha_estimada_a_acabarse()

    nombre_del_alimento = Alimento(nombre_del_alimento,caducidad,fecha_estimada)
    lista.append(nombre_del_alimento)
    print(nombre_del_alimento) #Solo para comprobar que funciona, quitar después

def mostrar_alimentos(lista):
    print("\nLos alimentos guardados son:")
    for alimento in lista:
        print(alimento.nombre)

def buscar_alimento(lista):
    print("\n¿Qué alimento desea buscar?: ")
    alimento_a_buscar = str(input()).capitalize()

    acum = 0
    for item in lista:
        if alimento_a_buscar == item.nombre:
            acum = acum + 1
            alimento = item

    if(acum > 0):
        print("El alimento se encuentra guardado")
        print(alimento)
    else:
        print("\nEl alimento no se encontró en la lista")

def editar_info_alimento(lista):
    alimento = str(input("\n¿Qué alimento desea editar?: ")).capitalize()
   
    acum = 0
    for item in lista:
        if alimento == item.nombre:
            acum = acum + 1
            alimento = item
   
    if(acum <= 0): print("\nEl alimento no se encuentra en la lista")
    
    else:
        print("\n¿Qué desea editar?","\n1. Caducidad","\n2. Fecha Estimada para Acabarse")
        print("Nota: Puede ingresar solo el número de la opción\n")
        respuesta = str(input())
        
        while(respuesta != "1" and respuesta != "2" and respuesta.lower() != "caducidad" and respuesta.lower() != "fecha estimada para acabarse"):
            print("\nNo entendí su respuesta. Por favor ingresala de nuevo")
            respuesta = str(input())
       
        if(respuesta == "1" or respuesta.lower() == "caducidad"):
            alimento.caducidad = caducidad_del_alimento()
        
        elif(respuesta == "2" or respuesta.lower() == "fecha estimada para acabarse"):
            alimento.fecha_estimada_a_acabarse = fecha_estimada_a_acabarse()

def borrar_alimento(lista):
    alimento = str(input("\n¿Qué alimento desea borrar?: ")).capitalize()
   
    acum = 0
    for item in lista:
        if alimento == item.nombre:
            acum = acum + 1
            alimento = item
   
    if(acum <= 0): print("\nEl alimento no se encuentra en la lista")
    
    else:
        respuesta = str(input("\n¿Está seguro que desea borrar este alimento y su información?\nEsta acción no se podrá revertir\n"))
       
        while(respuesta.lower() != "si" and respuesta.lower() != "sí" and respuesta.lower() != "no"):
            print("\nNo entendí tu respuesta. Por favor ingresala de nuevo")
            respuesta = str(input())
       
        if(respuesta.lower() == "si" or respuesta.lower() == "sí"):
            lista.remove(alimento)
            del alimento
            print("\nEl alimento y su información han sido eliminados exitosamente")
            mostrar_alimentos(lista)

def salir_app():
    print("\nHa salido de la app. \nVuelva pronto!!!\n")

def desea_continuar():
    respuesta = str(input("\n¿Desea hacer algo más?: "))
    
    while(respuesta.lower() != "si" and respuesta.lower() != "sí" and respuesta.lower() != "no"):
        print("\nNo entendí tu respuesta. Por favor ingresala de nuevo")
        respuesta = str(input())
    
    if(respuesta.lower() == "si" or respuesta.lower() == "sí"):
        opciones()
    else:
        salir_app()

def opciones(lista):
    print("\n¿Qué desea hacer ahora?")
    print("Nota: Puede ingresar solo el número de la opción\n")
    print("1. Añadir un alimento")
    print("2. Mostrar los alimentos actuales")
    print("3. Buscar un alimento específico junto con su información")
    print("4. Editar la información de algún alimento")
    print("5. Borrar un alimento junto con su información")
    print("6. Salir de la app\n")
    respuesta = str(input())
    
    while(respuesta != "1" and respuesta != "2" and respuesta != "3" and respuesta != "4" and respuesta != "5" and respuesta != "6"\
        and respuesta.lower() != "añadir un alimento" and respuesta.lower() != "mostrar los alimentos actuales"\
        and respuesta.lower() != "buscar un alimento específico junto con su información"\
        and respuesta.lower() != "editar la información de algún alimento"\
        and respuesta.lower() != "borrar un alimento junto con su información" and respuesta.lower() != "salir de la app"):
        print("\nNo entendí su respuesta. Por favor ingresala de nuevo")
        respuesta = str(input())

    if(respuesta == "1" or respuesta.lower() == "añadir un alimento"):
        crearAlimento()
        desea_continuar()
    elif(respuesta == "2" or respuesta.lower() == "mostrar los alimentos actuales"):
        mostrar_alimentos(lista)
        desea_continuar()
    elif(respuesta == "3" or respuesta.lower() == "buscar un alimento específico junto con su información"):
        buscar_alimento(lista)
        desea_continuar()
    elif(respuesta == "4" or respuesta.lower() == "editar la información de algún alimento"):
        editar_info_alimento(lista)
        desea_continuar()
    elif(respuesta == "5" or respuesta.lower() == "borrar un alimento junto con su información"):
        borrar_alimento(lista)
        desea_continuar()
    elif(respuesta == "6" or respuesta.lower() == "salir de la app"):
        salir_app()
