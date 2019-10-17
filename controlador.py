from os import  getcwd
from os import name
from os.path import expanduser
from tkinter import Button
from tkinter import X
class Controlador():
    """
        Clase dedicada a determinar el directorio , el prpcesamiento de los archivos
        asi como la actualizacion del gui
    """
    def iconos(self):
        pass
    def cambiar_directorio(self,directorio):
        pass
    def crear_barra(self,b_lateral):
        self.directorios=self.definir_directorios()
        for nombre,direccion in self.directorios.items():
            auxButton=Button(master=b_lateral,text=nombre)
            auxButton.pack(fill=X)
            print("Hola")
    def definir_directorios(self):
        directorios={}
        if name == "posix":
            pass
        else:  # windows
            directorios["Escritorios"]=expanduser("~/Desktop")
            directorios["Descargas"]=expanduser("~/Downloads")
        return directorios