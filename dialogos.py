from tkinter import Button,Tk,Label,Entry,LEFT,RIGHT,Toplevel,HORIZONTAL,BOTH,VERTICAL,X,BOTTOM,Frame
from tkinter.ttk import Separator
class Dialogo():
    """
    Clase encargada de presntar los dialogos para la obtencion:
    -Nombre del archivo
    -Nombre de la carpeta
    -Confirmacion de la eliminacion
    -Renombre de archivo
    """
    def __init__(self,root):
        """
        Contructor
        Se inicia a None los valores de toplevel y answer
        se gurada el padre para poder realizar las ventanas
        :param root:
        """
        #padre
        self.root=root
        #varible que gurda las respuesta
        self.answer=None
        #top level
        self.toplevel=None
    def destroyTopLevel(self):
        """
        Metodo que destruye el toplevel
        :return: None
        """
        if  self.toplevel!=None:
            self.toplevel.destroy()
        print("La respuesta es ", self.answer)

    def getSring(self,answer):
        """
        Metodo que se encarga de asignar la respuesta a la varible answer
        y depues destruye el toplevel
        :param answer:
        :return:
        """
        self.answer=answer
        self.destroyTopLevel()

    def getRespuesta(self):
        """
        Metodo que devuelve la respuesta capturada por el toplevel
        :return: La respuesta
        """
        return self.answer
    def topGetStringName(self,modal=True,stringDefault="Dame el nombre de la carpeta"):
        """
        Metodo que se encarga de contruir un toplevel que puede ser modal y muetra un string como ayuda
        el dato obtenido se guarda en la variable answer y se puede ibtener por el metodo getRespuesta
        :param modal: Booleano que identifica si la ventana sera modal o no
        :param stringDefault: El valor por defecto del texto de ayuda que se mostrara
        :return:None
        """

        #se inicia la respuesta en None para eliminar la basura
        self.answer=None

        #se crea el toplevel
        self.toplevel=Toplevel(self.root)

        #se agrgan los elementos y los separadores
        frameprincipal=Frame(master=self.toplevel)
        frameprincipal.pack()
        separador = Separator(frameprincipal, orient=HORIZONTAL)
        separador.pack(expand=True, pady=5)
        label=Label(frameprincipal,text=stringDefault)
        label.pack()
        separador = Separator(frameprincipal, orient=HORIZONTAL)
        separador.pack(expand=True, pady=5, padx=100)
        entry=Entry(frameprincipal)
        entry.pack()
        separador = Separator(frameprincipal, orient=VERTICAL)
        separador.pack(side=LEFT, pady=10,padx=10)
        button=Button(frameprincipal,text="Aceptar",command=lambda: self.getSring(entry.get()) )
        button.pack(side=LEFT)
        separador = Separator(frameprincipal, orient=HORIZONTAL)
        separador.pack(side=LEFT,fill=X,pady=10, padx=50)
        button = Button(frameprincipal, text="Cancelar",command=self.destroyTopLevel)
        button.pack(side=LEFT)
        separador = Separator(frameprincipal, orient=HORIZONTAL )
        separador.pack(fill=X, pady=20, padx=10)

        #Si es modal se configura la ventana
        if modal:
            self.toplevel.transient(self.root)
            self.toplevel.grab_set()
            self.root.wait_window(self.toplevel)


app=Tk()
d=Dialogo(app)
button=Button(master=app,text="abrir",command=d.topGetStringName)
button.pack()
button=Button(master=app,text="Quitar",command=None)
button.pack()
app.mainloop()

