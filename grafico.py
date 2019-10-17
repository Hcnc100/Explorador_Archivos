from tkinter import *
from controlador import Controlador
class Interfaz():
    """
    Esta clase se encarga de mostrar los elementos visuales de los archivos
    Esta clase se controla con la clase controlador
    """
    def __init__(self):
        """
            Esta clase incia la interfaz
            se crea un canvas y una barra lateral(un frame)
        """
        controlador=Controlador()
        root=Tk()
        frame=Frame(root,height=500)
        frame.pack(fill=BOTH, expand=1)
        b_lateral=Frame(frame,width=150,height=500,bg="#dedede")
        b_lateral.pack(side=LEFT,fill=BOTH);
        canvas=Canvas(frame,bg="#000000",width=600,height=500)
        canvas.pack(side=LEFT,fill=BOTH, expand=1)
        controlador.crear_barra(b_lateral)
        root.mainloop()