import wrap
import random




width=700
heith=700
wrap.world.create_world(width,heith)


for block_line in range(0,240,32):
    for brick in range(block_line+16,288,32):
        wrap.sprite.add("mario-scenery", brick, 206+block_line, "ground")

for block_line in range(0,240,32):
    for brick in range(304,576-block_line,32):
        wrap.sprite.add("mario-items", brick, 206+block_line, "block_empty")

for block_line in range(0,256,32):
    for brick in range(304,block_line+368,32):
        wrap.sprite.add("mario-scenery", brick, 462+block_line, "block")

for block_line in range(0,256,32):
    for brick in range(240-block_line,304,32):
        wrap.sprite.add("mario-items", brick, 462+block_line, "block_bricks")

