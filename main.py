import math
from matplotlib import pyplot as plt


class Pen():
    def __init__(self,x=0,y=0,a=0,c='#000000',s=1):
        '''
        a:角度 c:颜色 s:粗细
        '''
        self.ax=plt.gca()
        self.ax.set_aspect('equal')
        self.x = x
        self.y = y
        self.a = a
        self.c = c
        self.s = s
        
        
    def moveTo(self,x,y):
        self.x = x
        self.y = y
        return self
    
    def setA(a):
        self.a = a
    def color(self,c:str):
        self.c = c
        return self
        
    def fd(self,n):
        #先搞坐标系，画图难
        rad=math.pi*self.a/180
        newp=[self.x+n*math.cos(rad),self.y+n*math.sin(rad)]
        self.ax.plot([self.x,newp[0]],[self.y,newp[1]],color = self.c, linewidth = self.s)
        self.x=newp[0]
        self.y=newp[1]
        return self
    
    def dfd(self,n):
        rad=math.pi*self.a/180
        newp=[self.x+n*math.cos(rad),self.y+n*math.sin(rad)]
        self.x=newp[0]
        self.y=newp[1]
        return self
    
    
    def size(self,s=1):
        self.s = s
        return self
    
    def rt(self,n):
        self.a+=n 
        return self
    
    def lt(self,n):
        self.a-=n
        return self
    

    def rec(self,w,h,ifSkew:bool = False):
        if ifSkew == False:
            X=[]
            Y=[]
            X.append(self.x+w/2)
            X.append(self.x+w/2)
            X.append(self.x+w/-2)
            X.append(self.x+w/-2)
            X.append(self.x+w/2)
        
            Y.append(self.y+h/2)
            Y.append(self.y+h/-2)
            Y.append(self.y+h/-2)
            Y.append(self.y+h/2)
            Y.append(self.y+h/2)
        
            self.ax.plot(X,Y)
            return self
        
        elif ifSkew == True:
            recordA = self.a
            recordX = self.x
            recordY = self.y
            self.dfd(h/2).lt(90).dfd(w/2).rt(180).fd(w).rt(90).fd(h).rt(90).fd(w).rt(90).fd(h)
            self.a = recordA
            self.x = recordX
            self.y = recordY
            return self
            
    def star(self,n,a,b):
        # n角数 a尖角的1/2 b边长
        for i in range(n):
            self.rt(a).fd(b).rt(180-2*a).fd(b).lt(180-a)
            self.rt(360/n)
        
        return self

