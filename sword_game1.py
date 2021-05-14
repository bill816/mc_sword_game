import mcpi.minecraft as minecraft
import mcpi.block as block

ballPosX = 0
ballPosY = 1
ballPosZ = 0
yelloScore = 0
blueScore = 0


def buildField():    
    mc.setBlocks(-29,0,-19,29,15,19,block.AIR.id)

    mc.setBlocks(-29,0,-19,29,0,19,block.WOOL.id,0)
    mc.setBlocks(-28,0,-18,28,0,18,block.WOOL.id,13)
    mc.setBlocks(0,0,-19,0,0,19,block.WOOL.id,0)
    mc.setBlocks(-29,0,-8,-18,0,8,block.WOOL.id,0)
    mc.setBlocks(29,0,-8,18,0,8,block.WOOL.id,0)
    mc.setBlocks(-28,0,-7,-19,0,7,block.WOOL.id,13)
    mc.setBlocks(28,0,-7,19,0,7,block.WOOL.id,13)
    mc.setBlocks(29,3,-5,29,3,5,block.WOOL.id,4)
    mc.setBlocks(-29,3,-5,-29,3,5,block.WOOL.id,11)
    mc = minecraft.Minecraft.create()
    mc.postToChat("welcome to nille's world")

mc = minecraft.Minecraft.create()

mc.postToChat("welcome to nille's world")

while True:
    if mc.getBlock(ballPosX,ballPosY,ballPosZ) == block.AIR.id:
        mc.setBlock(ballPosX,ballPosY,ballPosZ,block.WOOL.id,1)

    events = mc.events.pollBlockHits()


    for e in events:
        if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z == ballPosZ:
           if e.face == 5:
              mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                mc.setBlock(e.pos.x-1,e.pos.y,e.pos.z,block.WOOL.id,1)
                ballPosX = ballPosX - 1
            if e.face == 3:
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z-1,block.WOOL.id,1)
                                ballPosZ = ballPosZ - 1
            if e.face == 4:
               mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
               mc.setBlock(e.pos.x+1,e.pos.y,e.pos.z,block.WOOL.id,1)
               ballPosX = ballPosX + 1
            if e.face == 2:
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z+1,block.WOOL.id,1)
                ballPosZ = ballPosZ + 1

        if ballPosX <-29 or ballPosX >29 or ballPosZ < -19 or ballPosZ > 19:
           if ballPosZ >= -5 and ballPosZ <= 5:
                   mc.postToChat('GOAL')
                if ballPosX <-29:
                   yelloScore = yelloScore + 1
                if ballPosX > 29:
                    blueScore = blueScore + 1
                mc.postToChat('YELLO:'+ str(yelloScore) + '   BLUE:' + str(blueScore))

            else:
                mc.postToChat('OUT')
    ballPosX = 0
    ballPosZ = 0
    buildField()
