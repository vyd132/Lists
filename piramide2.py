import wrap
import random



width=700
heith=500
wrap.world.create_world(width,heith)

for block_line in range(16,500,32):
    wrap.sprite.add("mario-scenery", block_line, 446, "block")

for block_line in range(16+32, 500-32, 32):
    wrap.sprite.add("mario-scenery", block_line, 446-32, "block")

for block_line in range(16+64, 500-64, 32):
    wrap.sprite.add("mario-scenery", block_line, 446-64, "block")
