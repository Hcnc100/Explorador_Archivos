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
        self.root = root
        self.canvas = canvas
        self.scrollbar = scrollbar
        self.carpeta_raiz = getcwd()
        self.init_icons(root)
        home = expanduser("~")
        print(home)
        if (name == "nt"):
            self.listadir={"Documentos":"\Documents","Escritorio":"\Desktop","Descargas":"\Downloads","Imagenes":"\Pictures"}
            for key,value in self.listadir.items():
                self.listadir[key]= home+value
            print(self.listadir)
        else:
            self.dirHome = home + "/Files"
            self.dirImagenes = home + "/Files/Imagenes"
            self.dirTexto = home + "/Files/Documentos"
        self.directorio_actual =getcwd()
        self.actualizar_canvas()
    def clearSelect(self):
        for icono in self.listaIcons:
            icono.clearSelect()

    def get_numero_archivos(self):
        return len(self.lista_files)
    def init_icons(self, root):
        if (name == "nt"):
            sep = "\\"
        else:
            sep = "/"
        self.carpeta = ImageTk.PhotoImage(master=root, file=join(self.carpeta_raiz, "img" + sep + "carpeta.png"))
        self.imagen = ImageTk.PhotoImage(master=root, file=join(self.carpeta_raiz, "img" + sep + "imagen.png"))
        self.texto = ImageTk.PhotoImage(master=root, file=join(self.carpeta_raiz, "img" + sep + "letra.png"))
        self.carpeta_select = ImageTk.PhotoImage(master=root,
                                                 file=join(self.carpeta_raiz, "img" + sep + "carpeta_select.png"))
        self.imagen_select = ImageTk.PhotoImage(master=root,
                                                file=join(self.carpeta_raiz, "img" + sep + "imagen_select.png"))
        self.texto_select = ImageTk.PhotoImage(master=root,
                                               file=join(self.carpeta_raiz, "img" + sep + "letra_select.png"))
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
        if (name=="nt"):
            lista = [{"type": "carpeta", "name": "..", "direccion": directorio[0:directorio.rfind("\\")]}]
        else:
            lista = [{"type": "carpeta", "name": "..", "direccion": directorio[0:directorio.rfind("/")]}]
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
        lista.sort(key=lambda x: x["type"])
        return lista
    def click_dentro_icon(self, x, y):
        for icono in self.iconos:
            if icono.contais(x, y):
                return icono
        return None
    def actualizar_direccion(self,nueva_direccion):
        self.directorio_actual=nueva_direccion
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
        self.lista_files = self.get_lista_files(self.directorio_actual)
        self.dibujar()
    def click_izquierdo(self, event):
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        auxIcono = self.click_dentro_icon(x, y)
        self.clearSelect()
        if auxIcono != None:
            auxIcono.setSelect()

    def click_dentro_icon(self, x, y):
        for icon in self.listaIcons:
            if icon.contais(x, y):
                return icon
        return None

    def doble_click_izquierdo(self, event):
        """
        funcion doble_click_izquierdo
            Funcion que se basa en el evebto de dar click sobre el canvas
            Si se le da click sobre un icono se selecciona
            Si se le da click a un icono y otro esat seleccionado se deselecciona y se selecciona el nuevo icono
            Si se da click sobre un espacio vacio se deselecciona si esque se habia seleccionado algo antes
        :param event: Evento lanzado por el canvas al dar doble click
        :return: None
        """
        canvas = event.widget
        x = canvas.canvasx(event.x)
        y = canvas.canvasy(event.y)
        auxIcono = self.click_dentro_icon(x, y)
        self.clearSelect()
        if auxIcono != None:
            if auxIcono.type == "carpeta":
                self.directorio_actual = auxIcono.direccion
                print(self.directorio_actual)
                self.actualizar_canvas()
            else:
                auxIcono.setSelect()
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