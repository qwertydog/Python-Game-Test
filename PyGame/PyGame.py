import os, sys, pygame, enum, math
from pygame.locals import *


def process_events():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:            
            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            message = "Mouse clicked at position: " + str(position)
            text = font.render(message, 1, (255, 0, 0))
            display.fill(Color("black"))        
            display.blit(text, position)    

        elif event.type == pygame.MOUSEBUTTONUP:
            pass

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.jump()

            elif event.key == pygame.K_DOWN:
                player.crouch()

            elif event.key == pygame.K_LEFT:
                player.move(Direction.left)

            elif event.key == pygame.K_RIGHT:
                player.move(Direction.right)

            elif event.key == pygame.K_SPACE:
                player.shoot()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.unjump()

            elif event.key == pygame.K_DOWN:
                player.stand()

            elif event.key == pygame.K_LEFT:
                player.stop(Direction.left)

            elif event.key == pygame.K_RIGHT:
                player.stop(Direction.right)

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

class Animation():
    def __init__(self, sprites_list):
        self.sprites = sprites_list
        self.num_sprites = len(sprites)

class Player(pygame.sprite.Sprite):
    velocity = [0, 0]
    state = "still"
    max_velocity = 10
    max_jump_height = 50

    def __init__(self, spritesheet, position=[0,0], direction = Direction.right):
        pygame.sprite.Sprite.__init__(self)
        
        self.spritesheet = spritesheet
        #self.animation_dict = animation_dict
        self.image = get_sprite_from_spritesheet(spritesheet, Rect(0, 64*8, 64, 64))
        self.rect = self.image.get_rect()
        self.position = position
        self.ground_level = self.rect.bottom
        self.direction = direction
        
    def update(self):
        if self.state == "still":
            pass
        elif self.state == "moving":
            self.move(self.direction)
        elif self.state == "jumping":
            self.jump()
        elif self.state == "crouching":
            self.crouch()

    def move(self, direction = Direction.right):
        
       # if self.rect.bottom == self.ground_level:
        if self.state != "moving":
            self.state = "moving"

       #Anima
       
       

        if direction != self.direction:
            self.image = pygame.transform.flip(self.image, 1, 0)
            self.direction = direction

        if direction == Direction.right:
            self.position[0] += self.velocity[0]
        else:
            self.position[0] -= self.velocity[0]

        if self.velocity[0] < self.max_velocity:
            self.velocity[0] += 1

    def stop(self, direction = Direction.right):
        if self.direction == direction:
            self.state = "still"
            self.velocity[0] = 0

    def jump(self):
        """self.state = "jumping"

        if self.velocity[1] > self.max_jump_height:
            self.velocity[1] = self.max_jump_height
        else:
            self.velocity[1] += 2

        if self.image.get_rect().bottom == self.ground_level:
            self.velocity[1] = -5

        if self.direction == Direction.right:
            self.position[0] += self.velocity[0]
        else:
            self.position[0] -= self.velocity[0]

        self.position[1] += self.velocity[1]"""
        pass

    def unjump(self):
        #self.state = "still"
        pass

    def crouch(self):
        pass

    def stand(self):
        pass    

    def draw(self):
        display.blit(self.image, tuple(self.position)) 


class Spritesheet():
    def __init__(self, spritesheet):
        
        self.sprite = load_image(spritesheet)
        self.rect = self.sprite.get_rect()



pygame.init()

resolution = width, height = (1280, 800)

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

ground_rect = Rect(0, 500+64, width, 500-64)

while process_events():

    """Drawing calls"""            

    display.fill(BLACK)
    display.fill((0, 130, 0), ground_rect)
    player.update()
    player.draw()

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()