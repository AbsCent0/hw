"""

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
   while True:
     dela = input('Как дела? ')
     if dela == 'Хорошо':
        print('Круто!')
        break
     else:
        print('Еще раз')   
if __name__ == "__main__":
    hello_user()