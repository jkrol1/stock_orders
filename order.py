from dataclasses import dataclass
from enum import Enum


class OrderType(Enum):
    BUY = 1
    SELL = 2


class OrderAction(Enum):
    ADD = 1
    REMOVE = 2


@dataclass
class Order:
    id: str
    type: OrderType
    action: OrderAction
    price: float
    quantity: int
