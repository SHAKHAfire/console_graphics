from math import sin, cos, tan, pi , sqrt


from settings import height, width, pointer

class Cell:
    def __init__(self, x, y, alive:bool = False):
        self.x = x
        self.y= y
        # graphical xy
        self.gx = x - width[0]
        self.gy = -(y - height[0])
        
        self.alive = alive
        
        self.rules()

    def __str__(self):
        if self.alive:
            return pointer
        
        if not self.gy :
            if not self.gx :
                return '<>'
            return '——'
        if not self.gx :
            return '||'
        return '  '
    
    def rules(self):
        # if self.gy == round(self.gx**2):
        #     self.alive = True
        # if self.gy == round(sin(self.gx * .2 *1)*6):
        #     self.alive = True
        # if self.gy == round(cos(self.gx * .2)*6):
        #     self.alive = True
        # if self.gy == round(sin(self.gx * 0.2)*6) and self.gy == round(cos(self.gx * 0.2)*6) :
        if self.gy == round(sqrt(abs(self.gx *10))):
            self.alive = True
        
        

matrix=[[Cell(x,y) for x in range(sum(width))] for y in range(sum(height))]



def display():
    for line in matrix:
        print(''.join(map(str ,line)))

display()