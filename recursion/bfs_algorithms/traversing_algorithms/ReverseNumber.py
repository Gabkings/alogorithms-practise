class Solution:
    def reverse(self, x: int) -> int:
        result , x_rem = 0 , abs(x)
        
        sign_multiplier = 1
        if x < 0:
           sign_multiplier = -1 
        min_int_32 = 2**31
        while x_rem:
            result = result * 10 + x_rem % 10
            if result * sign_multiplier <= -min_int_32 or result * sign_multiplier >= min_int_32-1:
                return 0
            x_rem //= 10
        return -result if x < 0 else result