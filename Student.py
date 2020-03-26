# class Member:
#     def __init__(self, new_gender, new_major, new_id):
#         self.__gender = new_gender #__gender就變成私有屬性
#         self.major = new_major
#         self.id = new_id
#
#     def get_gender(self):
#         """回傳private屬性"""
#         return self.__gender
#
#     def set_gender(self, new_gender):
#         if new_gender == 'M' or new_gender == 'F':
#             self.__gender = new_gender
#         else:
#             print('=======請傳入"M"或"F"=======')
#
#     def borrow_resources(self):
#         pass
#
#     def check_auth(self):
#         pass
#
# class Student(Member):
#     def __init__(self,new_gender, new_major,new_id):
#         super().__init__(new_gender,new_major,new_id)
#     def borrow_resources(self):
#         print('student borrow')
#     def join_class(self):
#         pass
#     def quit_class(self):
#         pass
# class Professor(Member):
#     def __init__(self,new_gender, new_major,new_id):
#         super().__init__(new_gender, new_major,new_id)
#
#     def borrow_resources(self):
#         print('professor borrow')
#
# student1 = Student('M','工管系','D0239867')
# student2 = Student('F','數媒系','D0171874')
# professor1 = Professor('F','經濟系','T123456')
# professor2 = Professor('M','財稅系','T296753')
#
# ls =[student1,student2,professor1,professor2]
# for item in ls:
#     item.borrow_resources()
# student1.__gender = 'Dog'  #把性別改成Dog了!
# print(student1.__gender)
# student1.set_gender('Dog')
# student1.__gender = 'Dog'
# print(student1.get_gender())
# student1.join_class() #Python執行會變成 Student.join_class(student1)

class Pokemon:
    def __init__(self,new_name,new_weight,new_height,new_food,new_cp):
        self.__name=new_name
        self.__weight=new_weight
        self.__height=new_height
        self.__food=new_food
        self.__cp=new_cp
    def eat(self):
        print(f'The pokemon is eating {self.__food}.')


import vending_machine.vending_service as m
flag = True #控制迴圈是否繼續執行

while flag:
    print('\n============================')
    select = eval(input('1.儲值\n2.購買\n3.查詢餘額\n4.離開\n請選擇:'))
    if select == 1:
        pass
    elif select ==2:
        pass
    elif select ==3:
        pass
    elif select ==4:
        print('bye')
        flag = 0 #也可以=false
        break

    else:
        print('====請輸入1-4之間====')
        continue
    if select ==1: #儲值
        m.deposit()

    elif select == 2: #購買
        m.buy()

    elif select ==3:
        print(f'目前餘額為{m.balance}元')
