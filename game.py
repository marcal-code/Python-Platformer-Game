
from settings import *
from player import Player

class Game:


    def __init__(self):

        pygame.init()

        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Game")

        self.clock = pygame.time.Clock()

        self.running = True

        self.player = Player()


    def get_background(self, file_name):

        bg_image = pygame.image.load(file_name)
        img_x, img_y, img_width , img_height = bg_image.get_rect()

        tiles = []

        for i in range(SCREEN_HEIGHT // img_height + 1):
            for j in range(SCREEN_WIDTH // img_width + 1):

                pos = (j * img_width, i * img_height)
                tiles.append(pos)

        return tiles, bg_image


    def update(self):

        self.player.update()


    def draw(self):

        self.window.fill((0, 0, 0))

        background, bg_image = self.get_background("./assets/Background/Brown.png")
        for tile in background:
            self.window.blit(bg_image, tile)

        self.player.draw(self.window)

    
    def run(self):

        self.clock.tick(FPS) 

        while(self.running):

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False 

                key_pressed = pygame.key.get_pressed()
                if (key_pressed[pygame.K_ESCAPE]):
                    self.running = False

            # do the updatings here
            self.update()

            # do the drawings here
            self.draw()

            pygame.display.flip()


    def __del__(self):

        pygame.quit()
