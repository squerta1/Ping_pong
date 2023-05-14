from pygame import *
font.init()

window = display.set_mode((960, 540))
display.set_caption('Ping_Pong')
background = transform.scale(image.load('Group1.png'), (960, 540))
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
        if keys[K_w] and self.rect.y > 25:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 415:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 25:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed
class Ball(GameSprite):
    
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed
        '''if self.rect.y <= 25 or self.rect.y >= 485:
            self.dir *= -1
'''
raket_1 = Player('raket.png', 40, 230, 15, 15, 100)
raket_2 = Player('raket.png', 900, 230, 15, 15, 100)
ball = Ball('ball.png', 50, 50, 20, 30, 30)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0, 0))
    raket_1.reset()
    raket_1.update_l()
    raket_2.reset()
    raket_2.update_r()
    ball.reset()
    ball.update()
    display.update()
    time.delay(50)
