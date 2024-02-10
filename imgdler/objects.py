from pathlib import Path


class ImageObject:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.read_bytes = None

    def read(self) -> bytes:
        self.read_bytes = self.path.read_bytes()
        return self.read_bytes
