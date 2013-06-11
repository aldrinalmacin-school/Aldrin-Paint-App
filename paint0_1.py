import pygame
import random
import math

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

  def load_image(self, image):
    self.blit(image, (0,0))

class Tool:
  BLACK = (0, 0, 0)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  WHITE = (255, 255, 255)
  BLUE = (0, 0, 255)

  PENCIL = 1
  LINE = 2
  AIR_BRUSH = 3
  ELLIPSE_MODE = 4
  def __init__(self):
    self.line_width = 1
    self.draw_color = Tool.BLACK
    self.mode = Tool.PENCIL

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

    #modes
    elif key_pressed == pygame.K_p:
      self.mode = Tool.PENCIL
    elif key_pressed == pygame.K_i:
      self.mode = Tool.LINE
    elif key_pressed == pygame.K_a:
      self.mode = Tool.AIR_BRUSH
    elif key_pressed == pygame.K_e:
      self.mode = Tool.ELLIPSE_MODE

    print "Line width: ", self.line_width
    print "Color: ", self.draw_color

def get_exact_mouse_pos():
  x,y = pygame.mouse.get_pos()
  return (x, y - STRIP_HEIGHT)

def main():
  pygame.init()
  canvas = Canvas(MAIN_WIDTH, MAIN_HEIGHT - STRIP_HEIGHT)
  screen = pygame.display.set_mode(MAIN_SIZE)
  tool = Tool()
  pygame.display.set_caption(MAIN_TITLE)
  line_start = (0, STRIP_HEIGHT)
  started_line = False

  frame_clock = pygame.time.Clock()
  game_running = True
  while(game_running):
    frame_clock.tick(30)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_running = False
      elif event.type == pygame.MOUSEMOTION:
        line_end = get_exact_mouse_pos()

        if pygame.mouse.get_pressed() == (1, 0, 0):
          if tool.mode == Tool.PENCIL:
            pygame.draw.line(canvas, tool.draw_color, line_start, line_end, tool.line_width)
          elif tool.mode == Tool.AIR_BRUSH:
            if pygame.mouse.get_pressed() == (1, 0, 0):
              num_of_sprays = tool.line_width * 10
              spray_area_size = tool.line_width * 5
              for x in range(0, num_of_sprays):
                x, y = get_exact_mouse_pos()

                t = 2 * math.pi * random.random()
                u = random.random() + random.random()
                if u > 1:
                  r = 2 - u
                else:
                  r = u
                position = (int((r * math.cos(t) * spray_area_size) + x), int((r * math.sin(t) * spray_area_size) + y))
                pygame.draw.circle(canvas, tool.draw_color, position, 1)

        line_start = line_end
      if event.type == pygame.MOUSEBUTTONUP:
        if tool.mode == Tool.LINE:
          if started_line:
            pygame.draw.line(canvas, tool.draw_color, started_line, get_exact_mouse_pos(), tool.line_width)
            started_line = False
          else:
            started_line = get_exact_mouse_pos()
        elif tool.mode == Tool.ELLIPSE_MODE:
          if started_line:
            x, y = get_exact_mouse_pos()
            w, h = started_line
            pygame.draw.ellipse(canvas, tool.draw_color, pygame.Rect(started_line, (x - w, y - h)))
            started_line = False
          else:
            started_line = get_exact_mouse_pos()

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
          canvas.load_image(pygame.image.load("painting.bmp"))
        else:
          tool.check_key_pressed(event.key)

    screen.blit(canvas, (0, STRIP_HEIGHT))
    pygame.display.flip()

if __name__ == "__main__": main()
