import sqlite3 as sql

from clases.pelicula import Pelicula


class Conexion:
    def __init__(self,nombreBaseDatos):
        self.conexion = sql.connect(nombreBaseDatos)
        self.cursor=self.conexion.cursor()
    def crearTabla(self):
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Pelicula (ID INTEGER PRIMARY KEY AUTOINCREMENT,TITULO VARCHAR(50),DURACION VARCHAR(10),GENERO VARCHAR(20),ESTUDIO_ANIMACION VARCHAR(50))''')
            self.conexion.commit()
    def mostrarTabla(self):
        sql = "SELECT ID,TITULO FROM Pelicula "
        self.cursor.execute(sql)
        resultados= self.cursor.fetchall()
        return print(resultados)
    def agregar(self,pelicula):
            titulo = pelicula.titulo

            # Verifica si ya existe un registro con el mismo título en la tabla
            existe = self.cursor.execute('SELECT TITULO FROM Pelicula WHERE TITULO = ?', (titulo,)).fetchone()

            if existe is None:
                duracion = pelicula.duracion
                genero = pelicula.genero
                estudio = pelicula.estudio

                self.cursor.execute(
                    '''INSERT OR IGNORE INTO Pelicula (TITULO, DURACION, GENERO, ESTUDIO_ANIMACION) VALUES (?, ?, ?, ?)''',
                    (titulo, duracion, genero, estudio))
                self.conexion.commit()
                print(f"Película '{titulo}' agregada correctamente.")
            else:
                print(f"La película '{titulo}' ya existe en la base de datos y no se ha agregado.")
    def actualizar(self,id):
            titulo=input('titulo:')
            duracion=input('Duracion:')
            genero=input('Genero:')
            estudio=input('Estudio:')
            sql= f"UPDATE pelicula set titulo='{titulo}', duracion='{duracion}', genero='{genero}',estudio_animacion='{estudio}' where id= {id}"
            self.cursor.execute(sql)
            self.conexion.commit()
    def eliminar(self,id):
        sql = f'DELETE FROM Pelicula WHERE ID = {id}'
        self.cursor.execute(sql)
        self.conexion.commit()
    def traerPelicula(self, id):

        sql = "SELECT * FROM pelicula WHERE ID = ?"
        fila = self.cursor.execute(sql, (id,)).fetchone()

        if fila:
            id, titulo, duracion, genero, estudio = fila
            pelicula = Pelicula(titulo, duracion, genero, estudio)
            return pelicula
        else:
            print(f"No se encontró una película con el ID {id}.")
            return None

    def mostar_info(self,id):
        sql=f'SELECT * FROM Pelicula WHERE Id={id}'
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        return print(resultados)