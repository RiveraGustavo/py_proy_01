import numpy as np

class TerrainGenerator:
    def __init__(self, width=800, height=800, seed=None):
        self.width = width
        self.height = height
        self.seed = seed
        if seed:
            np.random.seed(seed)

    def generate_base(self):
        # Ruido base
        world = np.random.rand(self.height, self.width)

        # Suavizado para formar continentes
        for _ in range(40):
            world = (
                world +
                np.roll(world, 1, axis=0) +
                np.roll(world, -1, axis=0) +
                np.roll(world, 1, axis=1) +
                np.roll(world, -1, axis=1)
            ) / 5

        # 🌊 Gradiente oeste → más océano a la izquierda
        gradient = np.linspace(0, 1, self.width)
        gradient = np.tile(gradient, (self.height, 1))

        world = world * gradient

        # 🌍 Máscara continental (favorece centro-este)
        y, x = np.ogrid[:self.height, :self.width]
        center_x = self.width * 0.65
        center_y = self.height * 0.5

        distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
        max_dist = np.sqrt(center_x**2 + center_y**2)

        mask = 1 - (distance / max_dist) **3
        mask = np.clip(mask, 0, 1)

        world = world * mask

        # ⛰ Cordillera vertical tipo Misty Mountains
        ridge_base = int(self.width * 0.85)
        ridge_width = int(self.width * 0.005)

        for y in range(self.height):

            # desplazamiento ondulado
            offset = int(20 * np.sin(y / 80))

            ridge_x = ridge_base + offset
            ridge_x = np.clip(ridge_x, 0, self.width - 1)

            if world[y, ridge_x] > 0.35:
                for x in range(self.width):
                    distance = abs(x - ridge_x)
                    
                    ridge_factor = np.exp(-(distance**2) / (2 * ridge_width**2))
                    world[y, x] += ridge_factor * 0.6

        #world = np.where(world < 0.35, 0, world)

        return world
