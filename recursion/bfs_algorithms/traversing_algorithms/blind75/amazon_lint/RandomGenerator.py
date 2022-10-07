class RandomGenerator:
    '''The contructor will be passed an integer n. generate is supposed to return a random number between 0 to n, but it is not supposed to return a number that it has already returned. If possiblities are exhauted, return -1 '''
    def __init__(self, n):
        self.n = n
        self.start = 0
        self.arr = list(range(n+1))
        
    def generate(self):
        if self.start > self.n:
            return -1
        
        r = random.randint(self.start, self.n)
        out = self.arr[r]
        
        temp = self.arr[self.start]
        self.arr[self.start] = self.arr[r]
        self.arr[r] = temp
        
        self.start += 1
        
        return out