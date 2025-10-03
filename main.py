"""
Punto de entrada principal del Sistema de Gestión de Biblioteca
Autor: [Nombre del Estudiante]
Fecha: [Fecha]
"""

from sistema_core import SistemaGestionBiblioteca
from interfaz import main as interfaz_principal
from datos_prueba import cargar_datos_prueba

def main():
    """Función principal del sistema"""
    sistema = SistemaGestionBiblioteca()
    
    print("Bienvenido al Sistema de Gestión de Biblioteca")
    
    # Preguntar si cargar datos de prueba
    cargar_prueba = input("¿Desea cargar datos de prueba? (s/n): ").strip().lower()
    if cargar_prueba == 's':
        cargar_datos_prueba(sistema)
    
    # Iniciar interfaz principal
    interfaz_principal(sistema)

if __name__ == "__main__":
    main()