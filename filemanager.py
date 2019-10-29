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
        print("nueva carpeta")
        print(ruta)
        print(exists(ruta))
        ruta=join(ruta, "Nueva Carpeta")
        print(exists(ruta))
        print(ruta)
        if exists(ruta):
            pass
        else:
            mkdir(ruta)
    def new_file(self,ruta):
        print("nueva archivo")
        #if exists(ruta):
        #    pass
        #else:
        #    self.touch(ruta)
    def paste(self):
        pass
    def propiedades(self):
        pass

    def touch(self,path):
        with open(path, 'a'):
            pass