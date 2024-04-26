from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

message = "Hello, World"

mc.postToChat(message)

mc.setBlock(x,y,z,45)

# Moving Block in range of 10
for i in range(10):
    x += 1
    mc.setBlock(x,y,z,0)
    mc.setBlock(x+1,y,z,45)
    sleep(1)
    
mc.setBlock(x+1,y,z,0)

    mc.setBlocks(x-1-i, y+13-i, z+5, x+1+i, y+13-i, z+5, brick)
