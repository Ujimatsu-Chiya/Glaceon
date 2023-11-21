from .array_generator import ArrayGen
from .io_file import IOFile
from .graph_generator import GraphGen
from .maze_generator import MazeGen
from .string_generator import StringGen
from .graph import Graph
from .utils.rand import *

from random import randint, uniform, random, choices, sample


class Gen(ArrayGen, GraphGen, StringGen, MazeGen):
    pass
