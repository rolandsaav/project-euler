#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def fibonacci(x):
    # calculates fibonacci numbers up to x
    left, right = 0, 1
    even = 0
    while right <= x:
        tmp = left + right
        left = right
        right = tmp

        if right % 2 == 0:
            even += right

    return even

print(
    fibonacci(4000000)
)
