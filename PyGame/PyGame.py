import os, sys, pygame, enum
from pygame.locals import *


def process_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
            (event.type == KEYDOWN and event.key == K_ESCAPE):
            
            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            text = font.render(str(pygame.mouse.get_pos()), 1, (255, 0, 0))
            display.fill(Color("black"))
            display.blit(text, (1000, 900))
            

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

def load_image(name):
    image = pygame.image.load(os.path.join("data", name))

    if image.getalpha():
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image


class Dir(enum.Enum):
    right = 1
    left = 2

class Player:
    def __init__(self, sprites, position=(0,0), velocity=0, direction=Dir.right):
        self.sprites_list = sprites
        self.position = position
        self.direction = direction
        self.velocity = velocity

    def update():
        pass

class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self, ):
        pygame.sprite.Sprite.__init__(self)
        
        this.image = load_image("platformerSprites.png")
        this.rect = rect



pygame.init()

resolution = width, height = (1280, 960)

FPS = 60

BLACK = Color("black")

display = pygame.display.set_mode(resolution)

pygame.display.set_caption("Campbell Game")

display.fill(BLACK)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 26)

#display.blit(spritesheet, (0, 0))

spritesGroup = pygame.sprite.Group()

#for sprite in spritesheet




#player1 = Player(sprites)


while process_events():

    """Drawing calls"""            

    #display.fill((0, 0, 0))
 
    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()