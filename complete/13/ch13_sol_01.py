class Square:
    def __init__(self, height,length):
        self.height = height
        self.length = length
    
    def area(self):
        return self.height * self.length
    
    def round(self):
        return (self.height + self.length) * 2



