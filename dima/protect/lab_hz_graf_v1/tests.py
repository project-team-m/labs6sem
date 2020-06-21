# Оформление при переписывании смотрите у танюхи (https://cdn.discordapp.com/attachments/544873516726485019/715574646103343175/IMG_20200527_203807.jpg)
def zadanie(p, q):
    N = p * q
    Fi_N = (p - 1) * (q - 1)
    print('N = {}, Fi(N) = {}'.format(N, Fi_N))
    k_v = 13 # Dima (1) Sanya(1)
    K_V = 197 # Dima(641) Sanya(881)
    fam = [12, 16, 15, 16, 15]  # KONON(12, 16, 15, 16, 16) or KOLES(12, 16, 13, 6, 19) копируете свои
    #значения в fam
    new_c = []
    for i in range(5):
        tmp = (fam[i] ** K_V) % N
        new_c.append(tmp)
        print('C{} = {} ** {} mod {} = {}'.format(i, fam[i], K_V, N, tmp))
    print('C = {} \n'.format(new_c))

    for i in range(5):
        tmp = new_c[i] ** k_v % N
        print('M{} = {} ** {} mod {} = {}'.format(i, new_c[i], k_v, N, tmp))
        #Каждый m(i) это буква вашей фамилии всего их 5(которые нам нужны)

def simple(digit):
    for i in range(2, digit):
        if digit % i == 0:
            return False

    return True

def check():
    a = 7
    i = 100
    while True:
        if simple(i) and ((i * a) % 720) == 1:
            print(i)
        i += 1

#check()
zadanie(17, 41)  # по варианту пишете p и q Дима(17, 41) Саня(23, 41)
