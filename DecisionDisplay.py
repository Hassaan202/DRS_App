import pygame
import sys
import time
from enum import Enum

class Decision(Enum):
    OUT = "OUT"
    NOT_OUT = "NOT OUT"
    LBW = "LBW"
    CAUGHT = "CAUGHT"
    RUN_OUT = "RUN OUT"

class DecisionDisplay:
    def __init__(self, screen_width=800, screen_height=600):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Cricket Decision Display")
        
        self.RED = (255, 0, 0)
        self.GREEN = (0, 200, 0)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        
        self.large_font = pygame.font.SysFont('Arial', 120, bold=True)
        
    def _draw_decision_box(self, decision):
        if decision in [Decision.OUT, Decision.LBW, Decision.CAUGHT, Decision.RUN_OUT]:
            box_color = self.RED
            text = str(decision.value)
        else:
            box_color = self.GREEN
            text = "NOT OUT"
            
        box_width = 600
        box_height = 300
        box_x = (self.screen_width - box_width) // 2
        box_y = (self.screen_height - box_height) // 2
        
        border_size = 10
        pygame.draw.rect(self.screen, self.BLACK, 
                         (box_x - border_size, box_y - border_size, 
                          box_width + 2*border_size, box_height + 2*border_size))
        pygame.draw.rect(self.screen, box_color, 
                         (box_x, box_y, box_width, box_height))
        
        text_surface = self.large_font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect(center=(self.screen_width//2, self.screen_height//2))
        self.screen.blit(text_surface, text_rect)
    
    def display_decision(self, decision, display_time=3.0):
        if isinstance(decision, str):
            try:
                decision = Decision(decision.upper())
            except ValueError:
                if decision.upper() == "OUT":
                    decision = Decision.OUT
                else:
                    decision = Decision.NOT_OUT
        
        start_time = time.time()
        while time.time() - start_time < display_time:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(self.BLACK)
            self._draw_decision_box(decision)
            pygame.display.flip()
            pygame.time.Clock().tick(60)
    
    def close(self):
        pygame.quit()


def show_decision(decision_str, display_time=3.0):
    display = DecisionDisplay()
    try:
        display.display_decision(decision_str, display_time)
    finally:
        display.close()


if __name__ == "__main__":
    display = DecisionDisplay()
    try:
        display.display_decision(Decision.OUT, 2)
        display.display_decision(Decision.NOT_OUT, 2)
        display.display_decision(Decision.LBW, 2)
    finally:
        display.close()