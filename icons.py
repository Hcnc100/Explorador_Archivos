class Icono():
    """
    Clase encargada de representar los iconos de un directorio
    Ademas de guardar referncias en cuanto a la posicion  y el tipo de icono que es
    """

    def __init__(self,dictIcon):
        self.nombre=dictIcon["name"]
        self.x=dictIcon["posX"]
        self.y=dictIcon["posY"]
        self.direccion=dictIcon["direccion"]
        self.img=dictIcon["img"]
        self.img_select=dictIcon["img_select"]
        self.type=dictIcon["type"]
        self.diametro=35

    def dibujar(self,canvas):
        """
        Metodo que se encaraga de pintar el icono en el canvas
        :param canvas: Canvas donde se pintaran lo iconos
        :return:
        """
        self.canvas=canvas
        # se crea un icono anexando una imagen que se presentara cuando se pase el mouse sobre el icono
        self.identificador=canvas.create_image(self.x,self.y,image=self.img,activeimage=self.img_select)

        #se imprime el nombre
        if len(self.nombre)>11:
            canvas.create_text(self.x,self.y+45, text=self.nombre,fill="white")
        else:
            canvas.create_text(self.x,self.y+40, text=self.nombre,fill="white")

        #si esta en modo debug se pinta el cuadro que representa los limites sobde se puden dar click a los iconos
        #esto no afecta el funcionamiento
        self.identificadorCuadro=canvas.create_rectangle(
		self.x-self.diametro,
		self.y-self.diametro,
		self.x+self.diametro,
        self.y+self.diametro,outline="white")

    def setSelect(self):
        """
        Funcion setselect , esta funcion se encarga de cambiar el icono por la imagen seleccionada del mismo icoos
        :return: None
        """
        self.canvas.itemconfigure(self.identificador,image=self.img_select)
    def clearSelect(self):
        """
        Funcion clearSelect , esta funcion se encarga de cambiar el icono por el icnono predeterminado
        :return: None
        """
        self.canvas.itemconfigure(self.identificador,image=self.img)

    def contais(self,x,y):
        """
        Fuuncion que se basa en una expresion matematica para determinar si las coordenadas dadas por el evento doble click
        estan dentro del rango del icono
        :param x: posicion de x del evento doble click
        :param y:  posicion de y del evento doble click
        :return: Retorna True o False dependiendo si se encuentra dentro del rango
        """
        return x>=self.x-self.diametro and y>=self.y-self.diametro and (self.x+self.diametro)-x >=0 and (self.y+self.diametro)-y >=0
