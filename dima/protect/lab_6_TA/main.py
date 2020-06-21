test_table = ['e', 'a', 'b']
symph_empty = 'Ǿ'

'''
View.out_table(['e', 'a', 'b'], [['q0', [['q0', 'q2'], ['q0', 'q1', 'q2'], ['q0', 'q1', 'q2']]],
                                     ['q1', [['q0', 'q2'], ['q0', 'q1', 'q2'], None]],
                                     ['q2', [None, 'q2', ['q0', 'q1', 'q2']]]])
'''

'''def take_way(self, vertex, string, repeats: list):
    if (vertexes := vertex.binds) and vertex not in repeats:
        repeats.append(vertex)
        for i in vertexes:
            string.append([i])
            if i[1].binds:
                for j in i[1].binds:
                    self.take_way(j[1], string[-1], repeats)
        return string
    else:
        return string'''


class Vertex:
    num = -1

    def __init__(self):
        self.binds = []
        self.back_binds = []
        self.number = Vertex.num
        Vertex.num += 1

    def back_bind(self, atr, obj):
        self.back_binds.append([str(atr).lower(), obj])

    def bind(self, atr, obj):
        self.binds.append([str(atr).lower(), obj])
        obj.back_bind(atr, self)

    def instance_vertex(self, arg='e'):
        vertexes = []
        for i in self.binds:
            if i[0] == arg:
                vertexes.append(i[1])

        if vertexes:
            return vertexes
        else:
            return None

    def back_vertex(self):
        for i in self.back_binds:
            yield i

    def to_null(self):
        Vertex.num = -1

    def __str__(self):
        return 'q{}'.format(self.number)


class Graph:
    def __init__(self):
        self.vertexes = [Vertex() for i in range(9)]
        self.vertexes[0].bind('e', self.vertexes[1])
        self.vertexes[1].bind('a', self.vertexes[2])
        self.vertexes[1].bind('b', self.vertexes[5])
        self.vertexes[2].bind('b', self.vertexes[3])
        self.vertexes[2].bind('a', self.vertexes[6])
        self.vertexes[3].bind('b', self.vertexes[3])
        self.vertexes[3].bind('a', self.vertexes[7])
        self.vertexes[4].bind('a', self.vertexes[4])
        self.vertexes[4].bind('b', self.vertexes[7])
        self.vertexes[5].bind('a', self.vertexes[2])
        self.vertexes[5].bind('b', self.vertexes[1])
        self.vertexes[6].bind('a', self.vertexes[7])
        self.vertexes[6].bind('b', self.vertexes[3])
        self.vertexes[7].bind('a', self.vertexes[4])
        self.vertexes[7].bind('b', self.vertexes[7])
        self.vertexes[7].bind('e', self.vertexes[8])

        self.alphabet = ['a', 'b']
        self.all_alphabet = ['e'] + self.alphabet

    def instance_vertex(self, arg, vertex):
        return self.vertexes[vertex].instance_vertex(arg)

    def plus(self, left, right, arg):
        return left.binds

    def del_vertex(self, vertex):
        for i in vertex.binds:
            old = list(vertex.back_vertex())
            for j in old:
                j.bind('{}*{}'.format(j.binds[0],
                                      i.binds[0]),
                       i.binds[1])
                del j.binds[j.binds.index(j)]
                del j.binds[j.binds.index(j)]
                # остановился тут, проблема с back_vertexes, необходима обновляемость


    def output(self):
        mass = []
        for i in self.vertexes:
            mass.append([str(i), []])
            for j in self.all_alphabet:
                mass[-1][-1].append(i.instance_vertex(j))

        View.out_table(self.all_alphabet, mass)


class View:
    @staticmethod
    def td(string, length):
        if string[0]:
            if isinstance(string[0], list):
                if len(string[0]) == 1:
                    centre = str(string[0][0])
                else:
                    centre = str(string[0])
            else:
                centre = str(string[0])
        else:
            centre = symph_empty
        if len(string) > 1:
            for i in string[1:]:
                if i:
                    centre += ' ' + str(i)
                else:
                    centre += ' ' + symph_empty
        return '{}{}{}  '.format(' ' * (length // 2 - len(centre) // 2),
                                 centre,
                                 ' ' * (length // 2 - len(centre) // 2))[:length]

    @staticmethod
    def tr(args, first, second, left_column=' '):
        string = View.td([left_column], first)
        for i in args:
            if isinstance(i, str) or isinstance(i, int) or i is None:
                col = [i]
            else:
                col = i

            string += View.td(col, second)
        return string

    @staticmethod
    def out_table(titles, params):
        first = 4
        second = 20
        print(View.tr(titles, first, second))

        for i in params:
            print(View.tr(i[1], first, second, i[0]))

if __name__ == '__main__':
    a = Graph()
    a.output()
    a.del_vertex(a.vertexes[7])
    a.output()
