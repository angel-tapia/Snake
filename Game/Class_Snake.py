screenSize = 500
class Snake:
    def __init__ (self):
        self.size=10
        self.speed=10
        #body[i][0]=x and body[i][1]=y
        self.body=[(screenSize/2,screenSize/2),(screenSize/2,screenSize/2+self.size)]
        self.direction = "Left"
    def move(self, food):
        mov =[(-self.speed,0),(self.speed,0),(0,-self.speed),(0,self.speed) ]
        directions = ["Left","Right","Up","Down"]
        idx=directions.index(self.direction)
        newhead=(self.body[0][0]+mov[idx][0],self.body[0][1]+mov[idx][1])
        self.body.insert(0,newhead)
        if newhead == food.pos:
            return True
        self.body.pop()
        return False

    def valid(self):
        x=self.body[0][0]
        y=self.body[0][1]
        if x < 0 or x > screenSize-self.size or y < 0 or y > screenSize-self.size:
            return False
        head=self.body[0]
        if self.body.count(head) > 1:
            return False
        return True

    def newdirection(self, direction):
        directions = ["Left","Up","Right","Down"]
        indexDir=directions.index(self.direction)
        indexNewDir=directions.index(direction)
        if (indexDir+2)%4 is not indexNewDir:
            self.direction=direction

class Food:
    def __init__ (self):
        self.size=10
        self.pos=(30,30)
