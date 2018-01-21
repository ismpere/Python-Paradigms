#Ismael Perez Martin
#Victor Rojo Alvarez

import math		#Importamos los pqeuetes necesarios para nuestro juego
import random
import pygtk
pygtk.require('2.0')	#Declaramos que la version de python utilizada sea la 2.0 para la compatibilidad
import gtk

class Juego:	#Definimos la clase Juego en la que se encontrara todo lo necesario para nuestra interfaz del juego y sus metodos

    def mostrarRecords(self, widget, data=None):	#Este metodo muestra una ventana con los record actuales del juego con su nivel
		ventanaRecords = gtk.Window()		#Definimos la ventana que albergara los record
		ventanaRecords.set_title("Records")
		ventanaRecords.set_size_request(400,260)
		if (len(self.puntuaciones) == 0):	#Si no hay ninguna puntuacion almacenada, muestra un mensaje de aviso
			aclaracion = gtk.Label("No hay ningun record almacenado en este momento")
			ventanaRecords.add(aclaracion)
			aclaracion.show()
		else:
			div1 = gtk.VBox(gtk.FALSE, 0)	#Creamos una caja horizontal que albergue las etiquetas nivel y puntuacion maxima en la caja principal
			div3 = gtk.HBox(gtk.FALSE, 0)
			etiqueta1 = gtk.Label("Nivel")
			div3.pack_start(etiqueta1, gtk.TRUE, gtk.TRUE, 0)
			etiqueta1.show()
			etiqueta2 = gtk.Label("Puntuacion maxima")
			div3.pack_start(etiqueta2, gtk.TRUE, gtk.TRUE, 0)
			etiqueta2.show()
			div1.pack_start(div3, gtk.TRUE, gtk.TRUE, 0)
			div3.show()							#Mostramos esta caja horizontal y comenzamos con los records
			for i in range(len(self.puntuaciones)):	#Recorremos la lista de puntuaciones para obtener los records
				dato = int(self.puntuaciones[i])	#Obtenemos cada nivel con su puntuacion junto y lo separamos con ayuda de la constante
				div2 = gtk.HBox(gtk.FALSE, 0)
				nivel = dato/self.cte
				puntitos =	dato%self.cte
				nivelazo = gtk.Label(" %s " % nivel)	#Insertamos el nivel y la puntuacion en una etiqueta, lo albergamos en una caja horizontal
				div2.pack_start(nivelazo, gtk.TRUE, gtk.TRUE, 0)	#y lo anadimos a la caja vertical principal, mostrandolo al final
				nivelazo.show()
				puntazos = gtk.Label(" %s " % puntitos)
				div2.pack_start(puntazos, gtk.TRUE, gtk.TRUE, 0)
				puntazos.show()
				div1.pack_start(div2, gtk.TRUE, gtk.TRUE, 0)
				div2.show()	#Mostramos la fila del nivel con su puntuacion
			ventanaRecords.add(div1)	#Al acabar de recorrer la lista anadimos la division pricipal a la ventana y lo mostramos todo
			div1.show()
		ventanaRecords.show()

    def actualizaPuntos (self):	#Este metodo actualiza la etiqueta de las puntuaciones cada vez que damos un golpe voluntario
	self.puntos = gtk.Label("Su puntuacion es:  %s puntos" % self.golpes) #para que el usuario sepa su puntuacion en todo momento
	self.puntuacion.attach(self.puntos, 0, 1, 0, 1)
	self.puntos.show()	#muestra la puntuacion
	

    def Iniciopuntuaciones(self):
		try:
			puntos = open("puntuaciones.txt", "r")      #Intentamos acceder al archivo en modo lectura para comprobar su existencia
   			self.puntuaciones=puntos.readlines()             #Guarda todo el contenido del archivo en la lista puntuaciones
    			for i1 in range(len(self.puntuaciones)):          #Quitamos los elementos que no necestiamos, como el salto de linea
        			aux=self.puntuaciones[i1]
        			aux=aux[0:]
        			aux=aux[:len(aux)-1]
        			self.puntuaciones[i1]=(aux)
		except(IOError):
   			puntos = open("puntuaciones.txt","w")       #Si el archivo no existe, el archivo se crea y se abre en modo escritura
		finally:
    			puntos.close()            

    def reiniciar (self, widget, data=None):	#Definimos el metodo reiniciar, el cual pondra el juego en sus valores iniciales
		if (self.acabado == True):				#y podremos volver a elejir el nivel en el que jugar
			self.ventanaFinal.hide()
		self.window.hide()
		self.golpes = 0
		self.golpesX = []
		self.golpesY = []
		for i in range((self.filas) + 4):
			for j in range((self.columnas) + 4):	#Volvemos a rellenar el tablero solo con eventos lannister para empezar de cero
				evento = gtk.EventBox()
				lannister = gtk.Image()
				lannister.set_from_file("house-lannister.jpg")
				evento.add(lannister)
				lannister.show()
				evento.estado = True				#redefinimos el estado de todos los eventos a True
				evento.x = j
				evento.y = i
				evento.set_events(gtk.gdk.BUTTON_PRESS_MASK)
				evento.connect("button_press_event", self.golpe)	#Conectamos de nuevo los manejadores a los nuevos eventos
				self.eventos[i][j]=evento
		self.metodoNivel()	#Iniciamos el selector de nivel e imprimimos nuestro tablero con sus controles
		self.imprimir()
	

    def finish(self, widget, data=None):	#Definimos un metodo finish el cual finaliza el proceso gtk.main() para cerrar el programa
	gtk.main_quit()

    def finalizar (self):				#Declaramos un metodo que servira para mostrar una ventana emergente al terminar el juego y asi elegir
	self.ventanaFinal = gtk.Window()	#si dar por terminado el juego o reiniciar nuestra partida
	self.ventanaFinal.connect("destroy", lambda w: gtk.main_quit())		#Al igual que en el metodo __init__ conectamos la ventana para que
	self.ventanaFinal.set_title("Hemos ganado la guerra a los stark!")	#al cerrarse termine el juego y establecemos campos como su titulo y anchura
       	self.ventanaFinal.set_size_request(400,260)
	divisioonV = gtk.VBox(gtk.FALSE, 0)		#creamos una estructura mediante una caja vertical que albergara un gif y los botones de reinicio
	if (self.record == True):				#y salir, junto a una etiqueta que mediante un mensaje nos informa de nuestras opciones
		espacio1 = gtk.Label(" ")
		divisioonV.pack_start(espacio1, gtk.TRUE, gtk.TRUE, 0)
		espacio1.show()
		reecord = gtk.Label("Has establecido un nuevo record!")
		divisioonV.pack_start(reecord, gtk.TRUE, gtk.TRUE, 0)
		reecord.show()
		espacio2 = gtk.Label(" ")
		divisioonV.pack_start(espacio2, gtk.TRUE, gtk.TRUE, 0)
		espacio2.show()
	starkG = gtk.Image()					
	starkG.set_from_file("tyrion.gif")
	divisioonV.pack_start(starkG, gtk.TRUE, gtk.TRUE, 0)
	starkG.show()
	anuncio = gtk.Label("Quieres terminar el juego o quieres comenzar una nueva guerra?")
	divisioonV.pack_start(anuncio, gtk.TRUE, gtk.TRUE, 0)
	anuncio.show()
	divisioonH = gtk.HBox(gtk.FALSE, 0)			#Albergamos los dos botones en una caja horizontal la cual estara incrustada en el final de nuestra 
	reiniciar2 = gtk.Button("Reiniciar Guerra")	#caja horizontal
	reiniciar2.connect("clicked", self.reiniciar)			#Conectamos cada boton con su manejador
	divisioonH.pack_start(reiniciar2, gtk.TRUE, gtk.TRUE, 0)
	reiniciar2.show()
	salir = gtk.Button("Salir")
	salir.connect("clicked", self.finish)
	divisioonH.pack_start(salir, gtk.TRUE, gtk.TRUE, 0)
	salir.show()
	divisioonV.pack_start(divisioonH, gtk.TRUE, gtk.TRUE, 0)
	divisioonH.show()	
	self.ventanaFinal.add(divisioonV)
	divisioonV.show()
	self.ventanaFinal.show()		#Tras haber ido mostrando los controles incrustados en la ventana en orden, mostramos la ventana de salida
	

    def resuelto (self):	#Definimos un metodo el cual comprobara si todas las casillas de nuestro tablero estan a True, en Lannister
	self.acabado = True
	for i in range (self.filas):	#Recorremos la matriz de eventos para comprobarlo
		for j in range (self.columnas):
			eventoR = self.eventos[i][j]
			if (eventoR.estado == False):
				self.acabado = False	#Si el tablero contiene algun Stark, pone a False la variable self.acabado para no ejecutar finalizar
	if (self.acabado == True):
		encontrado=False
                for d in range(len(self.puntuaciones)):  #buscamos en las puntuaciones que habiamos leido si existe una puntuafcion anterior para el nivel jugado
			aux=int(self.puntuaciones[d])
                        if(self.nivel==(aux//self.cte)):
				encontrado=True
                            	if(self.golpes<(aux-(self.nivel*self.cte))):  #Si la encuentra, la compara y la sustituye ne caspo de ser un nuevo record
                                	self.record = True
                                	self.puntuaciones[d]=(self.nivel*(self.cte)+self.golpes)
		if(encontrado==False):	#Si no la encuentra la almacena en la lista de las puntuaciones  
                        self.record = True
                        self.puntuaciones.append(self.nivel*(self.cte)+self.golpes)
		print(self.puntuaciones)
		fichero= open("puntuaciones.txt","w")   #Abrimos el fichero en modo escritura
		for c in range(len(self.puntuaciones)):      #Por cada elemento en la lista lo escribimos en una linea
    			aux=self.puntuaciones[c]
    			fichero.write(str(aux)+"\n")
		fichero.close()         #Cerramos el fichero y finaliza el programa
		self.finalizar()	#Si el tablero no contiene ningun Stark, ejecuta el metodo finalizar		

    def destroy (self, widget, data=None):	#Oculta la ventanaNivel
	self.ventanaNivel.hide()

    def iniciador_callback (self, widget, entradaNivel):	#Comprueba si el nivel introducido es numero entero mayor que 1 y si lo es muestra la ventana principal y llama a golpeinicial, sino vuelve a pedir el nivel
	try:
		self.nivel = int(self.entradaNivel.get_text())	#Comprueba lo anterior mediante la conversion entero y el calculo de un logaritmo
		math.log(self.nivel)
	except(ValueError):
		self.metodoNivel()	#Si no consigue alguna de las dos opciones anteriores, repite el metodoNivel para la seleccion del nivel de nuevo
	else:
		self.window.show()	#Muestra la ventana principal de nuestro juego y ejecuta los golpes iniciales asociados al nivel introduucido mediante golpeInicial
		self.golpeInicial()

    def activador_callback(self, widget, entradaNivel):		#Se activa al producirse alguna modificacion en el cuadro de texto, esconde la ventana con destroy 
	self.entradaNivel.connect("activate", self.destroy, self.entradaNivel)	#y conecta el evento activate (pulsacion de enter) a la entrada de texto para poder 
	self.entradaNivel.connect("activate", self.iniciador_callback, self.entradaNivel)	#iniciar el juego

    def metodoNivel (self):	#Este metodo crea nuestro selector de nivel para introducirlo antes de empezar el juego
	self.ventanaNivel = gtk.Window()	#Crea la ventana en la que introduciremos el nivel junto a unas etiquetas mediante una division
	divisionN = gtk.VBox(gtk.FALSE, 0)	#hecha con una caja horizontal anadida en la ventana
	self.ventanaNivel.set_title("Kill the Stark")	#Establecemos los campos titulo y anchura de la ventana y conectamos "destroy" con el cierre del juego
        self.ventanaNivel.connect("destroy", lambda w: gtk.main_quit())
        self.ventanaNivel.set_border_width(10)
	frase1 = gtk.Label("Buenas jugador!")	#Creamos las etiquetas de la ventana del nivel
	frase2 = gtk.Label("La guerra se cierne sobre nosotros y nuestro objetivo")
	frase3 = gtk.Label("es eliminar todo rastro posible de la familia Stark!")
	frase4 = gtk.Label("Ayudanos a acabar con ellos dejando el tablero libre")
	frase5 = gtk.Label("de cualquier rastro de esa familia y su maldito invierno.")
	frase6 = gtk.Label("Elija un nivel para nuestra guerra y comencemos!")
	divisionN.pack_start(frase1, gtk.TRUE, gtk.TRUE, 0)	#Las introducimos en nuestra caja horizontal y las mostramos por orden
	frase1.show()
	divisionN.pack_start(frase2, gtk.TRUE, gtk.TRUE, 0)
	frase2.show()
	divisionN.pack_start(frase3, gtk.TRUE, gtk.TRUE, 0)
	frase3.show()
	divisionN.pack_start(frase4, gtk.TRUE, gtk.TRUE, 0)
	frase4.show()
	divisionN.pack_start(frase5, gtk.TRUE, gtk.TRUE, 0)
	frase5.show()
	divisionN.pack_start(frase6, gtk.TRUE, gtk.TRUE, 0)
	frase6.show()
	self.entradaNivel = gtk.Entry(0)	#Creamos nuestra entrada de texto y la introducimos en la caja horizontal, conectando su evento "changed"
	divisionN.pack_start(self.entradaNivel, gtk.TRUE, gtk.TRUE, 0)	#con el callback self.activador_callback, y mostramos la entrada
	self.entradaNivel.show()
	self.entradaNivel.connect("changed", self.activador_callback, self.entradaNivel)
	self.ventanaNivel.add(divisionN)	#Unimos la division a la ventana del nivel y las mostramos
	divisionN.show()		
	self.ventanaNivel.show()

    def golpeInicial(self):	#Ejecuta el golpe inicial dependiendio del nivel
	for i in range (self.nivel):
		fila = (random.randrange(self.filas)) + 2	#Elije un evento aleatorio de nuestra matriz de eventos, establece a False el controlador
		columna = (random.randrange(self.columnas)) + 2	#ya que no hemos dado el golpe voluntariamente y lo ejecuta
		eventoG = self.eventos[fila][columna]
		self.controlador = False
		self.golpe(eventoG)

    def deshacer(self, evento, data=None):	#Metodo que extrae de la lista de golpes el ultimo golpe dado y lo elimina dando otro golpe en el
	try:
		evento = gtk.EventBox()			#Intenta extraer la coordenada x del ultimo golpe y si no puede muestra una ventana informando de que 
		evento.x = self.golpesX.pop()	#no se puede deshacer ningun golpe mediante una etiqueta y un gif
	except(IndexError):
		ventana = gtk.Window()	#Creamos la ventana junto con sus campos, con una caja horizontal que se anadira a la ventana emergente
		ventana.set_title("Apresurate o los Stark ganaran!")
       		ventana.set_size_request(400,200)
		divisioon = gtk.VBox(gtk.FALSE, 0)
		starkG = gtk.Image()
		starkG.set_from_file("stark.gif")
		divisioon.pack_start(starkG, gtk.TRUE, gtk.TRUE, 0)
		starkG.show()	#Mostramos en orden los elementos de la caja horizontal
		anuncio = gtk.Label("No puede deshacer jugadas ya que no hay ninguna realizada")
		divisioon.pack_start(anuncio, gtk.TRUE, gtk.TRUE, 0)
		anuncio.show()
		ventana.add(divisioon)
		divisioon.show()
		ventana.show()	#Mostramos la ventana emergente
	else:
		evento.y = self.golpesY.pop()	#Golpea sin almacenar el golpe mediante el valor booleano de self.controlador
		self.controlador = False
		self.golpe(evento)

    def cambiador(self, identificador, v, f, evX, evY):	#Metodo que se encarga de sustituir una imagen por otra y cambia su estado
	if (identificador == 1):	#Cambia de Lannister a Stark
		evento = gtk.EventBox()	#Crea los nuevos eventos stark, les agrega su estado False y los introduce en la matriz de eventos
		stark = gtk.Image()		#en el lugar del evento al que sustituyen
		stark.set_from_file("Staark.jpg")
		evento.add(stark)
		stark.show()
		evento.estado = False
		evento.x = (evY - 2) + f	#Establece las coordenadas del evento
		evento.y = evX + v
		evento.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		evento.connect("button_press_event", self.golpe)	#Reconecta los nuevos eventos a los manejadores golpe
		self.eventos[evX + v][(evY - 2) + f]=evento
	else:						#Cambia de Stark a Lannister con el mismo procedimiento que antes, poniendo su estado a True
		evento = gtk.EventBox()
		lannister = gtk.Image()
		lannister.set_from_file("house-lannister.jpg")
		evento.add(lannister)
		lannister.show()
		evento.estado = True
		evento.x = (evY - 2) + f
		evento.y = evX + v
		evento.set_events(gtk.gdk.BUTTON_PRESS_MASK)
		evento.connect("button_press_event", self.golpe)
		self.eventos[evX + v][(evY - 2) + f]=evento
		
    def golpe (self, evento, data=None):	#Se encarga de cambiar de estado las casillas mediante el cambiador, solo este metodo es quien decide a quien hay que cambiar para que finalmente salga la forma deseada del golpe
        x = evento.y	#Asigna a x e y las coordenadas del evento
        y = evento.x
        if (self.controlador == True):	#Si el controlador esta acivado (es decir si el golpe lo hemos dado nosotros) almacena el golpe en la lista de golpes para poder deshacerlo
            self.golpesX.append(y)
            self.golpesY.append(x)
	    self.golpes = self.golpes + 1	#Aumenta unitariamente los golpes si los hemos realizado nosotros
	    self.puntos.hide()
	    self.actualizaPuntos()

        for i in range (1,4):	#Ejecuta el golpe en la mancha y ejecuta el cambiador en cada caso, dependiendo si es lannister->stark o viceversa
            evento1 = self.eventos[x - 2][(y - 2) + i]	#mediante el estado del evento
    	    if (evento1.estado == True):
		self.cambiador(1,-2,i,x,y)
	    else:
		self.cambiador(0,-2,i,x,y)
		
        for j in range (5):	#Repite el proceso en 5 filas, cada una con su rango de afectacion
            evento1 = self.eventos[x - 1][(y - 2) + j]
	    if (evento1.estado == True):
		self.cambiador(1,-1,j,x,y)
	    else:
		self.cambiador(0,-1,j,x,y)

        for k in range (5):
            evento1 = self.eventos[x][(y - 2) + k]
	    if (evento1.estado == True):
		self.cambiador(1,0,k,x,y)
	    else:
		self.cambiador(0,0,k,x,y)

        for l in range (5):
            evento1 = self.eventos[x + 1][(y - 2) + l]
	    if (evento1.estado == True):
		self.cambiador(1,1,l,x,y)
	    else:
		self.cambiador(0,1,l,x,y)

        for n in range (1,4):
            evento1 = self.eventos[x + 2][(y - 2) + n]
	    if (evento1.estado == True):
		self.cambiador(1,2,n,x,y)
	    else:
		self.cambiador(0,2,n,x,y)

	self.imprimir()	#Imprime el tablero para que el usuario vea el cambio de su golpe, comprueba si el tablero esta resuelto y pone a True el controlador
	self.resuelto()
	self.controlador = True	

    def imprimir(self):		#Introduce las eventbox en la tabla, es la forma que tenemos de imprimirlas en pantalla y de actualizar lo eu el usuario ve en el tablero
	for ia in range (self.filas):
                for ja in range (self.columnas):	#Anade a la tabla los eventos exceptuando el marco, el cual no tiene que ver el usuario
			evento = gtk.EventBox()
                        evento = self.eventos[ia+2][ja+2]	#Selecciona los eventos desde nuestra matriz de eventos
                        self.table.attach(evento, ia, ia+1, ja, ja+1)
                        evento.show()	#Muestra cada evento asociado a la tabla

    def __init__(self):
	self.record = False
	self.controlador = False	#Iniciamos la varable controlador en True, es la encargada de controlar que solo los golpes que hemos dado se almacenen
	self.filas = 10			#Ponemos el numero de filas y de columnas
	self.columnas = 10
	self.golpes = 0
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)	#Creamos la ventana principal, con su titulo y los botones
        self.window.set_title("Kill the Stark")
        self.window.connect("destroy", lambda w: gtk.main_quit())	#Hacemos que al cerrarse finalice el programa
        self.window.set_border_width(10)
        file_menu = gtk.Menu()		#Creamos un menu y una barra de menu para poder ver los record pulsando en este
	ver_puntuaciones = gtk.MenuItem("Ver puntuaciones")
	file_menu.append(ver_puntuaciones)
	ver_puntuaciones.connect("activate", self.mostrarRecords)
	ver_puntuaciones.show()
	menu_bar = gtk.MenuBar()
	menu_bar.show()
	file_item = gtk.MenuItem("Archivo")	#Albergamos en archivo un submenu que contiene ver record, para que sea mas intuitivo
	file_item.show()
	file_item.set_submenu(file_menu)
	menu_bar.append(file_item)
	particion = gtk.VBox(gtk.FALSE, 0)	#Creamos una caja horizontal a mayores para albergar la barra de menu y los demas controles del juego
	particion.pack_start(menu_bar, gtk.TRUE, gtk.TRUE, 0)
        cajaVertical = gtk.VBox(gtk.FALSE, 0)
        botonReiniciar = gtk.Button("Reiniciar")	#Incluimos un boton para el reinicio
        botonReiniciar.connect("clicked", self.reiniciar)
        cajaVertical.pack_start(botonReiniciar, gtk.TRUE, gtk.TRUE, 0)
        botonReiniciar.show()				#Mostramos por orden los controles de la ventana principal
	self.puntuacion = gtk.Table(1,1, gtk.FALSE)
	cajaVertical.pack_start(self.puntuacion, gtk.TRUE, gtk.TRUE, 0)
	self.puntuacion.show()
	self.puntos = gtk.Label("Su puntuacion es:  %s puntos" % self.golpes)
	self.puntuacion.attach(self.puntos, 0, 1, 0, 1)
	self.puntos.show()
        cajaHorizontal = gtk.HBox(gtk.FALSE, 0)
        cajaHorizontal.pack_start(cajaVertical, gtk.TRUE, gtk.TRUE, 0)
        cajaVertical.show()
        self.table = gtk.Table(self.filas, self.columnas, gtk.FALSE)	#Incluimos una tabla donde van las imagenes y las event box
        cajaHorizontal.pack_start(self.table, gtk.TRUE, gtk.TRUE, 0)
        self.table.show()
        self.botonDeshacer = gtk.Button("Deshacer")		#Creamos el boton deshacer
	self.botonDeshacer.connect("clicked", self.deshacer)	#Conectamos el botonDeshacer con su manejador
	cajaHorizontal.pack_start(self.botonDeshacer, gtk.TRUE, gtk.TRUE, 0)
        self.botonDeshacer.show()
        particion.pack_start(cajaHorizontal, gtk.TRUE, gtk.TRUE, 0)
        cajaHorizontal.show()
        particion.show()
        self.window.add(particion)	#Anadimos la caja horizontal donde estan todos nuestros widget a la ventana principal
        self.eventos= []	#Listas para almacenar las cajas de eventos, los golpes que vamos dando en el tablero y la puntuacion, iniciadas todas a 0
	self.cte=(10**15)    #Numero que empleamos para escribir y leer los datos del fichero
	self.golpesX = []
	self.golpesY = []
	self.puntuaciones=[] #Lista donde almacenamos todas las puntuaciones
        for i in range((self.filas) + 4):	#Creamos mediante un bucle una matriz de eventbox con imagenes, la matriz tiene 4 filas y 4 columnas de mas ya que las empleamos de marco para evitar errores
			self.eventos.append([])
			for j in range((self.columnas) + 4):
				evento = gtk.EventBox()
				lannister = gtk.Image()
				lannister.set_from_file("house-lannister.jpg")	#Creamos e incluimos la imagen en las eventbox, lannister en un principio
				evento.add(lannister)	
				lannister.show()
				evento.estado = True	#establecemos el estado y coordenadas de los eventos (Lannister->True)
				evento.x = j
				evento.y = i
				evento.set_events(gtk.gdk.BUTTON_PRESS_MASK)
				evento.connect("button_press_event", self.golpe)	#Conectamos los eventos con sus manejadores
				self.eventos[i].append(None)
				self.eventos[i][j]=evento	#Incluimos las eventbox en la matriz de eventos
	self.metodoNivel()	#Ejecutamos el metodoNivel y el imprimir para comenzar nuestro juego
	self.imprimir()	
	self.Iniciopuntuaciones()

def main():		#Ejecuta el main de gtk para que el programa pase a la espera de un evento sobre el que reaccionar
    gtk.main()
    return 0

if __name__ == "__main__":	#Si el programa se ejecuta directamente o se pasa como argumento al interprete esto se ejecuta haciendo que se cree una instancia para la clase Juego y despues se ejecute el main de gtk
    Juego()
    main()
