import mcpi.minecraft as minecraft

import mcpi.block as block
import datetime


startPosY = 100

ballPosX = 0
ballPosY = startPosY + 1
ballPosZ = 0

yelloScore = 0
blueScore = 0
preTime = 0

def buildField():
    mc.setBlocks(-29,startPosY,-19,29,15,19,block.AIR.id)

    mc.setBlocks(-29,startPosY,-19,29,startPosY,19,block.WOOL.id,0)
    mc.setBlocks(-28,startPosY,-18,28,startPosY,18,block.WOOL.id,13)
    mc.setBlocks(ballPosX,startPosY,-19,ballPosX,0,19,block.WOOL.id,0)
    mc.setBlocks(-29,startPosY,-8,-18,startPosY,8,block.WOOL.id,0)
    mc.setBlocks(29,startPosY,-8,18,startPosY,8,block.WOOL.id,0)
    mc.setBlocks(-28,startPosY,-7,-19,startPosY,7,block.WOOL.id,13)
    mc.setBlocks(28,startPosY,-7,19,startPosY,7,block.WOOL.id,13)

    mc.setBlocks(29,startPosY+3,-5,29,startPosY+3,5,block.WOOL.id,4)
    mc.setBlocks(-29,startPosY+3,-5,-29,startPosY+3,5,block.WOOL.id,11)

    showYelloScore(29,startPosY+5,-1,yelloScore)
    showBlueScore(-29,startPosY+5,1,blueScore)

def showYelloScore(baseX,baseY,baseZ,num):
   if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetZ = 0
       for line in f.readlines():
            data = line.split(",")
            for cell in data:
               if cell == "1":
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,4)
               else:
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

               offsetZ = offsetZ + 1

            offsetY = offsetY - 1
            offsetZ = 0

def showBlueScore(baseX,baseY,baseZ,num):
    if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetZ = 0
       for line in f.readlines():
            data = line.split(",")
            for cell in data:
               if cell == "1":
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,11)
               else:                    
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

               offsetZ = offsetZ - 1

            offsetY = offsetY - 1
            offsetZ = 0

def showNum(baseX,baseY,baseZ,num):
    if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetX = 0
       for line in f.readlines():
            data = line.split(",")
            for cell in data:
                offsetX = offsetX + 1
                offsetY = offsetY - 1
                offsetX = 0
                
                
mc = minecraft.Minecraft.create()
mc.postToChat("welcome to nille's world")
buildField()

while True:
    if mc.getBlock(ballPosX,ballPosY,ballPosZ) == block.AIR.id:
        mc.setBlock(ballPosX,ballPosY,ballPosZ,block.WOOL.id,1)
        
    timeNow = datetime.datetime.now()
    if preTime != timeNow.minute:
        preTime = timeNow.minute
        if timeNow.hour/10 != 0:
            showNum(-8,3,-20,int(timeNow.hour/10))
        else:
            mc.setBlocks(-8,3,-20,-6,7,-20,block.AIR.id)
        showNum(-4,3,-20,int(timeNow.hour%10))
        mc.setBlock(0,4,-20,block.WOOL.id,15)
        mc.setBlock(0,6,-20,block.WOOL.id,15)
        showNum(2,3,-20,int(timeNow.minute/10))
        showNum(6,3,-20,int(timeNow.minute%10))
        
    events = mc.events.pollBlockHits()

    for e in events:
        if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z ==ballPosZ:
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
            mc.setBlock(ballPosX,ballPosY,ballPosZ,block.TNT.id,1)
            if ballPosZ >= -5 and ballPosZ <= 5:
                mc.postToChat('GOAL')
            if ballPosX <-29:
                yelloScore = yelloScore + 1
            if ballPosX > 29:
                blueScore = blueScore + 1
                
            mc.postToChat('YELLO:'+ str(yelloScore) + '   BLUE:' +str(blueScore))
            
        else:
            mc.postToChat('OUT')
        ballPosX = yelloScore - blueScore
        if ballPosX > 15:
            ballPosX = 15
        if ballPosX < -15:
            ballPosX = -15
        ballPosZ = 0
        buildField()