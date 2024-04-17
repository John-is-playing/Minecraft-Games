import mcpi.minecraft as minecraft      # import the minecraft library
import mcpi.block as block              # import the block library
import datetime                         # import the datetime library

# Set some values
ballPosX = 0                            # ball position x
ballPosY = 1                            # ball position y
ballPosZ = 0                            # ball position z
yelloScore = 0                          # yellow score
blueScore = 0                           # blue score
offsetY = 0                             # offset y
offsetZ = 0                             # offset z
offsetX = 0                             # offset x

preTime = 0                             # previous time

# Build the field
def buildField() -> None:
    mc.setBlocks(-29, 0, -19, 29, 15, 19, block.AIR.id)  # clear the field

    mc.setBlocks(-29, 0, -19, 29, 0, 19, block.WOOL.id, 0)  # set the floor
    mc.setBlocks(-28, 0, -18, 29, 0, 18, block.WOOL.id, 13)  # set the walls
    mc.setBlocks(ballPosX, 0, -19, ballPosX, 0, 19, block.WOOL.id, 0)        # set the ball position
    mc.setBlocks(-29, 0, -8, -18, 0, 8, block.WOOL.id, 0)     # set the blue team goal
    mc.setBlocks(29, 0, -8, 18, 0, 8, block.WOOL.id, 0)    # set the yellow team goal
    mc.setBlocks(-28, 0, -7, -19, 0, 7, block.WOOL.id, 13)       # set the blue team goal line
    mc.setBlocks(28, 0, -7, 19, 0, 7, block.WOOL.id, 13)         # set the yellow team goal line

    mc.setBlocks(29, 3, -5, 29, 3, 5, block.WOOL.id, 4)    # set the yellow team scoreboard
    mc.setBlocks(-29, 3, -5, -29, 3, 5, block.WOOL.id, 11)  # set the blue team scoreboard
    
    showYelloScore(29, 5, -1, yelloScore)    # show the yellow team score
    showBlueScore(-29, 5, 1, blueScore)      # show the blue team score
    return

# Show the Yellow team score with the given position and number
def showYelloScore(baseX, baseY, baseZ, num) -> None:
    global ballPosX, ballPosY, ballPosZ, blueScore, yelloScore,preTime, offsetY, offsetZ, offsetX       # global variables
    if num >= 0 and num <= 9:                 # check if the number is smaller than 10
        FNAME = "/home/web/Minecraft/SwordBall/CSV/num" + str(num) + ".csv"         # file name
        f = open(FNAME, "r")                    # open the file
        offsetY = 4                            # reset offset y
        offsetZ = 0                            # reset offset z
        for line in f.readlines():            # read the file line by line
            data = line.split(",")            # split the line by comma
            for cell in data:                # read the cell by cell
                if cell == "1":                # if the cell is 1
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.WOOL.id, 4)    # set the block to yellow
                else:                        # if the cell is not 1
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.AIR.id)    # set the block to air
                offsetZ = offsetZ + 1        # increase the offset z
            offsetY = offsetY - 1            # decrease the offset y
            offsetZ = 0                       # reset the offset z
        f.close()                              # close the file
    else:                                    # if the number is bigger than 9
        mc.postToChat("Yellow won!")         # show the message
        exit()                               # exit the program
    return

# Show the Blue team score with the given position and number
def showBlueScore(baseX, baseY, baseZ, num) -> None:    # same as showYelloScore
    global ballPosX, ballPosY, ballPosZ, blueScore, yelloScore,preTime, offsetY, offsetZ, offsetX   # global variables
    if num >= 0 and num <= 9:                   
        FNAME = "/home/web/Minecraft/SwordBall/R_CSV/num" + str(num) + ".csv"
        f = open(FNAME, "r")
        offsetY = 4
        offsetZ = 0
        for line in f.readlines():
            data = line.split(",")
            for cell in data:
                if cell == "1":
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.WOOL.id, 4)
                else:
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.AIR.id)
                offsetZ += 1
            offsetY = offsetY - 1
            offsetZ = 0
    else:
        mc.postToChat("Blue won!")
        exit()
    return

# Show the number with the given position and number
def showNum(baseX, baseY, baseZ, num) -> None :    # same as showYelloScore
    global ballPosX, ballPosY, ballPosZ, blueScore, yelloScore,preTime, offsetY, offsetZ, offsetX
    if num >= 0 and num <= 9:
        FNAME = "/home/web/Minecraft/SwordBall/CSV/num" + str(num) + ".csv"
        f = open(FNAME, "r")
        offsetY = 4
        offsetX = 0
        for line in f.readlines():
            data = line.split(",")
            for cell in data:
                if cell == "1":
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.WOOL.id, 4)
                else:
                    mc.setBlock(baseX,baseY+offsetY, baseZ+offsetZ, block.AIR.id)
                    offsetX += 1
            offsetY = offsetY - 1
            offsetZ = 0
    return

mc = minecraft.Minecraft.create()       # create the minecraft object
mc.postToChat("Welcome to football contest!")   # show the message

buildField()                             # build the field
while True:                              # main loop
    if mc.getBlock(ballPosX,ballPosY,ballPosZ) == block.AIR.id:      # if the ball is not on the field
        mc.setBlock(ballPosX,ballPosY,ballPosZ, block.WOOL.id, 1)    # set the ball to white

    timeNow = datetime.datetime.now()    # get the current time
    if preTime != timeNow.minute:        # if the minute is changed
        preTime = timeNow.minute          # update the previous time
        if timeNow.hour//10 != 0:          # if the hour is not 00
            showNum(-8,3,-20,timeNow.hour//10)    # show the hour
        else:                                # if the hour is 00
            mc.setBlocks(-8,3,-20,-6,7,-20,block.AIR.id)    # clear the hour
        showNum(-4,3,-20,timeNow.hour % 10)    # show the minute
        mc.setBlock(0,4,-20,block.WOOL.id, 15)    # show the colon
        mc.setBlock(0,6,-20,block.WOOL.id, 15)    # show the colon
        showNum(2,3,-20,timeNow.minute // 10)    # show the second
        showNum(6,3,-20,timeNow.minute % 10)         # show the second

    events = mc.events.pollBlockHits()   # get the block hits

    for e in events:                      # loop through the block hits
        if e.pos.x == ballPosX and e.pos.y == ballPosY and e.pos.z == ballPosZ:  # if the ball is hit
            if e.face == 5:  # if the ball is hit from the top
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)    # set the ball to air
                mc.setBlock(e.pos.x-1,e.pos.y,e.pos.z,block.WOOL.id, 1)  # set the ball to white
                ballPosX = ballPosX - 1    # move the ball to the left
            if e.face == 3:  # if the ball is hit from the bottom
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)    # set the ball to air
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z-1,block.WOOL.id, 1)  # set the ball to white
                ballPosZ = ballPosZ - 1    # move the ball to the back
            if e.face == 4:      # if the ball is hit from the left
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)    # set the ball to air
                mc.setBlock(e.pos.x+1,e.pos.y,e.pos.z,block.WOOL.id, 1)  # set the ball to white
                ballPosX = ballPosX + 1    # move the ball to the right
            if e.face == 2:  # if the ball is hit from the right
                mc.setBlock(e.pos.x,e.pos.y,e.pos.z,block.AIR.id)    # set the ball to air
                mc.setBlock(e.pos.x-1,e.pos.y,e.pos.z+1,block.WOOL.id, 1)   # set the ball to white
                ballPosZ = ballPosZ + 1    # move the ball to the front

    if ballPosX < -29 or ballPosX > 29 or ballPosZ < -19 or ballPosZ > 19:  # if the ball is out of the field
        if ballPosZ >= -5 and ballPosZ <= 5:     # if the ball is in the center
            mc.setBlock(ballPosX,ballPosY,ballPosZ,block.AIR.id)    # set the ball to air
            mc.postToChat("GOAL")                 # show the message
            if ballPosX <-29:                     # if the ball is in the left side
                yelloScore += 1                     # increase the yellow score
            if ballPosX > 29:                     # if the ball is in the right side
                blueScore += 1                      # increase the blue score
            mc.postToChat(f"YELLO:{str(yelloScore)}     Blue:{str(blueScore)}")    # show the score
        else:                                     # if the ball is not in the center
            mc.setBlock(ballPosX,ballPosY,ballPosZ,block.TNT.id, 1)    # set the ball to TNT
            mc.postToChat("OUT")                  # show the message
        ballPosX = yelloScore - blueScore      # reset the ball position
        if ballPosX > 15:                       # if the ball position is too far
            ballPosX = 15                       # set the ball position to 15
        if ballPosX < -15:                      # if the ball position is too far
            ballPosX = -15                      # set the ball position to -15
        ballPosZ = 0                            # reset the ball position
        buildField()                            # build the field again
