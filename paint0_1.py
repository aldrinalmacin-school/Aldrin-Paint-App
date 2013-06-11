import pygame

class Canvas(pygame.Surface):
  def __init__(self, width, height):
    pygame.Surface.__init__(self, (width, height))
    self.size = (width, height)
    self.fill((255,255,255))

  def clear(self):
    self.fill((255,255,255))

def main():
  pygame.init()
  canvas = Canvas(600,500)
  screen = pygame.display.set_mode(canvas.get_size())
  pygame.display.set_caption("Aldrin's Paint")

  frame_clock = pygame.time.Clock()
  game_running = True
  while(game_running):
    frame_clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    screen.blit(canvas, (0, 0))
    pygame.display.flip()

if __name__ == "__main__": main()
