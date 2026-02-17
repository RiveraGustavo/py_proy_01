import numpy as np

class RiverGenerator:
    def __init__(self, world, flow = 0, sea_level=0.35):
        self.world = world
        self.height, self.width = world.shape
        self.sea_level = sea_level
        self.rivers = np.zeros_like(world)
        self.flow = np.zeros_like(world)


    def get_lowest_neighbor(self, y, x):
        lowest = (y, x)
        lowest_value = self.world[y, x]

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:

                ny = y + dy
                nx = x + dx

                if 0 <= ny < self.height and 0 <= nx < self.width:
                    if self.world[ny, nx] < lowest_value:
                        lowest_value = self.world[ny, nx]
                        lowest = (ny, nx)

        return lowest

    def generate_rivers(self, min_height=0.9, max_rivers=40):

        candidates = np.argwhere(self.world >= min_height)

        np.random.shuffle(candidates)

        river_count = 0

        for y, x in candidates:

            if river_count >= max_rivers:
                break

            path = []
            cy, cx = y, x
            
            while self.world[cy, cx] > self.sea_level:

                path.append((cy, cx))

                ny, nx = self.get_lowest_neighbor(cy, cx)

                # Si no hay descenso, detener
                if (ny, nx) == (cy, cx):
                # erosionar ligeramente
                    self.world[cy, cx] -= 0.02
                    continue

                cy, cx = ny, nx

            if len(path) > 20:  # evitar ríos pequeños
                #for py, px in path:
                    #self.rivers[py, px] = 1
                for py, px in path:
                    self.flow[py, px] += 1

                river_count += 1
            self.rivers = self.flow > 2

            if self.world[cy, cx] <= self.sea_level:
                # crear delta
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ny = cy + dy
                        nx = cx + dx
                        if 0 <= ny < self.height and 0 <= nx < self.width:
                            self.flow[ny, nx] += 2
                    break

            neighbors = []
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    ny = cy + dy
                    nx = cx + dx
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        neighbors.append(self.world[ny, nx])

                if min(neighbors) >= self.world[cy, cx]:
                    self.rivers[cy, cx] = 1  # lago
                break

        return self.rivers
