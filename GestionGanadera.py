#_____________________________________________________________________Librerias_____________________________________________________________________

#Maneja las pausas de tiempo
import time as t

#Maneja fechas y horas 
from datetime import *

#Maneja la BDD
import sqlite3

#Crear tablas agradables visualmente 
import tabulate 

#Limpiar la consola
import os as os

#libreria para crear barra de carga (puramente estetico)
import tqdm

#Salida de hiperTexto con arte ASCII code
import pyfiglet

#_____________________________________________________________________Librerias_____________________________________________________________________


#Estilos disponibles
# * **simple:** Este es el estilo de tabla por defecto. Las celdas están alineadas a la izquierda y no hay líneas de cuadrícula.
# * **grid:** Este estilo de tabla añade líneas de cuadrícula a la tabla.
# * **fancy_grid:** Este estilo de tabla añade líneas de cuadrícula y un borde a la tabla.
# * **pipe:** Este estilo de tabla utiliza el carácter de tubería (|) para separar las celdas.
# * **orgtbl:** Este estilo de tabla utiliza la sintaxis de Org-mode para crear tablas.
# * **rst:** Este estilo de tabla utiliza la sintaxis de reStructuredText para crear tablas.
# * **mediawiki:** Este estilo de tabla utiliza la sintaxis de MediaWiki para crear tablas.
# * **html:** Este estilo de tabla utiliza la sintaxis HTML para crear tablas.
# * **latex:** Este estilo de tabla utiliza la sintaxis LaTeX para crear tablas.

#Tipo de estilo de los outputs (Se puede cambiar por el estilo deseado)
fontStyle = "fancy_gr"

#_____________________________________________________________________Simulacion de carga_____________________________________________________________________

# Create an instance of the tqdm.tqdm class.
pbar = tqdm.tqdm(range(0,100,5))

# Iterate over the list of elements.
for i in pbar:
    
    #limpiamos la terminal
    os.system('cls')
    
    # Actualizacion de la barra de progreso.
    pbar.update()

    # Escribimos el estado del bucle
    pbar.write(f"{i}")

    t.sleep(0.15)

os.system('cls')

# Close the progress bar.
pbar.close()

#Nombre del programa con la ayuda de pyfiglet
text = pyfiglet.print_figlet(text="Gestion Ganadera",
                             colors="WHITE",
                             font="roman")

t.sleep(5)

os.system("cls")
#_____________________________________________________________________Simulacion de carga_____________________________________________________________________


# Diccionarios con los tipo de valores de cada tabla

Animales = {'FhaterCowId': 'Number',
'MotherCowId': 'Number',
'BornDate': 'Date',
'Genere':  'Text',
'Category':  'Text',
'SubCategoty':  'Text',
'BornWeight': 'Number',
'LowedCow': 'Date',
'LowedCause':  'Text',
'MensGain' : 'Number'}

Campo = {
    'HighCamp' : 'Date',
    'TipeCamp' : 'Text',
    'Hect' : 'Number',
    'NameCamp' : 'Text',
    'OwnweCampo' : 'Text'
}

Potrero = {
    'Measure' : 'Number',
    'GrassVol' : 'Number',
    'GrassVolImpl' : 'Number',
    'AnimWeight' : 'Number',
    'CampID' : 'Number',
}

Parcela = {
    'PotreroID' : 'Number',
    'Descripcion': 'Text'
}

Seguimiento = {
    'Animal': 'Number',
    'BornState': 'Number'
}


DictDiccitionaries = {"Animales":Animales,
                       "Campo":Campo,
                       "Potrero":Potrero,
                       "Parcela":Parcela,
                       "Seguimiento":Seguimiento}


conector = sqlite3.connect("GestionGanadera.db")

def val_range(maxim,minin):
    while True:
        x = str(input(" ▶ "))

        print(x)
        print(x <= str(maxim) and x >= str(minin))

        if int(x) <= int(maxim) and int(x) >= int(minin):
            return str(x)
        else:
            print("Su valor tiene que estar entre",minin ,"y",maxim ,sep = " ")


def ValidacionFecha():
       
    while True:
        # try:
            print("Ingresa una fecha en el formato MM(mes): ")
            #Arreglar val_range 
            fechaM = val_range(12,1)
            datetime.strptime(str(fechaM),'%m')
            print("Fecha válida")
            break
        # except ValueError:
            # print("Fecha inválida")

    while True:
        try:
            fechaD = input("Ingresa una fecha en el formato DD(dia): ")
            datetime.strptime(str(fechaD),'%d')
            print("Fecha válida")
            break
        except ValueError:
            print("Fecha inválida")
    while True:
        try:
            #fecha = input("Ingresa una fecha en el formato YYYY-MM-DD: ")
            print("Ingresa una fecha en el formato YYYY(año): ")
            fechaY = val_range(2022,1900)
            #datetime.strptime(fecha, '%Y-%m-%d')
            datetime.strptime(str(fechaY), '%Y')
            print("Fecha válida")
            break
        except ValueError:
            print("Fecha inválida")

    fecha = str(fechaY) + "-" + str(fechaM) + "-" + str(fechaD)
    # RevfechaY = str(reversed(fechaY))
    # RevfechaM = str(reversed(fechaM))
    # RevfechaD = str(reversed(fechaD))
    # fecha_val = "-".join([RevfechaY,RevfechaM,RevfechaD])
    # fecha_hoy = str(reversed(str(datetime.strptime(fechaY, '%Y'))))+ str(reversed(str(datetime.strptime(fechaM,'%m')))) + str(reversed(str(datetime.strptime(fechaD,'%d'))))
    # print(fecha_val +"\n" + fecha_hoy)

    print(fecha)
    return fecha



#Validacion de datos(Agregar rangos de numeros y largo de los valores)

#Esta definicion busca retornar valores validados un 100%
def numeric(Numeric_string,Long_of_String,Max_number):
    c = 0
    #El while true se encarga de forzar un valor apto para el codigo
    while True:

        #Esto mantiene la solides del codigo verifica que Numeric_string sea tipo int para que isdigit acepte la condicion
        if Numeric_string.isdigit() and len(Numeric_string) <= 3 and int(Numeric_string) >= 1 and int(Numeric_string) <= int(Max_number):
            print(Numeric_string.isdigit())
            return Numeric_string #El return frena el while True
        else:
            if c == 0:
                Numeric_string = input("Ingrese una opcion valida > ")

            if c == 1 and len(Numeric_string) >= 2:
                Numeric_string = input("Ingrese una opcion valida de {} cifras > ".format(Long_of_String))

            if c == 1:
                Numeric_string = input("Ingrese una opcion valida  entre {} y {} > ".format(1,Max_number))

            if c > 1 and c <= 3:
                Numeric_string = input("Ingrese una opcion valida de {} cifras entre {} y {} > ".format(Long_of_String,1,Max_number))

            if c > 3:
                Numeric_string = input("!!BUSQUE AYUDA!!> ")


        #Manera de ayudar al usuario , mientras mas se equivoca mas va a ayudarlo para poder cargar los datos necesarios
        c += 1

def string(CadenaTexto):

    while True:
        Bucle = False

        #Navego por cada caracter del texto buscando un numero para validar una cadena pura
        for caracteres in CadenaTexto:
            if caracteres.isdigit():
                Bucle = True
        #Si el bucle es falso significa que nunca encontro un digito en la cadena de texto
        if Bucle == False:
            return CadenaTexto

        #Si el bucle es verdadero (Else ya que solo se pueden tomar 2 valores en un booleano) se vuelve a pedir una cadena de texto
        else:
            CadenaTexto = input('Tiene que ingresar un texto sin numeros  > ')


#Seleccionamos y reconocemos las tablas que se creron
def SelectTable(Mensage):
    cursor = conector.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence';")

    tables = cursor.fetchall()

    print(Mensage)

    #Diccionario para el tabulate
    TemplateList = []

    for i in range(len(tables)):
        TemplateList.append([i+1,tables[i][0]])

    tabu = tabulate.tabulate(TemplateList,headers=["Opcion","Registros"],numalign="center")

    print(tabu)

    Option = numeric(input("Ingrese una opcion(un numero) > "),1,len(tables))

    MainTable = tables[int(Option)-1][0]

    return MainTable


#Creamos todas las tablas en el dispositivo del usuario
conector.execute("""CREATE TABLE IF NOT EXISTS Animales(ID INTEGER PRIMARY KEY AUTOINCREMENT,
FhaterCowId NUMBER(3) NULL,
MotherCowId NUMBER(3) NOT NULL,
BornDate DATE NOT NULL,
Genere VARCHAR(1) NOT NULL,
Category NOT NULL,
SubCategoty NOT NULL,
BornWeight NOT NULL,
LowedCow DATE NULL,
LowedCause VARCHAR(100) NULL,
MensGain NOT NULL
)""")

# Componer IDS de campo/parcela/animal
conector.execute("""CREATE TABLE IF NOT EXISTS Campo (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    HighCamp DATE,
    TipeCamp VARCHAR2(6),
    Hect NUMBER(3),
    NameCamp VARCHAR2(10),
    OwnerCamp VARCHAR2(10)
)""")

conector.execute("""CREATE TABLE IF NOT EXISTS Potrero(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Measure NUMBER(10),
    GrassVol NUMBER(3),
    GrassVolImpl NUMBER(3),
    AnimWeight NUMBER(3),
    CampID NUMBER(3)
)""")

conector.execute("""CREATE TABLE IF NOT EXISTS Parcela (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProteroID NUMBER(3),
    Descrip VARCHAR(90)
)""")

conector.execute("""CREATE TABLE IF NOT EXISTS Seguimiento (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    FollowDate DATE,
    AnimalID NUMBER(3),
    BornState NUMBER(1)
)""")

#Tablas
#  Animales
#  Campo
#  Potrero
#  Parcela
#  Seguimiento

# Los animales se dividen en categorias como:

    #  Terneros machos (hasta los 12 meses)
    #  Toros
    #  Vaquillonas 1 año
    #  Vaquillonas 2 años (hasta los 18 meses, que pasan a ser vacas vientre)
    #  Vacas vientres: (Tienen un ternero al año)

    # - Primera parición
    # - Segunda parición
    # - Vacas plantel
    # - Vacas CUT (Ultimo ternero)
    # - Vacas descarte

# CRUD de cada tabla

# cursor = conector.cursor()
# cursor.execute("SELECT name FROM pragma_table_info('Animales')")
# nombres = cursor.fetchall()
# for campor in nombres:
#     print(campor)


#Validar Cada variable y todo los campos que contengas ID( 'ID' in campo )
#Cargar los datos a BBDD
class ChargeState():
    def __init__(self,table):
        global nombres
        self.table = table

    def InputData(self):
        cursor = conector.cursor()
        cursor.execute("SELECT name FROM pragma_table_info('"+ self.table +"')")
        nombres = cursor.fetchall()
        datos = []


        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]
        # if self.table in DictDiccitionaries:

        for i in nombres:
            # if "ID" in i[0].upper():
            #     c = conn.cursor()
            #     c.execute("SELECT * FROM table WHERE column='value'")
            #     rows = c.fetchall()
            #     for row in rows:
            #         print(row)

            if "ID" == i[0].upper():
                pass
            else:
                if TemplateVerification[i[0]] == "Number":
                    datos.append(numeric(input("Ingrese el campo " + i[0] + ' > '),2,70))
                
                elif TemplateVerification[i[0]] == "Date":
                    print("Ingrese el campo " + i[0])
                    datos.append(ValidacionFecha())
                
                elif TemplateVerification[i[0]] == "Text":
                    datos.append(string(input("Ingrese el campo " + i[0] + ' > ')))


        cursor = conector.cursor()

        # Adaptacion para sqlite (?,?,?,?,?)

        # ATENCION: NO EJECUTAR SIN VALIDAR LOS DATOS ANTERIORMENTE
        print((len(datos)/2)-1)

        print(len(datos))

        print(datos)

        ValuesInputs = "?,"*((len(datos)))

        # Sacamos la coma de mas (?,?,?,?,?,) <<<
        ValuesInputs = ValuesInputs[:-1]

        print("Value Inputs :",ValuesInputs)

        cursor.executemany("INSERT INTO "+ self.table +" VALUES (null," + ValuesInputs + ")",[datos,])
        conector.commit()

class ReadState():

    def __init__(self,table):
        self.table = table

    def ReadAll(self):
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        #Tabulate formate table 
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)

    def ReadColumn(self):
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()

        #Coincidencias en el diccionario para poder identicar los valores
        TemplateVerification = {}

        for i in DictDiccitionaries:
            if i == self.table:
                TemplateVerification = DictDiccitionaries[i]

        IdOption = numeric(input("Registro especifico(ID) : "),1,len(rows))

        #Arreglar Error del fetchall()
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + " WHERE ID = '"+ IdOption +"'")
        rows = c.fetchall()
        tabu = tabulate.tabulate(rows,headers=TemplateVerification.keys(),tablefmt=fontStyle,numalign="center",stralign="center")
        print(tabu)

        #Arreglar Error del fetchall()
        # c = conector.cursor()
        # c.execute("SELECT * FROM " + self.table + " WHERE " + self.column + "= " + self.campo)
        # rows = c.fetchall()
        # for row in rows:
        #     print(row)

        # c.close()


class UpdateState():
    # def __init__(self,table,column,modify,columnId,id):
    #     self.table = table
    #     self.column = column
    #     self.id = id
    #     self.columnId = columnId
    #     self.modify = modify

    def __init__(self,table):
        self.table = table

    def UpdateTable(self,column,modify,id):
        self.column = column #Columna que sera modificada
        self.id = id #Id unico de cada instancia
        self.modify = modify #Dato guardado en una instancia anterior que sera modificada

        c = conector.cursor()
        c.execute("UPDATE " + self.table + " SET " + self.column + "='" + self.modify + "' WHERE ID ='" + self.id + "'")
        c.commit()

        c.close()

class DeleteState():
    def __init__(self,table):
        self.table = table

    def DeleteTableColumn(self,id):
        self.id = id
        c = conector.cursor()
        c.execute("DELETE FROM "+ self.table +" WHERE ID ='"+self.id+"'")
        c.commit()

        c.close()

    #Inhabilitado para el usuario comun
    def DeleteTable(self):
        print("[Eliminando Tabla]")
        c = conector.cursor()
        c.execute("DELETE FROM "+ self.table +"")
        conector.commit()

        print("Tabla {} eliminada".format(self.table))


        c.close()

#Crear ordenes Sql en vez de una clase 
class DeleteSqlite():
    def __init__(self,table):
        self.table = table 

    def CloneTables(self):
        #Conectamos y creamos la base de datps eliminada
        conector_deleted = sqlite3.connect("GestionGanaderaDelete.db")
        cursor_deleted = conector_deleted.cursor()
        cursor_original = conector.cursor()

        #Obtenemos la estructura de la tabla
        cursor_original.execute("SELECT * FROM sqlite_master WHERE type='table' AND name = '{}'".format(self.table))
        TableStucture = cursor_original.fetchone()[0]
        print(TableStucture)

        #Creamos la tabla en la base de datos
            
        #cursor_deleted.execute(TableStucture)
        #conector_deleted.commit()

# Instance = DeleteSqlite('Animales')
# Instance.CloneTables()


# Puntos a resolver :

#CRUD de todas las tablas LISTO
#______________________________________________________

OptionList = [[1,"Cargar Datos"],[2,"Consultar Información"],[3,"Actualizar Datos"],[4,"Eliminar Datos"]]

#Esto tiene que ser mas amigable para el usuario

tabu = tabulate.tabulate(OptionList,headers=["Opcion","Control de Datos"],numalign="center")

print(tabu)

Option = numeric(input("\n > "),1,4)

os.system('cls')

#Create
#______________________________________________________


if "1" in Option:

    MainTable = SelectTable("Que datos desearia cargar?")

    os.system('cls')

    #Esta variable solo guarda la instancia, (No hay necesidad de que sea un diccionario)
    # Instance = {}

    Instance = ChargeState(MainTable)

    Instance.InputData()

#Como crear una funcion en la clase que pida propiedades de unicamente la funcion independientemente del constructor

#Read
#______________________________________________________


if "2" in Option:

    MainTable = SelectTable("Que datos desearia consultar, elija su opcion")


    ReadOption = numeric(input("""Opciones:
        01_Toda la base de """ + MainTable + """
        02_Consulta especifica por columna
         > """),1,2)

    # Instance = ReadState

    if "1" in ReadOption:
        #Creamos una instancia para leer todos los campos de una tabla
        Instance = ReadState(MainTable)
        Instance.ReadAll()

    if "2" in ReadOption:

        Instance = ReadState(MainTable)
        Instance.ReadColumn()


#Renovar modificación
#Buscar como encontrar el nombre de todas los campos de la DDBB
if "3" in Option:

    MainTable = SelectTable("Que datos desearia modificar, elija su opcion?")

    #Extraemos los datos necesarios de la base de datos para poder realizar la actualizacion
    cursor = conector.cursor()
    a = cursor.execute("PRAGMA table_info('"+ MainTable +"')").fetchall()    
    cursor.close()

    
    #Coincidencias en el diccionario para poder identicar los valores
    # TemplateVerification = {}

    # for i in DictDiccitionaries:
    #     if i == MainTable:
    #         TemplateVerification = DictDiccitionaries[i]



    # tabu = list(tabulate.tabulate(a,headers=Headers))

    # print(tabu)

    Anser = string(input('Desea modificar la tabla? > '))

    ban = 0

    #Primero le preguntamos al usuario que parte de la tabla quiere modificar en el siguiente orden(1_Columna a modificar / 2_Modificacion / 3_Id unica)
    while True:


        if "Y" in Anser.upper():
            if ban == 1:
                Anser = string(input('Desea seguir modificando la tabla? > '))

            ban = 1
            #Lista para guardar las columnas
            Columns = []

            #Enumerate es una funcioin que tira dos valores por indice(Indice y Valor)
            for indice,row in enumerate(a):
                if not row[1] == 'ID':
                    print(indice,row[1])
                    Columns.append(row[1])
            print('')
            ModColumn = numeric(input("Que columna quiere modificar? > "),1,len(a)-1)

            #Buscamos los valores cargados en la base de datos, por ahora 0

            ReadInstance1 = ReadState(MainTable)
            print("[++]Instancia ")
            ReadInstance1.ReadAll()

            print("Estos son los indices que tiene disponibles : \n")

            for indice in a:
                print("ID ",indice[0])

            ModIndice = numeric(input("Que indice unico quiere modificar ? "),2,len(a)-1)

            #Esto es una variable auxiliar para poder mostrar informacion mas precisa al usuario final
            InfoIndice = ''

            for indices in a:
                if int(ModIndice) == int(indices[0]):
                    InfoIndice = indices[int(ModColumn)]
                    print(InfoIndice)
                    print(indices)

            Modify = string(input("Actualizacion de {}: ".format(InfoIndice)))

            UpdateInstance1 = UpdateState(MainTable)
            print("[++]Instancia ")
            UpdateInstance1.UpdateTable(ModColumn,Modify,ModIndice)


            cursor = conector.cursor()
            a = cursor.execute("PRAGMA table_info('"+ MainTable +"')").fetchall()

        if 'N' in Anser.upper():
            break



#Delete State Class
if "4" in Option:

    print("""1_Eliminar todos los datos \n2_Eliminar dato especifico""")

    OptionDelete = val_range(2,1)

    MainTable = SelectTable("Que dato quiere eliminar, elija su opcion?")

    if OptionDelete == 1:
        Instance01 = DeleteState(MainTable)
        Instance01.DeleteTable()

    if OptionDelete == 2:
        Instance02 = DeleteState(MainTable)
        Instance03 = ReadState(MainTable)
        Instance03.ReadAll()

        # .Instance02.

# Realizar un listado de animales. LISTO
#______________________________________________________

# Resuelto el el read de toda la tabla Animales

# Realizar un listado de bajas. CREAR CLASE DELETE
#______________________________________________________



# Realizar un listado de animales por parcela SISTEMA DE PARCELAS (ID PRINCIPAL)
#______________________________________________________


# Realizar un listado de animales por categoría SQLITE3 clasificacion por categoria / REALIZAR VALIDACION DE CATEGORIAS
#______________________________________________________

# Realizar un listado de campos por propietario
#______________________________________________________


# Conocer la ubicación de cada animal.
#______________________________________________________

# Calcular cuántos animales entran por parcela.
#______________________________________________________

# Atencion: No esta definido la capacidad de la parcelas pero el codigo va a suponer que estan perfectamente divididad para calcular en base a la capacidad del campo completo
