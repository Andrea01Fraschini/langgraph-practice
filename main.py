import sys

from loguru import logger

logger.remove()
fmt = "{level: <8 } | {message}"
logger.add(sys.stderr, format=fmt)

def main() -> None:
    logger.info("Hello from langgraph-practice!")


if __name__ == "__main__":
    main()
