import wrap
import random

sprites=[]
balls=[]

width=700
heith=500
wrap.world.create_world(width,heith)

mar= wrap.sprite.add("mario-1-big",width/2,heith/2,"walk1")
arm= wrap.sprite.add("mario-enemies",width/2,heith/2,"armadillo_go")
cloud= wrap.sprite.add("mario-enemies",width/2,heith/2,"cloud")
crab= wrap.sprite.add("mario-enemies",width/2,heith/2,"crab")
plant= wrap.sprite.add("mario-enemies",width/2,heith/2,"plant_blue")

sprites.append(mar)
sprites.append(arm)
sprites.append(cloud)
sprites.append(crab)
sprites.append(plant)
print(sprites)


xspeed=5
yspeed=5


for hi in sprites:
    x= random.randint(100,300)
    y= random.randint(100,400)
    wrap.sprite.move_to(hi,x,y)
    s_width=random.randint(20,50)
    s_heith = random.randint(20, 50)
    wrap.sprite.set_size(hi,s_width,s_heith)



print(balls)

@wrap.on_key_down(wrap.K_SPACE)
def ball_spawn():
    for b_spawn in sprites:
        sy = wrap.sprite.get_y(b_spawn)
        s_right = wrap.sprite.get_right(b_spawn)
        ball = wrap.sprite.add("mario-enemies", s_right, sy, "lava_ball")
        balls.append(ball)
        wrap.sprite.move_left_to(ball, s_right)
        wrap.sprite.set_angle(ball, 180)

@wrap.always()
def ball_move():
    global xspeed,yspeed
    for b_move in balls:
        bx= wrap.sprite.get_x(b_move)
        by = wrap.sprite.get_y(b_move)
        if by>=heith-17:
            continue
        if bx>=width-15:
            wrap.sprite.set_angle(b_move, 270)
            wrap.sprite.move(b_move, 0, 5)
        else:
            wrap.sprite.move(b_move, 5, 0)



