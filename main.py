import math

from world import World

WORLD = World(math.exp(6), 5, 1000)

WORLD.run_evolution()
