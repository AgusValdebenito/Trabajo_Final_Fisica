import numpy as np
from typing import Union

class Proyectil:
    """Representa un proyectil con física básica y resistencia aerodinámica.

    Attributes:
        x0 (float): Posición inicial en X [m].
        y0 (float): Posición inicial en Y [m].
        vx0 (float): Velocidad inicial en X [m/s].
        vy0 (float): Velocidad inicial en Y [m/s].
        masa (float): Masa del proyectil [kg].
        coef_arrastre (float): Coeficiente de arrastre [kg/s].
        gravedad (float): Aceleración gravitatoria [m/s^2].
    """
    def __init__(self, x0: float = 0.0, y0: float = 0.0, vx0: float = 10.0, 
                 vy0: float = 10.0, masa: float = 1.0, coef_arrastre: float = 0.01, 
                 gravedad: float = 9.81):
        self.x0 = x0
        self.y0 = y0
        self.vx0 = vx0
        self.vy0 = vy0
        self.masa = masa
        self.coef_arrastre = coef_arrastre
        self.gravedad = gravedad

    def derivadas(self, estado: np.ndarray, con_resistencia: bool = False) -> np.ndarray:
        """Calcula las derivadas del estado (x, y, vx, vy) respecto al tiempo.

        Args:
            estado (np.ndarray): Vector de estado [x, y, vx, vy].
            con_resistencia (bool): Si True, aplica arrastre aerodinámico.

        Returns:
            np.ndarray: Derivadas [vx, vy, dvx/dt, dvy/dt].
        """
        x, y, vx, vy = estado
        if con_resistencia:
            v = np.sqrt(vx**2 + vy**2)
            dvx_dt = -(self.coef_arrastre / self.masa) * v * vx
            dvy_dt = -self.gravedad - (self.coef_arrastre / self.masa) * v * vy
        else:
            dvx_dt = 0.0
            dvy_dt = -self.gravedad
        return np.array([vx, vy, dvx_dt, dvy_dt])

    def energia_cinetica(self, estado: np.ndarray) -> float:
        """Calcula la energía cinética del proyectil.

        Args:
            estado (np.ndarray): Vector de estado [x, y, vx, vy].

        Returns:
            float: Energía cinética [J].
        """
        _, _, vx, vy = estado
        return 0.5 * self.masa * (vx**2 + vy**2)

    def energia_potencial(self, estado: np.ndarray) -> float:
        """Calcula la energía potencial gravitatoria del proyectil.

        Args:
            estado (np.ndarray): Vector de estado [x, y, vx, vy].

        Returns:
            float: Energía potencial [J].
        """
        _, y, _, _ = estado
        return self.masa * self.gravedad * y

    def energia_mecanica(self, estado: np.ndarray) -> float:
        """Calcula la energía mecánica total del proyectil.

        Args:
            estado (np.ndarray): Vector de estado [x, y, vx, vy].

        Returns:
            float: Energía mecánica total [J].
        """
        return self.energia_cinetica(estado) + self.energia_potencial(estado)
