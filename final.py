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
        if key_pressed[K_s] and self.rect.y < win_height - 100:
           self.rect.y += self.speed
    def update2(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - 100:
           self.rect.y += self.speed

back = (32, 118, 67)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
clock = time.Clock()
fps = 60

player1 = GameSprite('racket.png', 10, 400, 3, 20, 100)
player2 = GameSprite('racket.png', 650, 400, 3, 20, 100)
ball = GameSprite('tenis_ball.png', 200, 200, 1, 50, 50)

red = 255, 36, 36

font.init()
font = font.Font(None , 52)
game_over = font.render('GAME OVER', True, (255, 36, 36))

speed_x = 4
speed_y = 4

point_1 = 0
point_2 = 0

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        display.update()
        window.fill(back)
        player1.reset()
        player2.reset()
        ball.reset()
        player1.update()
        player2.update2()

        ball.rect.y += speed_y
        ball.rect.x += speed_x

        game_over = font.render(str(point_1) + ':' + str(point_2), True, (255, 255, 255))
        window.blit(game_over, (300, 100))

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x > win_width-50 or ball.rect.x < 0:     
            speed_x *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            #finish = True
            point_1 += 1
            #window.blit(game_over, (0, 0))

        if ball.rect.x > win_width-50:
            #finish = True
            point_2 += 1


    display.update()
    clock.tick(fps)
        
