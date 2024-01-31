import wrap
import random


# rez= range(5,12,4)

# for ran in rez:
#     print(ran)


width=700
heith=500
wrap.world.create_world(width,heith)

for tank in range(30):
    x=random.randint(100,600)
    y = random.randint(100, 400)
    cost= random.choice(["tank_enemy_size1_green1","tank_enemy_size1_purple1","tank_enemy_size1_yellow1"])
    wrap.sprite.add("battle_city_tanks",x,y,cost)

@wrap.always()
def t_angle(pos_x,pos_y):
    for tank in range(30):
        wrap.sprite.set_angle_to_point(tank,pos_x,pos_y)

