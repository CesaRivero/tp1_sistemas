from clases.Conexion import Conexion
from clases.cine import Cine
from clases.pelicula import Pelicula

conexion = Conexion('mibase.db')
#conexion.cursor.execute(   '''DROP table Pelicula''')
conexion.crearTabla()

pelicula= Pelicula("DaVinci","1.50","Fantasia")
pelicula1= Pelicula("Argentina 1985","2.30","Drama")
pelicula2= Pelicula("NWA","2.10","Drama")
pelicula3= Pelicula("El planeta del tesoro","1.30","aventura","Pixar")
#agrego peliculas a la bdd
conexion.agregar(pelicula)
conexion.agregar(pelicula1)
conexion.agregar(pelicula2)
conexion.agregar(pelicula3)

cine= Cine("Gaumont","Av. Rivadavia 1500")
#Agrego peliculas a la programacion
cine.agregarPelicula(pelicula)
cine.agregarPelicula(pelicula1)
cine.agregarPelicula(pelicula2)
cine.agregarPelicula(pelicula3)


opciones= input('\nBienvenido\n1-Ver programacion\n2-Crear Pelicula\n3-Agregar pelicula a programacion\n4-Editar\n5-Borrar\n6-Ver Peliculas\n7-Quitar pelicula de programacion\n0-Salir\n')
while opciones != '0':
    if opciones == '1': #Ver programacion
        cine.mostrarProgramacion()

    elif opciones == '2': #Crear pelicula
            titulo = input('Titulo:')
            duracion = input('Duracion en Horas:')
            genero = input('Genero:')
            estudio = input('Estudio:')
            peliculainicial=Pelicula(titulo,duracion,genero,estudio)
            conexion.agregar(peliculainicial)

    elif opciones == '3': #Agregar pelicula a programacion
        conexion.mostrarTabla()
        id=int(input('Seleccione pelicula a agregar a la programacion:'))
        #Agregar verificacion si a exite en programacion mostrar mensaje
        peliculaAguardar=conexion.traerPelicula(id)

        existe_en_programacion = False

        for pelicula in cine.programacion:
            if peliculaAguardar.titulo == pelicula.titulo:
                existe_en_programacion = True
                break  # Termina el bucle si la película ya existe

        if existe_en_programacion:
            print('La película ya se encuentra en Programación')
        else:
            cine.agregarPelicula(peliculaAguardar)


    elif opciones == '4': #editar
        conexion.mostrarTabla()
        id=int(input('Seleccione pelicula a actualizar'))
        conexion.actualizar(id)

    elif opciones == '5':#borrar
        conexion.mostrarTabla()
        id = input('Seleccione pelicula para eliminar de la bdd')
        conexion.eliminar(id)
    elif opciones == '6': #Ver peliculas
        conexion.mostrarTabla()
        id = input('Seleccione pelicula para ver mas informacion: ')
        conexion.mostar_info(id)

    elif opciones == '7':#quitar pelicula de programacion
        resultado_mostrar_programacion = cine.mostrarProgramacion()

        if resultado_mostrar_programacion == 'No hay películas para mostrar':
            print(resultado_mostrar_programacion)
        else:
            if 0 < len(cine.programacion):
                id = int(input('Seleccione película para eliminar de la programacion'))
                cine.eliminarPelicula(id)


    opciones = input(
        '\nBienvenido\n1-Ver programacion\n2-Crear Pelicula\n3-Agregar pelicula a programacion\n4-Editar\n5-Borrar\n6-Ver Peliculas\n7-Quitar pelicula de programacion\n0-Salir\n')

