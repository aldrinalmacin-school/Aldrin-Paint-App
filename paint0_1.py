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

class Tool:
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  WHITE = (255, 255, 255)
  BLUE = (0, 0, 255)
  def __init__(self):
    self.line_width = 1
    self.draw_color = Tool.BLACK

  def check_key_pressed(self, key_pressed):
    # Draw Colors
    if key_pressed == pygame.K_r:
      self.draw_color = Tool.RED
    elif key_pressed == pygame.K_g:
      self.draw_color = Tool.GREEN
    elif key_pressed == pygame.K_w:
      self.draw_color = Tool.WHITE
    elif key_pressed == pygame.K_b:
      self.draw_color = Tool.BLUE
    elif key_pressed == pygame.K_k:
      self.draw_color = Tool.BLACK

    #line widths
    elif key_pressed == pygame.K_1:
      self.line_width = 1
    elif key_pressed == pygame.K_2:
      self.line_width = 2
    elif key_pressed == pygame.K_3:
      self.line_width = 3
    elif key_pressed == pygame.K_4:
      self.line_width = 4
    elif key_pressed == pygame.K_5:
      self.line_width = 5
    elif key_pressed == pygame.K_6:
      self.line_width = 6
    elif key_pressed == pygame.K_7:
      self.line_width = 7
    elif key_pressed == pygame.K_8:
      self.line_width = 8
    elif key_pressed == pygame.K_9:
      self.line_width = 9

    print "Line width: ", self.line_width
    print "Color: ", self.draw_color

def main():
  pygame.init()
  canvas = Canvas(MAIN_WIDTH, MAIN_HEIGHT - STRIP_HEIGHT)
  screen = pygame.display.set_mode(MAIN_SIZE)
  tool = Tool()
  pygame.display.set_caption(MAIN_TITLE)

  frame_clock = pygame.time.Clock()
  game_running = True
  while(game_running):
    frame_clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          print "Quit the game"
          game_running = False
        elif event.key == pygame.K_c:
          print "Clear the canvas"
          #clear screen
          canvas.clear()
        elif event.key == pygame.K_s:
          print "Save the Drawing"
          #save picture
          pygame.image.save(canvas, "painting.bmp")
        elif event.key == pygame.K_l:
          print "Load the Drawing"
          #load picture
          canvas = pygame.image.load("painting.bmp")
        else:
          tool.check_key_pressed(event.key)

    screen.blit(canvas, (0, STRIP_HEIGHT))
    pygame.display.flip()

if __name__ == "__main__": main()
