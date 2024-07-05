from .shape import Shape
from ..services import read_files
from ..calculations.dims import *
import random

class BagOfSeven:
    def __init__(self, 
                 constants, 
                 event_state,
                 screen,
                 shapes,
                 container_coords):
        self.constants = constants
        self.shape_rotations = shapes
        self.queue = []
        self.seven = []
        self.event_state = event_state
        self.screen = screen
        self.container_coords = container_coords
        self.current_color_scheme = 3

    def load_seven(self, grid_row):
        current_color_scheme = self.event_state.get_color_scheme()
        
        if current_color_scheme == 0:
            colors = self.constants['GREEN_BLUE']
        elif current_color_scheme == 1:
            colors = self.constants['GREEN_YELLOW']
        elif current_color_scheme == 2:
            colors = self.constants['GREEN_PURPLE']
        elif current_color_scheme == 3:
            colors = self.constants['GREEN_PINK']
        elif current_color_scheme == 4:
            colors = self.constants['BLUE_GREEN']
        elif current_color_scheme == 5:
            colors = self.constants['BLUE_YELLOW']
        elif current_color_scheme == 6:
            colors = self.constants['BLUE_PURPLE']
        elif current_color_scheme == 7:
            colors = self.constants['BLUE_RED']
        elif current_color_scheme == 8:
            colors = self.constants['BLUE_PINK']
        elif current_color_scheme == 9:
            colors = self.constants['YELLOW_PURPLE']
        elif current_color_scheme == 10:
            colors = self.constants['YELLOW_PINK']
        elif current_color_scheme == 11:
            colors = self.constants['YELLOW_RED']
        elif current_color_scheme == 12:
            colors = self.constants['YELLOW_ORANGE']
        elif current_color_scheme == 13:
            colors = self.constants['ORANGE_PINK']
        elif current_color_scheme == 14:
            colors = self.constants['ORANGE_PURPLE']
        elif current_color_scheme == 15:
            colors = self.constants['ORANGE_RED']
        elif current_color_scheme == 16:
            colors = self.constants['ORANGE_GRAY']
        elif current_color_scheme == 17:
            colors = self.constants['GRAY_RED']
        elif current_color_scheme == 18:
            colors = self.constants['GRAY_PURPLE']
        elif current_color_scheme == 19:
            colors = self.constants['GRAY_YELLOW']
        elif current_color_scheme == 20:
            colors = self.constants['GRAY_GREEN']
        else:
            colors = self.constants['COLOR_GRAY']


        for k, v in self.shape_rotations.items():
            if k == "BLACK":
                continue
            random_color = random.choice(colors)
            # block_size = self.constants['BLOCK_SIZE']
            random_pos = calculate_shape_pos(grid_row, k)
            blit_coords = [random_pos[0], random_pos[1]]
            shape_obj = Shape(self.constants,
                              self.event_state,
                              self.screen,
                              self.shape_rotations,
                              k,
                              random_color,
                              blit_coords,
                              random_pos[2]
                              )
            self.seven.append(shape_obj)
        self.seven  = random.sample(self.seven, len(self.seven))
    
    def append_queue(self):
        if len(self.queue) == 0:
            for x in range(0, 3):
                self.seven[x].block_color = self.constants['GRAY']
                self.queue.append(self.seven[x])
            del self.seven[0: 3]
            return
        self.seven[0].block_color = self.constants['GRAY']
        self.queue.append(self.seven[0])
        del self.seven[0]

    def get_queue_element(self):
        current_color_scheme = 0
        current_color_scheme = self.event_state.get_color_scheme()
        if current_color_scheme == 0:
            colors = self.constants['GREEN_BLUE']
        elif current_color_scheme == 1:
            colors = self.constants['GREEN_YELLOW']
        elif current_color_scheme == 2:
            colors = self.constants['GREEN_PURPLE']
        elif current_color_scheme == 3:
            colors = self.constants['GREEN_PINK']
        elif current_color_scheme == 4:
            colors = self.constants['BLUE_GREEN']
        elif current_color_scheme == 5:
            colors = self.constants['BLUE_YELLOW']
        elif current_color_scheme == 6:
            colors = self.constants['BLUE_PURPLE']
        elif current_color_scheme == 7:
            colors = self.constants['BLUE_RED']
        elif current_color_scheme == 8:
            colors = self.constants['BLUE_PINK']
        elif current_color_scheme == 9:
            colors = self.constants['YELLOW_PURPLE']
        elif current_color_scheme == 10:
            colors = self.constants['YELLOW_PINK']
        elif current_color_scheme == 11:
            colors = self.constants['YELLOW_RED']
        elif current_color_scheme == 12:
            colors = self.constants['YELLOW_ORANGE']
        elif current_color_scheme == 13:
            colors = self.constants['ORANGE_PINK']
        elif current_color_scheme == 14:
            colors = self.constants['ORANGE_PURPLE']
        elif current_color_scheme == 15:
            colors = self.constants['ORANGE_RED']
        elif current_color_scheme == 16:
            colors = self.constants['ORANGE_GRAY']
        elif current_color_scheme == 17:
            colors = self.constants['GRAY_RED']
        elif current_color_scheme == 18:
            colors = self.constants['GRAY_PURPLE']
        elif current_color_scheme == 19:
            colors = self.constants['GRAY_YELLOW']
        elif current_color_scheme == 20:
            colors = self.constants['GRAY_GREEN']
        else:
            colors = self.constants['COLOR_GRAY']

        self.queue[0].block_color = random.choice(colors)
        element = self.queue[0]
        del self.queue[0]
        self.append_queue()
        return element