import numpy as np

class Proyectil:
    def __init__(self, x0=0.0, y0=0.0, vx0=10.0, vy0=10.0, masa=1.0, coef_arrastre=0.01, gravedad=9.81):
        self.x0 = x0
        self.y0 = y0
        self.vx0 = vx0
        self.vy0 = vy0
        self.masa = masa
        self.coef_arrastre = coef_arrastre
        self.gravedad = gravedad

    def derivadas(self, estado, con_resistencia=False):
        x, y, vx, vy = estado
        if con_resistencia:
            v = np.sqrt(vx**2 + vy**2)
            dvx_dt = -(self.coef_arrastre / self.masa) * v * vx
            dvy_dt = -self.gravedad - (self.coef_arrastre / self.masa) * v * vy
        else:
            dvx_dt = 0.0
            dvy_dt = -self.gravedad
        return np.array([vx, vy, dvx_dt, dvy_dt])

    def energia_cinetica(self, estado):
        _, _, vx, vy = estado
        return 0.5 * self.masa * (vx**2 + vy**2)

    def energia_potencial(self, estado):
        _, y, _, _ = estado
        return self.masa * self.gravedad * y

    def energia_mecanica(self, estado):
        return self.energia_cinetica(estado) + self.energia_potencial(estado)
