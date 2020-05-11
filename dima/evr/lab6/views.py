from random import randint, choice


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
    def __init__(self, Osob=10, Gen=10, Pcross=0.8, Pmut=0.8, Lim=3, Left=1, Right=100, Nproc=4):
        self.C = [[randint(Left, Right) for i in range(Gen)] for i in range(Osob)]
        self.Pcross = Pcross
        self.Pmut = Pmut
        self.Lim = Lim
        self.Left = Left
        self.Right = Right
        self.Nproc = Nproc

    def crossover_first(self, left, right):
        if randint(0, 100) / 100 <= self.Pcross:
            new_osob = []
            for i in range(len(left)):
                if randint(0, 5) == 0:
                    new_osob.append(right[i])
                elif right[i] > left[i]:
                    new_osob.append(left[i])
                else:
                    new_osob.append(right[i])
            return new_osob

    def crossover_second(self, left, middle, right):
        if randint(0, 100) / 100 <= self.Pcross:
            new_osob = []
            if sum(middle) < sum(right):
                osob = middle
            elif sum(middle) > sum(right):
                osob = right
            else:
                return None

            for i in range(len(left)):
                if randint(0, 3) == 0:
                    new_osob.append(osob[i])
                elif osob[i] > left[i]:
                    new_osob.append(left[i])
                else:
                    new_osob.append(osob[i])
            return new_osob

    def mut(self, obj):
        if randint(0, 100) / 100 <= self.Pmut:
            obj[choice(obj)], obj[obj.index(min(obj))] = obj[obj.index(min(obj))], obj[obj.index(min(obj))]

    def check_end(self, T):
        for i in range(len(self.C)):
            if HDA().main(self.C[i], self.Nproc) != T[i]:
                return False
        else:
            return True

    def default(self):
        new_C = self.C.copy()
        left = choice(new_C)
        del new_C[new_C.index(left)]
        right = choice(new_C)
        cross = self.crossover_first(left, right)
        if cross:
            self.C[self.C.index(left)] = cross

    def modification(self):
        new_C = self.C.copy()
        left = choice(new_C)
        del new_C[new_C.index(left)]
        middle = choice(new_C)
        del new_C[new_C.index(middle)]
        right = choice(new_C)
        cross = self.crossover_first(left, right)
        if cross:
            self.C[self.C.index(left)] = cross

    def tournament(self):
        for left in self.C:
            new_C = self.C.copy()
            del new_C[new_C.index(left)]
            right = choice(new_C)
            cross = self.crossover_first(left, right)
            if cross:
                self.C[self.C.index(left)] = cross

    def main_first(self):
        count = 0
        repeats = 0
        print('Generation quality at the start:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print()
        while repeats < self.Lim:
            count += 1
            T = [HDA().main(i, self.Nproc) for i in self.C]
            self.default()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Standard GA generation:')
        self.output_mass()
        print('Generation quality at the end of standard GA:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print('All generations:', count)
        print()

    def main_second(self):
        count = 0
        repeats = 0
        while repeats < self.Lim:
            count += 1
            T = [HDA().main(i, self.Nproc) for i in self.C]
            self.modification()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Modification GA generation:')
        self.output_mass()
        print('Generation quality at the end modification GA:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print('All generations:', count)
        print()

    def main_tournament(self):
        count = 0
        repeats = 0
        while repeats < self.Lim:
            count += 1
            T = [HDA().main(i, self.Nproc) for i in self.C]
            self.tournament()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Tournament GA generation:')
        self.output_mass()
        print('Generation quality at the end tournament GA:', min([HDA().main(i, self.Nproc) for i in self.C]))
        print('All generations:', count)
        print()



    def output_mass(self, mass=None):
        #print('-'*25)
        if not mass:
            mass = self.C
        for i in range(len(mass)):
            print('Gene vector №{} = '.format(i + 1), mass[i])
        print('-'*25)

if __name__ == '__main__':
    a = GA(Lim=3)
    print('Primary generation:')
    a.output_mass()
    a.main_first()
    a.main_second()
    a.main_tournament()
