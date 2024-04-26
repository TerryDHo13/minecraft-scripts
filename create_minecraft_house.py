from mcpi.minecraft import *
mc = Minecraft.create()

# Get current position
x, y, z = mc.player.getPos()

# Identify Block ID 
stone = 1
brick = 45
air = 0
wood_plank = 5
glass_pane = 102
stairs = 53
fence = 85
roof = 67
roof_flat = 4

mc.setBlocks(x-10, y, z-10, x+10, y+15, z+10, air)

mc.setBlocks(x-7, y-1, z-7, x+7, y-3, z+7, stone)

mc.setBlocks(x-7, y, z-7, x+7, y, z-7, fence)
mc.setBlocks(x-7, y, z-7, x-7, y, z+7, fence)
mc.setBlocks(x+7, y, z+7, x+7, y, z-7, fence)
mc.setBlocks(x+7, y, z+7, x-7, y, z+7, fence)

mc.setBlocks(x-5, y, z-5, x+5, y+9, z+5, brick)

mc.setBlocks(x-4, y, z-4, x+4, y+8, z+4, air)

mc.setBlocks(x-4, y-1, z-4, x+4, y-1, z+4, wood_plank)

mc.setBlocks(x-4, y+4, z-4, x+4, y+4, z+4, wood_plank)

mc.setBlocks(x-4, y+9, z-4, x+4, y+9, z+4, wood_plank)

mc.setBlock(x-5, y, z, 64, 0)
mc.setBlock(x-5, y+1, z, 64, 8)

mc.setBlocks(x-5,y+1,z-2,x-5,y+2,z-3,glass_pane)
mc.setBlocks(x-5,y+1,z+2,x-5,y+2,z+3,glass_pane)
mc.setBlocks(x-5,y+6,z-2,x-5,y+7,z-3,glass_pane)
mc.setBlocks(x-5,y+6,z+2,x-5,y+7,z+3,glass_pane)
mc.setBlocks(x+5,y+1,z-2,x+5,y+2,z-3,glass_pane)
mc.setBlocks(x+5,y+1,z+2,x+5,y+2,z+3,glass_pane)
mc.setBlocks(x+5,y+6,z-2,x+5,y+7,z-3,glass_pane)
mc.setBlocks(x+5,y+6,z+2,x+5,y+7,z+3,glass_pane)


mc.setBlocks(x+3,y+4,z+4,x,y+4,z+3,air)

for i in range(5):
    mc.setBlock(x+i-1,y+i,z+3,stairs)
    mc.setBlock(x+i-1,y+i,z+4,stairs)

mc.setBlocks(x-1,y+5,z+4,x-1,y+5,z+2,fence)
mc.setBlocks(x-1,y+5,z+2,x+2,y+5,z+2,fence)

for i in range(5):
    mc.setBlocks(x-5+i, y+10+i, z-5, x-5+i, y+10+i, z+5, roof)
    mc.setBlocks(x+5-i, y+10+i, z-5, x+5-i, y+10+i, z+5, roof, 1)

mc.setBlocks(x, y+14, z-5, x, y+14, z+5, roof_flat)

for i in range(4):
    mc.setBlocks(x-1-i, y+13-i, z-5, x+1+i, y+13-i, z-5, brick)
for i in range(4):
    mc.setBlocks(x-1-i, y+13-i, z+5, x+1+i, y+13-i, z+5, brick)

