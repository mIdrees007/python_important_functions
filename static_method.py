class Math:
    
    def __init__(self, num):
        
        self.num = num
    
    def addnum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b

a = Math(5)
print(a.num)

a.addnum(5)

print(a.num)

print(Math.add(12, 34))