from enum import Enum

class Direction(Enum):
  NONE = 0
  UP = 1
  DOWN = 2
  LEFT = 3
  RIGHT = 4

class Terrain(Enum):
  NONE = 0
  GROUND = 1
  WATER = 2


symbols = {
  Terrain.GROUND: "#",
  Terrain.WATER: "~"
}

default_map = "map.txt"
