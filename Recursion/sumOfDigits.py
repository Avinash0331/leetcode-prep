def sumOfDigits(n):
        # code here
        if n ==0:
            return 0
        d = n%10
        n = n//10
        ans = sumOfDigits(n)
        return ans + d

print(sumOfDigits(123))