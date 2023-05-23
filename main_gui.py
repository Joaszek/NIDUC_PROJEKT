import pygame
import numpy as np

from pygame_gui import UI_DROP_DOWN_MENU_CHANGED, UIManager, UI_BUTTON_PRESSED
from pygame_gui.elements import UIButton, UIHorizontalSlider, UIDropDownMenu

from tower import Tower
from packet import Packet

pygame.init()

pygame.display.set_caption('Arq simulator')
window_surface = pygame.display.set_mode((800, 600))
manager = UIManager((800, 600))

TOWER_SIZE = 150
TOWER_IMAGE = pygame.image.load('tower.png')
TOWER = pygame.transform.scale(TOWER_IMAGE, (TOWER_SIZE, TOWER_SIZE))
towers = [Tower(25, 200, TOWER, "sender", manager),
          Tower(625, 200, TOWER, "receiver", manager)]

packets = []


background = pygame.Surface((800, 600))
background.fill(manager.ui_theme.get_colour('dark_bg'))

start_button = UIButton((350, 400), 'Start')
stop_button = UIButton((420, 400), 'Stop')

slider_speed = UIHorizontalSlider(pygame.Rect(
    (100, 100), (100, 25)), 1, (1, 100), manager=manager)


slider_length = UIHorizontalSlider(pygame.Rect(
    (250, 100), (100, 25)), 50, (0, 100), manager=manager)

slider_packets = UIHorizontalSlider(pygame.Rect(
    (400, 100), (100, 25)), 1, (1, 100), manager=manager)

pygame.font.init()

font = pygame.font.SysFont('Montserrat Thin', 30)
font_small = pygame.font.SysFont('Montserrat Thin', 15)

text_sender = font.render('Sender', False, (255, 255, 255))
text_receiver = font.render('Receiver', False, (255, 255, 255))
text_legend = font.render('Legend:', False, (255, 255, 255))
text_normal = font_small.render('- Normal packet', False, (255, 255, 255))
text_disrupted = font_small.render(
    '- Disrupted packet', False, (255, 255, 255))
text_ack = font_small.render('- Ack packet', False, (255, 255, 255))
text_slider_speed = font_small.render(
    "Simulation speed", False, (255, 255, 255))
text_slider_length = font_small.render("Probabilty", False, (255, 255, 255))
text_slider_packets = font_small.render(
    "Number of Packets", False, (255, 255, 255))

text_drop_down = font_small.render(
    "Select a error-control method", False, (255, 255, 255))


drop_down = UIDropDownMenu(['no arq', 'arq'],
                           'no arq',
                           pygame.Rect((550, 100), (150, 25)),
                           manager=manager)


def draw_line_dashed(surface, color, start_pos, end_pos, width=1, dash_length=10, exclude_corners=True):

    # convert tuples to numpy arrays
    start_pos = np.array(start_pos)
    end_pos = np.array(end_pos)

    # get euclidian distance between start_pos and end_pos
    length = np.linalg.norm(end_pos - start_pos)

    # get amount of pieces that line will be split up in (half of it are amount of dashes)
    dash_amount = int(length / dash_length)

    # x-y-value-pairs of where dashes start (and on next, will end)
    dash_knots = np.array([np.linspace(
        start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()

    return [pygame.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)
            for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]


clock = pygame.time.Clock()
is_running = True

is_paused = False


packet = None
while is_running:
    time_delta = clock.tick(60) / 1000.0
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            is_running = False
        if event.type == UI_BUTTON_PRESSED:
            if event.ui_element == start_button:
                is_paused = False
                if towers[0].packet is None and towers[1].packet is None:
                    towers[0].arq_received = True
                    towers[0].send_packets(
                        towers[1], slider_packets.get_current_value())
            if event.ui_element == stop_button:
                is_paused = True

        if (event.type == UI_DROP_DOWN_MENU_CHANGED
                and event.ui_element == drop_down):
            for tower in towers:
                tower.arq = drop_down.selected_option
        manager.process_events(event)

    manager.update(time_delta)
    window_surface.blit(background, (0, 0))

    pygame.draw.line(window_surface, (255, 255, 255),
                     (160, 240), (640, 240), 4)
    draw_line_dashed(window_surface, (255, 255, 255),
                     (150, 260), (650, 260), 4, 10)
    if is_paused:
        time_delta = 0
    for tower in towers:
        tower.draw(window_surface)
        tower.update(event_list, time_delta * slider_speed.get_current_value(),
                     slider_length.get_current_value())

    text_number_speed = font_small.render(
        str(slider_speed.get_current_value()), False, (255, 255, 255))
    text_number_length = font_small.render(
        str(slider_length.get_current_value()), False, (255, 255, 255))
    text_number_packets = font_small.render(
        str(slider_packets.get_current_value()), False, (255, 255, 255))

    window_surface.blit(text_sender, (50, 350))
    window_surface.blit(text_receiver, (635, 350))

    window_surface.blit(text_legend, (570, 480))
    window_surface.blit(text_normal, (600, 520))
    window_surface.blit(text_disrupted, (600, 540))
    window_surface.blit(text_ack, (600, 560))

    window_surface.blit(text_slider_speed, (90, 75))
    window_surface.blit(text_slider_length, (250, 75))
    window_surface.blit(text_slider_packets, (385, 75))

    window_surface.blit(text_drop_down, (550, 75))

    window_surface.blit(text_number_speed, (150, 125))
    window_surface.blit(text_number_length, (300, 125))
    window_surface.blit(text_number_packets, (450, 125))

    pygame.draw.circle(window_surface, (0, 255, 0), (580, 525), 8)
    pygame.draw.circle(window_surface, (255, 0, 0), (580, 545), 8)
    pygame.draw.circle(window_surface, (255, 165, 0), (580, 565), 8)

    manager.draw_ui(window_surface)
    pygame.display.update()
