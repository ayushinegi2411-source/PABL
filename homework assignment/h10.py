#Given an integer n, find its factorial. Return a list of integers denoting the digits 
#that make up the factorial of n. 

def factorial(n):
    result = [1] 
    for x in range(2, n + 1):
        carry = 0

        for i in range(len(result)):
            product = result[i] * x + carry
            result[i] = product % 10
            carry = product // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

    return result[::-1]

n = 5
print(factorial(n))