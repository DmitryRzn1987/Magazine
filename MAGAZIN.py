class Store:
    def __init__(self):
        self.cart = []
        self.orders = []
        self.menu_options = {
            '1': self.add_product,
            '2': self.view_basket,
            '3': self.remove_product,
            '4': self.checkout,
            '5': self.view_orders,
            '6': self.exit_store
        }

    def show_menu(self):
        print("\nМеню:")
        for i, option in enumerate(self.menu_options.keys(), start=1):
            print(f"{i}-{self.menu_options[option].__name__.replace('_', ' ').title()}")

    def get_user_input(self, prompt, valid_options=None):
        while True:
            user_input = input(prompt).strip()
            if not valid_options or user_input in valid_options:
                return user_input
            else:
                print('Неверный ввод. Пожалуйста, повторите.')

    def add_product(self, product):
        self.cart.append(product)

    def view_basket(self):
        if self.cart:
            print('Корзина:')
            cart_count = {item: self.cart.count(item) for item in set(self.cart)}
            print(cart_count)
        else:
            print('Корзина пуста!')

    def remove_product(self, product):
        if self.cart and product in self.cart:
            self.cart.remove(product)
            print('Товар удален')
        else:
            print("Такого товара нет" if self.cart else 'Товаров нет')

    def checkout(self):
        if self.cart:
            self.orders.extend(self.cart)
            print(self.orders)

    def view_orders(self):
        print(self.orders if self.orders else 'Заказов нет')

    def exit_store(self):
        print("Выход из магазина.")
        exit(0)

    def process_choice(self, choice):
        menu_option = self.menu_options.get(choice)
        if menu_option:
            if menu_option == self.add_product:
                products = {'1': 'Хлеб', '2': 'Яйцо', '3': 'Молоко'}
                menu_option(products.get(self.get_user_input("Выберете товар: "), "Неверный выбор"))
            else:
                menu_option()
        else:
            print("Неверный выбор")

    def run(self):
        while True:
            self.show_menu()
            choice = self.get_user_input("Выберете действие: ", self.menu_options.keys())
            self.process_choice(choice)

if __name__ == "__main__":
    store = Store()
    store.run()
