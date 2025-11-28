import os
from collections import deque

# =======================================================
# NODO Y ÁRBOL BINARIO DE BÚSQUEDA (ABB)
# =======================================================

class Nodo:
    """Representa un nodo del árbol binario."""
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Implementación básica de un árbol binario de búsqueda (ABB)."""
    def __init__(self):
        self.raiz = None

    def insertar(self, clave, valor):
        """Inserta un nuevo nodo en el árbol manteniendo el orden."""
        if self.raiz is None:
            self.raiz = Nodo(clave, valor)
        else:
            self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if clave < nodo.clave:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            if nodo.derecho is None:
                nodo.derecho = Nodo(clave, valor)
            else:
                self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor  # Actualiza si la clave ya existe

    def buscar(self, clave):
        """Busca una clave dentro del árbol y devuelve el valor asociado."""
        return self._buscar_recursivo(self.raiz, clave)

    def _buscar_recursivo(self, nodo, clave):
        if nodo is None:
            return None
        if clave == nodo.clave:
            return nodo.valor
        elif clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        else:
            return self._buscar_recursivo(nodo.derecho, clave)

    def recorrer_inorden(self):
        """Devuelve una lista de los valores en orden ascendente."""
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izquierdo, lista)
            lista.append(nodo.valor)
            self._inorden(nodo.derecho, lista)

    def eliminar(self, clave):
        """Elimina un nodo por su clave."""
        self.raiz, eliminado = self._eliminar_recursivo(self.raiz, clave)
        return eliminado

    def _eliminar_recursivo(self, nodo, clave):
        if nodo is None:
            return nodo, False

        if clave < nodo.clave:
            nodo.izquierdo, eliminado = self._eliminar_recursivo(nodo.izquierdo, clave)
        elif clave > nodo.clave:
            nodo.derecho, eliminado = self._eliminar_recursivo(nodo.derecho, clave)
        else:
            # Nodo encontrado
            if nodo.izquierdo is None:
                return nodo.derecho, True
            elif nodo.derecho is None:
                return nodo.izquierdo, True

            sucesor = self._minimo(nodo.derecho)
            nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
            nodo.derecho, _ = self._eliminar_recursivo(nodo.derecho, sucesor.clave)
            return nodo, True

        return nodo, eliminado

    def _minimo(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual


# =======================================================
# SISTEMA DE GESTIÓN DE BIBLIOTECA (CON ÁRBOLES)
# =======================================================

class SistemaBiblioteca:
    """
    Sistema de gestión de biblioteca con árboles binarios.
    - Los libros y usuarios se almacenan en árboles binarios de búsqueda.
    - Los préstamos se manejan con una cola (deque).
    """

    def __init__(self):
        self.libros = ArbolBinarioBusqueda()
        self.usuarios = ArbolBinarioBusqueda()
        self.prestamos = deque()

    # ------------------- LIBROS -------------------

    def agregar_libro(self, codigo, titulo, autor, anio):
        if self.libros.buscar(codigo):
            print("\nYa existe un libro con ese código.")
            return
        libro = {
            "codigo": codigo,
            "titulo": titulo,
            "autor": autor,
            "anio": anio,
            "disponible": True
        }
        self.libros.insertar(codigo, libro)
        print("\nLibro agregado correctamente.")

    def editar_libro(self, codigo):
        libro = self.libros.buscar(codigo)
        if not libro:
            print("\nNo se encontró un libro con ese código.")
            return

        print(f"\nEditando el libro '{libro['titulo']}' (deje vacío para no modificar):")
        nuevo_titulo = input(f"Nuevo título [{libro['titulo']}]: ") or libro['titulo']
        nuevo_autor = input(f"Nuevo autor [{libro['autor']}]: ") or libro['autor']
        nuevo_anio = input(f"Nuevo año [{libro['anio']}]: ") or libro['anio']

        libro['titulo'] = nuevo_titulo
        libro['autor'] = nuevo_autor
        libro['anio'] = nuevo_anio
        print("\nLibro actualizado correctamente.")

    def eliminar_libro(self, codigo):
        eliminado = self.libros.eliminar(codigo)
        if eliminado:
            print("\nLibro eliminado exitosamente.")
        else:
            print("\nNo se encontró ningún libro con ese código.")

    def buscar_libro(self, codigo):
        libro = self.libros.buscar(codigo)
        if libro:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"\nLibro encontrado:\nTítulo: {libro['titulo']}\nAutor: {libro['autor']}\nAño: {libro['anio']}\nEstado: {estado}")
        else:
            print("\nNo se encontró ningún libro con ese código.")
        return libro

    def mostrar_libros(self):
        lista = self.libros.recorrer_inorden()
        if not lista:
            print("\nNo hay libros registrados.")
            return
        print("\nCatálogo de libros:")
        for libro in lista:
            estado = "Disponible" if libro["disponible"] else "Prestado"
            print(f"• {libro['codigo']} | {libro['titulo']} | {libro['autor']} | {libro['anio']} | {estado}")

    # ------------------- USUARIOS -------------------

    def agregar_usuario(self, cedula, nombre):
        if self.usuarios.buscar(cedula):
            print("\nYa existe un usuario con esa cédula.")
            return
        usuario = {"cedula": cedula, "nombre": nombre}
        self.usuarios.insertar(cedula, usuario)
        print("\nUsuario registrado correctamente.")

    def editar_usuario(self, cedula):
        usuario = self.usuarios.buscar(cedula)
        if not usuario:
            print("\nNo se encontró un usuario con esa cédula.")
            return

        print(f"\nEditando usuario '{usuario['nombre']}' (deje vacío para no modificar):")
        nuevo_nombre = input(f"Nuevo nombre [{usuario['nombre']}]: ") or usuario['nombre']
        usuario['nombre'] = nuevo_nombre
        print("\nUsuario actualizado correctamente.")

    def eliminar_usuario(self, cedula):
        eliminado = self.usuarios.eliminar(cedula)
        if eliminado:
            print("\nUsuario eliminado exitosamente.")
        else:
            print("\nNo se encontró ningún usuario con esa cédula.")

    def mostrar_usuarios(self):
        lista = self.usuarios.recorrer_inorden()
        if not lista:
            print("\nNo hay usuarios registrados.")
            return
        print("\nUsuarios registrados:")
        for usuario in lista:
            print(f"• {usuario['cedula']} - {usuario['nombre']}")

    # ------------------- PRÉSTAMOS -------------------

    def solicitar_prestamo(self, cedula, codigo_libro):
        usuario = self.usuarios.buscar(cedula)
        libro = self.libros.buscar(codigo_libro)

        if not usuario or not libro:
            print("\nError: usuario o libro no encontrado.")
            return

        if not libro["disponible"]:
            print("\nEl libro ya está prestado.")
            return

        libro["disponible"] = False
        self.prestamos.append((usuario, libro))
        print(f"\nPréstamo registrado: '{libro['titulo']}' para {usuario['nombre']}.")

    def devolver_libro(self):
        if not self.prestamos:
            print("\nNo hay préstamos pendientes.")
            return

        usuario, libro = self.prestamos.popleft()
        libro["disponible"] = True
        print(f"\nLibro devuelto: '{libro['titulo']}' por {usuario['nombre']}.")

    def mostrar_prestamos(self):
        if not self.prestamos:
            print("\nNo hay préstamos activos.")
            return
        print("\nPréstamos activos:")
        for usuario, libro in self.prestamos:
            print(f"• {usuario['nombre']} → {libro['titulo']} ({libro['autor']})")


# =======================================================
# MENÚ PRINCIPAL
# =======================================================

def menu():
    sistema = SistemaBiblioteca()

    while True:
        print("\n" + "-" * 50)
        print("SISTEMA DE GESTIÓN DE BIBLIOTECA (ÁRBOLES)")
        print("-" * 50)
        print("1. Agregar libro")
        print("2. Editar libro")
        print("3. Eliminar libro")
        print("4. Ver lista de libros")
        print("5. Buscar libro por código")
        print("6. Registrar usuario")
        print("7. Editar usuario")
        print("8. Eliminar usuario")
        print("9. Ver usuarios registrados")
        print("10. Solicitar préstamo")
        print("11. Devolver libro")
        print("12. Ver préstamos activos")
        print("13. Limpiar pantalla")
        print("14. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            codigo = input("Código del libro: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año de publicación: ")
            sistema.agregar_libro(codigo, titulo, autor, anio)

        elif opcion == "2":
            codigo = input("Código del libro a editar: ")
            sistema.editar_libro(codigo)

        elif opcion == "3":
            codigo = input("Código del libro a eliminar: ")
            sistema.eliminar_libro(codigo)

        elif opcion == "4":
            sistema.mostrar_libros()

        elif opcion == "5":
            codigo = input("Ingrese el código del libro: ")
            sistema.buscar_libro(codigo)

        elif opcion == "6":
            cedula = input("Cédula del usuario: ")
            nombre = input("Nombre del usuario: ")
            sistema.agregar_usuario(cedula, nombre)

        elif opcion == "7":
            cedula = input("Cédula del usuario a editar: ")
            sistema.editar_usuario(cedula)

        elif opcion == "8":
            cedula = input("Cédula del usuario a eliminar: ")
            sistema.eliminar_usuario(cedula)

        elif opcion == "9":
            sistema.mostrar_usuarios()

        elif opcion == "10":
            cedula = input("Cédula del usuario: ")
            codigo = input("Código del libro: ")
            sistema.solicitar_prestamo(cedula, codigo)

        elif opcion == "11":
            sistema.devolver_libro()

        elif opcion == "12":
            sistema.mostrar_prestamos()

        elif opcion == "13":
            os.system("cls" if os.name == "nt" else "clear")

        elif opcion == "14":
            print("\nGracias por usar el sistema.")
            break

        else:
            print("\nOpción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
