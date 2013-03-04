import sys
import math
from Tkinter import *
from PIL import Image, ImageTk
master = Tk()

cvswidth = 800
cvsheight = 800
cvs = Canvas(master,width = cvswidth,height = cvsheight)
cvs.pack()
window = Tk()
scaleprompt = raw_input("Scale?")
scale = float(scaleprompt)

#image1 = Image.open("/Users/anselsteele/Desktop/foldpy/sprites/robot1a.gif")
#polystring1 = list(image1.getdata())
#polystring1 = [300, 300, 290, 220, 280, 220, 270, 270, 270, 300, 280, 320, 260, 320, 250, 300, 250, 290, 250, 280, 270, 220, 270, 220, 270, 200, 290, 200, 300, 200, 300, 190, 290, 190, 290, 150, 340, 150, 340, 190, 330, 190, 330, 200, 360, 200, 360, 220, 380, 280, 380, 300, 370, 320, 350, 320, 360, 300, 360, 280, 350, 220, 340, 220, 330, 300, 340, 300, 340, 390, 370, 390, 370, 400, 320, 400, 320, 300, 310, 300, 310, 400, 260, 400, 260, 390, 290, 390, 290, 300, 300, 300]
#polystring1 = [300, 300, 300, 370, 320, 380, 310, 390, 310, 450, 300, 460, 300, 470, 310, 480, 310, 540, 280, 550, 270, 560, 270, 570, 340, 570, 340, 550, 330, 540, 340, 500, 340, 460, 330, 450, 340, 440, 350, 380, 360, 380, 370, 440, 380, 450, 370, 460, 370, 500, 380, 540, 370, 550, 370, 570, 440, 570, 440, 560, 430, 550, 400, 540, 400, 480, 410, 470, 410, 460, 400, 450, 400, 390, 390, 380, 410, 370, 410, 300, 400, 260, 400, 250, 410, 250, 430, 320, 430, 380, 420, 390, 410, 410, 410, 420, 420, 440, 430, 450, 420, 430, 420, 420, 420, 410, 430, 390, 440, 390, 450, 410, 450, 430, 440, 450, 450, 440, 460, 420, 460, 410, 450, 390, 440, 380, 450, 360, 450, 330, 460, 320, 450, 310, 430, 250, 430, 240, 410, 230, 390, 220, 380, 210, 500, 420, 380, 210, 380, 200, 390, 200, 390, 170, 380, 150, 370, 140, 360, 140, 350, 140, 340, 150, 330, 170, 330, 200, 340, 200, 340, 210, 330, 220, 290, 240, 280, 250, 260, 310, 250, 320, 260, 330, 260, 360, 270, 380, 260, 390, 250, 410, 250, 420, 260, 440, 270, 450, 260, 430, 260, 410, 270, 390, 280, 390, 290, 410, 290, 420, 290, 430, 280, 450, 290, 440, 300, 420, 300, 410, 290, 390, 280, 380, 280, 320, 300, 250, 310, 250, 300, 300]
#polystring1 =[200, 200, 230, 170, 260, 150, 290, 140, 320, 140, 350, 150, 380, 170, 410, 200, 430, 230, 440, 260, 440, 290, 430, 320, 410, 350, 380, 380, 350, 400, 330, 410, 330, 590, 280, 590, 280, 410, 260, 400, 230, 380, 200, 350, 180, 320, 170, 290, 170, 260, 180, 230, 200, 200]
polystring1 =[200, 200, 550, 200, 550, 220, 200, 220, 200, 230, 550, 230, 550, 280, 210, 280, 210, 290, 550, 290, 550, 360, 220, 360, 220, 370, 550, 370, 550, 460, 230, 460, 230, 470, 550, 470, 550, 490, 140, 490, 140, 440, 490, 440, 490, 430, 140, 430, 140, 410, 480, 410, 480, 400, 140, 400, 140, 350, 470, 350, 470, 340, 140, 340, 140, 270, 460, 270, 460, 260, 140, 260, 140, 200, 180, 200, 180, 190, 130, 190, 130, 500, 560, 500, 560, 190, 200, 190, 200, 200]
#polystring1 =[]
#polystring1 =[]
#polystring1 =[]
scalearray1 = []

limcheck = 0
center = [501,491]
xcounter = 0
ycounter = 1
loopcounter = 0
counterlim = len(polystring1) - 1
while loopcounter <= counterlim:
    findx = xcounter
    findy = ycounter
    dispx = polystring1[findx] - center[0]
    dispy = polystring1[findy] - center[1]
    scalex = dispx * scale
    scaley = dispy * scale
    newx = center[0] + scalex
    newy = center[1] + scaley
    scalearray1.append(newx)
    scalearray1.append(newy)
    xcounter = xcounter + 2
    ycounter = ycounter + 2
    loopcounter = loopcounter + 2
#Experimental method for recentering scaled image if it exceeds boundaries
#oddeven = 1
#skip = 1
#complete = 0
#while complete == 0:
#    for element in scalearray1:
 #       oddeven = oddeven * -1
  #      if element > 800:
   #         if oddeven == 1:
    #            skip = 1
     #           for element in scalearray1:
      #              skip = skip * -1
       #             if skip == -1:
        #                element = element -1
         #   if oddeven == -1:
          #      skip = 1
           #        skip = skip * -1
            #        if skip == 1:
             #           element = element -1
        #if element < 0:
         #   if oddeven == 1:
          #      skip = 1
           #     for element in scalearray1:
            #       if skip == -1:
             #           element = element +1
            #if oddeven == -1:
             #   skip = 1
              #  for element in scalearray1:
               #     skip = skip * -1
                #    if skip == 1:
                 #       element = element +1
                        
    #failure = 0                    
    #for element in scalearray1:
     #   if element > 800 or element <0:
      #      failure = 1
    #if failure == 1:
     #   complete = 0
    #else:
     #   complete = 1 
    #print scalearray1
        
        
cvs.create_polygon(scalearray1,fill = 'green',tag = 'polygon1')
cvs.update()
master.mainloop()
