import sys

from loguru import logger

from src.utils import my_sum

logger.remove()
fmt = '{level: <8 } | {message}'
logger.add(sys.stderr, format=fmt)


def test_sum_int() -> None:
    assert my_sum(3, 5) == 8


def test_sum_str() -> None:
    assert my_sum('a', 'b') == 'ab'


def test_sum_float() -> None:
    assert my_sum(3.3, 4.4) == 7.7
