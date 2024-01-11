def mag():

    korz = []
    sp_zak = []

    while True:
        print('1-Добавить товар')
        print('2-Посмотреть корзину')
        print('3-Удалить товар')
        print('4-Оформить заказ')
        print('5-Просмотр заказов')
        print('6-Выход')

        vibor = input("Выберете действие: ")

        if vibor == '1':
            print('1-Хлеб')
            print('2-Яйцо')
            print('3-Молоко')
            prod = input("Выберете товар: ")
            if prod == '1':
                korz.append('Хлеб')
            elif prod == '2':
                korz.append('Яйцо')
            elif prod == '3':
                korz.append('Молоко')
        elif vibor == '2':
            if korz:
                print('Корзина:')
                my_korz = {j: korz.count(j) for j in korz}
                print(my_korz)
            else:
                print('Корзина пуста!')
        elif vibor == '3':
            if korz:
                prod = input('Выберете товар: ')
                if prod in korz:
                    korz.remove(prod)
                    print('Товар удален')
                else:
                    print("Такого товара нет")

            else:
                print('Товаров нет')
        elif vibor == '4':
            if korz:
                sp_zak.extend(korz)
                print(sp_zak)
        elif vibor == '5':
            if sp_zak:
                print(sp_zak)

        elif vibor == '6':
            break
        else:
            print("Неверный выбор")


mag()
