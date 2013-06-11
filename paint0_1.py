import pygame

MAIN_WIDTH = 600
MAIN_HEIGHT = 500
MAIN_SIZE = (MAIN_WIDTH, MAIN_HEIGHT)
MAIN_TITLE = "Aldrin's Paint"
STRIP_HEIGHT = 40

class Canvas(pygame.Surface):
  def __init__(self, width, height):
    pygame.Surface.__init__(self, (width, height))
    self.size = (width, height)
    self.clear()

  def clear(self):
    self.fill((255,255,255))

def main():
  pygame.init()
  canvas = Canvas(MAIN_WIDTH, MAIN_HEIGHT - STRIP_HEIGHT)
  screen = pygame.display.set_mode(MAIN_SIZE)
  pygame.display.set_caption(MAIN_TITLE)

  frame_clock = pygame.time.Clock()
  game_running = True
  while(game_running):
    frame_clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.blit(canvas, (0, STRIP_HEIGHT))
    pygame.display.flip()

if __name__ == "__main__": main()
