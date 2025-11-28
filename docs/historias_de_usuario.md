📄 Historias de Usuario – Sistema de Gestión de Biblioteca
HU-01 – Gestión de libros

Como bibliotecario
quiero registrar, editar y eliminar libros desde el sistema
para mantener actualizado el catálogo de la biblioteca.

Criterios de aceptación

El sistema debe validar si la clave/código del libro ya existe antes de agregarlo.

El sistema debe permitir editar título, autor y año dejando los valores actuales si el usuario no cambia el campo.

El sistema debe permitir eliminar libros y mostrar mensajes claros de éxito o error.

HU-02 – Consulta del catálogo de libros

Como usuario de la biblioteca o bibliotecario
quiero consultar la lista completa de libros y buscar un libro por su código
para conocer su disponibilidad y detalles.

Criterios de aceptación

El sistema debe mostrar todos los libros en orden ascendente por código.

Cada libro debe mostrar: código, título, autor, año y estado (Disponible/Prestado).

Al buscar un libro por código:

Si existe, se deben mostrar sus datos.

Si no existe, debe mostrar: “No se encontró ningún libro con ese código.”

Si no hay libros registrados, debe mostrar: “No hay libros registrados.”

HU-03 – Gestión de usuarios

Como bibliotecario
quiero registrar, editar y eliminar usuarios del sistema
para llevar un control de quién puede realizar préstamos de libros.

Criterios de aceptación

El sistema debe validar si ya existe un usuario con la misma cédula antes de registrarlo.

Al registrar un usuario exitosamente, debe mostrar: “Usuario registrado correctamente.”

Al editar un usuario:

Si la cédula existe, debe permitir modificar el nombre.

Si no existe, debe mostrar: “No se encontró un usuario con esa cédula.”

Al eliminar un usuario:

Si se elimina, debe mostrar: “Usuario eliminado exitosamente.”

Si no existe, debe mostrar: “No se encontró un usuario con esa cédula.”

El sistema debe mostrar una lista de todos los usuarios registrados.

HU-04 – Registro de préstamos

Como bibliotecario
quiero registrar préstamos de libros a los usuarios
para controlar qué usuario tiene cada libro y evitar prestar un libro ya prestado.

Criterios de aceptación

El sistema debe validar que el usuario y el libro existan; si no, debe mostrar: “Error: usuario o libro no encontrado.”

El sistema debe evitar prestar libros que ya están marcados como “Prestado”.

Al registrar un préstamo, el sistema debe:

Marcar el libro como no disponible.

Guardar el préstamo en la cola FIFO.

Mostrar un mensaje indicando el usuario y el libro prestado.

Si el libro ya está prestado, debe mostrar: “El libro ya está prestado.”

HU-05 – Gestión de devoluciones y préstamos activos

Como bibliotecario
quiero registrar la devolución de libros y visualizar todos los préstamos activos
para llevar un control claro del inventario prestado.

Criterios de aceptación

Si no hay préstamos pendientes, el sistema debe mostrar: “No hay préstamos pendientes.”

Al devolver un libro, debe tomarse el primer préstamo registrado (orden FIFO).

El sistema debe marcar el libro devuelto como disponible.

El sistema debe mostrar un mensaje indicando qué usuario devolvió qué libro.

Al ver préstamos activos:

Si no hay préstamos, debe mostrar: “No hay préstamos activos.”

Si los hay, debe listar usuario → libro (autor).