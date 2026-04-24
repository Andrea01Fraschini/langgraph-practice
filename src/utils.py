import sys

from loguru import logger, Record


def my_sum[T: (float, str)](a: T, b: T) -> T:
    return a + b


def init_logger() -> None:
    def dynamic_formatter(record: dict[str, Record]) -> str:
        level_name = record['level'].name

        if level_name == 'INFO':
            return '<cyan><b>{level:<7}</b></cyan> | {message}\n'

        elif level_name in ('ERROR', 'CRITICAL'):
            return (
                '<red><b>{level:<7}</b></red> | <red><b>{message}</b></red>\n'
            )

        elif level_name == 'WARNING':
            return '<yellow><b>{level:<7}</b></yellow> | {message}\n'

        elif level_name == 'DEBUG':
            return '{level:<7} | <dim>{message}</dim>\n'

        return '<b>{level:<7}</b> | {message}\n'

    logger.remove()
    logger.add(sys.stderr, format=dynamic_formatter)
