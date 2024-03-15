from logging import getLogger, Formatter, FileHandler, DEBUG, WARNING
from rich.logging import RichHandler


def imgdler_logger():
    from datetime import date
    from pathlib import Path

    log_filename = f"{str(date.today()).replace('-', '')}.log"
    log_dir = Path(__file__).parent.parent / "log"
    log_dir.mkdir(exist_ok=True)

    logger = getLogger(__name__)
    logger.setLevel(DEBUG)

    file_handler = FileHandler(log_dir / log_filename)
    file_handler.setLevel(DEBUG)
    file_handler.setFormatter(
        Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s - %(name)s - %(funcName)s - %(message)s"
        )
    )

    stream_handler = RichHandler(rich_tracebacks=True)
    stream_handler.setLevel(WARNING)
    stream_handler.setFormatter(
        Formatter("%(asctime)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    )

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger


logger = imgdler_logger()
