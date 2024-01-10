from typing import Dict, List, Optional

from sortedcontainers import SortedDict

from order import *
from exceptions import *


class OrderManager:
    def __init__(self) -> None:
        self._buy_orders: Dict[str, Order] = dict()
        self._buy_prices = SortedDict()
        self._sell_orders: Dict[str, Order] = dict()
        self._sell_prices = SortedDict()

    def place(self, order: Order) -> None:
        if order.action == OrderAction.ADD:
            self._add(order)
        elif order.action == OrderAction.REMOVE:
            self._remove(order)
        else:
            raise InvalidOrderActionError

        print("Order has been placed")
        self.display_best_prices()

    def _add(self, order: Order) -> None:
        if self._order_exists(order):
            raise OrderAlreadyPlacedError

        if order.type == OrderType.BUY:
            self._add_order_to_prices(order, self._buy_prices)
            self._buy_orders[order.id] = order
        elif order.type == OrderType.SELL:
            self._add_order_to_prices(order, self._sell_prices)
            self._sell_orders[order.id] = order
        else:
            raise InvalidOrderTypeError

    @staticmethod
    def _add_order_to_prices(order: Order, prices_container: SortedDict) -> None:
        if not prices_container.get(order.price):
            prices_container[order.price] = {order.id}
        else:
            prices_container[order.price].add(order.id)

    def _remove(self, order) -> None:
        if not self._order_exists(order):
            raise OrderDoesNotExistError

        if order.type == OrderType.BUY:
            del self._buy_orders[order.id]
            self._remove_order_from_prices(order, self._buy_prices)
        elif order.type == OrderType.SELL:
            del self._sell_orders[order.id]
            self._remove_order_from_prices(order, self._sell_prices)
        else:
            raise InvalidOrderTypeError

    def _order_exists(self, order: Order) -> bool:
        return order.id in self._buy_orders or order.id in self._sell_orders

    @staticmethod
    def _remove_order_from_prices(order: Order, prices_container: SortedDict) -> None:
        ids_set = prices_container[order.price]
        if len(ids_set) == 1:
            del prices_container[order.price]
        else:
            ids_set.remove(order.id)

    def display_best_prices(self) -> None:
        best_buy_order_ids = self._buy_prices.peekitem(0)[1] if self._buy_prices else []
        best_sell_order_ids = (
            self._sell_prices.peekitem(-1)[1] if self._sell_prices else []
        )
        best_buy_orders = self._get_orders_by_id_from_orders(
            best_buy_order_ids, self._buy_orders
        )
        best_sell_orders = self._get_orders_by_id_from_orders(
            best_sell_order_ids, self._sell_orders
        )
        print(
            f"Buy orders with the best price: {best_buy_orders}\nSell orders with the best price: {best_sell_orders}\n"
        )

    @staticmethod
    def _get_orders_by_id_from_orders(
        order_ids: List[str], orders_container: Dict[str, Order]
    ) -> List[Optional[Order]]:
        return [
            orders_container.get(order_id)
            for order_id in order_ids
            if orders_container.get(order_id)
        ]
