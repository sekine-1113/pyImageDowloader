from logging import getLogger, Formatter, FileHandler, DEBUG, WARNING
from rich.logging import RichHandler


def imgdler_logger():
    from datetime import datetime
    from pathlib import Path

    now = datetime.now()
    today = now.date()
    log_filename = f"{today.year}{today.month if today.month > 9 else '0' + str(today.month)}{today.day if today.day > 9 else '0' + str(today.day)}.log"

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