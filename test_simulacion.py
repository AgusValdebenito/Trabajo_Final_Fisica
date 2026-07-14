import numpy as np
from proyectil import Proyectil
from simulador import simular

def test_conservacion_sin_resistencia():
    p = Proyectil(vx0=30.0, vy0=40.0)
    t, estados = simular(p, t_max=5.0, dt=0.01, con_resistencia=False)
    e0 = p.energia_mecanica(estados[0])
    for i in range(len(estados)):
        if abs(p.energia_mecanica(estados[i]) - e0) > 0.01:
            return False, f"Energia cambio de {e0:.6f} a {p.energia_mecanica(estados[i]):.6f}"
    return True, ""

def test_disipacion_con_resistencia():
    p = Proyectil(vx0=30.0, vy0=40.0, coef_arrastre=0.1)
    t, estados = simular(p, t_max=5.0, dt=0.01, con_resistencia=True)
    e0 = p.energia_mecanica(estados[0])
    ef = p.energia_mecanica(estados[-1])
    if ef >= e0:
        return False, f"Energia final {ef:.6f} no es menor que inicial {e0:.6f}"
    return True, ""

def test_alcance_ideal_mayor():
    p_ideal = Proyectil(vx0=30.0, vy0=40.0)
    p_real = Proyectil(vx0=30.0, vy0=40.0, coef_arrastre=0.1)
    t_ideal, estados_ideal = simular(p_ideal, t_max=5.0, dt=0.01, con_resistencia=False)
    t_real, estados_real = simular(p_real, t_max=5.0, dt=0.01, con_resistencia=True)
    x_ideal = estados_ideal[-1, 0]
    x_real = estados_real[-1, 0]
    if x_ideal <= x_real:
        return False, f"Alcance ideal {x_ideal:.6f} no es mayor que real {x_real:.6f}"
    return True, ""

def test_rk4_analitico():
    p = Proyectil(vx0=30.0, vy0=40.0)
    t, estados = simular(p, t_max=5.0, dt=0.01, con_resistencia=False)
    indices = [int(len(t) / 4), int(len(t) / 2), int(3 * len(t) / 4)]
    for idx in indices:
        ti = t[idx]
        x_sim, y_sim = estados[idx, 0], estados[idx, 1]
        x_ana = p.vx0 * ti
        y_ana = p.vy0 * ti - 0.5 * p.gravedad * ti**2
        if abs(x_sim - x_ana) > 0.01 or abs(y_sim - y_ana) > 0.01:
            return False, f"En t={ti:.3f}: sim ({x_sim:.6f}, {y_sim:.6f}) vs ana ({x_ana:.6f}, {y_ana:.6f})"
    return True, ""

if __name__ == '__main__':
    tests = [
        ("Conservacion de energia sin resistencia", test_conservacion_sin_resistencia),
        ("Disipacion de energia con resistencia", test_disipacion_con_resistencia),
        ("Alcance ideal mayor que real", test_alcance_ideal_mayor),
        ("RK4 reproduce solucion analitica", test_rk4_analitico),
    ]
    passed = 0
    for nombre, fn in tests:
        ok, motivo = fn()
        if ok:
            print(f"OK: {nombre}")
            passed += 1
        else:
            print(f"FAIL: {nombre} - {motivo}")
    print(f"{passed}/{len(tests)} tests passed")
