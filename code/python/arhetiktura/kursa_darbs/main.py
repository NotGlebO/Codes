import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider

def bezier(t, p0, p1, p2):
    return (1 - t)**2 * p0 + 2 * (1 - t) * t * p1 + t**2 * p2

def update(frame):
    t = frame / frames
    x, y = bezier(t, p0, p1, p2)
    trajectory.append((x, y))
    point.set_data(x, y)
    line.set_data(*zip(*trajectory))
    return point, line

def start_animation(event):
    animation.event_source.start()

def stop_animation(event):
    animation.event_source.stop()

# Создание фигуры и осей
fig, ax = plt.subplots()
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)

# Управляющие точки кривой Безье
p0 = np.array([1, 1])
p1 = np.array([2, 3])
p2 = np.array([4, 1])

# Отображение управляющих точек
control_points, = ax.plot([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], 'go', zorder=3)

# Обновление управляющих точек при перемещении
def update_control_points():
    control_points.set_data([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]])


def on_click(event):
    global p0, p1, p2
    if event.inaxes == ax:
        if np.linalg.norm(np.array([event.xdata, event.ydata]) - p0) < 0.1:
            p0[0], p0[1] = event.xdata, event.ydata
        elif np.linalg.norm(np.array([event.xdata, event.ydata]) - p1) < 0.1:
            p1[0], p1[1] = event.xdata, event.ydata
        elif np.linalg.norm(np.array([event.xdata, event.ydata]) - p2) < 0.1:
            p2[0], p2[1] = event.xdata, event.ydata
        update(0)





# Инициализация точки и линии траектории
point, = ax.plot([], [], 'ro', zorder=2)
line, = ax.plot([], [], 'b-', alpha=1, zorder=1)



# Количество кадров анимации
frames = 100
trajectory = []



# Создание кнопок "Старт"
ax_start_button = plt.axes([0.8, 0.01, 0.1, 0.04])
start_button = Button(ax_start_button, 'Start')
start_button.on_clicked(start_animation)

ax_stop_button = plt.axes([0.65, 0.01, 0.1, 0.04])
stop_button = Button(ax_stop_button, 'Stop')
stop_button.on_clicked(stop_animation)

# Добавление обработчика событий для перемещения точек
fig.canvas.mpl_connect('button_press_event', on_click)

# Инициализация траектории при создании окна
for i in range(frames):
    t = i / frames
    x, y = bezier(t, p0, p1, p2)
    trajectory.append((x, y))

# Задание анимации
animation = FuncAnimation(fig, update, frames=frames, interval=50, blit=True)

plt.show()