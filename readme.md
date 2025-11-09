# Sistema de Gestión de Biblioteca

Sistema de gestión de biblioteca implementado en **Python**, con enfoque en el uso de **estructuras de datos no lineales (árboles)** para mejorar la eficiencia en la manipulación y búsqueda de información.  
Esta versión amplía la etapa anterior del proyecto, incorporando **árboles binarios de búsqueda (BST)** y **árboles AVL balanceados**, junto con **pruebas automatizadas** y **benchmarks de rendimiento**.

---

## Índice

- [Descripción](#descripción)
- [Novedades de esta versión](#novedades-de-esta-versión)
- [Características](#características)
- [Estructura del proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Benchmarks y gráficas de rendimiento](#benchmarks-y-gráficas-de-rendimiento)
- [Pruebas unitarias](#pruebas-unitarias)
- [Contribuir](#contribuir)
- [Licencia](#licencia)
- [Autor / Contacto](#autor--contacto)

---

## Descripción

Este proyecto académico implementa un **Sistema de Gestión de Biblioteca** con operaciones de registro, préstamo y devolución de libros, así como administración de usuarios.  
La tercera fase se centra en **estructuras no lineales**, aplicando **árboles de búsqueda** y **árboles AVL** para optimizar la búsqueda y manipulación de datos.

---

## 🆕 Novedades de esta versión

- Implementación de **árboles binarios de búsqueda (ArbolBST)**.  
- Implementación de **árboles AVL balanceados (ArbolAVL)**.  
- Integración de un nuevo sistema `SistemaBibliotecaArbol` basado en árboles.  
- **Benchmarks de rendimiento** comparando BST, AVL y listas lineales.  
- **Gráficas de rendimiento** generadas automáticamente con Matplotlib.  
- **Pruebas unitarias e integración** usando `pytest`.  
- Documento de informe técnico en formato **APA 7 (PDF y DOCX)**.

---

## Características

- Registro, edición y consulta de **libros** y **usuarios**.  
- Gestión de **préstamos y devoluciones**.  
- Árboles de búsqueda para mejorar tiempos de búsqueda O(log n).  
- **AVL balanceado** para inserciones eficientes y consistentes.  
- **Benchmarks automáticos** y visualización comparativa (BST vs AVL vs Lista).  
- **Suite de pruebas** automatizada con `pytest`.

---

## Estructura del proyecto
```text
sistema-gestion-biblioteca/
├── main.py                        # Punto de entrada principal
├── sistema_core.py                # Lógica del sistema base
├── sistema_core_arbol.py          # Versión con árboles (BST / AVL)
├── modelos.py                     # Clases: Libro, Usuario, Prestamo
├── interfaz.py                    # Interfaz de consola (CLI)
├── estructuras_datos.py           # Listas, colas y pilas (versión anterior)
├── arboles.py                     # Implementación de árbol binario de búsqueda (BST)
├── arboles_avl.py                 # Implementación del árbol AVL
├── benchmarks.py                  # Pruebas de rendimiento (BST vs Lista)
├── bench_bst_vs_avl.py            # Comparativa BST vs AVL
├── grafico_benchmarks.py          # Generación de gráficas PNG
├── tests/
│   ├── test_bst.py                # Pruebas unitarias del BST
│   └── test_sistema_arbol.py      # Pruebas de integración del sistema con árboles
├── datos_prueba.py                # Datos de ejemplo
├── README.md
├── Actividad3_Sistema_Gestion_Biblioteca.pdf   # Informe en formato APA 7
└── Actividad3_Sistema_Gestion_Biblioteca.docx  # Versión editable del informe
```

---

## Requisitos

   - Python 3.8 o superior
   - Librerías requeridas:

---

```bash

   pip install matplotlib pytest reportlab python-docx

```

---

## Instalación

1. Clona el repositorio:

   ```bash
   git clone https://github.com/BlackT1221/sistema-gestion-biblioteca.git
   cd sistema-gestion-biblioteca
   ```

2. (Opcional) Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

---

## Uso

Ejecuta el programa principal:

   ```bash
   python main.py
   ```

O prueba la versión extendida con árboles:

   ```bash
   python main_arboles.py
   ```

Sigue las opciones del menú para:

- Añadir / editar / listar libros y usuarios.
- Prestar o devolver libros.
- Cargar datos de prueba.
- Salir del programa.

---

## Benchmarks y gráficas de rendimiento

Ejecuta los benchmarks:

   ```bash
   python benchmarks.py
   python bench_bst_vs_avl.py
   ```

Genera las gráficas comparativas:

   ```bash
   python grafico_benchmarks.py
   ```

📊 Se generarán los archivos:

   - grafico_aleatorio.png
   - grafico_ordenado.png

Que muestran el rendimiento de inserción y búsqueda en:

   - BST (árbol binario de búsqueda)
   - AVL (árbol balanceado)
   - Lista (estructura lineal)

---

## Pruebas unitarias

Ejecuta las pruebas con:

   ```bash
   python -m pytest -q
   ```

Incluye:

   - Pruebas del árbol binario (tests/test_bst.py).
   - Pruebas de integración con el sistema (tests/test_sistema_arbol.py).

Ejemplo de salida esperada:

   ```bash
   ...                                                                 [100%]
   3 passed in 0.05s
   ```

---

## Contribuir

Si deseas mejorar el proyecto:

   - Haz un fork del repositorio.
   - Crea una rama nueva (feature/nueva-funcionalidad).
   - Envía un pull request con tus cambios.
   
---

## Licencia

Este proyecto es de uso académico y educativo.
Puede ser reutilizado y adaptado citando al autor original.

## Autor / Contacto

Autor: Christian David Martínez Cruz
📧 Correo: cdmartinez1121@gmail.com
📅 Última actualización: 9 de noviembre de 2025