def hourglass_pattern(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "* " * i)
    for i in range(2, n + 1):
        print(" " * (n - i) + "* " * i)
n = 5
print(hourglass_pattern(n))
