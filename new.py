def fibo(n):
    a = 0
    b = 1
    if n == 0:
        print("provide valid input")
    elif n== 1:
        print(a)

    else:
        print(a,b, end=" ")
        for i in range(n-2):
            c = a + b
            a = b
            b = c
            print(b,end=" ")
fibo(10)
