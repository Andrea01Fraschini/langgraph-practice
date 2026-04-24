from pathlib import Path

from loguru import logger

from src.utils import init_logger

init_logger()

documents_root_dir = Path("./fastapi/docs/en/docs")


def main() -> None:
    logger.info("Fetching documents' names...")
    docs_path_iter = documents_root_dir.rglob("*.asds")
    num_documents = len(list(docs_path_iter))

    if num_documents == 0:
        logger.warning("Number of documents is 0")

    logger.info(f"Number of documents: {num_documents}")


if __name__ == "__main__":
    main()
