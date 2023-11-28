def fibonacci(number):
    fib_sequence = [1, 1]
    list_fibonacci = []
    fibonacci = 0
    for i in range(0, number-2):
        fibonacci += i
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

print(fibonacci(10))