# check divisibility by Digit Sum and Product

class solution:
    def checkDivibility(self, n: int) -> bool:
        # N = 99 
        # bool true if  (9+9)
        
        total = 0
        multiply = 1
        while n> 0:
            digit = n % 10
            total += digit
            multiply *= digit
            n//=10
        print(23%11)
        
        return n%(total+multiply)==0
        
sol = solution()
n = 23
print(sol.checkDivibility(n))