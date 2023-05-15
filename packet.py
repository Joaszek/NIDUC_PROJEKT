import pygame


class Packet:
    counter = 0

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.received = False
        self.color = (0, 255, 0)
        self.id = Packet.counter
        Packet.counter += 1

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), 30)

    def update(self, dt):

        if self.type == "normal":
            self.color = (0, 255, 0)
        elif self.type == "disrupted":
            self.color = (255, 0, 0)
        elif self.type == "ack":
            self.color = (255, 165, 0)

        if self.type == "normal" or self.type == "disrupted":
            self.x += 100 * dt
        else:
            self.x -= 100 * dt
