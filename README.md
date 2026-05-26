# Perfect_number_finder

Short python script that uses Eukleid-Euler theorem to fond perfect numbers

Using sympy library to find primes (as it´s faster than using own script)

Prime number funciton (without sympy):
```python
import math
def isprime(number):
    a,square = 3, math.isqrt(number)
    if number % 2 == 0:
        return False
    if number == 2:
        return True
    else:
        while a <= square:
            if number%a ==0:
                return False
            a+=2
        return True
        


