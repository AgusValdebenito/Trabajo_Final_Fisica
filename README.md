# Trabajo Final Integrador - Física
**Carrera:** Ingeniería en Informática  
**Cátedra:** Física  
**Universidad:** Universidad de Mendoza  

---

## 1. Proyecto
**Título:** Simulación computacional del tiro parabólico: comparación de movimiento ideal y real.

### Justificación
Este proyecto integra los contenidos de cinemática y leyes de Newton con herramientas de modelización computacional en Python. Permite contrastar el movimiento ideal (solución analítica cerrada) con el movimiento real sujeto a resistencia cuadrática del aire (resolución numérica mediante RK4), facilitando un análisis crítico fundamentado en la teoría física.

---

## 2. Entregables
De acuerdo con las exigencias de la cátedra, el grupo presentará:

1.  **Código fuente en Python:** Debidamente documentado, organizado en módulos y funcional.
2.  **Informe escrito (máx. 10 páginas):**
    *   Introducción teórica.
    *   Desarrollo del modelo físico y método numérico (RK4).
    *   Resultados obtenidos (gráficos, tablas, animaciones).
    *   Análisis crítico y comparación: Teoría ideal vs. Simulación real.
    *   Conclusiones.
3.  **Exposición oral (15 min):** Defensa del trabajo y demostración en vivo de la simulación.

---

## 3. División de tareas
Para asegurar un equilibrio de carga, se establece la siguiente división basada en el dominio técnico y conceptual:

| Integrante | Área de enfoque | Responsabilidades clave |
|------------|-----------------|-------------------------|
| **Agus** | **Física y Cálculo** | Modelado matemático, leyes de Newton, ecuaciones de resistencia, integración numérica (RK4), validación de consistencia física. |
| **Ale** | **Visualización e Informe** | Interfaz (GUI/CLI), animaciones (`matplotlib.animation`), coherencia visual, redacción del informe técnico, revisión de formato APA. |

*Ambos integrantes son responsables de la calidad final y de asegurar que el acoplamiento entre el motor físico (Agus) y la capa de presentación (Ale) sea limpio y mantenible.*

---

## 4. Instalación
```bash
pip install -r requirements.txt
```

## 5. Ejecución
```bash
python main.py
```

## 6. Roadmap
| Hito | Descripción | Responsable |
|------|-------------|-------------|
| 1 | Definición del modelo físico (Ideal vs. Real) | Agus |
| 2 | Implementación del motor numérico (RK4) | Agus |
| 3 | Desarrollo de interfaz y animaciones | Ale |
| 4 | Integración y validación (física + visual) | Ambos |
| 5 | Mejora de exportación CSV y mensajes de error | Ale |
| 6 | Corrección de errores y limpieza de código muerto | Ambos |
| 7 | Redacción del informe y registro de prompts IA | Ale |
| 8 | Preparación de la exposición oral | Ambos |

---

## 7. Uso responsable de IA
Este proyecto se adhiere a las pautas de la cátedra sobre el uso de Inteligencia Artificial. La IA se utiliza como asistente de aprendizaje para exploración conceptual, verificación de sintaxis y retroalimentación formativa.

*   **Política:** El código, el análisis crítico y la defensa son de autoría exclusiva del grupo.
*   **Validación:** Se incluye en la carpeta `/docs` el **"Registro de uso de IA"** (basado en el Anexo C de la cátedra), donde se detallan los prompts utilizados, el contexto de uso y las validaciones humanas realizadas.

---

## 8. Criterios de evaluación (Checklist)
- [ ] **Modelado físico (30%):** Correcta aplicación de leyes y ecuaciones.
- [ ] **Calidad de programación (30%):** POO, modularidad, uso de librerías (`numpy`, `matplotlib`).
- [ ] **Análisis de resultados (20%):** Comparación trayectoria ideal vs. real (resistencia cuadrática).
- [ ] **Presentación (20%):** Informe técnico claro, calidad de gráficos y defensa oral.

## 9. Funcionalidades implementadas
- Interfaz interactiva con sliders (Velocidad, Ángulo, Altura inicial, Coef. arrastre)
- Botón "Lanzar" con animación progresiva de la trayectoria
- Checkbox "Fijar" para superponer trayectorias con colores distintos
- Exportación de datos a CSV con metadatos y timestamp
- Corte automático de la simulación al llegar al piso (y=0)
- Cálculo dinámico del tiempo de vuelo
- Validación de parámetros (masa > 0, dt > 0)
