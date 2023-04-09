from pygame import *
'''Необходимые классы'''
 
#класс-родитель для спрайтов
class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, player_width, player_height):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
       
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()

        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed 
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 500:
           self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 500:
           self.rect.y += self.speed

back = (32, 118, 67)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))


player1 = GameSprite('racket.png', 10, 400, 1, 20, 100)
player2 = GameSprite('racket.png', 500, 400, 1, 20, 100)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 100, 100)

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
           

    display.update()
    window.fill(back)
    player1.reset()
    player2.reset()
    ball.reset()
    player1.update()
    player2.update2()
