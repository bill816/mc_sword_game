import mcpi.minecraft as minecraft
import mcpi.block as block
import datetime

sx = 1079
sy = 66 
sz = 1281


widthx = 29
widthz = 19

ballPosX = sx
ballPosY = sy + 1
ballPosZ = sz

yelloScore = 0
blueScore = 0

preTime = 0

def showYelloScore(mc,baseX,baseY,baseZ,num):
   if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetZ = 0
       for line in f.readlines():
            data = line.strip().split(",")
            print(data)
            for cell in data:
               if cell == "1":
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,4)
               else:
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

               offsetZ = offsetZ + 1

            offsetY = offsetY - 1
            offsetZ = 0

def showBlueScore(mc,baseX,baseY,baseZ,num):
    if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetZ = 0
       for line in f.readlines():
            data = line.strip().split(",")
            for cell in data:
               if cell == "1":
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.WOOL.id,11)
               else:                    
                   mc.setBlock(baseX,baseY+offsetY,baseZ+offsetZ,block.AIR.id)

               offsetZ = offsetZ - 1

            offsetY = offsetY - 1
            offsetZ = 0

def showNum(mc,baseX,baseY,baseZ,num):
    if num >= 0 and num <= 9:
       FNAME = "num"+str(num)+".csv"
       f = open(FNAME,"r")
       offsetY = 4
       offsetX = 0
       for line in f.readlines():
            data = line.strip().split(",")
            for cell in data:
                if cell == "1":
                    mc.setBlock(baseX+offsetX,baseY+offsetY,baseZ,block.WOOL.id,1)
                else:
                    mc.setBlock(baseX+offsetX,baseY+offsetY,baseZ,block.AIR.id)
                offsetX = offsetX + 1
            offsetY = offsetY - 1
            offsetX = 0

def buildField(mc):    


    leftx = sx - widthx 
    rightx = sx + widthx 

    topz = sz - widthz
    downz = sz + widthz

    #先填一个立体空气
    mc.setBlocks(leftx,sy,topz,rightx,sy + 15,downz,block.AIR.id)

    #画一个白色平面足球场
    mc.setBlocks(leftx,sy,topz,rightx,sy,downz,block.WOOL.id,0)
    #画一个绿色平面足球场,覆盖上面的白色
    mc.setBlocks(sx-28,sy,sz-18,sx+28,sy,sz+18,block.WOOL.id,13)
    #白色中点
    mc.setBlocks(sx,sy,topz,sx,sy,downz,block.WOOL.id,0)

    #蓝队球门
    mc.setBlocks(sx-29,sy,sz-8,sx-18,sy,sz+8,block.WOOL.id,0)
    mc.setBlocks(sx-28,sy,sz-7,sx-19,sy,sz+7,block.WOOL.id,13)

    #黄队球门
    mc.setBlocks(sx+29,sy,sz-8,sx+18,sy,sz+8,block.WOOL.id,0)
    mc.setBlocks(sx+28,sy,sz-7,sx+19,sy,sz+7,block.WOOL.id,13)

    '''
    #左边球门附近白平面
    mc.setBlocks(leftx,sy,sz-8,leftx+1,sy,block.WOOL.id,0)
    #填充回绿色
    mc.setBlocks(leftx+1,sy,sz-7,sx-19,sy,sz+7,block.WOOL.id,13)

    #右边球门附近白平面
    mc.setBlocks(sx+29,sy,sz-8,sx+18,sy,sz+8,block.WOOL.id,0)
    #填充回绿色
    mc.setBlocks(sx+28,sy,sz-7,sx+19,sy,sz+7,block.WOOL.id,13)
    '''
    
    #左边分数
    mc.setBlocks(sx+29,sy+3,sz-5,sx+29,sy+3,sz+5,block.WOOL.id,4)
    #右边分数
    mc.setBlocks(sx-29,sy+3,sz-5,sx-29,sy+3,sz+5,block.WOOL.id,11)

    showYelloScore(mc,sx+29,sy+5,sz-1,yelloScore)
    showBlueScore(mc,sx-29,sy+5,sz+1,blueScore)

def main():
    mc = minecraft.Minecraft.create()
    mc.postToChat("welcome to bill's world")
    buildField(mc)

    global preTime
    global ballPosX
    global ballPosY
    global ballPosZ
    global yelloScore
    global blueScore 

    while True:
        import time
        time.sleep(0.2)
        timeNow = datetime.datetime.now()
        print(timeNow)
        if preTime != timeNow.minute:
            preTime = timeNow.minute
            if timeNow.hour/10 != 0:
                showNum(mc,sx-8,sy+3,sz-20,int(timeNow.hour/10))
            else:
                mc.setBlocks(sx-8,sy+3,sz-20,sx-6,sy+7,sz-20,block.AIR.id)
            showNum(mc,sx-4,sy+3,sz-20,int(timeNow.hour%10))
            mc.setBlock(sx,sy+4,sz-20,block.WOOL.id,15)
            mc.setBlock(sx,sy+6,sz-20,block.WOOL.id,15)
            showNum(mc,sx+2,sy+3,sz-20,int(timeNow.minute/10))
            showNum(mc,sx+6,sy+3,sz-20,int(timeNow.minute%10))
        


        #如果球的位置为空气，设置球的位置
        if mc.getBlock(ballPosX,ballPosY,ballPosZ) == block.AIR.id:
            mc.setBlock(ballPosX,ballPosY,ballPosZ,block.WOOL.id,1)

        #检测球被击打事件
        events = mc.events.pollBlockHits()
        print(events)
        for e in events:
            #击打为球的位置
            if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z == ballPosZ:
                #击打东面
                if e.face == 5:
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                    mc.setBlock(e.pos.x-1,e.pos.y,e.pos.z,block.WOOL.id,1)
                    ballPosX = ballPosX - 1
                #击打南面
                if e.face == 3:
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z-1,block.WOOL.id,1)
                    ballPosZ = ballPosZ - 1
                #击打西面
                if e.face == 4:
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                    mc.setBlock(e.pos.x+1,e.pos.y,e.pos.z,block.WOOL.id,1)
                    ballPosX = ballPosX + 1
                #击打北面
                if e.face == 2:
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)
                    mc.setBlock(e.pos.x,e.pos.y,e.pos.z+1,block.WOOL.id,1)
                    ballPosZ = ballPosZ + 1

            if ballPosX <sx-29 or ballPosX >sx+29 or ballPosZ < sz-19 or ballPosZ > sz+19:
                if ballPosZ >= sz-5 and ballPosZ <= sz+5:
                    #进球了
                    mc.postToChat('GOAL')
                    if ballPosX <sx-29:
                        yelloScore = yelloScore + 1
                    if ballPosX > sx+29:
                        blueScore = blueScore + 1
                    mc.postToChat('YELLO:'+ str(yelloScore) + '   BLUE:' + str(blueScore))
                else:
                    #在出界位置放一个炸弹
                    #mc.setBlock(ballPosX,ballPosY,ballPosZ,block.TNT.id,1)
                    mc.postToChat('OUT')

                ballPosX = sx
                ballPosY = sy + 1
                ballPosZ = sz

                '''
                ballPosX = yelloScore - blueScore
                if ballPosX > 15:
                    ballPosX = 15
                if ballPosX < -15:
                    ballPosX = -15
                ballPosZ = 0
                '''
                buildField(mc)

if __name__ == "__main__":
    main()