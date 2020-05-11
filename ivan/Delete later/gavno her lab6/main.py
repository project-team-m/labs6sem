from random import randint, choice


class GenAlg:
    def __init__(self, indiv=10, gen=10, Pcross=0.8, Pmut=0.8, lim=30, low=1, top=100, proc=4):
        self.C = [[randint(low, top) for i in range(gen)] for i in range(indiv)]
        self.Pcross = Pcross
        self.Pmut = Pmut
        self.lim = lim
        self.low = low
        self.top = top
        self.proc = proc
        self.tmp = self.C


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

    def main_hda(self, mass, proc):
        return max(self.HDA(list(reversed(sorted(mass))), proc))

    def output_mass(self, mass=None):
        if not mass:
            mass = self.C
        for i in range(len(mass)):
            print('Поколение №{} = '.format(i + 1), mass[i])
        print()

    '''def mutation_old(self, obj):
        if randint(0, 100) / 100 <= self.Pmut:
            obj[choice(obj)], obj[obj.index(min(obj))] = obj[obj.index(min(obj))], obj[obj.index(min(obj))]'''

    def mutation_upd(self, obj):
        if randint(0, 100) / 100 <= self.Pmut:
        	print('Изначальный ген:', obj)
            for i in range(len(obj)):
                if obj[i] - 1 > self.low:
					print('Была мутирована хромосома:', obj[i], 'на: ', end='')
                    obj[i] = randint(self.low, obj[i] - 1)
                    print(obj[i])
                    break
            print('Мутировавший ген:', obj)


    def check_end(self, T):
        for i in range(len(self.C)):
            if self.main_hda(self.C[i], self.proc) != T[i]:
                return False
        else:
            return True

    '''def crossover(self, low, top):
        if randint(0, 100) / 100 <= self.Pcross:
            new_indiv = []
            for i in range(len(low)):
                if randint(0, 5) == 0:
                    new_indiv.append(top[i])
                elif top[i] > low[i]:
                    new_indiv.append(low[i])
                else:
                    new_indiv.append(top[i])
            return new_indiv'''

class standart(GenAlg):
    def standart(self):
        new_C = self.tmp.copy()
        low = choice(new_C)
        del new_C[new_C.index(low)]
        top = choice(new_C)
        self.mutation_upd(choice(self.tmp))
        #cross = self.crossover(low, top)
        #if cross:
            #self.tmp[self.C.index(low)] = cross

    def main(self):
        count = 0
        repeats = 0
        print('Качество поколения на старте:', min([self.main_hda(i, self.proc) for i in self.tmp]))
        print()
        while repeats < self.lim:
            count += 1
            T = [self.main_hda(i, self.proc) for i in self.tmp]
            self.standart()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Стандартные ГА поколения:')
        self.output_mass()
        print('Качество поколения в конце стандарта Га:', min([self.main_hda(i, self.proc) for i in self.tmp]))
        print('Всего поколений:', count)
        print()

class modif(GenAlg):
    def modification(self):
        new_C = self.tmp.copy()
        low = choice(new_C)
        del new_C[new_C.index(low)]
        middle = choice(new_C)
        del new_C[new_C.index(middle)]
        top = choice(new_C)
        #cross = self.crossover(low, top)
        #if cross:
            #self.tmp[self.tmp.index(low)] = cross

    def main(self):
        count = 0
        repeats = 0
        while repeats < self.lim:
            count += 1
            T = [self.main_hda(i, self.proc) for i in self.tmp]
            self.modification()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Модификация ГА поколения:')
        self.output_mass()
        print('Качество генерации в конце модификации ГА:', min([self.main_hda(i, self.proc) for i in self.tmp]))
        print('Всего поколений:', count)
        print()

class tour(GenAlg):
    def tournament(self):
        for low in self.tmp:
            new_C = self.tmp.copy()
            del new_C[new_C.index(low)]
            top = choice(new_C)
            #cross = self.crossover(low, top)
            #if cross:
                #self.tmp[self.tmp.index(low)] = cross

    def main(self):
        count = 0
        repeats = 0
        while repeats < self.lim:
            count += 1
            T = [self.main_hda(i, self.proc) for i in self.tmp]
            self.tournament()
            if self.check_end(T):
                repeats += 1
            else:
                repeats = 0
        print('Турнирный ГА поколения:')
        self.output_mass()
        print('Качество поколения в конце турнира ГА:', min([self.main_hda(i, self.proc) for i in self.tmp]))
        print('Всего поколений:', count)
        print()

if __name__ == '__main__':
    ga = GenAlg(lim=30)
    df = standart()
    md = modif()
    tr = tour()
    print('Количество особей 10\nКоличество генов 10\nВероятность кроссовера 0.8\nВероятность мутации 0.8\nПредел повторений 3\n')
    print('Первичное поколение:')
    ga.output_mass()
    df.main()
    md.main()
    tr.main()
