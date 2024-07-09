from enum import Enum, unique


def check_order_status(input_value: str) -> bool:
    for status in OrderStatus:
        if status.value == input_value:
            return True
    return False


@unique
class OrderStatus(Enum):
    RECEIVED = "Recebido"
    DOING = "Em Preparação"
    READY = "Pronto"
    DONE = "Finalizado"

    def __str__(self) -> str:
        return self.value
