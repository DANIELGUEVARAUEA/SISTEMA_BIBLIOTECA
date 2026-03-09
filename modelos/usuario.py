# ==========================================
# MODELO USUARIO
# Representa un usuario de la biblioteca
# ==========================================

class Usuario:

    def __init__(self, nombre, id_usuario):

        # Nombre del usuario
        self.nombre = nombre

        # ID único del usuario
        self.id_usuario = id_usuario

        # Lista de libros prestados
        # REQUISITO: usar LISTA
        self.libros_prestados = []


    # ==========================================
    # PRESTAR LIBRO
    # ==========================================
    def prestar_libro(self, libro):

        self.libros_prestados.append(libro)


    # ==========================================
    # DEVOLVER LIBRO
    # ==========================================
    def devolver_libro(self, libro):

        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)


    # ==========================================
    # REPRESENTACIÓN DEL USUARIO
    # ==========================================
    def __str__(self):

        return f"{self.nombre} (ID:{self.id_usuario})"