class Restaurant:
    def __init__(self, name: str, cuisine: str, menu: dict[str, dict[str, int]]):
        self.name = name
        self.cuisine = cuisine
        self.menu = menu


class FastFood(Restaurant):
    def __init__(
        self, name, cuisine, menu: dict[str, dict[str, int]], drive_thru: bool
    ):
        super().__init__(name, cuisine, menu)
        self.drive_thru = drive_thru

    def order(self, dish_name, quantity):
        if dish_name not in self.menu:
            return "Dish not available"

        dish = self.menu[dish_name]
        available_qty: int = dish.get("quantity", 0)
        if quantity > available_qty:
            return "Requested quantity not available"

        price: int = dish.get("price", 0)
        result_price: int = price * quantity
        dish["quantity"] -= quantity
        return result_price
