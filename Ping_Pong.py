from pygame import *
font.init()
font2 = font.SysFont('Palatino', 66)
font1 = font.SysFont('Arial', 40)
window = display.set_mode((960, 540))
display.set_caption('Ping_Pong')
background = transform.scale(image.load('Group 1.png'), (960, 540))
game = True
Finish = False
Fps = 60
win = font2.render('Left player WIN!', True, (175, 210, 31))
win_1 = font2.render('Right player WIN!', True, (175, 210, 31))
lost_l = 0
lost_r = 0


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
    def __init__(self, player_image, player_x, player_y, player_speed_x, w, h, player_speed_y):
        super().__init__(player_image, player_x, player_y, player_speed_x, w, h)
        self.speed_y = player_speed_y
    
    def update(self):
        self.rect.x += self.speed
        self.rect.y += self.speed_y
        
        

raket_1 = Player('raket.png', 40, 230, 15, 15, 100)
raket_2 = Player('raket.png', 900, 230, 15, 15, 100)
ball = Ball('ball.png', 50, 50, 5, 30, 30, 5)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if Finish != True:
        window.blit(background, (0, 0))
        raket_1.reset()
        raket_1.update_l()
        raket_2.reset()
        raket_2.update_r()
        ball.reset()
        ball.update()
        text_l = font1.render(str(lost_l), 1, (0, 0, 0))
        text_r = font1.render(str(lost_r), 1, (0, 0, 0))
        window.blit(text_l, (430, 25))
        window.blit(text_r, (485, 25))
        if ball.rect.y < 25 or ball.rect.y > 485:
            ball.speed_y *= -1
        if sprite.collide_rect(raket_1, ball):
            ball.speed *= -1
        if sprite.collide_rect(raket_2, ball):
            ball.speed *= -1
        if ball.rect.x < 0:
            lost_r += 1
            ball.rect.x = 465
            ball.rect.y = 255
            ball.speed *= -1
            ball.speed_y *= -1
        if lost_l >= 5:
            window.blit(transform.scale(image.load('Group 3.png'), (960, 540)), (0, 0))
            Finish = True
        if ball.rect.x > 960:
            lost_l += 1
            ball.rect.x = 465
            ball.rect.y = 255
            ball.speed *= -1
            ball.speed_y *= -1
        if lost_r >= 5:
            window.blit(transform.scale(image.load('Group 2.png'), (960, 540)), (0, 0))
            Finish = True
    display.update()
    time.delay(10)
