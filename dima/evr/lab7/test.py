Xm = 78
Cm = 1.49
def f1(x):
    return 1.13 / (0.13 * (x / Xm) * (x / Xm) + 1) * Cm

def f2(x):
    return (x / Xm) / (3.58 * (x / Xm) * (x / Xm) - 35.2 * (x / Xm) + 120) * Cm

for i in range(1,30):
    x = i * 50
    c = x / Xm
    print(x, end=' = ')
    if c <= 8:
        print(f1(x))
    else:
        print(f2(x))

