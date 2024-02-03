import wrap
import random




width=500
heith=500
wrap.world.create_world(width,heith)


for block_line in range(0,240,32):
    for brick in range(block_line+48,436-block_line,32):
        wrap.sprite.add("mario-scenery", brick, block_line+16+block_line, "ground")

for block_line in range(0,240,32):
    for brick in range(block_line+48,436-block_line,32):
        wrap.sprite.add("mario-scenery", brick, 464-block_line-block_line, "ground")

for block_line in range(0,240,32):
    for brick in range(block_line+32,468,32):
        wrap.sprite.add("mario-scenery", 464,brick , "ground")