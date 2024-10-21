class POINTYPOINTYPOINTY:
    def __init__(self, x=0 , y=0):
        self.x=x
        self.y=y
    def __str__(self):
        print('(',self.x,',',self.y,')')
# printing obj
POINTY=POINTYPOINTYPOINTY(2,3)
POINTY.__str__()