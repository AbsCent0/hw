"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta
def print_days():
    dt_today = date.today()
    dt_yes = dt_today - timedelta(1)
    dt_30 = dt_today - timedelta(30)
    print(dt_yes)
    print(dt_today)
    print(dt_30)



def str_2_datetime(date_string):
    date_string = '01/01/20 12:10:03.234567'
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
     print_days()
     print(str_2_datetime("01/01/20 12:10:03.234567"))