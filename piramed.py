import wrap
import random


blocks=[32,64,96,128,160,192,224,256]

width=700
heith=500
wrap.world.create_world(width,heith)
line=576


for block_line in range(0,256,32):
    for ladder in range(16+block_line, 500-block_line, 32):
        wrap.sprite.add("mario-scenery", ladder, 446-block_line, "block")
