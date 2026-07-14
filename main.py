from proyectil import Proyectil
from simulador import simular
from graficador import graficar_trayectorias, graficar_energia, animar_trayectoria, graficar_interactivo

def main():
    # Configuración de parámetros iniciales
    params = {
        'x0': 0.0, 'y0': 0.0,
        'vx0': 20.0, 'vy0': 20.0,
        'masa': 1.0, 'coef_arrastre': 0.05,
        'gravedad': 9.81
    }
    p = Proyectil(**params)
    t_max = 4.0
    dt = 0.01

    # Ejecución de la interfaz interactiva
    graficar_interactivo(p, t_max, dt, simular)

if __name__ == "__main__":
    main()
