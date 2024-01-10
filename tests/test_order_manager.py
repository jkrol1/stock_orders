from typing import List, Generator

from _pytest.capture import CaptureFixture

from order import Order
from order_manager import OrderManager


def test_order_placing(order_manager, mock_orders) -> None:
    _add_orders_to_order_manager(mock_orders, order_manager)

    assert list(order_manager._buy_orders.keys()) == ["001", "004"]
    assert list(order_manager._buy_prices.items()) == [(20.0, {"001"}), (25.0, {"004"})]
    assert list(order_manager._sell_orders.keys()) == ["002", "005"]
    assert list(order_manager._sell_prices.items()) == [
        (25.0, {"002"}),
        (28.0, {"005"}),
    ]


def test_display_best_prices(
    order_manager: OrderManager, mock_orders: List[Order], capsys: CaptureFixture
) -> None:
    _add_orders_to_order_manager(mock_orders, order_manager)
    captured = capsys.readouterr()
    order_manager.display_best_prices()

    assert (
        "Buy orders with the best price: [Order(id='001', type=<OrderType.BUY: 1>, action=<OrderAction.ADD: 1>, price=20.0, quantity=100)]"
        in captured.out
    )
    assert (
        "Sell orders with the best price: [Order(id='005', type=<OrderType.SELL: 2>, action=<OrderAction.ADD: 1>, price=28.0, quantity=100)]"
        in captured.out
    )


def _add_orders_to_order_manager(
    orders: List[Order], order_manager: OrderManager
) -> None:
    for order in orders:
        order_manager.place(order)
