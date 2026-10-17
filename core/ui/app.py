import pygame
import core.config.settings
import core.ui.gui.out
import core.ui.controls.input
class GameApp:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        pygame.display.set_caption("cyber-fare")

        self.clock = pygame.time.Clock()
        self.state = core.config.settings.temp()
        self.input = core.ui.controls.input.OperationsScreen()
        self.out = core.ui.gui.out.OperationsScreen()
    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.input.handle_event(
                        event, self.state
                    )

            self.out.draw(self.screen, self.state)
            pygame.display.flip()
            self.clock.tick(40)

        pygame.quit()
