import numpy as np
from typing import Callable, Tuple
from proyectil import Proyectil

def paso_rk4(f: Callable[[np.ndarray, float], np.ndarray], 
             y: np.ndarray, t: float, dt: float) -> np.ndarray:
    """Realiza un paso del método Runge-Kutta de cuarto orden (RK4).

    Args:
        f (Callable): Función que devuelve las derivadas del estado.
        y (np.ndarray): Estado actual.
        t (float): Tiempo actual.
        dt (float): Paso de tiempo.

    Returns:
        np.ndarray: Nuevo estado tras el paso dt.
    """
    k1 = f(y, t)
    k2 = f(y + 0.5 * dt * k1, t + 0.5 * dt)
    k3 = f(y + 0.5 * dt * k2, t + 0.5 * dt)
    k4 = f(y + dt * k3, t + dt)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

def simular(proyectil: Proyectil, t_max: float, dt: float, 
            con_resistencia: bool = False) -> Tuple[np.ndarray, np.ndarray]:
    """Simula la trayectoria de un proyectil utilizando el método RK4.

    Args:
        proyectil (Proyectil): Instancia del objeto proyectil.
        t_max (float): Tiempo total de simulación [s].
        dt (float): Paso de tiempo [s].
        con_resistencia (bool): Si True, considera la resistencia aerodinámica.

    Returns:
        Tuple[np.ndarray, np.ndarray]: (tiempos, estados) donde estados 
                                       contiene [x, y, vx, vy].
    """
    estado = np.array([proyectil.x0, proyectil.y0, proyectil.vx0, proyectil.vy0], dtype=float)
    tiempos = [0.0]
    estados = [estado.copy()]
    t = 0.0
    while t < t_max:
        t += dt
        estado = paso_rk4(lambda y, t: proyectil.derivadas(y, con_resistencia), estado, t, dt)
        tiempos.append(t)
        estados.append(estado.copy())
    return np.array(tiempos), np.array(estados)
