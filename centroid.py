from Tkinter import *
master = Tk()
cvs = Canvas(master,width = 800, height = 800)
cvs.pack()
#polygon = [200, 200, 230, 200, 260, 210, 290, 230, 320, 260, 340, 290, 350, 320, 350, 350, 340, 380, 320, 410, 290, 440, 260, 460, 230, 470, 200, 470, 170, 460, 140, 440, 110, 410, 90, 380, 80, 350, 80, 320, 90, 290, 110, 260, 140, 230, 170, 210, 200, 200]
#polygon = [200, 200, 210, 190, 220, 190, 270, 190, 330, 240, 370, 340, 310, 440, 210, 430, 120, 390, 100, 350, 130, 330, 170, 360, 200, 380, 290, 400, 330, 340, 300, 260, 260, 220, 210, 220, 190, 260, 160, 290, 50, 260, 200, 200]
polygon = [200, 200, 200, 70, 240, 70, 240, 200, 430, 480, 370, 480, 230, 260, 220, 230, 200, 260, 80, 470, 20, 200, 70, 60, 200, 200]
showpoly = cvs.create_polygon(polygon,fill = 'blue')
alternate = -1
polygonx = []
polygony = []
for element in polygon:
    alternate = alternate * -1
    if alternate == 1:
        polygonx.append(element)
    if alternate == -1:
        polygony.append(element)
setlength = len(polygon)/2
xsum = 0
ysum = 0
for element in polygonx:
    xsum = xsum + element
for element in polygony:
    ysum = ysum + element

xaverage = xsum/setlength
yaverage = ysum/setlength

centroid = [xaverage,yaverage]

showcentroid = cvs.create_rectangle(xaverage - 2, yaverage -2,xaverage + 2, yaverage +2, fill = 'red')
master.mainloop()
