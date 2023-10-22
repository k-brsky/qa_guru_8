import pytest

class TestProducts:

    def test_product_check_quantity(self, product):
        # Проверяем, что метод возвращает True по значениям подходящего диапазона
        case_1 = 0
        assert product.check_quantity(case_1) == True
        case_2 = 1
        assert product.check_quantity(case_2) == True
        case_3 = 500
        assert product.check_quantity(case_3) == True
        case_4 = 999
        assert product.check_quantity(case_4) == True
        case_5 = 1000
        assert product.check_quantity(case_5) == True

        # Проверяем, что метод возвращает False по значениям неподходящего диапазона
        case_6 = 1001
        assert product.check_quantity(case_6) == False
        case7 = 1500
        assert product.check_quantity(case7) == False

    def test_product_buy(self, product):
        # Объявляем переменную количества продуктов к покупке
        count_products_to_buy = 500
        # Объявляем переменную изначального количества продуктов
        start_product_quantity = product.quantity
        # Совершаем покупку количества продуктов из переменной count_products_to_buy
        product.buy(count_products_to_buy)
        # Проверяем, что изначальное количество продуктов уменьшилось на количество покупаемых продуктов
        assert product.quantity == (start_product_quantity - count_products_to_buy)

    def test_product_buy_more_than_available(self, product):
        # Объявляем переменную количества продуктов, превышающую наличие
        count_products_to_buy = 1500
        # Проверяем, что при попытке покупки количества продуктов, превышающего наличие, выводится ValueError
        with pytest.raises(ValueError):
            product.buy(count_products_to_buy)

class TestCart:
    def test_add_product(self, cart, product):
        # Вызываем метод добавления продукта в корзину с количеством 1
        cart.add_product(product, 1)
        # Проверяем, что количество продукта в корзине стало 1
        assert cart.products[product] == 1

        # Вызываем метод добавления к существующему продукту 5 таких же элементов
        cart.add_product(product, 5)
        # Проверяем, что количество продуктов в корзине стало 6
        assert cart.products[product] == 6

    def test_remove_product(self, cart, product):
        # Добавляем 6 продуктов в корзину
        cart.add_product(product, 6)
        # Вызываем метод удаления продукта из корзины с удалением 1 элемента
        cart.remove_product(product, 1)
        # Проверяем, что при удалении 1 элемента продукта, в корзине останется 5 элементов продукта
        assert cart.products[product] == 5

        # Добавляем 5 продуктов в корзину
        cart.add_product(product, 5)
        # Вызываем метод удаления продуктов из корзины с количеством элементов к удалению
        # равному количеству элементов в корзине(5 добавили в этой итерации, 5 осталось с предыдущей)
        cart.remove_product(product, 10)
        # Проверяем, что в корзине нет продуктов
        assert product not in cart.products

        # Добавляем 5 продуктов в корзину
        cart.add_product(product, 5)
        # Вызываем метод удаления продуктов из корзины без передачи количества элементов к удалению
        cart.remove_product(product)
        # Проверяем, что в корзине нет продуктов
        assert product not in cart.products

        # Добавляем 5 продуктов в корзину
        cart.add_product(product, 5)
        # Вызываем метод удаления продуктов из корзины с количеством элементов к удалению,
        # превышающем количество элементов в корзине
        cart.remove_product(product, 10)
        # Проверяем, что в корзине нет продуктов
        assert product not in cart.products

    def test_clear(self, cart, product):
        # Добавляем 5 продуктов в корзину
        cart.add_product(product, 5)
        # Вызываем метод очистки корзины
        cart.clear()
        # Проверяем, что корзина пуста
        assert cart.products == {}

    def test_get_total_price(self, cart, product): #нужно ли здесь вообще продукт передавать
        # Добавляем 5 продуктов в корзину
        cart.add_product(product, 5)
        # Вызываем метод подсчета цены в корзине и передаем его результат в переменную
        counted_price = cart.get_total_price()
        # Проверяем, что значение метода подсчета цены в корзине равно цене 5 продуктов
        assert counted_price == (product.price * 5)

    def test_buy(self, cart, product):
        # Объявляем переменную изначального количества продуктов
        start_product_quantity = product.quantity
        # Объявляем переменную с количеством продуктов для покупки
        count_products_to_buy = 200
        # Добавляем в корзину продукты из переменной выше
        cart.add_product(product, count_products_to_buy)
        # Вызываем метод покупки
        cart.buy()
        # Проверяем, что корзина пуста
        assert cart.products == {}
        # Проверяем, что количество продуктов уменьшилось
        assert product.quantity == (start_product_quantity - count_products_to_buy)

        # Объявляем переменную с излишним количеством для покупки
        count_products_to_buy = 1500
        # Добавляем в корзину продукты из переменной выше
        cart.add_product(product, count_products_to_buy)
        #Проверяем на ошибку ValueError
        with pytest.raises(ValueError):
            cart.buy()
