import numpy as np

def paso_rk4(f, y, t, dt):
    k1 = f(y, t)
    k2 = f(y + 0.5 * dt * k1, t + 0.5 * dt)
    k3 = f(y + 0.5 * dt * k2, t + 0.5 * dt)
    k4 = f(y + dt * k3, t + dt)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

def simular(proyectil, t_max, dt, con_resistencia=False):
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
