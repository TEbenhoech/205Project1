from PIL import Image
import os
#https://github.com/TEbenhoech/205Project1
path = "/home/ubuntu/workspace/Project1Images/"
images = os.listdir(path)
#Making array of images from file
for i in range(len(images)):
    images[i] = Image.open("%s%s" % (path,images[i]))
#Getting image size and setting up result image
xSize, ySize = images[0].size
result = Image.new("RGB",(xSize,ySize),color=0)
#Initializing arrays to store pixel values
redPixles = []
greenPixles = []
bluePixles =[]
#Looping through every pixel of the iamges, and then every image
for x in range(xSize):
    for y in range(ySize):
        for i in range(len(images)):
            #Getting pixel values
            red , green , blue = images[i].getpixel((x,y))
            redPixles.append(red)
            greenPixles.append(green)
            bluePixles.append(blue)
        #Sorting for median
        redPixles.sort()
        greenPixles.sort()
        bluePixles.sort()
        #Drawing pixel
        result.putpixel((x,y),(redPixles[4],greenPixles[4],bluePixles[4]))
        #Reset arrays for next pixel
        redPixles = []
        greenPixles = []
        bluePixles = []
    print(x)
result.save("%s%s" % (path,"result.png"))