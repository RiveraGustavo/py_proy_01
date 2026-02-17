from terrain import TerrainGenerator
from rivers import RiverGenerator
from render import render_heightmap

if __name__ == "__main__":
    generator = TerrainGenerator(seed=42)
    world = generator.generate_base()
    river_gen = RiverGenerator(world)

    rivers = river_gen.generate_rivers()

    render_heightmap(world, rivers)
    #render_heightmap(world)
