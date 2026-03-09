# ==========================================
# SERVICIO DE BIBLIOTECA
# Contiene toda la lógica del sistema
# ==========================================

from modelos.libro import Libro
from modelos.usuario import Usuario


class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros
        # clave = ISBN
        # valor = objeto Libro
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set para controlar IDs únicos
        self.ids_usuarios = set()


    # ==========================================
    # AÑADIR LIBRO
    # ==========================================
    def agregar_libro(self, titulo, autor, categoria, isbn):

        if isbn in self.libros:
            print("ISBN ya existe.")
            return

        libro = Libro(titulo, autor, categoria, isbn)

        self.libros[isbn] = libro

        print("Libro agregado correctamente.")


    # ==========================================
    # QUITAR LIBRO
    # ==========================================
    def quitar_libro(self, isbn):

        if isbn in self.libros:

            del self.libros[isbn]

            print("Libro eliminado.")

        else:
            print("Libro no encontrado.")


    # ==========================================
    # REGISTRAR USUARIO
    # ==========================================
    def registrar_usuario(self, nombre, id_usuario):

        if id_usuario in self.ids_usuarios:
            print("ID ya registrado.")
            return

        usuario = Usuario(nombre, id_usuario)

        self.usuarios[id_usuario] = usuario

        self.ids_usuarios.add(id_usuario)

        print("Usuario registrado.")


    # ==========================================
    # ELIMINAR USUARIO
    # ==========================================
    def eliminar_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            del self.usuarios[id_usuario]

            self.ids_usuarios.remove(id_usuario)

            print("Usuario eliminado.")

        else:
            print("Usuario no encontrado.")


    # ==========================================
    # PRESTAR LIBRO
    # ==========================================
    def prestar_libro(self, id_usuario, isbn):

        if isbn not in self.libros:
            print("Libro no existe.")
            return

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        libro = self.libros[isbn]

        if libro.prestado:
            print("Libro ya prestado.")
            return

        usuario = self.usuarios[id_usuario]

        libro.prestado = True

        usuario.prestar_libro(libro)

        print("Libro prestado.")


    # ==========================================
    # DEVOLVER LIBRO
    # ==========================================
    def devolver_libro(self, id_usuario, isbn):

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        if isbn not in self.libros:
            print("Libro no existe.")
            return

        usuario = self.usuarios[id_usuario]

        libro = self.libros[isbn]

        usuario.devolver_libro(libro)

        libro.prestado = False

        print("Libro devuelto.")


    # ==========================================
    # BUSCAR POR TITULO
    # ==========================================
    def buscar_titulo(self, titulo):

        for libro in self.libros.values():

            if titulo.lower() in libro.obtener_titulo().lower():
                print(libro)


    # ==========================================
    # BUSCAR POR AUTOR
    # ==========================================
    def buscar_autor(self, autor):

        for libro in self.libros.values():

            if autor.lower() in libro.obtener_autor().lower():
                print(libro)


    # ==========================================
    # BUSCAR POR CATEGORIA
    # ==========================================
    def buscar_categoria(self, categoria):

        for libro in self.libros.values():

            if categoria.lower() in libro.categoria.lower():
                print(libro)


    # ==========================================
    # LIBROS DE UN USUARIO
    # ==========================================
    def libros_usuario(self, id_usuario):

        if id_usuario not in self.usuarios:
            print("Usuario no existe.")
            return

        usuario = self.usuarios[id_usuario]

        for libro in usuario.libros_prestados:
            print(libro)


    # ==========================================
    # GUARDAR DATOS
    # ==========================================
    def guardar_datos(self):

        with open("libros.txt", "w", encoding="utf-8") as f:

            for libro in self.libros.values():

                f.write(f"{libro.obtener_titulo()}|{libro.obtener_autor()}|{libro.categoria}|{libro.isbn}|{libro.prestado}\n")


        with open("usuarios.txt", "w", encoding="utf-8") as f:

            for usuario in self.usuarios.values():

                f.write(f"{usuario.nombre}|{usuario.id_usuario}\n")

        print("Datos guardados.")


    # ==========================================
    # CARGAR DATOS
    # ==========================================
    def cargar_datos(self):

        try:

            with open("libros.txt","r",encoding="utf-8") as f:

                for linea in f:

                    titulo,autor,categoria,isbn,prestado = linea.strip().split("|")

                    libro = Libro(titulo,autor,categoria,isbn)

                    libro.prestado = prestado == "True"

                    self.libros[isbn] = libro

        except:
            pass


        try:

            with open("usuarios.txt","r",encoding="utf-8") as f:

                for linea in f:

                    nombre,id_usuario = linea.strip().split("|")

                    usuario = Usuario(nombre,id_usuario)

                    self.usuarios[id_usuario] = usuario

                    self.ids_usuarios.add(id_usuario)

        except:
            pass