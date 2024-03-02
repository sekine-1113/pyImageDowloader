import sys
from abc import ABC, abstractmethod
from pathlib import Path

import requests

from imgdler.generators import BasePathGenerator, MD5HashedPathGenerator
from imgdler.objects import ImageObject
from imgdler.logger import logger


class Downloadable(ABC):
    @abstractmethod
    def download(self):
        ...


class ImageDownloader(Downloadable):
    def __init__(self, save_dir: str | Path = None, mkdir=True, parents=True, exist_ok=True, filename_generator: BasePathGenerator=MD5HashedPathGenerator()) -> None:
        if save_dir is None:
            tmp = Path(sys.argv[0]).parent
            save_dir = tmp / "images"
            logger.info(f"saving dir: {save_dir}")
        self._save_dir = save_dir if isinstance(save_dir, Path) else Path(save_dir)
        if mkdir:
            self._save_dir.mkdir(parents=parents, exist_ok=exist_ok)
            logger.info(f"make: {save_dir}")
        self._generator = filename_generator

    def _get_image(self, image_url: str) -> requests.Response:
        response = requests.get(image_url)
        return response

    def _check_error(self, response: requests.Response):
        if response.status_code != 200:
            logger.error(f"{response.status_code} {response.reason}")
            raise Exception(f"{response.status_code} {response.reason}")
        return False

    def _generate_filename(self, response: requests.Response) -> Path:
        file = self._save_dir / self._generator.generate(response)
        logger.info(f"generate: {file.absolute()}")
        return file

    def _write(self, filename: str | Path, binary: str | bytes, overwrite: bool=False) -> ImageObject:
        filepath = self._save_dir / filename

        if not overwrite and filepath.exists():
            logger.info(f"exists: {filepath.absolute()}")
            return ImageObject(filepath)

        filepath.write_bytes(binary)
        image_object = ImageObject(filepath)
        image_object.read()
        logger.info(f"create: {image_object.path}")
        return image_object

    def download(self, image_url: str, /, *, overwrite=False) -> ImageObject:
        response = self._get_image(image_url)
        self._check_error(response)
        self._generated_filepath = self._generate_filename(response)
        image_object = self._write(self._generated_filepath, response.content, overwrite)
        logger.info("done download")
        return image_object

    def new_client(self, filename_generator: BasePathGenerator = None):
        if (filename_generator is None):
            filename_generator = self._generator
        new_downloader = ImageDownloader(self._save_dir, filename_generator = filename_generator)
        logger.info("create new client")
        return new_downloader
