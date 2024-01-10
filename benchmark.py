import random
import time
from typing import Callable, List

from order_manager import OrderManager
from order import *


def measure_runtime(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time} seconds to execute")
        return result

    return wrapper


@measure_runtime
def run_order_add_benchmark(number_of_orders: int) -> None:
    order_manager = OrderManager()
    for i in range(0, number_of_orders):
        order_id = f"{i:08d}"
        order_type = random.choice([OrderType.BUY, OrderType.SELL])
        order_action = OrderAction.ADD
        price = round(random.uniform(1.0, 100.0), 2)
        quantity = random.randint(1, 1000)

        order = Order(order_id, order_type, order_action, price, quantity)
        order_manager.place(order)


def run_order_remove_benchmark(number_of_orders: int) -> None:
    orders_manager = OrderManager()
    random_orders = [
        Order(
            str(i),
            OrderType.BUY if i % 2 == 0 else OrderType.SELL,
            OrderAction.ADD,
            round(random.uniform(1.0, 100.0), 2),
            random.randint(1, 1000),
        )
        for i in range(1, number_of_orders)
    ]

    for order in random_orders:
        orders_manager.place(order)

    random_orders = [
        Order(order.id, order.type, OrderAction.REMOVE, order.price, order.quantity)
        for order in random_orders
    ]

    _remove_orders(orders_manager, random_orders)


@measure_runtime
def _remove_orders(order_manager: OrderManager, orders: List[Order]):
    for order in orders:
        order_manager.place(order)
