import pygame
import sys
from ..calculations.shapes_calculations import adjust_speeds

class EventHandle:
    def __init__(self, event_variables, gui_collisions, constants):
        self.events_mapper = {
            pygame.QUIT: self.quit_handler,
            pygame.KEYDOWN: self.keydown_handler,
            pygame.KEYUP: self.keyup_handler,
            pygame.MOUSEBUTTONDOWN: self.mousedown_handler,
            pygame.MOUSEBUTTONUP: self.mouseup_handler
        }
        self.event_variables = event_variables
        self.gui_collisions = gui_collisions
        self.constants = constants
        self.keys_pressed = {}

    def quit_handler(self, event):
        self.event_variables.set_running(False)
        sys.exit()

    def adjust_movement_speeds(self):
        pass

    def keydown_handler(self, event):
        if event.key == pygame.K_q:
            self.event_variables.set_running(False)

        elif event.key == pygame.K_DOWN:
            delay = adjust_speeds(self.event_variables, self.constants)
            self.event_variables.set_movement_delay(delay // 6)

        elif event.key == pygame.K_UP:
            curr_shape = self.event_variables.get_current_shape()
            curr_shape.increment_current_rotation()
        
        elif event.key == pygame.K_SPACE:
            curr_pause = self.event_variables.get_pause()
            self.event_variables.set_pause(not curr_pause)

        elif event.key == pygame.K_1:
            self.event_variables.set_color_scheme(0)
        elif event.key == pygame.K_2:
            self.event_variables.set_color_scheme(1)
        elif event.key == pygame.K_3:
            self.event_variables.set_color_scheme(2)
        elif event.key == pygame.K_4:
            self.event_variables.set_color_scheme(3)
        elif event.key == pygame.K_5:
            self.event_variables.set_color_scheme(4)
        elif event.key == pygame.K_6:
            self.event_variables.set_color_scheme(5)
        elif event.key == pygame.K_7:
            self.event_variables.set_color_scheme(6)
        elif event.key == pygame.K_8:
            self.event_variables.set_color_scheme(7)
        elif event.key == pygame.K_9:
            self.event_variables.set_color_scheme(8)
        elif event.key == pygame.K_0:
            self.event_variables.set_color_scheme(9)
        elif event.key == pygame.K_o:
            self.event_variables.set_color_scheme(10)
        elif event.key == pygame.K_w:
            self.event_variables.set_color_scheme(11)
        elif event.key == pygame.K_e:
            self.event_variables.set_color_scheme(12)
        elif event.key == pygame.K_r:
            self.event_variables.set_color_scheme(13)
        elif event.key == pygame.K_t:
            self.event_variables.set_color_scheme(14)
        elif event.key == pygame.K_y:
            self.event_variables.set_color_scheme(15)
        elif event.key == pygame.K_u:
            self.event_variables.set_color_scheme(16)
        elif event.key == pygame.K_i:
            self.event_variables.set_color_scheme(17)

    def keyup_handler(self, event):
        if event.key == pygame.K_DOWN:
            delay = adjust_speeds(self.event_variables, self.constants)
            self.event_variables.set_movement_delay(delay)

        if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
            self.keys_pressed.pop(event.key, None)

    def mousedown_handler(self, event):
        self.event_variables.set_is_mouse_pressed(True)
        self.gui_collisions.mouse_down_collisions()

    def mouseup_handler(self, event):
        self.event_variables.set_is_mouse_pressed(False)

    def handle_event(self, event):
        type_func = self.events_mapper.get(event.type)
        if type_func:
            type_func(event)

        keys = pygame.key.get_pressed()
        self.event_variables.set_left_pressed(keys[pygame.K_LEFT])
        self.event_variables.set_right_pressed(keys[pygame.K_RIGHT])
