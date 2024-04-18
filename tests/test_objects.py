import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(sys.argv[0]).parent.parent))
from imgdler.objects import ImageObject


class TestImageObject(unittest.TestCase):

    def test_ImageObject(self):
        parent_dir = Path(__file__).parent
        path = parent_dir / Path("test_images/1KB.png")
        image = ImageObject(path)
        self.assertEqual(image.path, parent_dir / Path("test_images/1KB.png"))

    def test_ImageObjectRead(self):
        parent_dir = Path(__file__).parent
        path = parent_dir / Path("test_images/1KB.png")
        image = ImageObject(path)
        image_bin = image.read()
        self.assertEqual(image_bin, b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x80\x00\x00\x02\x80\x01\x03\x00\x00\x006\x03[`\x00\x00\x00\x04gAMA\x00\x00\xb1\x8f\x0b\xfca\x05\x00\x00\x00 cHRM\x00\x00z&\x00\x00\x80\x84\x00\x00\xfa\x00\x00\x00\x80\xe8\x00\x00u0\x00\x00\xea`\x00\x00:\x98\x00\x00\x17p\x9c\xbaQ<\x00\x00\x00\x06PLTE\xfff\x00\xff\xff\xffWo\xb6\xfc\x00\x00\x00\x01bKGD\x01\xff\x02-\xde\x00\x00\x00\x07tIME\x07\xe3\x03\x1a\x01\x07\x16\x9eWG\x06\x00\x00\x00HIDATx\xda\xed\xc1\x01\x01\x00\x00\x00\x82 \xff\xafnH@\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x19\xca\x80\x00\x01`<\xcb\x88\x00\x00\x00%tEXtdate:create\x002019-03-26T10:07:22+09:00'\x88\xc1T\x00\x00\x00%tEXtdate:modify\x002019-03-26T10:07:22+09:00V\xd5y\xe8\x00\x00\x02\xa3tEXtComment\x00JHHLHuHpK38IpK1RFq7xGOhZlbD2ZupI9CivV1fMu1MNB0P3u3bUXWvreljURqpQ8CbfY9NX2mq3VeJmBPIRWGdxt4MLNM6cZdcX0YbfUhrQCesbgkD6cs9WOnhTDiMckKoGVS9VHtAQuR49FeRmSbnK2puV6qTfXbqdVd7U32wV7ye2py5KO2aLffQFNUwokEIgZHCpVN0vK8HPnQN2MCpbSquNqac3XNaWxFPggWWrsaUOUpE5FJqGCg7i47EaE9FW0VdnZ7h9sxg2SEAC53y0hA8oGQuwwwwVFQguAR7QqVg1HCbvpFRZ6OSNzJs9dxx0UfXAJEimmJAqN2JttYKlDOSPIl6DmNVkkqn22MlNvLANoRl1VaJfj9VjueCMC12st2iZaClz52EYqkmuuDsYb1oJUfclfsll20OusFnPDdgADr4nhyUx9YLTApt2xbfusEgeH66gc8VxtAVvjNlrs53MteRpNC03yTHAvohEoZp3Lv7zgHnnnGfnBsZGkEB9rWBEXatCahqW1Xiln2w0tv62vTSB40wZpsLfkVjAexCciJOP02EC5H30MS1MZ4qgGRdrGnoeMlh4ycDJ0L34E7hVA9gPUPGtYzIrMl2WZKBmxAi2nIxFVnjXm7CNKihBxFmt76yoerJaAFCvH6nUBy\n\xb6\n\x0b\xa5\x00\x00\x00\x00IEND\xaeB`\x82")



if __name__ == "__main__":
    unittest.main()
