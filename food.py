class Food:

    def __init__(self) -> None:
        self.weight: int = -1
        self.amount: int = -1

    def calories(self) -> int:
        raise NotImplementedError()

    def get_weight(self) -> int:
        raise NotImplementedError()

    def __eq__(self, other: object) -> bool:
        #if not isinstance(other, Food):
            #return NotImplemented
        if self.calories() == other.calories():
            return True
        else:
            return False

    def __lt__(self, other: object) -> int:
        #if not isinstance(other, Food):
            #return NotImplemented
        if self.calories() < other.calories():
            return True
        else:
            return False


class Apples(Food):

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def calories(self) -> int:
        return 102 * self.amount

    def get_weight(self) -> int:
        return 200 * self.amount


class Oranges(Food):

    def __init__(self, amount: int) -> None:
        self.amount = amount

    def calories(self) -> int:
        return 94 * self.amount

    def get_weight(self) -> int:
        return 200 * self.amount


class CookieDough(Food):

    def __init__(self, weight: int) -> None:
        self.weight = weight

    def calories(self) -> int:
        return int(2.44 * self.weight)

    def get_weight(self) -> int:
        return self.weight


class Chicken(Food):

    def __init__(self, weight: int, amount: int) -> None:
        self.weight = weight
        self.amount = amount

    def calories(self) -> int:
        return 244 * self.amount

    def get_weight(self) -> int:
        return 111 * self.weight


class Fish(Food):

    def __init__(self, weight: int, amount: int) -> None:
        self.weight = weight
        self.amount = amount

    def calories(self) -> int:
        return 40 * self.amount

    def get_weight(self) -> int:
        return 10 * self.weight


if __name__ == "__main__":
    apple_obj = Apples(12)
    orange_obj = Oranges(12)
    cookieDough_obj = CookieDough(100)
    chicken_obj = Chicken(1000, 10)
    fish_obj = Fish(1000, 10)
    print(apple_obj.calories())
    print(chicken_obj.get_weight())
    print(apple_obj == orange_obj)
    print(fish_obj < chicken_obj)