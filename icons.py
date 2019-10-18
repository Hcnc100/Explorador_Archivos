class Icono():
    """docstring forIconos."""

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
        self.frame=canvas
        self.identificador=canvas.create_image(self.x,self.y,image=self.img,activeimage=self.img_select)
        if len(self.nombre)>11:
            canvas.create_text(self.x,self.y+45, text=self.nombre,fill="white")
        else:
            canvas.create_text(self.x,self.y+40, text=self.nombre,fill="white")
        self.identificadorCuadro=self.frame.create_rectangle(
		self.x-self.diametro,
		self.y-self.diametro,
		self.x+self.diametro,
        self.y+self.diametro,outline="white")
    def setSelect(self):
        self.frame.itemconfigure(self.identificador,image=self.img_select)
    def clearSelect(self):
        self.frame.itemconfigure(self.identificador,image=self.img)
    def contais(self,x,y):
        return x>=self.x-self.diametro and y>=self.y-self.diametro and (self.x+self.diametro)-x >=0 and (self.y+self.diametro)-y >=0
