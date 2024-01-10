class InvalidOrderActionError(Exception):
    pass


class InvalidOrderTypeError(Exception):
    pass


class OrderAlreadyPlacedError(Exception):
    pass


class OrderDoesNotExistError(Exception):
    pass
