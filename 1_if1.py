def main():
   age=int(input('Введите ваш возраст: '))
   if  2 <= age <= 6:
    return 'Детский сад'
   elif 7 <= age <= 18:
    return 'Школа'
   elif 19 <= age <= 23:
    return 'ВУЗ'
   elif 24 <= age <= 65:
    return 'Работа'
if __name__ == "__main__":
    print(main())   