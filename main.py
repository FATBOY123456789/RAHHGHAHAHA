class POINTYPOINTYPOINTY:
    def __init__(self, x=0 , y=0):
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})", format(self.x,self.y)
# printing obj
POINTY=POINTYPOINTYPOINTY(2,3)
print(POINTY)