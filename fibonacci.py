x = int(input("Enter up to value : "))
a, b = 0, 1
for i in range(100):
    print(a)
    a, b = b, a + b
    # Output fibonacci only within 100
    if a == x:
        print("{} is a Fibonacci number".format(a))
        break
