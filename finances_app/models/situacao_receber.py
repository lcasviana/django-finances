from enum import Enum

class SituacaoReceber(Enum):
    A_RECEBER = "A Receber"
    RECEBIDO = "Recebido"

    @classmethod
    def choices(cls):
        return [(i, i.value) for i in cls]
