import wrap
import random


# rez= range(5,12,4)

# for ran in rez:
#     print(ran)








for dec in range(40,700,40):
    if dec ==160:
        continue
    wrap.sprite.add("mario-items",dec,100,"coin")


for dec in range(20,700,30):
    wrap.sprite.add("mario-enemies",dec,heith-100,"cloud")

for dec in range(50,300,30):
    wrap.sprite.add("mario-items",150,dec,"block_bricks")