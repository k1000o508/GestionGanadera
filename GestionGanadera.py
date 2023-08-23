
import sqlite3
# import mysql.connector

# Gestion Ganadera Olivia Orozco / Camilo Sanchez

# Diccionarios con los tipo de valores de cada tabla

#Hace una comparacion con la MainTable
ListaDiccitionaries = ["Animales","Campo","Potrero","Parcela","Seguimiento"]

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

conector = sqlite3.connect("GestionGanadera.db")


def val_range(maxim,minin):
   while True:
        x = int(input(" ▶ "))

        if x >= maxim and x <= minin:            
            return x
        else:
            print("Su valor tiene que estar entre",minin ,"y",maxim ,sep = " ")


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
def SelectTable():
    cursor = conector.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = cursor.fetchall()

    print('Que campo quiere cargar?')

    for i in range(len(tables)):
        print(i+1,tables[i])

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
        print('Campos de la tabla',cursor.fetchall())
        datos = []
        for i in nombres:
            if "ID" in i[0]:
                pass
            else:
                datos.append(input("Ingrese el campo " + i[0] + ' > '))
                
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
        for row in rows:
            print(row[0])

    def ReadColumn(self):
       
        #Arreglar Error del fetchall()
        c = conector.cursor()
        c.execute("SELECT * FROM " + self.table + "")
        rows = c.fetchall()
        for row in rows:
            print(row[0])


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
        c = conector.cursor()
        c.execute("DELETE FROM "+ self.table +"")
        conector.commit()

        print("Tabla {} eliminada".format(self.table))


        c.close()




# Animal
# Campo 
# Potrero
# Parcela
# Seguimiento

#CRUD de todas las tablas
#______________________________________________________



#Esto tiene que ser mas amigable para el usuario
Option = numeric(input("""Menu de opciones:
    01_Create
    02_Read
    03_Update
    04_Delete

    > """),1,4) 

#Create
#______________________________________________________


if "1" in Option:

    MainTable = SelectTable()

    #Esta variable solo guarda la instancia, (No hay necesidad de que sea un diccionario)
    # Instance = {}

    print('Main table',MainTable)

    Instance = ChargeState(MainTable)

    Instance.InputData()

#Como crear una funcion en la clase que pida propiedades de unicamente la funcion independientemente del constructor

#Read
#______________________________________________________


if "2" in Option:

    MainTable = SelectTable()


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


#Buscar como encontrar el nombre de todas los campos de la DDBB
if "3" in Option:
    
    MainTable = SelectTable()

    #Extraemos los datos necesarios de la base de datos para poder realizar la actualizacion
    cursor = conector.cursor()
    a = cursor.execute("PRAGMA table_info('"+ MainTable +"')").fetchall()
    cursor.close()

    for indice in a:

        print(indice)

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
    MainTable = SelectTable()

    print("""1_Eliminar Tabla completa \n2_Eliminar registro por ID""")
    
    OptionDelete = val_range(1,2)
    
    if OptionDelete == 1:
        Instance01 = DeleteState(MainTable)
        Instance01.DeleteTable() 

    if OptionDelete == 2:
        Instance02 = DeleteState(MainTable)
        Instance03 = ReadState(MainTable)
        Instance03.ReadAll()

        

        # .Instance02.

# Realizar un listado de animales.
#______________________________________________________

# cursor = conector.cursor()
# cursor.execute("SELECT * FROM Animales")
# rows = cursor.fetchall()
# for row in rows:
#     print(row)

# Realizar un listado de bajas.
#______________________________________________________

# class Deleted():
#     def __init__(self):
#         pass

# Realizar un listado de animales por parcela
#______________________________________________________

#Voy a realizar un buscador a partir del id de los animales

# Realizar un listado de animales por categoría
#______________________________________________________

#Buscar como hacer consultas como BBDD para poder hacerlo de sqlite3

# Realizar un listado de campos por propietario
#______________________________________________________



# Conocer la ubicación de cada animal.
#______________________________________________________

# A partir del id

# Calcular cuántos animales entran por parcela.
#______________________________________________________

# Atencion: No esta definido la capacidad de la parcelas pero el codigo va a suponer que estan perfectamente divididad para calcular en base a la capacidad del campo completo 

