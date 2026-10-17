import pygame
class OperationsScreen:
    def __init__(self):
        self.font = pygame.font.SysFont("consolas", 18)
        self.title_font = pygame.font.SysFont(
            "consolas", 26, bold=True
        )

        self.background = (16, 24, 35)
        self.panel = (29, 42, 56)
        self.text = (230, 238, 246)
        self.muted = (145, 163, 180)
        self.accent = (60, 190, 210)

    def label(self, surface, text, x, y, color=None, font=None):
            image = (font or self.font).render(
                text, True, color or self.text
            )
            surface.blit(image, (x, y))
    
    def draw(self, surface, state):
        surface.fill(self.background)
        self.device_rects = {}

        # Header
        self.label(
            surface, "CYBER-FARE", 24, 20,
            self.accent, self.title_font
        )
        self.label(
            surface, f"DAY {state['day']:02}",
            300, 27, self.muted
        )

        button = pygame.Rect(850, 22, 220, 42)
        pygame.draw.rect(surface, self.panel, button, border_radius=6)
        self.label(
            surface,
            "Resume Simulation" if state["paused"]
            else "Pause Simulation",
            865, 33
        )

        # Financial overview
        stats = [
            ("CASH", f"${state['cash']:,}"),
            ("DAILY REVENUE", f"${state['daily_revenue']:,}"),
            ("DAILY EXPENSES", f"${state['daily_expenses']:,}"),
            ("REPUTATION", str(state["reputation"])),
        ]

        for i, (name, value) in enumerate(stats):
            x = 24 + i * 265
            rect = pygame.Rect(x, 90, 245, 85)
            pygame.draw.rect(
                surface, self.panel, rect, border_radius=8
            )
            self.label(surface, name, x + 14, 103, self.muted)
            self.label(
                surface, value, x + 14, 133,
                self.text, self.title_font
            )

        # Network panel
        network = pygame.Rect(24, 200, 680, 380)
        pygame.draw.rect(
            surface, self.panel, network, border_radius=8
        )
        self.label(
            surface, "NETWORK TOPOLOGY",
            42, 215, self.accent
        )

        # Draw connections behind the devices.
        devices = {
            device["id"]: device for device in state["devices"]
        }

        firewall = devices["firewall"]
        web = devices["web"]
        database = devices["database"]

        for first, second in [
            (firewall, web),
            (firewall, database),
        ]:
            pygame.draw.line(
                surface, self.muted,
                (first["x"], first["y"]),
                (second["x"], second["y"]), 3
            )

        # Draw selectable devices.
        for device in state["devices"]:
            x, y = device["x"], device["y"]
            rect = pygame.Rect(x - 65, y - 32, 130, 64)
            self.device_rects[device["id"]] = rect

            color = (
                self.accent
                if device["id"] == state["selected_device"]
                else (63, 81, 99)
            )

            pygame.draw.rect(
                surface, color, rect, border_radius=7
            )
            self.label(
                surface, device["kind"],
                x - 52, y - 12
            )
            self.label(
                surface, device["status"],
                x - 52, y + 9, (220, 225, 230)
            )

        # Selected device inspector
        inspector = pygame.Rect(725, 200, 350, 380)
        pygame.draw.rect(
            surface, self.panel, inspector, border_radius=8
        )
        self.label(
            surface, "DEVICE INSPECTOR",
            743, 215, self.accent
        )

        selected = next(
            (
                d for d in state["devices"]
                if d["id"] == state["selected_device"]
            ),
            None,
        )

        if selected:
            self.label(
                surface, selected["name"],
                743, 260, self.text, self.title_font
            )
            self.label(
                surface, f"Type: {selected['kind']}",
                743, 310
            )
            self.label(
                surface, f"Status: {selected['status']}",
                743, 342
            )
            self.label(
                surface, "Configuration controls",
                743, 400, self.muted
            )
            self.label(
                surface, "Coming in the next milestone",
                743, 430, self.muted
            )

        # Incident feed
        self.label(
            surface, "INCIDENT FEED",
            24, 610, self.accent
        )

        for i, incident in enumerate(state["incidents"]):
            self.label(
                surface, f"• {incident}",
                24, 645 + i * 25
            )

        if state["paused"]:
            self.label(
                surface, "SIMULATION PAUSED",
                800, 665, self.accent
            )