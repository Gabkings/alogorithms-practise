# def getSum(n):
     
#     nsum = 0;
#     while (n != 0):
#         nsum = nsum + n % 10;
#         n = n // 10;
#     return nsum

# # print(getSum(99))


# def getDigits(sum):
#     alldigits = []
#     for i in range(100):
#         for j in range(100):
#             result = i + j 
#             if result == (2 * sum):
#                 alldigits.append([i,j] if i != 0 else i > 0)
    
#     return alldigits

# print(getDigits(5))

def getSum(n):
     
    sum1 = 0;
    while (n != 0):
        sum1 = sum1 + n % 10;
        n = n // 10;
     
    return sum1;
 
# Function to find the smallest
# number whose sum of digits is also N
def smallestNumber(N):
 
    i = 1;
    while (1):
        # Checking if number has
        # sum of digits = N
        if (getSum(i) == 2*N):
            print(i);
            break;
         
        i += 1;
     
# Driver code
N = 5;
smallestNumber(N);

