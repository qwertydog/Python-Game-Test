import os, sys, pygame, enum, math
from pygame.locals import *


def process_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
            
            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            position = pygame.mouse.get_pos()
            message = "Mouse clicked at position: " + str(position)
            text = font.render(message, 1, (255, 0, 0))
            display.fill(Color("black"))
            player.draw()
            display.blit(text, position)
            

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass

            elif event.key == pygame.K_DOWN:
                pass

            elif event.key == pygame.K_LEFT:
                pass

            elif event.key == pygame.K_RIGHT:
                pass

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                pass

            elif event.key == pygame.K_DOWN:
                pass

            elif event.key == pygame.K_LEFT:
                pass

            elif event.key == pygame.K_RIGHT:
                pass

    return True

def width_from_percent(percent):
    return math.round(percent * width)

def height_from_percent(percent):
    return math.round(percent * height)

def load_image(name):
    image = pygame.image.load(os.path.join("data", name))

    if image.get_alpha() != None:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image

def get_sprite_from_spritesheet(spritesheet, sprite_rect = pygame.Rect(0, 0, 64, 64)):

    surf = pygame.Surface(sprite_rect.size).convert_alpha()

    surf.blit(spritesheet.sprite, (0, 0), sprite_rect)

    return surf

class Direction(enum.Enum):
    right = 1
    left = 2

class Player(pygame.sprite.Sprite):
    def __init__(self, spritesheet, position=[0,0], velocity=0, direction = Direction.right):
        pygame.sprite.Sprite.__init__(self)

        self.spritesheet = spritesheet
        self.position = position
        self.direction = direction
        self.velocity = velocity

    def move(self, direction = Direction.right):
        self.position[0] += 1
        self.direction  = direction
        self.velocity = 1

    def draw(self):
        self.sprite = get_sprite_from_spritesheet(self.spritesheet)
        display.blit(self.sprite, tuple(self.position)) 


class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, spritesheet):
        pygame.sprite.Sprite.__init__(self)
        
        self.sprite = load_image(spritesheet)
        self.rect = self.sprite.get_rect()



pygame.init()

resolution = width, height = (1280, 960)

FPS = 60

BLACK = Color("black")

display = pygame.display.set_mode(resolution)

pygame.display.set_caption("Game")

display.fill(BLACK)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

#spritesGroup = pygame.sprite.Group()

player_spritesheet = Spritesheet("platformerSprites.png")

player = Player(player_spritesheet, [500, 500])


while process_events():

    """Drawing calls"""            

    #display.fill((0, 0, 0))

    #player.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()