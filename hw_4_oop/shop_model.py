class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int) -> None:
        if quantity >= 0:
            self.stock += quantity
        else:
            raise ValueError("Некорректное количество товара")


class Order:
    def __init__(self, products: dict[Product, int] | None = None) -> None:
        self.products = products if products is not None else {}

    def add_product(self, product: Product, quantity: int) -> None:
        if quantity <= product.stock:
            if product in self.products:
                self.products[product] += quantity
            else:
                self.products[product] = quantity
        else:
            raise ValueError("Товара недостаточно на складе")

    def calculate_total(self) -> float:
        total = 0
        for prod in self.products:
            total += prod.price * self.products[prod]
        return total

    def remove_product(self, product: Product, quantity: int) -> None:
        if quantity < product.stock and product in self.products:
            self.products[product] -= quantity
        elif quantity == product.stock:
            self.products.pop(product)
        else:
            raise ValueError("Товара больше нет на складе")

    def return_product(self, product: Product, quantity: int) -> None:
        self.remove_product(product, quantity)
        # следующее условие противоречит другим условиям задачи, так как нет
        # механизма который будет уменьшать кол-во товара на складе,
        # при такой реализации товар будет добавляться лишний раз:
        # "вызывать метод update_stock(quantity) у объекта Product,
        # чтобы увеличить количество товара на складе;"


class Store:
    def __init__(self, products: list[Product] | None = None) -> None:
        self.products = products if products is not None else []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def list_products(self) -> list[str | float | int]:
        list_of_products = []
        for prod in self.products:
            list_of_products.append(prod.name)
            list_of_products.append(prod.price)
            list_of_products.append(prod.stock)
            print(
                f"Товар {prod.name} стоимостью {prod.price} в количестве {prod.stock}"
            )
        return list_of_products

    def create_order(self) -> Order:
        return Order()
