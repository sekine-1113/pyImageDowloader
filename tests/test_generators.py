import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).parent.parent))
from imgdler.generators import PathGenerator, MD5HashedPathGenerator


class MockResponse:

    def __init__(self, url, content) -> None:
        self.url = url
        self.content = content


class TestPathGenerator(unittest.TestCase):

    def test_PathGenerator(self):
        generator = PathGenerator()
        path = generator.generate(MockResponse("http://example.com/test.jpg", b"test"))
        self.assertEqual(path.name, "test.jpg")


class TestMD5HashedPathGenerator(unittest.TestCase):

    def test_MD5HashedPathGenerator(self):
        generator = MD5HashedPathGenerator()
        path = generator.generate(MockResponse("http://example.com/test.jpg", b"test"))
        self.assertEqual(path.name, "098f6bcd4621d373cade4e832627b4f6.jpg")


if __name__ == "__main__":
    unittest.main()
