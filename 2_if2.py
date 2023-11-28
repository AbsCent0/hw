def main():
    one = input('Введите 1 строку: ')
    two = input('Введите 2 строку: ')
    if (type(one)) is str and (type(two)) is str:
      if one == two:
       return '1'
    if len(one)>len(two):
       return '2'
    if two == 'learn':
       return '3'
if __name__ == "__main__":
    print(main())
