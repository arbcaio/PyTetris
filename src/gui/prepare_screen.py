import pygame
from ..calculations.dims import *
import random

class GameScreen:
    def __init__(self, screen, constants, event_state):
        self.screen = screen
        display_info = pygame.display.Info()
        self.screen_width = display_info.current_w
        self.screen_height = display_info.current_h
        self.constants = constants
        self.inititialized = False
        self.event_state = event_state

    def draw_game_container(self, color):
        cont_width, cont_height = self.screen_width-600, self.screen_height
        dimensions = place_item_at_screen_center(self.screen_width,
                                           self.screen_height,
                                           cont_width, cont_height)
        self.grid_start_x = dimensions[0]
        self.grid_start_y = dimensions[1]
        self.container_width = dimensions[2]
        self.container_height = dimensions[3]
        self.event_state.set_container_coords(self.grid_start_x, 
                                              self.grid_start_y,
                                              self.container_width,
                                              self.container_height)

        pygame.draw.rect(self.screen, color, dimensions)

    def draw_boundaries(self):
        current_color_scheme = 0
        current_color_scheme = self.event_state.get_color_scheme()

        if current_color_scheme == 0: 
            random_colors = self.constants['GREEN_BLUE']
        elif current_color_scheme == 1:
            random_colors = self.constants['GREEN_YELLOW']
        elif current_color_scheme == 2:
            random_colors = self.constants['GREEN_PURPLE']
        elif current_color_scheme == 3:
            random_colors = self.constants['GREEN_PINK']
        elif current_color_scheme == 4:
            random_colors = self.constants['BLUE_GREEN']
        elif current_color_scheme == 5:
            random_colors = self.constants['BLUE_YELLOW']
        elif current_color_scheme == 6:
            random_colors = self.constants['BLUE_PURPLE']
        elif current_color_scheme == 7:
            random_colors = self.constants['BLUE_RED']
        elif current_color_scheme == 8:
            random_colors = self.constants['BLUE_PINK']
        elif current_color_scheme == 9:
            random_colors = self.constants['YELLOW_PURPLE']
        elif current_color_scheme == 10:
            random_colors = self.constants['YELLOW_PINK']
        elif current_color_scheme == 11:
            random_colors = self.constants['YELLOW_RED']
        elif current_color_scheme == 12:
            random_colors = self.constants['YELLOW_ORANGE']
        elif current_color_scheme == 13:
            random_colors = self.constants['ORANGE_PINK']
        elif current_color_scheme == 14:
            random_colors = self.constants['ORANGE_PURPLE']
        elif current_color_scheme == 15:
            random_colors = self.constants['ORANGE_RED']
        elif current_color_scheme == 16:
            random_colors = self.constants['ORANGE_GRAY']
        elif current_color_scheme == 17:
            random_colors = self.constants['GRAY_RED']
        elif current_color_scheme == 18:
            random_colors = self.constants['GRAY_PURPLE']
        # elif current_color_scheme == 19:
        #     random_colors = self.constants['GRAY_YELLOW']
        # elif current_color_scheme == 20:
        #     random_colors = self.constants['GRAY_GREEN']
        else:
            random_colors = self.constants['COLOR_GRAY']

        boundaries \
            = calculate_boundaries_container(self.grid_start_x,
                                             self.grid_start_y,
                                             self.container_width,
                                             self.container_height)
        cidx = 0
        for x in boundaries:
            boundary = x['boundary']
            line_width = x['width']
            color_random = random_colors[cidx]
            cidx += 1
            pygame.draw.rect(self.screen, color_random, boundary, width=line_width)
            if cidx >= len(random_colors):
                cidx = 0
        