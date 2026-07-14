import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, CheckButtons
import numpy as np
import csv
from typing import Callable, Tuple, Any

def configurar_estilo_apa() -> None:
    """Configura los gráficos con estilo profesional (APA)."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 12,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'legend.fontsize': 10,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'grid.color': 'gray',
        'grid.linestyle': '--',
        'grid.linewidth': 0.5
    })

def graficar_trayectorias(resultados_ideal: Tuple[np.ndarray, np.ndarray], 
                          resultados_real: Tuple[np.ndarray, np.ndarray]) -> None:
    """Genera gráfico comparativo de trayectorias X-Y.

    Args:
        resultados_ideal: (tiempos, estados) ideal.
        resultados_real: (tiempos, estados) real.
    """
    configurar_estilo_apa()
    _, estados_ideal = resultados_ideal
    _, estados_real = resultados_real

    plt.figure(figsize=(10, 6))
    plt.plot(estados_ideal[:, 0], estados_ideal[:, 1], label='Ideal', linestyle='--')
    plt.plot(estados_real[:, 0], estados_real[:, 1], label='Real (con arrastre)')
    plt.xlabel('Posición X [m]')
    plt.ylabel('Posición Y [m]')
    plt.title('Trayectoria del Proyectil')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def graficar_energia(proyectil: Any, resultados_ideal: Tuple[np.ndarray, np.ndarray], 
                     resultados_real: Tuple[np.ndarray, np.ndarray]) -> None:
    """Genera gráfico comparativo de energía mecánica total vs. tiempo.

    Args:
        proyectil: Instancia de Proyectil.
        resultados_ideal: (tiempos, estados) ideal.
        resultados_real: (tiempos, estados) real.
    """
    configurar_estilo_apa()
    tiempos_ideal, estados_ideal = resultados_ideal
    tiempos_real, estados_real = resultados_real

    energia_ideal = [proyectil.energia_mecanica(e) for e in estados_ideal]
    energia_real = [proyectil.energia_mecanica(e) for e in estados_real]

    plt.figure(figsize=(10, 6))
    plt.plot(tiempos_ideal, energia_ideal, label='Ideal')
    plt.plot(tiempos_real, energia_real, label='Real (con arrastre)')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Energía Mecánica [J]')
    plt.title('Energía Mecánica vs Tiempo')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def animar_trayectoria(proyectil: Any, resultados: Tuple[np.ndarray, np.ndarray]) -> None:
    """Animación de la trayectoria utilizando FuncAnimation.

    Args:
        proyectil: Instancia de Proyectil.
        resultados: (tiempos, estados).
    """
    tiempos, estados = resultados
    fig, ax = plt.subplots(figsize=(10, 6))
    
    x_min, x_max = np.min(estados[:, 0]), np.max(estados[:, 0])
    y_min, y_max = np.min(estados[:, 1]), np.max(estados[:, 1])
    
    ax.set_xlim(x_min - 1, x_max + 1)
    ax.set_ylim(y_min - 1, y_max + 1)
    ax.set_xlabel('Posición X [m]')
    ax.set_ylabel('Posición Y [m]')
    ax.set_title('Animación de la Trayectoria')
    ax.grid(True)
    
    punto, = ax.plot([], [], 'ro')
    linea, = ax.plot([], [], 'b-')

    def init():
        punto.set_data([], [])
        linea.set_data([], [])
        return punto, linea

    def update(frame):
        punto.set_data([estados[frame, 0]], [estados[frame, 1]])
        linea.set_data(estados[:frame+1, 0], estados[:frame+1, 1])
        return punto, linea

    ani = FuncAnimation(fig, update, frames=len(tiempos), init_func=init, blit=True, interval=20)
    plt.show()

def graficar_interactivo(proyectil: Any, t_max: float, dt: float, 
                         funcion_simular: Callable) -> None:
    """Interfaz interactiva para modificar parámetros."""
    configurar_estilo_apa()
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.35)

    v0_init = np.sqrt(proyectil.vx0**2 + proyectil.vy0**2)
    theta_init = np.degrees(np.arctan2(proyectil.vy0, proyectil.vx0))
    
    ax.set_xlabel('Posición X [m]')
    ax.set_ylabel('Posición Y [m]')
    ax.set_title('Simulación Interactiva')
    ax.grid(True)
    
    ax_v0 = plt.axes([0.2, 0.23, 0.65, 0.03])
    ax_theta = plt.axes([0.2, 0.18, 0.65, 0.03])
    ax_y0 = plt.axes([0.2, 0.13, 0.65, 0.03])
    ax_arrastre = plt.axes([0.2, 0.08, 0.65, 0.03])
    
    s_v0 = Slider(ax_v0, 'V0 [m/s]', 0.1, 100.0, valinit=v0_init)
    s_theta = Slider(ax_theta, 'Theta [°]', 0.0, 90.0, valinit=theta_init)
    s_y0 = Slider(ax_y0, 'y0 [m]', 0.0, 50.0, valinit=proyectil.y0)
    s_arrastre = Slider(ax_arrastre, 'Arrastre', 0.0, 1.0, valinit=proyectil.coef_arrastre)
    
    ax_button = plt.axes([0.8, 0.02, 0.15, 0.04])
    btn_lanzar = Button(ax_button, 'Lanzar')
    
    ax_hold = plt.axes([0.05, 0.02, 0.1, 0.04])
    cb_hold = CheckButtons(ax_hold, ['Hold'], [False])
    
    ax_export = plt.axes([0.35, 0.02, 0.15, 0.04])
    btn_export = Button(ax_export, 'Exportar CSV')
    
    ani = None
    last_results = None
    
    def actualizar_parametros(val):
        # Validación
        v0 = max(0.1, s_v0.val)
        theta = np.radians(s_theta.val)
        y0 = max(0.0, s_y0.val)
        arrastre = max(0.0, s_arrastre.val)
        
        proyectil.vx0 = v0 * np.cos(theta)
        proyectil.vy0 = v0 * np.sin(theta)
        proyectil.y0 = y0
        proyectil.coef_arrastre = arrastre
        
    def ejecutar_lanzamiento(event):
        nonlocal ani, last_results
        if ani is not None and ani.event_source is not None:
            ani.event_source.stop()

        if not cb_hold.get_status()[0]:
            for line in ax.lines:
                line.remove()
            
        tiempos_nuevos, estados_nuevos = funcion_simular(proyectil, t_max, dt, con_resistencia=True)
        last_results = (tiempos_nuevos, estados_nuevos)
        
        linea, = ax.plot(estados_nuevos[:, 0], estados_nuevos[:, 1], '-')
        punto, = ax.plot([], [], 'ro', markersize=8)
        
        x_min, x_max = np.min(estados_nuevos[:, 0]), np.max(estados_nuevos[:, 0])
        y_min, y_max = np.min(estados_nuevos[:, 1]), np.max(estados_nuevos[:, 1])
        
        padding = 5
        ax.set_xlim(x_min - padding, x_max + padding)
        ax.set_ylim(min(y_min, 0) - padding, y_max + padding)
        
        def init():
            punto.set_data([], [])
            return punto,
        
        def update(frame):
            punto.set_data([estados_nuevos[frame, 0]], [estados_nuevos[frame, 1]])
            return punto,
        
        ani = FuncAnimation(fig, update, frames=len(estados_nuevos), init_func=init, blit=True, interval=20, repeat=False)
        fig.canvas.draw_idle()
        
    def exportar_csv(event):
        if last_results is not None:
            tiempos, estados = last_results
            with open('simulacion_exportada.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['tiempo', 'x', 'y', 'vx', 'vy'])
                for i in range(len(tiempos)):
                    writer.writerow([tiempos[i], estados[i, 0], estados[i, 1], estados[i, 2], estados[i, 3]])
            print("Datos exportados a simulacion_exportada.csv")
        
    s_v0.on_changed(actualizar_parametros)
    s_theta.on_changed(actualizar_parametros)
    s_y0.on_changed(actualizar_parametros)
    s_arrastre.on_changed(actualizar_parametros)
    btn_lanzar.on_clicked(ejecutar_lanzamiento)
    btn_export.on_clicked(exportar_csv)
    
    plt.show()
