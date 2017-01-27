import math

from world import World

WORLD = World(math.exp(6), 2, 100)

WORLD.run_evolution()
