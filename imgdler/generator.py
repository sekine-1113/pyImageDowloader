import hashlib
from abc import ABC, abstractmethod
from pathlib import Path

import requests


class BasePathGenerator(ABC):
    @abstractmethod
    def generate(self, response: requests.Response) -> Path:
        ...


class PathGenerator(BasePathGenerator):
    def generate(self, response: requests.Response) -> Path:
        return Path(response.url.split("/")[-1])


class MD5HashedPathGenerator(BasePathGenerator):
    def generate(self, response: requests.Response) -> Path:
        filename = hashlib.md5(response.content).hexdigest()
        ext = response.url.split("/")[-1].split(".")[-1]
        return Path(f"{filename}.{ext}")
