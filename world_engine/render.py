def render_heightmap(world, rivers=None):
    import numpy as np
    import matplotlib.pyplot as plt

    ocean = world < 0.35
    beach = (world >= 0.35) & (world < 0.4)
    plains = (world >= 0.4) & (world < 0.65)
    mountains = world >= 0.65

    colored = np.zeros((*world.shape, 3))

    colored[ocean] = [0.1, 0.2, 0.6]
    colored[beach] = [0.9, 0.8, 0.5]
    colored[plains] = [0.2, 0.6, 0.2]
    colored[mountains] = [0.5, 0.5, 0.5]
    

    if rivers is not None:
        if rivers is not None:
            max_flow = np.max(rivers)
            normalized = rivers / (max_flow + 1e-6)

            for y in range(world.shape[0]):
                for x in range(world.shape[1]):
                    if rivers[y, x] > 0:
                        intensity = normalized[y, x]
                        colored[y, x] = [0.0, 0.3 + 0.5*intensity, 0.9]

    plt.figure(figsize=(8,8))
    plt.imshow(colored)
    plt.xticks([])
    plt.yticks([])
    plt.title("Mundo con Ríos Reales")
    plt.show()
