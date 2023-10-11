import collections


class Teque():
    def __init__(self):
     self.de=collections.deque([])
     #print("deque: ", self.de)
    def push_back(self,x):
       self.de.append(x)
    def push_front(self,x):
       self.de.appendleft(x)
    def push_middle(self,x):
       if(len(self.de)%2!=0):
        indeksMiddel=round(((len(self.de)+1)/2))
       else:
         indeksMiddel=round(((len(self.de))/2))
       self.de.insert(indeksMiddel,x)
      
    def get(self,x):
      return self.de[x]


 


    