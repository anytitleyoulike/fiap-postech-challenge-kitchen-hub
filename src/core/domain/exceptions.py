class OperationalException(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)

class NotFoundError(Exception):
    def __init__(self, message: str = ""):
        super().__init__(message)
