class Cine:
    def __init__(self,nombre,direccion):
        self.nombre=nombre
        self.direccion=direccion
        self.programacion= []

    def agregarPelicula(self,pelicula):
        self.programacion.append(pelicula)
    def mostrarProgramacion(self):
        if len(self.programacion)>0:
            for pelicula in self.programacion:
                print(pelicula.titulo)
        else: print('No hay peliculas para mostrar')
    def eliminarPelicula(self,id):
        if id-1 < len(self.programacion):
            self.programacion.pop(id-1)
        else:
            print("Índice fuera de rango, no se puede eliminar.")