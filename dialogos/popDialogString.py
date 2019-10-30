from tkinter import Toplevel,Frame,HORIZONTAL,VERTICAL,X,Label,Button,LEFT,Entry,Tk
from tkinter.ttk import Separator
respuesta=None

def destroy(toplevel):
    """
    Funcion que se encarga de destruir la ventana
    :param toplevel:El top level a destruir
    :return: None
    """
    toplevel.destroy()
def getAnswer(answer,toplevel):
    """
    Funcion que se encarga de obtener la respuesta de la ventana
    :param answer:
    :param toplevel:
    :return:
    """
    global respuesta
    respuesta=answer
    destroy(toplevel)

def topGetStringName(root=None,titulo="Sin tutulo",modal=True, stringDefault="Dame el nombre de la carpeta"):
    """
    Metodo que se encarga de contruir un toplevel que puede ser modal y muetra un string como ayuda

    :param modal: Booleano que identifica si la ventana sera modal o no
    :param stringDefault: El valor por defecto del texto de ayuda que se mostrara
    :return:None
    """
    global respuesta
    # se inicia la respuesta en None para eliminar la basura
    answer = None

    # se crea el toplevel
    toplevel = Toplevel(root)

    toplevel.title(titulo)

    #se evita que se redimencione la pantalla
    toplevel.resizable(0, 0)

    # se agrgan los elementos y los separadores
    frameprincipal = Frame(master=toplevel)
    frameprincipal.pack()
    separador = Separator(frameprincipal, orient=HORIZONTAL)
    separador.pack(expand=True, pady=5)
    label = Label(frameprincipal, text=stringDefault)
    label.pack()
    separador = Separator(frameprincipal, orient=HORIZONTAL)
    separador.pack(expand=True, pady=5, padx=100)
    entry = Entry(frameprincipal)
    entry.pack()
    separador = Separator(frameprincipal, orient=VERTICAL)
    separador.pack(side=LEFT, pady=10, padx=10)
    button = Button(frameprincipal, text="Aceptar", command=lambda: getAnswer(entry.get(),toplevel))
    button.pack(side=LEFT)
    separador = Separator(frameprincipal, orient=HORIZONTAL)
    separador.pack(side=LEFT, fill=X, pady=10, padx=50)
    button = Button(frameprincipal, text="Cancelar", command=lambda :getAnswer(None,toplevel))
    button.pack(side=LEFT)
    separador = Separator(frameprincipal, orient=HORIZONTAL)
    separador.pack(fill=X, pady=20, padx=10)

    #se agrega un protocolo para manejar la destruccion del toplevel
    toplevel.protocol("WM_DELETE_WINDOW", lambda :getAnswer(None,toplevel))

    # Si es modal se configura la ventana
    if modal:
        toplevel.transient(root)
        toplevel.grab_set()
        toplevel.focus()
        root.wait_window(toplevel)
    return respuesta

"""
#Ejemplo de la utlilizacion del dialogo

def getRespuesta(root):
    respuesta=topGetStringName(root,stringDefault="Dame el nombre\na")
    print("La respuesta es",respuesta)


app=Tk()
button=Button(master=app,text="abrir",command=lambda :getRespuesta(app))
button.pack()
button=Button(master=app,text="Quitar",command=None)
button.pack()
app.mainloop()
"""

