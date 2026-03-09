# ==========================================
# MAIN
# Punto de entrada del sistema
# ==========================================

from servicios.biblioteca_servicio import BibliotecaServicio


def menu():

    print("\n===== BIBLIOTECA DIGITAL DG =====")

    print("1. Agregar libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar por titulo")
    print("8. Buscar por autor")
    print("9. Buscar por categoria")
    print("10. Libros de usuario")
    print("11. Guardar y salir")


def main():

    biblioteca = BibliotecaServicio()

    biblioteca.cargar_datos()

    while True:

        menu()

        opcion = input("Seleccione opción: ")

        if opcion == "1":

            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoria: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo,autor,categoria,isbn)


        elif opcion == "2":

            isbn = input("ISBN: ")

            biblioteca.quitar_libro(isbn)


        elif opcion == "3":

            nombre = input("Nombre: ")
            id_usuario = input("ID: ")

            biblioteca.registrar_usuario(nombre,id_usuario)


        elif opcion == "4":

            id_usuario = input("ID: ")

            biblioteca.eliminar_usuario(id_usuario)


        elif opcion == "5":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.prestar_libro(id_usuario,isbn)


        elif opcion == "6":

            id_usuario = input("ID usuario: ")
            isbn = input("ISBN libro: ")

            biblioteca.devolver_libro(id_usuario,isbn)


        elif opcion == "7":

            titulo = input("Titulo: ")

            biblioteca.buscar_titulo(titulo)


        elif opcion == "8":

            autor = input("Autor: ")

            biblioteca.buscar_autor(autor)


        elif opcion == "9":

            categoria = input("Categoria: ")

            biblioteca.buscar_categoria(categoria)


        elif opcion == "10":

            id_usuario = input("ID usuario: ")

            biblioteca.libros_usuario(id_usuario)


        elif opcion == "11":

            biblioteca.guardar_datos()

            print("Sistema cerrado.")

            break


if __name__ == "__main__":
    main()