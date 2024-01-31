import wrap
import random




width=700
heith=700
wrap.world.create_world(width,heith)


for block_line in range(0,256,32):
    for ladder in range(16+block_line, 500-block_line, 32):
        wrap.sprite.add("mario-scenery", ladder, 684-block_line, "block")

for block_line in range(0,256,32):
    for ladder in range(16+block_line, 500-block_line, 32):
        wrap.sprite.add("mario-scenery", ladder, 204+block_line, "ground")
