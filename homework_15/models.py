import uuid


def generate_uuid():
    random_uuid = uuid.uuid4()
    return random_uuid


class User:
    def __init__(self, type):
        self.id = generate_uuid()
        self.type = type

    def __str__(self):
        return f"User('{self.type}', {self.id})"


class Host(User):
    def __init__(self, type="host"):
        super().__init__(type)  # TODO check
        self.type = type

    def create_room(self, amount, price, ac, refrigerator):
        id = generate_uuid()
        Room(
            id,
            self.id,
            True,
            amount,
            price,
            ac,
            refrigerator,
        )

    def __str__(self):
        return f"{super().__str__()} \n Host('{self.type}', {self.id})"


class Guest(User):
    def __init__(self, type="guest"):
        super().__init__(type)  # TODO check
        self.type = type

    def check_if_available(self):
        pass

    def make_reservations(self):
        pass

    def __str__(self):
        return f"{super().__str__()} \n Guest('{self.type}', {self.id})"


class Room:
    def __init__(
        self,
        id,
        host_id,
        available: bool,
        amount: int,
        price: float,
        ac: bool,
        refrigerator: bool,
    ):
        self.id = id
        self.host_id = host_id
        self.available = available
        self.price = price
        self.amount = amount
        self.ac = ac
        self.refrigerator = refrigerator


host = Host()
guest = Guest()
print(host)
print(guest)
