import wrap
import random




width=700
heith=700
wrap.world.create_world(width,heith)

for vine in range(0,500,28):
    wrap.sprite.add("mario-items",width-200,vine,"vine2")

for line in range(450,500,32):
    for ground in range(16,732,32):
        wrap.sprite.add("mario-scenery",ground,line,"ground")

for block_line in range(16,256,32):
    for brick in range(block_line,288,32):
        wrap.sprite.add("mario-scenery", brick, 434-block_line, "block")

for stairs in range(0,6):
    wrap.sprite.add("mario-items", 24+stairs*48,50+stairs*24 , "moving_platform1")
