from DAO_Models import Client, Processor, Basket, Order
from config import DATABASE
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine, update

from datetime import datetime

from models import lacksError

'''
Пользователь видит список процессоров +++
Пользователь может посмотреть список товаров в корзине +++
Пользователь может добавить в корзину товар, увеличить его количество в корзине, удалить из корзины +++
При нажатии кнопки оплатить идет проверка на количество денег, если денег хватает, 
то идет проверка на наличие на складе +++
если хватает денег и хватает товаров на складе
то товар спиывается со склада, у пользователя списываются деньги за товар, в поле дата заказа появляется NOW()
'''
'''
Менеджер может менять хар-ки товаров и добавлять | удалять товары
Кладовщик может изменять кол-во товаров на складе
'''


class ClientService:
    engine = create_engine(URL(**DATABASE), echo=False)
    session = sessionmaker(bind=engine)
    session = session()

    def show_processors(self):
        return [processor for processor in self.session.query(Processor)]

    def get_proc_from_basket(self, id_client):
        return [[processor.id, processor.name, processor.price, basket.quantity] for processor,
                                                                                     basket in
                self.session.query(Processor, Basket). \
                    filter(Basket.id_processor == Processor.id, Basket.id_client == id_client)]

    # Возвращает json всех объектов к орзине
    def show_basket(self, id_client):
        response = []
        for i in self.get_proc_from_basket(id_client):
            response.append('''Processor: {
    id: %s,
    name: %s,
    price: %s,
    quantity: %s
}''' % (i[0], i[1], i[2], i[3]))
        return response

    def check_in_the_clients(self, id_client):
        if not self.session.query(Client).filter(Client.id == id_client).first():
            raise lacksError("Client does not exists")

    def check_in_the_processors(self, id_processor):
        if not self.session.query(Processor).filter(Processor.id == id_processor).first():
            raise lacksError("Processor does not exists")

    def add_to_basket(self, id_processor, id_client):
        self.check_in_the_processors(id_processor)
        self.check_in_the_clients(id_client)
        proc_from_basket = self.session.query(Basket, Order).filter(Basket.id_order == Order.id,
                                                               Basket.id_client == id_client,
                                                               Basket.id_processor == id_processor,
                                                               Order.date_order == None).all()
        if proc_from_basket:
            proc_from_basket[0][0].quantity += 1
            self.session.commit()
        else:
            response = self.session.query(Basket, Order).filter(Basket.id_order == Order.id,
                                                           Basket.id_client == id_client,
                                                           Order.date_order == None).all()
            if response:
                field = Basket(id_processor, 1, id_client, response[0][1].id)
                self.session.add(field)
                self.session.commit()
            else:
                order = Order()
                self.session.add(order)
                self.session.commit()
                field = Basket(id_processor, 1, id_client, self.session.query(Order).all()[-1].id)
                self.session.add(field)
                self.session.commit()

    def remove_from_basket(self, id_processor, id_client):
        self.check_in_the_processors(id_processor)
        self.check_in_the_clients(id_client)
        proc_from_basket = self.session.query(Basket, Order).filter(Basket.id_order == Order.id,
                                                               Basket.id_client == id_client,
                                                               Basket.id_processor == id_processor,
                                                               Order.date_order == None).all()
        if proc_from_basket:
            if proc_from_basket[0][0].quantity > 1:
                proc_from_basket[0][0].quantity -= 1
                self.session.commit()
            elif proc_from_basket[0][0].quantity == 1:
                self.session.delete(proc_from_basket[0][0])
                self.session.commit()

    def enough_balance(self, id_client):
        response = self.session.query(Client, Basket, Order, Processor).filter(
            Client.id == Basket.id_client,
            Basket.id_order == Order.id,
            Basket.id_processor == Processor.id,
            Basket.id_client == id_client,
            Order.date_order == None
        ).all()
        if response:
            all_price = 0
            for i in response:
                all_price += i[1].quantity * i[3].price

            if all_price > response[0][0].balance:
                raise lacksError('insufficient funds')
            else:
                return all_price
        else:
            raise lacksError('Order is not exists')

    def check_enough_on_stocks(self, id_client):
        response = self.session.query(Client, Basket, Order, Processor).filter(
            Client.id == Basket.id_client,
            Basket.id_order == Order.id,
            Basket.id_processor == Processor.id,
            Basket.id_client == id_client,
            Order.date_order == None
        ).all()
        for i in response:
            if i[1].quantity > i[3].balance:
                raise lacksError('Insufficient processors in stocks')

    def end_order(self, id_client):
        response = self.session.query(Client, Basket, Order, Processor).filter(
            Client.id == Basket.id_client,
            Basket.id_order == Order.id,
            Basket.id_processor == Processor.id,
            Basket.id_client == id_client,
            Order.date_order == None
        ).first()
        response[2].date_order = datetime.now()
        self.session.commit()

    def pay(self, id_client, price):
        client = self.session.query(Client).filter(Client.id == id_client).first()
        client.balance -= price
        self.session.commit()

    def write_off_processors(self, id_client):
        response = self.session.query(Client, Basket, Order, Processor).filter(
            Client.id == Basket.id_client,
            Basket.id_order == Order.id,
            Basket.id_processor == Processor.id,
            Basket.id_client == id_client,
            Order.date_order == None
        ).all()
        for i in response:
            i[3].balance -= i[1].quantity

        self.session.commit()

    def buy(self, id_client):
        all_price = self.enough_balance(id_client)
        self.check_enough_on_stocks(id_client)
        self.pay(id_client, all_price)
        self.write_off_processors(id_client)
        self.end_order(id_client)


class StorekeeperService:
    engine = create_engine(URL(**DATABASE), echo=False)
    session = sessionmaker(bind=engine)
    session = session()

    def get_processor(self, id_processor):
        proc = self.session.query(Processor).filter(Processor.id == id_processor).first()
        if not proc:
            raise lacksError("Processor does not exists")
        else:
            return proc

    def change_balance(self, id_processor, new_balance):
        processor = self.get_processor(id_processor)
        processor.balance = new_balance
        self.session.commit()


class ManagerService:
    engine = create_engine(URL(**DATABASE), echo=False)
    session = sessionmaker(bind=engine)
    session = session()

    def get_processor(self, id_processor):
        proc = self.session.query(Processor).filter(Processor.id == id_processor).first()
        if not proc:
            raise lacksError("Processor does not exists")
        else:
            return proc

    def insert_new_processor(self, **kwargs):
        a = Processor(**kwargs)
        self.session.add(a)
        self.session.commit()

    def remove_processor(self, id_processor):
        self.session.delete(self.get_processor(id_processor))
        self.session.commit()

    def update_characteristics(self, id_processor, **kwargs):
        a = self.get_processor(id_processor)
        a.update_characteristics(**kwargs)
        self.session.commit()


if __name__ == '__main__':
    a = ClientService()
    b = ManagerService()
    print(a.show_processors())
    print(b.get_processor(2))

    '''ManagerService().insert_new_processor(name = 'AMD Ryzen 9 3900X TRAY',
                                          price = 454,
                                          clock = 4600,
                                          cores = 12,
                                          threads = 24,
                                          l3_cache = 64,
                                          process_t = 12)'''

    '''ManagerService().update_characteristics(id_processor=9,
                                          name='AMD Ryzen 9 39asd00X TRAY',
                                          price=44,
                                          clock=460,
                                          cores=122)'''
