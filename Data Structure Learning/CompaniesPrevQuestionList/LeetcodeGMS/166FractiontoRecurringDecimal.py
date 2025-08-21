class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"
        
        result = []
        #check for -ive sign
        if (numerator<0) ^ (denominator<0):
            result.append("-")
        
        numerator = abs(numerator)
        denominator = abs(denominator)

        result.append(str(numerator//denominator))
        remainder = numerator % denominator

        if remainder == 0:
            return "".join(result)
        
        result.append(".")
        remainder_map = {}

        while remainder:
            if remainder in remainder_map:
                insert_index = remainder_map[remainder]
                result.insert(insert_index, "(")
                result.append(")")
                break

            remainder_map[remainder] = len(result)
            remainder *= 10
            result.append(str(remainder//denominator))
            remainder %= denominator

        return "".join(result)
    
sol = Solution()
numerator = 4
denominator = 333
print(sol.fractionToDecimal(numerator, denominator))