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

## 3. Tareas realizadas
- Modelado matemático del tiro parabólico con y sin resistencia aerodinámica
- Implementación del método numérico RK4 para integración de EDOs
- Desarrollo de interfaz gráfica interactiva con sliders, botones y animaciones
- Exportación de datos a CSV con metadatos
- Validación física y numérica de los resultados
- Redacción del informe técnico

## 4. Instalación
```bash
pip install -r requirements.txt
```

## 5. Ejecución
```bash
python main.py
```

## 6. Uso responsable de IA
Este proyecto se adhiere a las pautas de la cátedra sobre el uso de Inteligencia Artificial. La IA se utiliza como asistente de aprendizaje para exploración conceptual, verificación de sintaxis y retroalimentación formativa.

*   **Política:** El código, el análisis crítico y la defensa son de autoría exclusiva del grupo.
*   **Validación:** Se incluye un registro de uso de IA en el anexo del informe, detallando los prompts utilizados y las validaciones humanas realizadas.

---


## 7. Funcionalidades implementadas
- Interfaz interactiva con sliders (Velocidad, Ángulo, Altura inicial, Coef. arrastre)
- Botón "Lanzar" con animación progresiva de la trayectoria
- Checkbox "Fijar" para superponer trayectorias con colores distintos
- Exportación de datos a CSV con metadatos y timestamp
- Corte automático de la simulación al llegar al piso (y=0)
- Cálculo dinámico del tiempo de vuelo
- Validación de parámetros (masa > 0, dt > 0)
