from enum import Enum

class SituacaoPagar(Enum):
    A_PAGAR = "A Pagar"
    PAGO = "Pago"

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]
