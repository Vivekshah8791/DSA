class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x=0
        y=0
        if xCenter<x1:
            x=x1
        elif xCenter>x2:
            x=x2
        else:
            x=xCenter
        if yCenter<y1:
            y=y1
        elif yCenter>y2:
            y=y2
        else:
            y=yCenter
        dis=(x-xCenter)**2+(y-yCenter)**2
        return dis<=radius**2