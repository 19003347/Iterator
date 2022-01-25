class power:
    def __init__(self,max=0):
        self.max  = max

    def iterate(self):
        self.n=0

    def next(self):

        if(self.n<=self.max):
            result=self.n**2
            self.n+=1
            return result
        else:
            raise StopIteration


s=power(5)
s.iterate()
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())
print(s.next())

