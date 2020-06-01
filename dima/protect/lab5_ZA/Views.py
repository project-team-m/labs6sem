import math
from random import choice
import time


class File:
    def __init__(self):
        self.path = 'accounts.cvs'

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def read(self):
        with open(self.path) as f:
            return f.read()

    def append(self, login, password, perfect, deviation):
        with open(self.path, 'a') as f:
            f.write('\n{},{},{},{}'.format(login, password, perfect, deviation))

    def get_users(self):
        with open(self.path) as f:
            users = {}
            for i in f:
                user = i.split('\n')[0].split(',')
                users[user[0]] = [user[1], float(user[2]), float(user[3])]

        return users


class Passwords:
    passwords = ['UPJirn', 'PR2d7p', 'f5cv0q', 'CsSP5r', 'CbuK7L', 'kklpeK', 'gdqlo2', 'FEPJhC',
                 'WzOwQk', '9ZenTW', 'Fjjl2s', 'I6aGfN', '8m5LYR', 'JTiSRr', 'wjmJhm', '37FTVt',
                 '6lj3TS', '5kLtEm', 'OoESOo', 'TjhAxl']

    def __write(self):
        with open('passwords', 'w') as f:
            string = ''
            for i in self.passwords:
                string += i + ','
            f.write(string)

    def __read(self):
        with open('passwords') as f:
            self.passwords = []
            for i in f.read().split(',')[:-1]:
                self.passwords.append(i)

    def get_password(self):
        return choice(self.passwords)


class User:
    def __init__(self):
        self.repeats = 4
        self.eps = 2

    def register(self):
        login = input('Enter a login: ')
        new_password = Passwords().get_password()
        run = True
        times = []
        while run:
            run = False
            print('Enter password {} {} times:'.format(new_password, self.repeats))
            for i in range(self.repeats):
                start = time.time()
                password = input('Attempt {}, enter a password: '.format(i + 1))
                times.append(time.time() - start)
                if password != new_password:
                    print('Uncorrected password, try again!')
                    run = True
                    times = []
                    break

        File().append(login,
                      new_password,
                      perfect := sum(times) / len(new_password),
                      sum([abs(perfect - i) for i in times]) / len(new_password))
        print('{}! Registration has successful'.format(login))

    def auth(self):
        users = File().get_users()
        login = input('Enter a login: ')
        if users.get(login):
            start = time.time()
            password = input('Enter a password: ')
            wasted = time.time() - start
            if not password == users.get(login)[0]:
                print('Uncorrected password!')
                return
            else:
                perfect = wasted * 4 / len(password)
                deviation = abs(wasted - users.get(login)[1]) * 4 / len(password)
                if not(abs(users.get(login)[1] - perfect) < self.eps and
                       abs(users.get(login)[2] - deviation) < self.eps):
                    print('Time mistake!')
                else:
                    print('Successful')
        else:
            print('Uncorrected login!')


if __name__ == '__main__':
    u = User()
    while True:
        a = input('1) Register new user.\n'
                  '2) Authorization user.\n'
                  '0) Exit.\n'
                  'Enter a number: ')
        if a == '1':
            u.register()
        elif a == '2':
            u.auth()
        elif a == '0':
            break
