"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
products = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},]
def main():
    total = 0
    total_average = []
    for phone in products:
       name = phone['product']
       sold = 0
       for phone_sold in phone['items_sold']:
           sold += phone_sold
           total += phone_sold
       average = round(sold/len(phone['items_sold']), 2)
       total_average.append(average)
       print(f'model: {name}, items_sold: {sold}, average: {average}')
    print(total)
    end_average = sum(total_average)/len(total_average)
    print(end_average)
if __name__ == "__main__":
    main()    