
from settings import *
from sprite import Sprite

class Player:
   
    GRAVITY_VELO = 0

    def __init__(self):

        self.position = Vec2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.velo = Vec2(1, 1)

        # NOTE(Tejas): True is left side and False is right,
        #              this is only here to flip the sprite.
        self.direction = False 

        self.is_on_ground = False

        # drawing player variables
        self.is_jumping = False
        self.is_falling = False
        self.is_running = True

        # sprite for the player
        player_jump = "./assets/MainCharacters/MaskDude/jump.png"
        self.player_jump = Sprite(player_jump, 32, 32, 1)

        player_fall = "./assets/MainCharacters/MaskDude/fall.png"
        self.player_fall = Sprite(player_fall, 32, 32, 1)

        player_idle_sheet = "./assets/MainCharacters/MaskDude/idle.png"
        self.player_idle = Sprite(player_idle_sheet, 32, 32, 11)

        player_running_sheet = "./assets/MainCharacters/MaskDude/run.png"
        self.player_run = Sprite(player_running_sheet, 32, 32, 12)
        

    def move(self, dx, dy):

        self.position.x += dx
        self.position.y += dy


    def update_gravity(self):

        self.GRAVITY_VELO += max(1, GRAVITY / FPS)
        self.move(0, self.GRAVITY_VELO)
            
   
    def update_key(self):

        keys = pygame.key.get_pressed()

        # Jump Key
        if keys[pygame.K_SPACE]:
            self.is_jumping = True

        # Player Moving Keys
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.move(+2, 0)
            self.is_running = True
            self.direction = False
        elif keys[pygame.K_a] or keys[pygame.K_LEFT] :
            self.move(-2, 0)
            self.is_running = True
            self.direction = True
        else:
            self.is_running = False


    def update(self):
       
        self.update_gravity()
        self.update_key()

        # TODO(Tejas): Player width is 32 but it is being 2x'ed so 64 / 2 = 32
        #              Maybe it would make sense to store this in a variable
        if self.position.y > SCREEN_HEIGHT - 32:
            self.position.y = SCREEN_HEIGHT - 32
            self.is_on_ground = True
        else:
            self.is_on_ground = False

        if self.is_on_ground:
            self.GRAVITY_VELO = 0
        

    def draw(self, window):

        if self.is_jumping:
            self.player_jump.animate(window, self.position, self.direction)
        elif self.is_falling:
            self.player_fall.animate(window, self.position, self.direction)
        elif self.is_running:
            self.player_run.animate(window, self.position, self.direction)
        else:
            self.player_idle.animate(window, self.position, self.direction)
