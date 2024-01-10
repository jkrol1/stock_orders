from typing import List

from pytest import fixture

from order import *
from order_manager import OrderManager


@fixture
def order_manager() -> OrderManager:
    return OrderManager()


@fixture
def mock_orders() -> List[Order]:
    return [
        Order("001", OrderType.BUY, OrderAction.ADD, 20.00, 100),
        Order("002", OrderType.SELL, OrderAction.ADD, 25.00, 200),
        Order("003", OrderType.BUY, OrderAction.ADD, 23.00, 50),
        Order("004", OrderType.BUY, OrderAction.ADD, 25.00, 70),
        Order("003", OrderType.BUY, OrderAction.REMOVE, 23.00, 50),
        Order("005", OrderType.SELL, OrderAction.ADD, 28.00, 100),
    ]
