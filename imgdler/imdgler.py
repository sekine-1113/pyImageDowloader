from imgdler.imgdler import Downloadable, ImageDownloader

def __warning():
    from rich.console import Console
    from rich.text import Text
    __duplicated_warn = """Warning: `imdgler.py` will be deprecated in v3.0.0~.
         If you are using `imdgler.py`, please change it to `imgdler.py`.
         There are no changes to the following classes: {}, {}
""".format(
        Downloadable.__name__,
        ImageDownloader.__name__,
    )
    Console().print(Text(__duplicated_warn, "#f0f033"))

__warning()
