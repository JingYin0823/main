class Drink:
    def __init__(self,new_name,new_price):
        self.__name=new_name
        self.__price=new_price

    def get_name(self):
        return self.get___name()
    def set_name(self,new_name):
        self.__name = new_name
    def get_price(self):
        return self.__price

from vending_machine.vending_service import Drink
balance = 0
drinks = [
    Drink('可樂',20),
    Drink('雪碧',20),
    Drink('茶裏王',20),
    Drink('原粹',20),
    Drink('純粹喝',20),
    Drink('水',20),]

def deposit():
    """
    儲值功能
    :return: nothing
    """
    global balance #宣告函式中會用到全域變數balance
    value = eval(input('儲值金額:'))
    while value <1:
            print('====儲值金額需大於零====')
            value = eval(input('儲值金額:'))
    balance +=value #只要這邊改*10 以下有balance都會改到
    print(f'儲值後額於為 {balance}元')
def add(x,y):
    """
    數字相加
    :param x:數字1
    :param y:數字2
    :return:相加結果
    """
    return x,y
def buy():
    global balance,drinks
    print('\n請選擇商品')
    for i in range(0, len(drinks)):
        print(f'({i + 1}) {drinks[i]["name"]} {drinks[i]["price"]}元')
    choose = eval(input('請選擇:'))
    buy_drink = drinks[choose - 1]
    if balance < buy_drink['price']:
        print('====餘額不足====')
    else:
        print(f'已購買{buy_drink["name"]}  {buy_drink["price"]}元')
        balance -= buy_drink['price']
        print(f'購買後餘額為{balance}元')

    while choose < 1 or choose > 6:
        print('====請輸入1-6之間====')
        choose = eval(input('請選擇:'))

        buy_drink = drinks[choose - 1]
        while balance < buy_drink['price']:
            print('====餘額不足，需要儲值嗎?====')
            want_deposit = input('y/n?')
            if want_deposit == 'y':
                deposit()
            elif want_deposit == 'n':
                break
            else:
                print('====請重新輸入====')

        # 儲值後餘額大於商品金額再購買
        if balance < buy_drink['price']:
            print('====餘額不足====')
        else:
            print(f'已購買{buy_drink["name"]}  {buy_drink["price"]}元')
            balance -= buy_drink['price']
            print(f'購買後餘額為{balance}元')

