from random import randint, choice


'''
все особи переносятся в след поколение
каждой из особей находится пара
в эти парах проходят кроссоверы
    у первой особи будут 0-4 гены первой особи и далее второй
    у второй наоборот
в мутации меняется 2 бита
'''


class HDA:
    def krit(self, mass, n):
        p = [[] for i in range(n)]

        for i in mass:
            sums = list(map(sum, p))
            p[sums.index(min(sums))].append(i)

        return p

    def HDA(self, mass, proc):
        Pa, Pb = self.krit(mass, 2)
        Pa = self.krit(Pa, proc // 2)
        Pb = self.krit(Pb, proc // 2)
        P = Pa + Pb
        sums = list(map(sum, P))
        return sums

    def main(self, mass, proc):
        return max(self.HDA(list(reversed(sorted(mass))), proc))


class GA:
    def __init__(self, Osob=10, Gen=10, Pcross=0.8, Pmut=0.2, Lim=3, Left=1, Right=100, Nproc=4):
        self.C = [[randint(Left, Right) for i in range(Gen)] for i in range(Osob)]
        self.Pcross = Pcross
        self.Pmut = Pmut
        self.Lim = Lim
        self.Left = Left
        self.Right = Right
        self.Nproc = Nproc

    def crossover(self, left, right):
        if randint(0, 100) / 100 <= self.Pcross:
            new_left = []
            new_right = []
            for i in range(5):
                new_left.append(left[i])
                new_right.append(right[i])

            for i in range(5, 10):
                new_left.append(right[i])
                new_right.append(left[i])

            return new_left, new_right

    def mut(self, mass):
        for i in mass:
            if randint(0, 100) / 100 <= self.Pmut:
                a = i.copy()
                first = choice(a)
                del a[a.index(first)]
                second = choice(a)
                i[i.index(first)] = randint(self.Left, first)
                i[i.index(second)] = randint(self.Left, second)

    def check_end(self, T):
        for i in range(len(self.C)):
            if HDA().main(self.C[i], self.Nproc) != T[i]:
                return False
        else:
            return True

    def create_new_couples(self):
        new_C = self.C.copy()
        new_couples = []
        for i in range(5):
            first = choice(new_C)
            del new_C[new_C.index(first)]
            second = choice(new_C)
            del new_C[new_C.index(second)]
            new_couples.append([first, second])

        return new_couples

    def find_top_individuals(self, T):
        tmp_T = {}
        for i in range(len(T)):
            tmp_T[T[i]] = i

        rating = [tmp_T[min(tmp_T)]]
        del tmp_T[min(tmp_T)]

        while tmp_T:
            rating.append(tmp_T[min(tmp_T)])
            del tmp_T[min(tmp_T)]

        return rating[:10]


    def default(self):
        new_couples = self.create_new_couples()

        new_C = self.C.copy()

        self.mut(new_C)

        for i in new_couples:
            new_couple = self.crossover(*i)
            if new_couple:
                new_C.append(new_couple[0])
                new_C.append(new_couple[1])

        print('All genes at the generation')
        self.output_mass(new_C)

        T = [HDA().main(i, self.Nproc) for i in new_C]

        rating = self.find_top_individuals(T)

        for i in range(len(rating)):
            self.C[i] = new_C[rating[i]]


    def main(self):
        count = 0
        repeats = 0
        print('Generation quality at the start:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print()
        while repeats < self.Lim:
            count += 1
            T = [HDA().main(i, self.Nproc) for i in self.C]
            self.default()
            print('Top 10 genes at the generation: ')
            self.output_mass()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        self.output_mass()
        print('Generation quality at the end of GA:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print('All generations:', count)
        print()



    def output_mass(self, mass=None):
        #print('-'*25)
        if not mass:
            mass = self.C
        for i in range(len(mass)):
            print('Gene vector №{} = '.format(i + 1), mass[i])
        print('-'*25)

def test():
    a = GA(Lim=3)
    a.C = [[59, 58, 87, 18, 28, 73, 69, 68, 73, 78],
           [43, 42, 51, 53, 88, 65, 38, 74, 84, 89],
           [70, 59, 55, 58, 93, 80, 36, 83, 5, 86],
           [98, 98, 46, 58, 46, 6, 12, 29, 78, 87],
           [74, 42, 27, 22, 50, 55, 53, 71, 54, 27],
           [6, 27, 27, 98, 24, 54, 15, 100, 34, 29],
           [26, 84, 79, 13, 72, 4, 60, 31, 13, 65],
           [78, 47, 49, 63, 60, 45, 58, 60, 49, 18],
           [72, 53, 18, 2, 87, 9, 50, 32, 60, 33],
           [8, 62, 97, 4, 66, 69, 69, 77, 67, 56]]
    a.output_mass()
    a.default()

def main():
    a = GA(Lim=3)
    print('Primary generation:')
    a.output_mass()
    a.main()


if __name__ == '__main__':
    main()

    #test()
