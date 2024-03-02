import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).parent.parent))
from imgdler.objects import ImageObject


class TestImageObject(unittest.TestCase):

    def test_ImageObject(self):
        image = ImageObject("example")
        self.assertEqual(image.path, "example")

    def test_ImageObjectRead(self):
        image = ImageObject("example")
        image.read()


if __name__ == "__main__":
    unittest.main()
