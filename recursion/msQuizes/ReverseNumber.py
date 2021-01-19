number = int(input("Enter a number to reverse"))
reverse_num = 0 
while number > 0:
    remainder = number % 10
    reverse_num = (reverse_num * 10) + remainder
    number = number // 10

print(reverse_num)

