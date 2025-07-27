class Solution:
    def calculate(self, s: str) -> int:
        # basic calculator will perform the basic calculation such as +, -, /, *
        #consider stack wise operation? or BOADMAS? 
        # Database that can be used is stack 
        # we need to consider brackets.
        # input is string? 

        stack =[]
        num = 0 
        sign = 1 # 1 is for positive and -1 for negative. 
        
