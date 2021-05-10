import math
def BracketCombinations(num): 
    def gen_catalan_seq(num): 
        xs = []
        n = 0
        c = 1
        for i in range(0, num + 1):
            xs.append(c)
            n += 1
            c = c * 2 * (2 * n - 1) // (n + 1)
        return xs
    # quiz totally satisfied by Catalan sequence
    return gen_catalan_seq(num)[num]
    # numerator = math.factorial(2*int(num))
    # denominator = math.factorial(num+1)*math.factorial(num)
    # #print numerator, denominator
    # return math.floor(numerator/denominator) 

# keep this function call here 
print(BracketCombinations(int(input("Enter a no: "))))