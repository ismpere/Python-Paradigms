#Ismael Perez Martin
#Victor Rojo Alvarez

import random
Filas = 10      #Filas que mostrara el tablero en el que jugaremos
Columnas = 10   #Columnas que mostrara el tablero en el que jugaremos
matriz = []     #Inicializamos el tablero como una lista    
#Inicializamos una tupla en la que guardamos las letras del abecedario, las cuales apareceran en el marco del tablero
letras = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
#Inicializamos un diccionario en el que asociamos a cada letra con su numero para efectuar los golpes
diccionario = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
golpes=[]       #Inicializamos la lista en la que guardaremos todos los golpes realizados por el usuario
intentos = 0
resuelto=False
puntuaciones= []    #Lista donde almacenamos las puntuaciones tras copiarlas del fichero
cte=(10**15)    #Numero que empleamos para escribir y leer los datos del fichero
try:
    puntos = open("puntuaciones.txt", "r")      #Intentamos acceder al archivo en modo lectura para comprobar su existencia
    puntuaciones=puntos.readlines()             #Guarda todo el contenido del archivo en la lista puntuaciones
    for i in range(len(puntuaciones)):          #Quitamos los elementos que no necestiamos, como el salto de linea
        aux=puntuaciones[i]
        aux=aux[0:]
        aux=aux[:len(aux)-1]
        puntuaciones[i]=(aux)    
except(IOError):
    puntos = open("puntuaciones.txt","w")       #Si el archivo no existe, el archivo se crea y se abre en modo escritura
finally:
    puntos.close()                              #Cierra el archivo

#Este metodo crea la matriz con el marco correspondiente para jugar    
def GeneraMatriz(Filas,Columnas):
    for i in range(Filas+4):        #Suma 4 a la constante Filas ya que crea un marco de dos huecos a cada lado para efectuar los golpes
        matriz.append([])           #Anade huecos vacios en cada fila del tablero (matriz)
        for j in range(Columnas+4): #Sumam 3 por la misma razon que lo hacia con la constante Filas
            matriz[i].append(None)  #Anade huecos vacios al igual que antes pero ahora en las columnas de cada fila
            matriz[i][j]="."        #Por ultimo, rellena todos los elementos de la matriz con puntos

#Mediante este metodo imprimime la parte que nos interesa de la matriz como usuarios, el "tablero real" en el que el usuario cree que juega
def ImprimeMatriz(Filas,Columnas):
    print(" "),
    for a in range (Columnas):
        print a,                    #Imprime el numero de columna elegido
    print
    for i in range(Filas):
        print letras[i],            #Imprime la letra corrispondiente a cada fila mediante la tupla letras
        for j in range(Columnas):
            print matriz[i+2][j+2], #Suma dos a cada variable para que imprima la parte central del tablero, la que nos interesa, despreciando los bordes
        print

#Este metodo realiza el golpe al "tablero"
def Golpe(Filas,Columnas):
    FilasG=Filas+2
    ColumnasG=Columnas+2
    for i in range (1,4):                               #Mediante el for recorre solo el numero de casillas que tiene que golpear en la fila superior del golpe
        if (matriz[FilasG-2][(ColumnasG-2)+i] == "."):  #mediante el if comprueba que hay en ese punto del tablero, y lo cambia por el termino contrario con los que jugamos(punto y cruz)
            matriz[FilasG-2][(ColumnasG-2)+i] = "x"     #Resta dos a la fila ya que el golpe empieza desde dos filas por debajo al punto seleccionado hasta dos filas por encima de dicho punto
        else:
            matriz[FilasG-2][(ColumnasG-2)+i] = "."
    for j in range (5):                                 #Repite el mismo proceso que antes hasta llegar a la quinta y ultima fila en la que se ejecuta el golpe
        if (matriz[FilasG-1][(ColumnasG-2)+j]=="."):    #Vuelve a repetir el mismo proceso hasta ejecutar las 5 filas
            matriz[FilasG-1][(ColumnasG-2)+j] = "x"
        else:
            matriz[FilasG-1][(ColumnasG-2)+j] = "."
    for k in range (5):
        if (matriz[FilasG][(ColumnasG-2)+k]=="."):
            matriz[FilasG][(ColumnasG-2)+k] = "x"
        else:
            matriz[FilasG][(ColumnasG-2)+k] = "."
    for l in range (5):
        if (matriz[FilasG+1][(ColumnasG-2)+l]=="."):
            matriz[FilasG+1][(ColumnasG-2)+l] = "x"
        else:
            matriz[FilasG+1][(ColumnasG-2)+l] = "."
    for o in range (1,4):
        if (matriz[FilasG+2][(ColumnasG-2)+o] == "."):
            matriz[FilasG+2][(ColumnasG-2)+o] = "x"
        else:
            matriz[FilasG+2][(ColumnasG-2)+o] = "."

#Con Golpeinicial ejecutamos tantos golpes aleatorios como nivel halla introducido el usuario, ejecutados en la zona visible del "tablero"
def GolpeInicial(Filas,Columnas,nivel):
    for i in range(nivel):
        FilasGo = (random.randrange(Filas))
        ColumnasGo = (random.randrange(Columnas))
        Golpe(FilasGo,ColumnasGo)                   #Una vez creados los parametros del golpe aleatoriamente este los ejecuta llamando al metodo Golpe con dichos parametros
                                                    #hasta terminar el for introducido en nivel
                                                    
#Resuelto nos devuelve mediante un valor booleano si el "tablero" esta completamente relleno de puntos, sin ninguna cruz
def Resuelto(Filas,Columnas):
    resuelto = True                 #En principio el "tablero" esta resuelto, a menos que en el for encuentre alguna cruz
    for i in range(Filas+2):
        for j in range(Columnas+2):
            if (matriz[i][j]=="x"):
                resuelto=False      #si encuentra una cruz mediante el if pone el valor booleano a False, por lo que el metodo devolvera dicho valor
    return resuelto                 #Retorna el valor obtenido

#este metodo se encarga de deshacer el ultimo golpe ejecutado, guardado en la lista golpes
def Deshacer():
    try:
        Dato = golpes.pop()         #Intenta eliminar el ultimo golpe de la lista
    except (IndexError):            #Si no hay ningun golpe, informa de ello y vuelve a imprimir la matriz
        print("No ha realizado ningun golpe, por lo que no puede deshacer ningun movimiento.")
        ImprimeMatriz(Filas,Columnas)
    else:
        FilaD=Dato[0]               #Si la lista no estaba vacia, ejecuta el ultimo golpe en la misma coordenada para deshacer sus efectos en el "tablero"
        ColumnaD=Dato[1]
        Golpe(diccionario[FilaD],int(ColumnaD))
        ImprimeMatriz(Filas,Columnas)           
        print("Ha deshecho su ultimo golpe")                             
 
#Mediante el control por variables booleanas controlamos el flujo de ejecucion, para terminar el juego cuando el comando salir lo ordene o el tablero este resuelto
validacion=False    #Ponemos el valor booleano a False para que cuando el nivel este bien introducido, se ponga a True
while(validacion==False):
    try:
        print ("Introduzca el nivel porfavor")
        nivel = input()     #Obtiene el nivel deseado por el jugador y lo almacenamos en la variablel nivel
        while (nivel<1):
            print("El nivel debe ser mayor que 0")
            nivel = input()
    except(NameError, SyntaxError):                     #Si el nivel no es un dato correcto, la validacon sigue a False y nos informa de ello, por lo que el bucle va a seguir ejecutandose   
        print ("El dato introducido no es un numero")   #hasta que el dato sea correcto
        validacion=False
    else:
        validacion=True                     #Cuando accedemos a else ya que el nivel es un dato correcto, ponemos a True el booleano para no ejecutar mas veces el bucle
        GeneraMatriz(Filas,Columnas)        #Generamos la matriz y con GolpeInicial ejecuta los golpes asociados al nivel introducido por el usuario
        GolpeInicial(Filas,Columnas,nivel)           
        
#Informa al usuario de todos los datos necesarios para jugar        
print("Introduzca la palabra <salir> si quiere terminar el juego.")
print("Introduzca la palabra <deshacer> para volver un golpe atras.")
print("El juego estara completado cuando todas las casillas del tablero contengan puntos (.)")
print("(Debe tener en cuenta que solo se puede rehacer cuando ha realizado algun golpe)")
print("Si el golpe contiene una columna de dos cifras (mayor que las que tiene el tablero)")
print("se ejecutara el golpe solo con el primer digito de la columna introducida (A55 se ejecutaria como A5)")

#Imprimimos la matriz, el "tablero" donde jugara el usuario
ImprimeMatriz(Filas,Columnas)
#Con el mismo algumento que antes, mediante valores booleanos controlamos el fujo de ejecucion
while(resuelto==False):
    validacion=False
    while(validacion==False):
        print("Intoduzca la fila y la columna a golpear (En formato LetraNumero: G4, H9...): ")
        Dato=raw_input()
        if(Dato == "deshacer"): #Si el usuario introduce "deshacer", el programa deshace su ultimo golpe con el metodo Deshacer
            Deshacer()
            validacion=True
        elif(Dato == "salir"):  #Si e usuario introduce "salir", se ponen a True todos lo booleanos para terminar la ejecucion del programa
            print("Ha decidido salir del juego")
            print("Adios!")
            validacion=True
            resuelto=True
        else:
            try:
                golpes.append(Dato)     #Almacenamos el comando en la lista de golpes y se ejecuta un golpe con dicho comando
                Fila=Dato[0]
                Columna=Dato[1]        
                Golpe(diccionario[Fila],int(Columna))
            except(KeyError,IndexError,ValueError): #Si el dato no ha sido un golpe valido, se informa al usuario y mediante el valor False se vuelve a ejecutar el bucle
                print("El dato introducido no es un golpe valido ni uno de los comandos permitidos.")
                golpes.pop()    #El programa elimina el ultimo golpe de la lista por no ser valido
            else:
                intentos=intentos+1 #Cada vez que se introduce un golpe valido, el contador intentos se incrementa una unidad, sin disminuir al deshacer
                validacion=True
                if(Resuelto(Filas, Columnas)==False):   #Mediante resuelto, sabemos si el tablero esta completo a puntos
                    ImprimeMatriz(Filas,Columnas)
                    print("Numero de golpes: "),        #Imprime la puntuacion actual (numero de golpes)
                    print(intentos)
                else:
                    print("Juego Completado!")          #Si se completa el nivel avisamos al usuario y le damos su puntuacion
                    print("Su puntuacion ha sido (Numero de golpes ejecutados): "),
                    print(intentos),
                    print(" Puntos")
                    resuelto=True  
                    encontrado=False
                    for d in range(len(puntuaciones)):  #buscamos en las puntuaciones que habiamos leido si existe una puntuafcion anterior para el nivel jugado
                        aux=int(puntuaciones[d])
                        if(nivel==(aux//cte)):
                            encontrado=True
                            if(intentos<(aux-(nivel*cte))):  #Si la encuentra, la compara y la sustituye ne caspo de ser un nuevo record
                                print("Has establecido un nuevo record!")
                                puntuaciones[d]=(nivel*(cte)+intentos)
                    if(encontrado==False):
                        print("Has establecido un nuevo record!")   #Si no la encuentra la almacena en la lista de las puntuaciones
                        puntuaciones.append(nivel*(cte)+intentos)
fichero= open("puntuaciones.txt","w")   #Abrimos el fichero en modo escritura
for c in range(len(puntuaciones)):      #Por cada elemento en la lista lo escribimos en una linea
    aux=puntuaciones[c]
    fichero.write(str(aux)+"\n")
fichero.close()         #Cerramos el fichero y finaliza el programa