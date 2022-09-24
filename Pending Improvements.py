class Alimento:
    def __init__(self,nombre,caducidad,fecha_estimada):
        self.nombre = str(nombre)
        self.caducidad = str(caducidad)
        self.fecha_estimada_a_acabarse = str(fecha_estimada)
    
    def __str__(self):
        return f"\nAlimento: {self.nombre.capitalize()}\nCaducará el {self.caducidad}\nSe acabará aproximadamente el { self.fecha_estimada_a_acabarse}"

def caducidad_del_alimento():
    año = input("Introduce el año de caducidad: ")
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
        
        
    mes = input("\nIntroduce el mes de caducidad: ")
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
    año = input("Introduce el año cuando consideras que podría acabarse: ")
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
        
        
    mes = input("\nIntroduce el mes cuando consideras que podría acabarse: ")
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


def crearAlimento():
    nombre_del_alimento = str(input("Ingresa el alimento a listar: "))
    nombre_del_alimento = nombre_del_alimento.lower()

    caducidad = caducidad_del_alimento()

    fecha_estimada = fecha_estimada_a_acabarse()

    nombre_del_alimento = Alimento(nombre_del_alimento,caducidad,fecha_estimada)
    print(nombre_del_alimento)
    


crearAlimento()
