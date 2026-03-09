# ==========================================
# MODELO LIBRO
# Representa un libro dentro del sistema
# ==========================================

class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # Se almacena título y autor en una TUPLA
        # porque son datos inmutables
        self.__datos = (titulo, autor)

        # Categoría del libro
        self.categoria = categoria

        # ISBN único del libro
        self.isbn = isbn

        # Estado del libro
        # False = disponible
        # True = prestado
        self.prestado = False


    # ==========================================
    # MÉTODOS DE ACCESO (ENCAPSULAMIENTO)
    # ==========================================

    def obtener_titulo(self):
        return self.__datos[0]

    def obtener_autor(self):
        return self.__datos[1]


    # ==========================================
    # REPRESENTACIÓN DEL LIBRO
    # ==========================================
    def __str__(self):

        estado = "Prestado" if self.prestado else "Disponible"

        return f"{self.obtener_titulo()} - {self.obtener_autor()} | {self.categoria} | ISBN:{self.isbn} | {estado}"