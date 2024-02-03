import wrap
import random
sprites=[]
number=[]

width=700
heith=500
wrap.world.create_world(width,heith)
wrap.sprite.add_text("text", 100, 100, text_color=[255, 255, 255])
wrap.sprite.add_text("text", 100, 100, text_color=[255, 255, 255])
wrap.sprite.add_text("text", 100, 100, text_color=[255, 255, 255])
wrap.sprite.add_text("text", 100, 100, text_color=[255, 255, 255])
wrap.sprite.add_text("text", 100, 100, text_color=[255, 255, 255])
id=0

for balls in range(0,700,32):
    ball=wrap.sprite.add("mario-enemies",balls+16,16,"fire_ball")
    wrap.sprite.set_size_percent(ball,200,200)
    sprites.append(ball)

@wrap.always()
def ball_move():
    for ball in range(len(sprites)):
        if ball%2==1:
            wrap.sprite.move(sprites[ball], 0, 5)
            wrap.sprite.move(number[ball], 0, 5)
            continue
        wrap.sprite.move(sprites[ball],0,4)
        wrap.sprite.move(number[ball], 0, 4)



for text in range(len(sprites)):
    x=wrap.sprite.get_x(sprites[text])
    numbers= wrap.sprite.add_text(str(text+1), x, 16, text_color=[84, 66, 255])
    number.append(numbers)

# exp=[632487,True,None,"hi"]
# for chislo in range(len(exp)):
#     print(exp[chislo])