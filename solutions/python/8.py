class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = 1
        if s and s[0] in ('-', '+'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]
        
        i = num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i+=1
            
        num = min(num*sign, 2**31-1)
        num = max(num, -2**31)

        return num
