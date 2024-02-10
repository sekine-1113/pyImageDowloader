import hashlib
from abc import ABC, abstractmethod
from pathlib import Path

import requests


class BaseFilenameGenerator(ABC):
    @abstractmethod
    def generate(self, response: requests.Response) -> Path:
        ...


class FilenameGenerator(BaseFilenameGenerator):
    def generate(self, response: requests.Response) -> Path:
        return Path(response.url.split("/")[-1])


class MD5HashedFilenameGenerator(BaseFilenameGenerator):
    def generate(self, response: requests.Response) -> Path:
        filename = hashlib.md5(response.content).hexdigest()
        ext = response.url.split("/")[-1].split(".")[-1]
        return Path(f"{filename}.{ext}")
