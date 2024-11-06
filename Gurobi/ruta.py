import matplotlib.pyplot as plt
import numpy as np

# Ejemplo de datos

stations = np.array([
    [-33.64384, -71.60655],
    [-33.64508, -71.62475],
])

pickup_points = np.array([
    [-33.66156, -71.62468],
    [-33.64055, -71.62975],
    [-33.62899, -71.63300],
    [-33.63596, -71.62219],
    [-33.63613, -71.61305],
    [-33.64370, -71.61198],
    [-33.65204, -71.60252]
])

shelters = np.array([
    [-33.63538, -71.62284],
    [-33.64510, -71.62439],
    [-33.65342, -71.60420],
    [-33.64654, -71.62293],
    [-33.66108, -71.62440]
])

# Ejemplo de rutas de buses (cada ruta es una lista de índices de puntos de recogida y refugios)
bus_routes = [
    [0, 7, 10, 5, 9],  # Ruta del bus 1
]

# Crear el gráfico
fig, ax = plt.subplots()

# Dibujar estaciones
ax.scatter(stations[:, 0], stations[:, 1], c='green', label='Estaciones')

# Dibujar puntos de encuentro
ax.scatter(pickup_points[:, 0], pickup_points[:, 1], c='blue', label='Puntos de Encuentro')

# Dibujar refugios
ax.scatter(shelters[:, 0], shelters[:, 1], c='red', label='Refugios')

# Dibujar rutas de buses
for route in bus_routes:
    route_coords = []
    for i in route:
        if i < len(stations):
            route_coords.append(stations[i])
        elif i < len(stations) + len(pickup_points):
            route_coords.append(pickup_points[i - len(stations)])
        else:
            route_coords.append(shelters[i - len(stations) - len(pickup_points)])
    route_coords = np.array(route_coords)
    ax.plot(route_coords[:, 0], route_coords[:, 1], label='Ruta del Bus')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# Añadir etiquetas y leyenda
#for i, point in enumerate(stations):
#    ax.text(point[0], point[1], f'S{i}', fontsize=12, ha='right')
#for i, point in enumerate(pickup_points):
#    ax.text(point[0], point[1], f'P{i}', fontsize=12, ha='right')
#for i, point in enumerate(shelters):
#    ax.text(point[0], point[1], f'R{i}', fontsize=12, ha='right')

ax.legend()
ax.set_title('Ruta de Bus 5')

plt.show()