from os import  getcwd
from os import name,listdir,makedirs
from os.path import expanduser,join,isdir,exists
from tkinter import Button
from tkinter import X
from PIL import ImageTk
from math import ceil
from icons import Icono
from tkinter import HORIZONTAL,BOTH
from tkinter.ttk import Separator
class Controlador():
    """
        Clase dedicada a determinar el directorio , el prpcesamiento de los archivos
        asi como la actualizacion del gui
    """
    def __init__(self,root,canvas,scrollbar):

        #Se asignan las varibles externas como varibles internas de la clase
        self.root = root
        self.canvas = canvas
        self.scrollbar = scrollbar

        # se inicia los iconos
        self.init_icons(root)

        #se crean un diccionario con los accesos directos a las carpetas principales dependidno del sistema operativo
        home = expanduser("~")
        print("Carpetas del usuario"+home)

        #windows
        if (name == "nt"):
            self.listadir={"Documentos":"\Documents","Escritorio":"\Desktop","Descargas":"\Downloads","Imagenes":"\Pictures"}
            for key,value in self.listadir.items():
                self.listadir[key]= home+value
            #print(self.listadir)
        else:
        #linux
            self.dirHome = home + "/Files"
            self.dirImagenes = home + "/Files/Imagenes"
            self.dirTexto = home + "/Files/Documentos"

        # se obtienen el directorio actual que sera de donde se inicie la aplicacion
        self.directorio_actual =getcwd()

        # se inicia el canvas con los iconos actuales de "directorio_actual"
        self.actualizar_canvas()

    def clearSelect(self):
        """
        Se limpia todos los iconos seleccionados
        :return: None
        """
        # se recorre todos los iconos y se aplica el metodo clearSelect que regresa el icono a su forma original
        for icono in self.listaIcons:
            icono.clearSelect()

    def get_numero_archivos(self):
        """
        Funcion que retorna la longitud de los archivos contenidos por el directorio actual
        :return: el numero de archivos
        """
        return len(self.lista_files)
    def init_icons(self, root):
        """
        Funcion que inicia los iconos, la ruta depende del sistema operativo que ocupe
        Las imagenes estan dentro de la carpeta img
        :param root: se necesita el canvas que se tomara de referencia para crear los iconos
        :return: None
        """
        #si es windows el seperador entre carpetas es \ el cual se escapa como "\\"
        if (name == "nt"):
            sep = "\\"
        else:
        #si es linux el separador es /
            sep = "/"
        #se inicia las imagenes
        self.carpeta = ImageTk.PhotoImage(master=root, file=join(getcwd(), "img" + sep + "carpeta.png"))
        self.imagen = ImageTk.PhotoImage(master=root, file=join(getcwd(), "img" + sep + "imagen.png"))
        self.texto = ImageTk.PhotoImage(master=root, file=join(getcwd(), "img" + sep + "letra.png"))
        self.carpeta_select = ImageTk.PhotoImage(master=root,
                                                 file=join(getcwd(), "img" + sep + "carpeta_select.png"))
        self.imagen_select = ImageTk.PhotoImage(master=root,
                                                file=join(getcwd(), "img" + sep + "imagen_select.png"))
        self.texto_select = ImageTk.PhotoImage(master=root,
                                               file=join(getcwd(), "img" + sep + "letra_select.png"))
    def redefinir_canvas(self):
        numero_archivos = self.get_numero_archivos()
        if numero_archivos - 30 > 0:
            largo = (ceil(numero_archivos / 6)) * 102
            self.canvas.config(scrollregion=(0, 0, 500, largo))
           #self.scrollbar.pack(side=RIGHT, fill=Y)
        else:
            #self.scrollbar.grid_forget()
            pass
    def get_lista_files(self, directorio):
        """
        Funcion que dependiendo de la direccion que se le da clasifica el contenido
        La clasifificacion actual es
            -carpeta
            -imagen
            -texto
        :param directorio: Directorio de donde se clasificaran los archivos
        :return: La lista de archivos ordenadas por tipo
        """
        #se recuerda que el signo de separacion varia dependiendo del sistema operativo

        #el primer valor siempre es una carpeta de valor ".." que lleva a un directorio mas arriba
        if (name=="nt"):
            lista = [{"type": "carpeta", "name": "..", "direccion": directorio[0:directorio.rfind("\\")]}]
        else:
            lista = [{"type": "carpeta", "name": "..", "direccion": directorio[0:directorio.rfind("/")]}]

        #se clasifica la lista del directorio proporcionado
        for archivo in listdir(directorio):
            if len(archivo) > 11:
                nombre = archivo[:11] + "\n" + archivo[11:]
            else:
                nombre = archivo
            if isdir(join(directorio, archivo)):
                lista.append({"type": "carpeta", "name": nombre, "direccion": join(directorio, archivo)})
            else:
                if archivo.endswith(".png"):
                    lista.append({"type": "imagen", "name": nombre, "direccion": join(directorio, archivo)})
                else:
                    lista.append({"type": "texto", "name": nombre, "direccion": join(directorio, archivo)})
        # se ordena la lista por tipo
        lista.sort(key=lambda x: x["type"])
        return lista

    def click_dentro_icon(self, x, y):
        """
        Funcion convocada por el canvas por la accion de doble click
        Esta funcion necesita los valores x,y proporcionada por el evento
        Retorna el icono que due seleccionado , si no fue seleccionado ni uno se retorna None
        :param x: valor x del canvas
        :param y: valor y del canvas
        :return:
        """

        #se recorre todos los iconos
        for icono in self.listaIcons:
            #se utiliza el metodo contains para determinar si se selecciono un icono
            if icono.contais(x, y):
                return icono
        return None

    def actualizar_direccion(self,nueva_direccion):
        """
        Funcion que se encarga de actualizar el directorio actual y que a su vez manda a actualizar los iconos
        :param nueva_direccion: La nueva direccion a cambiar
        :return:
        """

        #se asigna la nueva direccion
        self.directorio_actual=nueva_direccion
        #se actualiza el canvas
        self.actualizar_canvas()

    def crear_barra(self,b_lateral):
        """
        Funcion dedicada a crear la barra lateral de los accesos directos que varian dependiendo del sistena operativo
        :param b_lateral: la barra proporcionada por la interfaz
        :return:
        """
        for nombre,direccion in self.listadir.items():
            separador=Separator(b_lateral, orient=HORIZONTAL)
            separador.pack(fill=BOTH,expand=True)
            auxButton=Button(master=b_lateral,text=nombre,command=lambda direccion=direccion:self.actualizar_direccion(direccion))
            auxButton.pack(fill=X)
        separador = Separator(b_lateral, orient=HORIZONTAL)
        separador.pack(fill=BOTH, expand=True)

    def dibujar(self):
        """
        Este metodo se basa en la aliminacion de todos los elementos del canvas
        y luego llama a la funcion create_iconos para poder hacer nuevos iconos
        :return: None
        """
        #se eliminan todos los elementos del canvas
        self.canvas.delete("all")
        self.canvas.update()
        self.redefinir_canvas()
        #se obteniene los iconos
        self.listaIcons = self.create_iconos(self.directorio_actual)
        # se pintan los iconos
        for icon in self.listaIcons:
            icon.dibujar(self.canvas)


    def actualizar_canvas(self):
        """
        Funcion que actualiza en canvas mandando a llamar la funcion que actualiza los elementos del directorio actual
        :return:None
        """
        self.lista_files = self.get_lista_files(self.directorio_actual)
        self.dibujar()


    def click_izquierdo(self, event):
        """
        Funcion que se encarga de cambiar el estado del icono a uno mas oscurecido cuando se da click en algun icono
        :param event: El evento que genera la llamada de esta funcion
        :return: None
        """
        # se obtiene el elemento que causo la llamada de la funcion
        canvas = event.widget

        #se obtienen las coordenadas del click que provoco el evento
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)

        #se obtiene el icono que se selecciono
        auxIcono = self.click_dentro_icon(x, y)

        #si algun icono fue seleccionado con anteriorida se limpia el select
        self.clearSelect()

        #si se selecciono un icono y no un espacio en blanco se cambia su icono
        if auxIcono != None:
            auxIcono.setSelect()



    def doble_click_izquierdo(self, event):
        """
        funcion que si se selecciona doble click sobre una carpeta se cambia la direccion actual,
        si no se abre el archivo con ya ayuda del sistema operativo
        :param event: Evento lanzado por el canvas al dar doble click
        :return: None
        """
        #se obtiene el elemnto de que lanzo el evento
        canvas = event.widget
        # se obitne las ccoordenadas
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        # se determina si se dio doble click sobre un icono
        auxIcono = self.click_dentro_icon(x, y)
        # si hay un icono selessionado con anterioridad se limpia
        self.clearSelect()
        if auxIcono != None:
            #si es una carpeta se actualiza la direccion
            if auxIcono.type == "carpeta":
                self.directorio_actual = auxIcono.direccion
                print(self.directorio_actual)
                self.actualizar_canvas()
            else:
            # si no se abre el archivo
                pass
    def create_iconos(self, direccion):
        """
        Funcion create_icons
            La funcion lo que hace es asiciar los iconos a los archivos por medio de la clasificacion de estos
            Se le asigna ina imagen normal y una imagen cuando se a seleccionado o se situa sobre el
        :param direccion: necesita la direccion de donde se muestran los archivos de forma grafica
        :return: ListIcon que es una lista que contiene todas las referncias ya con su icono
        """

        contenido = self.get_lista_files(direccion)
        listIcon = []
        x = 50
        y = 50
        for archivo in contenido:
            if archivo["type"] == "carpeta":
                archivo["img"] = self.carpeta
                archivo["img_select"] = self.carpeta_select
            elif archivo["type"] == "imagen":
                archivo["img"] = self.imagen
                archivo["img_select"] = self.imagen_select
            else:
                archivo["img"] = self.texto
                archivo["img_select"] = self.texto_select
            archivo["posX"] = x
            archivo["posY"] = y
            listIcon.append(Icono(archivo))
            x += 80
            if x > 500:
                y += 100
                x = 50
        return listIcon