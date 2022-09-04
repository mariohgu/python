import time

class FiboIter:
    
    def __init__(self,max:int=None):
        self.max=max

    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.c = 0
        return self
    
    def __next__(self):
        
        if not self.max or self.n2+self.n1 <= self.max:
            if self.c == 0:
                self.c += 1
                return self.n1
            elif self.c == 1:
                self.c += 1
                return self.n2
            else:
                self.c += 1
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                return self.aux
        else:
            raise StopIteration
            

if __name__ == "__main__":
    fibonacci = FiboIter(1)
    for elem in fibonacci:
        print (elem)
        time.sleep(1)
