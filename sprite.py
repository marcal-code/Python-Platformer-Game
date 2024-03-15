
from settings import *

class Sprite:

    def __init__(self, sprite_sheet, sprite_w, sprite_h, num_frames, ani_speed = TICK, scale_factor = 2):

        self.sprite_sheet = pygame.image.load(sprite_sheet)
        self.sprite_dim = self.sprite_sheet.get_rect()

        # scale the sprite sheet
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet,
                                                   (self.sprite_sheet.get_width() * scale_factor,
                                                    self.sprite_sheet.get_height() * scale_factor))

        self.sprite_dim = Vec2(sprite_w * scale_factor, sprite_h * scale_factor)
        self.num_frames = num_frames
        self.animation_speed = ani_speed

        self.frames = [pygame.Rect(i * self.sprite_dim.x, 0, self.sprite_dim.x, self.sprite_dim.y)
                       for i in range(self.num_frames)]

        self.frame_index = 0
        self.animation_timer = 0


    def animate(self, window, position, do_flip):

        sprite = self.sprite_sheet
        if do_flip:
            sprite = pygame.transform.flip(self.sprite_sheet, True, False)

        window.blit(sprite,
                    (position.x - self.sprite_dim.x / 2, position.y - self.sprite_dim.x / 2),
                    self.frames[self.frame_index])

        self.animation_timer += 1
        if self.animation_timer >= self.animation_speed:
            self.frame_index = (self.frame_index + 1) % self.num_frames
            self.animation_timer = 0
            self.animation_speed = TICK

