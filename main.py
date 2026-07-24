from proyectil import Proyectil
from simulador import simular
from graficador import graficar_interactivo

def main():
    # Configuración de parámetros iniciales
    params = {
        'x0': 0.0, 'y0': 0.0,
        'vx0': 20.0, 'vy0': 20.0,
        'masa': 1.0, 'coef_arrastre': 0.05,
        'gravedad': 9.81
    }
    p = Proyectil(**params)

    # Ejecución de la interfaz interactiva
    graficar_interactivo(p, 0.01, simular)

if __name__ == "__main__":
    main()
