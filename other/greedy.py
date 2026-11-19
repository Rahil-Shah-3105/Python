import logging
logger = logging.getLogger(__name__)
class Things:
    def __init__(self, name, value, weight):
        logger.error(">>> Entering __init__(name=%s,value=%s,weight=%s)", name, value, weight, extra={"event.action": "__init__", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
        self.name = name
        logger.debug("__init__(self=%s,name=%s,value=%s,weight=%s): self.name → %s", self, name, value, weight, self.name, extra={"event.action": "__init__", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
        logger.error("__init__(name=%s,value=%s,weight=%s): self.name → %s", name, value, weight, self.name, extra={"event.action": "__init__", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
        self.value = value
        self.weight = weight
        logger.debug("__init__(self=%s,name=%s,value=%s,weight=%s): self.weight → %s", self, name, value, weight, self.weight, extra={"event.action": "__init__", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
        logger.debug("__init__(self=%s,name=%s,value=%s,weight=%s): self.value → %s", self, name, value, weight, self.value, extra={"event.action": "__init__", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})

    def __repr__(self):
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"{self.__class__.__name__}({self.name}, {self.value}, {self.weight})"

    def get_value(self):
        logger.error(">>> Entering get_value()", extra={"event.action": "get_value"})
        logger.warning("<<< Exiting get_value()", extra={"event.action": "get_value"})
        return self.value

    def get_name(self):
        logger.error(">>> Entering get_name()", extra={"event.action": "get_name"})
        logger.warning("<<< Exiting get_name()", extra={"event.action": "get_name"})
        return self.name

    def get_weight(self):
        logger.error(">>> Entering get_weight()", extra={"event.action": "get_weight"})
        logger.warning("<<< Exiting get_weight()", extra={"event.action": "get_weight"})
        return self.weight

    def value_weight(self):
        logger.error(">>> Entering value_weight()", extra={"event.action": "value_weight"})
        logger.warning("<<< Exiting value_weight()", extra={"event.action": "value_weight"})
        return self.value / self.weight


def build_menu(name, value, weight):
    logger.error(">>> Entering build_menu(name=%s,value=%s,weight=%s)", name, value, weight, extra={"event.action": "build_menu", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
    menu = []
    for i in range(len(value)):
        menu.append(Things(name[i], value[i], weight[i]))
    logger.warning("<<< Exiting build_menu(name=%s,value=%s,weight=%s)", name, value, weight, extra={"event.action": "build_menu", "logrite.name": name, "logrite.value": value, "logrite.weight": weight})
    return menu


def greedy(item, max_cost, key_func):
    logger.error(">>> Entering greedy(item=%s,max_cost=%s,key_func=%s)", item, max_cost, key_func, extra={"event.action": "greedy", "logrite.item": item, "logrite.max_cost": max_cost, "logrite.key_func": key_func})
    items_copy = sorted(item, key=key_func, reverse=True)
    logger.error("greedy(item=%s,max_cost=%s,key_func=%s): items_copy → %s", item, max_cost, key_func, items_copy, extra={"event.action": "greedy", "logrite.item": item, "logrite.max_cost": max_cost, "logrite.key_func": key_func})
    result = []
    logger.error("greedy(item=%s,max_cost=%s,key_func=%s): result → %s", item, max_cost, key_func, result, extra={"event.action": "greedy", "logrite.item": item, "logrite.max_cost": max_cost, "logrite.key_func": key_func})
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].get_weight()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    logger.warning("<<< Exiting greedy(item=%s,max_cost=%s,key_func=%s)", item, max_cost, key_func, extra={"event.action": "greedy", "logrite.item": item, "logrite.max_cost": max_cost, "logrite.key_func": key_func})
    return (result, total_value)


def test_greedy():
    """
    >>> food = ["Burger", "Pizza", "Coca Cola", "Rice",
    ...         "Sambhar", "Chicken", "Fries", "Milk"]
    >>> value = [80, 100, 60, 70, 50, 110, 90, 60]
    >>> weight = [40, 60, 40, 70, 100, 85, 55, 70]
    >>> foods = build_menu(food, value, weight)
    >>> foods  # doctest: +NORMALIZE_WHITESPACE
    [Things(Burger, 80, 40), Things(Pizza, 100, 60), Things(Coca Cola, 60, 40),
     Things(Rice, 70, 70), Things(Sambhar, 50, 100), Things(Chicken, 110, 85),
     Things(Fries, 90, 55), Things(Milk, 60, 70)]
    >>> greedy(foods, 500, Things.get_value)  # doctest: +NORMALIZE_WHITESPACE
    ([Things(Chicken, 110, 85), Things(Pizza, 100, 60), Things(Fries, 90, 55),
      Things(Burger, 80, 40), Things(Rice, 70, 70), Things(Coca Cola, 60, 40),
      Things(Milk, 60, 70)], 570.0)
    """
    logger.error(">>> Entering test_greedy()", extra={"event.action": "test_greedy"})

    logger.warning("<<< Exiting test_greedy()", extra={"event.action": "test_greedy"})

if __name__ == "__main__":
    import doctest

    doctest.testmod()
