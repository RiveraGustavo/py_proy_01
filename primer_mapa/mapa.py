import numpy as np
import matplotlib.pyplot as plt

# Tamaño
width, height = 800, 800

# Generar "continente"
world = np.random.rand(height, width)

# Suavizar para formar masas de tierra
for _ in range(6):
    world = (world +
             np.roll(world, 1, axis=0) +
             np.roll(world, -1, axis=0) +
             np.roll(world, 1, axis=1) +
             np.roll(world, -1, axis=1)) / 5

plt.figure(figsize=(10,10))

# Estilo pergamino
plt.imshow(world, cmap="copper")
plt.xticks([])
plt.yticks([])

# Nombre del mundo
plt.text(300, 100, "Reinos de Valandor", fontsize=28, fontweight='bold')

# Dibujar montañas (triángulos)
mountains = [(300,400), (330,420), (360,410), (390,430)]
for x, y in mountains:
    plt.plot([x-10, x, x+10], [y+10, y-10, y+10], color="black")

# Dibujar bosque (pequeños árboles)
forest = [(500,500), (520,510), (540,495), (510,480)]
for x, y in forest:
    plt.plot(x, y, marker="^", color="darkgreen")

# Ciudades
cities = {
    "Eldoria": (200, 300),
    "Tharond": (600, 250),
    "Puerto Gris": (150, 650)
}

for name, (x, y) in cities.items():
    plt.plot(x, y, 'ko')
    plt.text(x+10, y+10, name, fontsize=12)

# Rosa de los vientos simple
plt.text(700, 100, "N", fontsize=20)
plt.arrow(710,150,0,-40, head_width=10)

plt.show()
