import wrap
import random




width=700
heith=500
wrap.world.create_world(width,heith)

for dec1 in range(20,500,32):
    for dec in range(20,700,160):
        wrap.sprite.add("battle_city_items",dec,dec1,"block_brick")
        wrap.sprite.add("battle_city_items", dec + 32, dec1, "block_snow")
        wrap.sprite.add("battle_city_items", dec+64, dec1, "block_snow")
        wrap.sprite.add("battle_city_items", dec + 96, dec1, "block_brick")
        bush=wrap.sprite.add("battle_city_items", dec + 128, dec1, "block_bushes")
        wrap.sprite.set_size_percent(bush,200,200)
