import pygame
import pygame_gui
from packet import Packet
from randGen import RandGen
import time
from pygame_gui.windows import UIMessageWindow
from pygame_gui.elements import UITextBox


class Tower:
    def __init__(self, x, y, image, type, manager):
        self.x = x
        self.y = y
        self.image = image
        self.packetList = []
        self.send_packet_list = []
        self.packet = None
        self.timer = pygame.time.get_ticks()
        self.other_tower = None
        self.type = type
        self.arq = "no arq"
        self.arq_received = True
        self.time = 0
        self.packet_disrupted = False
        self.random = RandGen(time.time())
        self.manager = manager
        self.message = "<p> Send packets:  </p>"
        self.text_box_x = 25
        if self.type == "receiver":
            self.text_box_x = 175
        self.text_box = UITextBox(
            html_text=self.message, relative_rect=pygame.Rect(self.text_box_x, 400, 150, 200), manager=self.manager)
        self.button_held = False

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        if self.packet is not None:
            self.packet.draw(window)

    def handle_events(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.x <= mouse_pos[0] <= self.x + self.image.get_width():
                    if self.y <= mouse_pos[1] <= self.y + self.image.get_height():
                        self.text_box.visible = not self.text_box.visible

    def update(self, event, dt, propability):
        self.handle_events(event)
        self.time += dt
        # sending queued packets
        if self.packet is None and self.packetList and self.arq_received:
            if self.arq == "no arq":
                self.arq_received = True
            else:
                self.arq_received = False
            self.timer = self.time
            self.packet = self.packetList.pop(0)
            self.send_packet_list.append(self.packet)
            self.text_box.append_html_text(
                "<p> id: " + str(self.packet.id) + " " + self.packet.type + "</p>")
        if not self.arq_received and self.time - self.timer >= 15:
            if self.packet is None and self.packetList:
                if self.arq == "no arq":
                    self.arq_received = True
                else:
                    self.arq_received = False
                self.timer = self.time
                self.packet = self.packetList.pop(0)
                self.text_box.append_html_text(
                    "<p> id: " + str(self.packet.id) + " " + self.packet.type + "</p>")

        if self.packet is not None:
            self.packet.update(dt)  # update packet position and color

            # possibility of disruption of packet (it always happens in the middle of the way)
            if (self.other_tower.x - self.x + 150) / 2 <= self.packet.x and not self.packet_disrupted and self.packet.type != "ack":
                number = self.random.random_zero_to_one()
                self.packet_disrupted = True
                if number <= propability / 100:
                    self.packet.type = "disrupted"

            # if packet reaches the receiver tower
            if self.type == "sender":
                if self.packet.x >= self.other_tower.x:
                    self.other_tower.receive_packet(self.packet, self)

            # if packet reaches the sender tower
            elif self.type == "receiver":
                if self.packet.x <= self.other_tower.x + 150:
                    self.packetList.remove(self.packet)
                    self.other_tower.receive_packet(self.packet, self)

    def send_packet(self, packet, receiver):
        self.packetList.append(packet)
        self.send_packet_list.append(packet)
        self.text_box.append_html_text(
            "<p> id: " + str(self.packet.id) + " " + self.packet.type + "</p>")

        self.other_tower = receiver

    def send_packets(self, receiver, number_of_packets):
        for i in range(number_of_packets):
            self.packetList.append(Packet(self.x + 50, self.y, "normal"))
        self.other_tower = receiver

    def receive_packet(self, packet, sender):
        # self.packet = packet
        # if packet correct to send ack
        # else dont
        self.other_tower = sender

        if self.type == "receiver":
            self.packet = None
            if packet.type == "normal" and self.arq != "no arq":
                self.packet = Packet(self.x + 50, self.y + 100, "ack")
                self.send_packet(
                    self.packet, sender)

            sender.packet = None
            sender.packet_disrupted = False
            if packet.type == "disrupted" and self.arq != "no arq":
                packet.x = sender.x + 50
                packet.type = "normal"
                sender.packetList.insert(0, packet)

        if self.type == "sender":
            if packet.type == "ack":
                self.arq_received = True
            else:
                self.arq_received = False
            sender.packet = None
