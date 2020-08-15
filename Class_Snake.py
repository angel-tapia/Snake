screenSize = 500
class Snake:
    def __init__ (self):
        self.size=10
        self.speed=10
        #body[i][0]=x and body[i][1]=y
        self.body=[(screenSize/2,screenSize/2),(screenSize/2,screenSize/2+self.size)]
        self.direction = "Left"
    def move(self,food):
        if self.direction is "Left":
            newhead=(self.body[0][0]-self.speed,self.body[0][1])
        if self.direction is "Right":
            newhead=(self.body[0][0]+self.speed,self.body[0][1])
        if self.direction is "Up":
            newhead=(self.body[0][0],self.body[0][1]-self.speed)
        if self.direction is "Down":
            newhead=(self.body[0][0],self.body[0][1]+self.speed)
        self.body.insert(0,newhead)
        if newhead == food.pos:
            return True
        self.body.pop()
        return False
    def valid(self):
        x=self.body[0][0]
        y=self.body[0][1]
        if x < 0 :
            return False
        if x > screenSize-self.size:
            return False
        if y < 0 :
            return False
        if y > screenSize-self.size:
            return False
        head=self.body[0]
        if self.body.count(head) > 1:
            return False
        return True
    def newdirection(self,direction):
        directions = ["Left","Up","Right","Down"]
        indexdir=directions.index(self.direction)
        indexnewdir=directions.index(direction)
        if (indexdir+2)%4 is not indexnewdir:
            self.direction=direction
class Food:
    def __init__ (self):
        self.size=10
        self.pos=(30,30)