import sys

from loguru import logger

logger.remove()
fmt = '{level: <8 } | {message}'
logger.add(sys.stderr, format=fmt)


def test_main() -> None:
    logger.info('CIAOOOOO')
    assert True
