from pygame import *
font.init()

window = display.set_mode((960, 540))
display.set_caption('Ping_Pong')
game = True
Fps = 60


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, w, h):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y > 10:
            self.rect.y += self.speed
        if keys[K_w] and self.rect.y < 950:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y > 10:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y < 950:
            self.rect.y -= self.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    time.delay(50)
