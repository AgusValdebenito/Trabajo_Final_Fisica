# Trabajo Final Integrador - Física

**Carrera:** Ingeniería en Informática  
**Cátedra:** Física  
**Universidad:** Universidad de Mendoza  

---

## Decisión del proyecto

**Opción elegida: A — Simulación del tiro parabólico con resistencia del aire**

### Justificación

Elegimos esta opción porque:

1. **Impacto visual** — las trayectorias con y sin resistencia se ven muy distintas y la animación es llamativa
2. **Dificultad moderada** — la física es cinemática básica (Unidad 2), no requiere conceptos avanzados
3. **Comparación teoría vs simulación** — la trayectoria ideal tiene solución analítica cerrada, la real se resuelve numéricamente, lo que permite contrastar ambas
4. **POO natural** — un proyectil es un objeto fácil de modelar con atributos y métodos

---

## Roadmap / Pasos a seguir

| Hito | Descripción | Archivos involucrados |
|------|-------------|----------------------|
| 1 | Clase `Proyectil` con atributos, derivadas y métodos de energía | `proyectil.py` |
| 2 | Función `paso_rk4` y `simular` para evolucionar el sistema | `simulador.py` |
| 3 | Gráficos comparativos de trayectorias y energía | `graficador.py` |
| 4 | Animación de la simulación | `graficador.py` |
| 5 | Orquestación y parámetros iniciales en `main.py` | `main.py` |
| 6 | Refinamiento de parámetros, ajustes visuales y documentación | Todos |

---

## División de tareas (2 integrantes)

| Integrante | Archivos | Responsabilidad |
|------------|----------|-----------------|
| **Persona 1** | `proyectil.py` + `simulador.py` | Modelo físico del proyectil + integración numérica RK4 |
| **Persona 2** | `graficador.py` + `main.py` | Visualizaciones (gráficos y animación) + orquestación |

Ninguno edita el mismo archivo al mismo tiempo.

---

## Especificaciones técnicas

> **Nota:** Estas son sugerencias iniciales. Pueden ser reevaluadas durante el avance del proyecto si encontramos una mejor forma de organizarnos.

| Aspecto | Elección inicial |
|---------|-----------------|
| Lenguaje | Python 3 |
| Paradigma | Programación Orientada a Objetos |
| Método numérico | Runge-Kutta 4 (RK4) |
| Librerías | `numpy`, `matplotlib` (+ `scipy` si es necesario) |
| Visualización | Gráficos estáticos + animación con `matplotlib.animation` |
| Organización | Módulos separados por responsabilidad |

---

## Criterios de evaluación — Checklist

- [ ] **Modelado físico (30%):** Leyes de Newton, cinemática, ecuaciones correctas
- [ ] **Calidad de programación (30%):** POO con clases, uso de librerías, código organizado en módulos
- [ ] **Análisis de resultados (20%):** Comparación trayectoria ideal vs real, gráficos de energía
- [ ] **Presentación (20%):** Informe claro, animaciones, gráficos con ejes y leyendas
- [ ] **Extra:** Animación funcionando, RK4 implementado, al menos 3 librerías científicas

---

## Material de referencia

- `Material de los profesores/` — PDFs y presentación con la consigna completa
- Python: `numpy.org`, `matplotlib.org`
- Runge-Kutta 4: explicación en `simulador.py`
