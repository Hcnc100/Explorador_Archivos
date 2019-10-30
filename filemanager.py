from os import mkdir
from os.path import exists,join
class FileManager():
    """
    Clase encargada de hacer las llamadas al sistema
    """
    def deleter(self):
        pass
    def rename(self):
        pass
    def copy(self):
        pass
    def new_directory(self,ruta):
        if exists(ruta):
            print("La carpeta ya existe")
        else:
            mkdir(ruta)
    def new_file(self,ruta):
        if exists(ruta):
            print("El archivo ya existe")
        else:
            self.touch(ruta)
    def paste(self):
        pass
    def propiedades(self):
        pass

    def touch(self,path):
        with open(path, 'a'):
            pass