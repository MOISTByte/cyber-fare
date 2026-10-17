import pygame
class OperationsScreen:
    def __init__(self):
        self.font = pygame.font.SysFont("consolas", 18)

        self.background = (16, 24, 35)
        self.panel = (29, 42, 56)
        self.text = (230, 238, 246)
        self.muted = (145, 163, 180)
        self.accent = (60, 190, 210)

        self.device_rects = {}
    def handle_event(self, event, state):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        if event.button != 1:
            return

        mouse = event.pos

        if pygame.Rect(850, 22, 220, 42).collidepoint(mouse):
            state["paused"] = not state["paused"]
            return

        for device_id, rect in self.device_rects.items():
            if rect.collidepoint(mouse):
                state["selected_device"] = device_id
                return