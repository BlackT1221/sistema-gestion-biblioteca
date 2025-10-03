# Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca implementado en **Python**. Permite administrar libros, usuarios y préstamos mediante una interfaz de consola sencilla.

---

## Índice

- [Descripción](#descripción)  
- [Características](#características)  
- [Estructura del proyecto](#estructura-del-proyecto)  
- [Requisitos](#requisitos)  
- [Instalación](#instalación)  
- [Uso](#uso)  
- [Ejemplos](#ejemplos)  
- [Contribuir](#contribuir)  
- [Licencia](#licencia)  
- [Autor / Contacto](#autor--contacto)

---

## Descripción

Proyecto orientado a prácticas docentes/personales para gestionar operaciones típicas de una biblioteca (registro de libros y usuarios, préstamos y devoluciones) usando estructuras de datos lineales en Python.

---

## Características

- Registrar, editar y consultar **libros** y **usuarios**.  
- Gestionar **préstamos** (prestar / devolver).  
- Comprobación de disponibilidad de ejemplares.  
- Interfaz de consola (CLI) simple.  
- Datos de prueba incluidos para pruebas rápidas.

---

## Estructura del proyecto

sistema-gestion-biblioteca/
├── main.py # Punto de entrada
├── sistema_core.py # Lógica del sistema (operaciones)
├── modelos.py # Clases: Libro, Usuario, Prestamo, ...
├── interfaz.py # Menús / interacción con usuario
├── estructuras_datos.py # Implementaciones de listas/colas/pilas
├── datos_prueba.py # Datos iniciales para pruebas
└── README.md

- `main.py` → llama al módulo de interfaz u orquesta el flujo principal.  
- `sistema_core.py` → contiene las operaciones (agregar, eliminar, prestar, etc.).  
- `modelos.py` → define los objetos utilizados (Libro, Usuario, Préstamo).  
- `estructuras_datos.py` → aquí están las listas, colas o pilas usadas.  
- `interfaz.py` → gestiona la interacción con el usuario (menús, entrada/salida).  
- `datos_prueba.py` → incluye datos predefinidos para levantar el sistema con ejemplos.  

---

## Requisitos

- Python 3.7 o superior  
- No depende de librerías externas (por ahora)  
- (Opcional) Un entorno virtual para facilitar instalación aislada  

---

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/BlackT1221/sistema-gestion-biblioteca.git
   cd sistema-gestion-biblioteca
   ```
2. (Opcional) Crea y activa un entorno virtual:
   ```bash
    python3 -m venv venv
    source venv/bin/activate   # macOS / Linux
    venv\Scripts\activate      # Windows
   ```

## Uso

Ejecuta el programa principal:

   ```bash
   python main.py
   ```

Sigue las opciones del menú para:

- Añadir / editar / listar libros y usuarios.
- Prestar o devolver libros.
- Cargar datos de prueba.
- Salir del programa.

## Ejemplos de flujo

1. Iniciar: python main.py.
2. Cargar datos de prueba.
3. Listar catálogo de libros.
4. Prestar libro X al usuario Y.
5. Verificar estado del préstamo.
6. Devolver el libro.

## Autor || Contacto

Autor: Christian Martinez
Correo: cdmartinez1121@gmail.com