'''
класс граф
внутри обекты
у объекта есть связь, ведущая в другой объект, с наименованием единицы, черезкоторую идём
'''

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
    num = 0
    lvl = 0

    def __init__(self):
        self.binds = []
        self.number = Vertex.num
        Vertex.num += 1

    def bind(self, atr, obj):
        self.binds.append([str(atr).lower(), obj])

    def instance_vertex(self, arg='e'):
        vertexes = []
        for i in self.binds:
            if i[0] == arg:
                vertexes.append(i[1])

        if vertexes:
            return vertexes
        else:
            return None

    def zeroing(self):
        Vertex.num = 0
        Vertex.lvl += 1

    def __str__(self):
        if Vertex.lvl == 0:
            return 'q{}'.format(self.number)
        elif Vertex.lvl == 1:
            return 'S{}'.format(self.number)
        elif Vertex.lvl == 2:
            return 'P{}'.format(self.number)


class Graph:
    def __init__(self):
        self.vertexes = [Vertex() for i in range(3)]
        self.vertexes[0].bind('e', self.vertexes[1])
        self.vertexes[0].bind('b', self.vertexes[1])
        self.vertexes[0].bind('e', self.vertexes[2])
        self.vertexes[1].bind('a', self.vertexes[0])
        self.vertexes[2].bind('a', self.vertexes[1])

        self.alphabet = ['a', 'b']

    def instance_vertex(self, arg, vertex):
        return self.vertexes[vertex].instance_vertex(arg)

    def equally(self, left, right):
        count = 0
        for i in range(len(left)):
            for j in range(len(right)):
                if left[i] == right[j]:
                    count += 1

        if count == len(left):
            return True

    def show_first_table(self):
        mass = []
        alphabet = ['e'] + self.alphabet
        for i in self.vertexes:
            params = []
            mass.append([str(i), params])
            for j in alphabet:
                if vertexes := i.instance_vertex(j):
                    result = []
                    for k in vertexes:
                        result.append(str(k))
                    params.append(result)
                else:
                    params.append(None)

        print('Start graph:')
        View.out_table(alphabet, mass)

    def crt_s_vertexes(self):
        s = []
        for i in self.vertexes:
            if i.instance_vertex('e'):
                s.append([i] + i.instance_vertex('e'))
            else:
                s.append([i])

        # костыль, передаётся чтобы вывести в таблице
        self.save_s = [[str(j) for j in i] for i in s]

        new_graph = [[[], []] for i in range(len(s))]

        for i in range(len(s)):
            for j in range(len(s[i])):
                for letter in range(len(self.alphabet)):
                    if vertexes := s[i][j].instance_vertex(self.alphabet[letter]):
                        for vertex in vertexes:
                            if vertex not in new_graph[i][letter]:
                                new_graph[i][letter].append(vertex)
                        for nested in vertexes:
                            if vertexes_nested := nested.instance_vertex('e'):
                                for vertex in vertexes_nested:
                                    if vertex not in new_graph[i][letter]:
                                        new_graph[i][letter].append(vertex)
                    elif vertexes := s[i][j].instance_vertex('e'):
                        for nested in vertexes:
                            if vertexes_nested := nested.instance_vertex(self.alphabet[letter]):
                                for vertex in vertexes_nested:
                                    if vertex not in new_graph[i][letter]:
                                        new_graph[i][letter].append(vertex)

        self.vertexes[0].zeroing()
        new_vertexes = [Vertex() for i in range(len(new_graph))]
        for i in range(len(new_graph)):
            for letter in range(len(self.alphabet)):
                for new_vertex in range(len(s)):
                    if self.equally(s[new_vertex], new_graph[i][letter]):
                        new_vertexes[i].bind(self.alphabet[letter], new_vertexes[new_vertex])
        self.vertexes = new_vertexes

    def show_second_table(self):
        mass = []
        alphabet = self.alphabet
        for i in range(len(self.vertexes)):
            params = []
            string = ''
            for s in self.save_s[i]:
                string += ' ' + s
            mass.append([str(self.vertexes[i]) + ' =' + string, params])
            for j in alphabet:
                if vertexes := self.vertexes[i].instance_vertex(j):
                    result = []
                    for k in vertexes:
                        result.append(str(k))
                    params.append(result)
                else:
                    params.append(None)

        print('S graph:')
        View.out_table(alphabet, mass)

    def crt_p_vertexes(self):
        p = [[self.vertexes[0]]]
        new_graph = [[[], []]]

        run = True
        i = 0
        while run:
            for j in range(len(p[i])):
                for letter in range(len(self.alphabet)):
                    if vertexes := p[i][j].instance_vertex(self.alphabet[letter]):
                        for potential_vertex in vertexes:
                            if potential_vertex not in new_graph[i][letter]:
                                new_graph[i][letter].append(potential_vertex)

            for j in new_graph:
                for letter in range(len(self.alphabet)):
                    if not j[letter] in p and j[letter]:
                        p.append(j[letter])
                        new_graph.append([[], []])

            if i + 1 == len(p):
                run = False
            else:
                i += 1

        self.save_p = [[str(j) for j in i] for i in p]

        self.vertexes[0].zeroing()
        new_vertexes = [Vertex() for i in range(len(p))]

        for i in range(len(new_graph)):
            for j in range(len(p)):
                for letter in range(len(self.alphabet)):
                    if new_graph[i][letter] == p[j]:
                        new_vertexes[i].bind(self.alphabet[letter], new_vertexes[j])

        self.vertexes = new_vertexes

    def show_third_table(self):
        mass = []
        alphabet = self.alphabet
        for i in range(len(self.vertexes)):
            params = []
            string = ''
            for s in self.save_p[i]:
                string += ' ' + s
            mass.append([str(self.vertexes[i]) + ' =' + string, params])
            for j in alphabet:
                if vertexes := self.vertexes[i].instance_vertex(j):
                    result = []
                    for k in vertexes:
                        result.append(str(k))
                    params.append(result)
                else:
                    params.append(None)

        print('P graph:')
        View.out_table(alphabet, mass)




    def main(self):
        self.show_first_table()
        self.crt_s_vertexes()
        self.show_second_table()
        self.crt_p_vertexes()
        self.show_third_table()


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
        first = 18
        second = 10
        print(View.tr(titles, first, second))

        for i in params:
            print(View.tr(i[1], first, second, i[0]))


if __name__ == '__main__':
    graph = Graph()
    graph.main()


