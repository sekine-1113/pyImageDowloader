import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).parent.parent))
from imgdler.imgdler import ImageDownloader


class TestImageDownloader(unittest.TestCase):

    def test_ImageDownloader(self):
        downloader = ImageDownloader("./images")
        copy_downloader = downloader.new_client()
        self.assertEqual(downloader._save_dir, copy_downloader._save_dir)


if __name__ == "__main__":
    unittest.main()
