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
    plt.subplots_adjust(bottom=0.5)

    v0_init = np.sqrt(proyectil.vx0**2 + proyectil.vy0**2)
    theta_init = np.degrees(np.arctan2(proyectil.vy0, proyectil.vx0))
    
    ax.set_xlabel('Posición X [m]')
    ax.set_ylabel('Posición Y [m]')
    ax.set_title('Simulación de Tiro Parabólico')
    ax.grid(True)
    
    ax_v0 = plt.axes((0.2, 0.40, 0.65, 0.03))
    ax_theta = plt.axes((0.2, 0.35, 0.65, 0.03))
    ax_y0 = plt.axes((0.2, 0.30, 0.65, 0.03))
    ax_arrastre = plt.axes((0.2, 0.25, 0.65, 0.03))
    ax_masa = plt.axes((0.2, 0.20, 0.65, 0.03))
    
    s_v0 = Slider(ax_v0, 'Velocidad [m/s]', 0.1, 100.0, valinit=v0_init)
    s_theta = Slider(ax_theta, 'Ángulo [°]', 0.0, 90.0, valinit=theta_init)
    s_y0 = Slider(ax_y0, 'Altura inicial [m]', 0.0, 50.0, valinit=proyectil.y0)
    s_arrastre = Slider(ax_arrastre, 'Coef. arrastre [kg/s]', 0.0, 0.5, valinit=proyectil.coef_arrastre)
    s_masa = Slider(ax_masa, 'Masa [kg]', 0.1, 20.0, valinit=proyectil.masa)
    
    ax_button = plt.axes((0.43, 0.03, 0.15, 0.05))
    btn_lanzar = Button(ax_button, 'Lanzar')
    
    ax_hold = plt.axes((0.28, 0.03, 0.10, 0.05))
    cb_hold = CheckButtons(ax_hold, ['Fijar'], [False])
    
    ax_comparativa = plt.axes((0.05, 0.03, 0.18, 0.05))
    cb_comparativa = CheckButtons(ax_comparativa, ['Ideal vs Real'], [False])
    
    ax_export = plt.axes((0.63, 0.03, 0.15, 0.05))
    btn_export = Button(ax_export, 'Exportar CSV')
    
    animacion = None
    last_results = None
    
    def actualizar_parametros(val):
        # Validación
        v0 = max(0.1, s_v0.val)
        theta = np.radians(s_theta.val)
        y0 = max(0.0, s_y0.val)
        arrastre = max(0.0, s_arrastre.val)
        masa = max(0.1, s_masa.val)
        
        proyectil.vx0 = v0 * np.cos(theta)
        proyectil.vy0 = v0 * np.sin(theta)
        proyectil.y0 = y0
        proyectil.coef_arrastre = arrastre
        proyectil.masa = masa
        
    def ejecutar_lanzamiento(event):
        nonlocal animacion, last_results
        if animacion is not None and animacion.event_source is not None:
            animacion.event_source.stop()

        if not cb_hold.get_status()[0]:
            for line in ax.lines:
                line.remove()
        
        t_vuelo_est = (proyectil.vy0 + np.sqrt(proyectil.vy0**2 + 2 * proyectil.gravedad * proyectil.y0)) / proyectil.gravedad
        t_max_dinamico = max(t_vuelo_est * 1.5, 2.0)
        
        def plotear_trayectoria(con_resistencia, label, estilo='-'):
            tiempos, estados = funcion_simular(proyectil, t_max_dinamico, dt, con_resistencia=con_resistencia)
            color = plt.cm.tab10(len(ax.lines) % 10)
            linea, = ax.plot(estados[:, 0], estados[:, 1], color=color, linestyle=estilo, label=label)
            return tiempos, estados
        
        if cb_comparativa.get_status()[0]:
            # Ideal
            plotear_trayectoria(False, 'Ideal', '--')
            # Real
            tiempos_nuevos, estados_nuevos = plotear_trayectoria(True, 'Real', '-')
        else:
            # Solo Real
            tiempos_nuevos, estados_nuevos = plotear_trayectoria(True, 'Real', '-')
            
        last_results = (tiempos_nuevos, estados_nuevos)
        
        # Limpiar textos y puntos anteriores para evitar superposición
        for txt in ax.texts:
            txt.remove()
        for line in ax.lines:
            if line.get_marker() == 'o':
                line.remove()

        # Animacion (sobre la trayectoria real)
        punto, = ax.plot([], [], 'ro', markersize=8)
        txt_metrics = ax.text(0.02, 0.98, '', transform=ax.transAxes, verticalalignment='top', fontsize=9, bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))
        
        x_min, x_max = np.min(estados_nuevos[:, 0]), np.max(estados_nuevos[:, 0])
        y_max = np.max(estados_nuevos[:, 1])
        
        # Padding dinámico: 5% del rango, mínimo 2 metros
        pad_x = max(2.0, (x_max - min(0, x_min)) * 0.05)
        pad_y = max(2.0, y_max * 0.05)
        
        ax.set_xlim(min(0, x_min - pad_x), x_max + pad_x)
        ax.set_ylim(min(0, -pad_y), y_max + pad_y)
        
        # Pre-calculos para metricas
        idx_ground = np.where(estados_nuevos[:, 1] >= 0)[0][-1] if np.any(estados_nuevos[:, 1] >= 0) else len(estados_nuevos) - 1
        alcance_max = round(estados_nuevos[idx_ground, 0], 2)
        altura_max = round(y_max, 2)
        tiempo_vuelo = round(tiempos_nuevos[idx_ground], 2)
        
        def init():
            punto.set_data([], [])
            txt_metrics.set_text('')
            return punto, txt_metrics
        
        def update(frame):
            x, y, vx, vy = estados_nuevos[frame]
            punto.set_data([x], [y])
            
            # Actualizar métricas
            e_mec = proyectil.masa * proyectil.gravedad * y + 0.5 * proyectil.masa * (vx**2 + vy**2)
            metrics_str = f"Alcance: {alcance_max} m\nAltura: {altura_max} m\nT. Vuelo: {tiempo_vuelo} s\nE. Mec: {e_mec:.1f} J"
            txt_metrics.set_text(metrics_str)
            
            return punto, txt_metrics
        
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
    s_masa.on_changed(actualizar_parametros)
    btn_lanzar.on_clicked(ejecutar_lanzamiento)
    btn_export.on_clicked(exportar_csv)
    
    plt.show()
