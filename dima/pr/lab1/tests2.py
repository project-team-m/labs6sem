class A:
    c = 0
    def __init__(self):
        A.c += 1


a1 = A()
a2 = A()
a3 = A()
a4 = A()
a5 = A()

print(a5.c)