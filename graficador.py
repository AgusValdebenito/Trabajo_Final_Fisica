import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button, CheckButtons
import numpy as np
import csv
from datetime import datetime
from typing import Callable
from proyectil import Proyectil

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

def graficar_interactivo(proyectil: Proyectil, dt: float, 
                         funcion_simular: Callable) -> None:
    """Interfaz interactiva para modificar parámetros."""
    configurar_estilo_apa()
    fig, ax = plt.subplots(figsize=(10, 8))
    plt.subplots_adjust(bottom=0.35)

    v0_init = np.sqrt(proyectil.vx0**2 + proyectil.vy0**2)
    theta_init = np.degrees(np.arctan2(proyectil.vy0, proyectil.vx0))
    
    ax.set_xlabel('Posición X [m]')
    ax.set_ylabel('Posición Y [m]')
    ax.set_title('Simulación de Tiro Parabólico')
    ax.grid(True)
    
    ax_v0 = plt.axes([0.2, 0.23, 0.65, 0.03])
    ax_theta = plt.axes([0.2, 0.18, 0.65, 0.03])
    ax_y0 = plt.axes([0.2, 0.13, 0.65, 0.03])
    ax_arrastre = plt.axes([0.2, 0.08, 0.65, 0.03])
    
    s_v0 = Slider(ax_v0, 'Velocidad [m/s]', 0.1, 100.0, valinit=v0_init)
    s_theta = Slider(ax_theta, 'Ángulo [°]', 0.0, 90.0, valinit=theta_init)
    s_y0 = Slider(ax_y0, 'Altura inicial [m]', 0.0, 50.0, valinit=proyectil.y0)
    s_arrastre = Slider(ax_arrastre, 'Coef. arrastre [kg/s]', 0.0, 0.5, valinit=proyectil.coef_arrastre)
    
    ax_button = plt.axes([0.8, 0.02, 0.15, 0.04])
    btn_lanzar = Button(ax_button, 'Lanzar')
    
    ax_hold = plt.axes([0.05, 0.02, 0.1, 0.04])
    cb_hold = CheckButtons(ax_hold, ['Fijar'], [False])
    
    ax_export = plt.axes([0.35, 0.02, 0.15, 0.04])
    btn_export = Button(ax_export, 'Exportar CSV')
    
    animacion = None
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
        nonlocal animacion, last_results
        if animacion is not None and animacion.event_source is not None:
            animacion.event_source.stop()

        if not cb_hold.get_status()[0]:
            for line in ax.lines:
                line.remove()
        
        t_vuelo_est = (proyectil.vy0 + np.sqrt(proyectil.vy0**2 + 2 * proyectil.gravedad * proyectil.y0)) / proyectil.gravedad
        t_max_dinamico = max(t_vuelo_est * 1.5, 2.0)
        tiempos_nuevos, estados_nuevos = funcion_simular(proyectil, t_max_dinamico, dt, con_resistencia=True)
        last_results = (tiempos_nuevos, estados_nuevos)
        
        color = plt.cm.tab10(len(ax.lines) % 10)
        linea, = ax.plot(estados_nuevos[:, 0], estados_nuevos[:, 1], color=color)
        punto, = ax.plot([], [], 'ro', markersize=8)
        
        x_min, x_max = np.min(estados_nuevos[:, 0]), np.max(estados_nuevos[:, 0])
        y_max = np.max(estados_nuevos[:, 1])
        
        padding = 5
        ax.set_xlim(x_min - padding, x_max + padding)
        ax.set_ylim(0 - padding, y_max + padding)
        
        def init():
            punto.set_data([], [])
            return punto,
        
        def update(frame):
            punto.set_data([estados_nuevos[frame, 0]], [estados_nuevos[frame, 1]])
            return punto,
        
        animacion = FuncAnimation(fig, update, frames=len(estados_nuevos), init_func=init, blit=True, interval=20, repeat=False)
        fig.canvas.draw_idle()
        
    def exportar_csv(event):
        if last_results is None:
            print("No hay datos. Ejecute un lanzamiento primero.")
            return
        tiempos, estados = last_results
        import os

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.abspath(f'simulacion_{timestamp}.csv')

        v0 = round(np.sqrt(proyectil.vx0**2 + proyectil.vy0**2), 2)
        theta = round(np.degrees(np.arctan2(proyectil.vy0, proyectil.vx0)), 1)

        mask_above = estados[:, 1] >= 0
        idx_ground = np.where(mask_above)[0][-1] if np.any(mask_above) else len(estados) - 1
        t_vuelo = round(tiempos[idx_ground], 2)
        alcance = round(estados[idx_ground, 0], 2)

        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            f.write(f"# Parametros: v0={v0} m/s, theta={theta}\u00b0, arrastre={proyectil.coef_arrastre}, gravedad={proyectil.gravedad}\n")
            f.write(f"# Tiempo de vuelo: {t_vuelo} s, Alcance: {alcance} m\n")
            writer = csv.writer(f)
            writer.writerow(['tiempo', 'x', 'y', 'vx', 'vy'])
            for i in range(len(tiempos)):
                writer.writerow([round(tiempos[i], 3), round(estados[i, 0], 3), round(estados[i, 1], 3), round(estados[i, 2], 3), round(estados[i, 3], 3)])
        print(f"Datos exportados a: {ruta}")
        
    s_v0.on_changed(actualizar_parametros)
    s_theta.on_changed(actualizar_parametros)
    s_y0.on_changed(actualizar_parametros)
    s_arrastre.on_changed(actualizar_parametros)
    btn_lanzar.on_clicked(ejecutar_lanzamiento)
    btn_export.on_clicked(exportar_csv)
    
    plt.show()
