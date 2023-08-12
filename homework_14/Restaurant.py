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
        if dish_name in self.menu:
            price: int = self.menu.get(dish_name, {}).get("price", 0)
            available_qty: int = self.menu.get(dish_name, {}).get("quantity", 0)
            result_price: int = 0

            if quantity <= available_qty:
                result_price = price * quantity
                self.menu[dish_name]["quantity"] -= quantity
                return result_price
            else:
                return "Requested quantity not available"
        else:
            return "Dish not available"
