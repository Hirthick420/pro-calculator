from typing import List, Tuple

class CalcHistory:
    """
    Stores successful calculations as (expression, result) tuples.
    """
    def __init__(self) -> None:
        self._ledger: List[Tuple[str, float]] = []

    def record(self, expr: str, result: float) -> None:
        self._ledger.append((expr, result))

    def entries(self) -> List[Tuple[str, float]]:
        return list(self._ledger)

    def clear(self) -> None:
        self._ledger.clear()
