from imgdler.imgdler import Downloadable, ImageDownloader


def __error():
    from imgdler.errors import warning
    from imgdler.logger import logger

    warning(""""Warning: `imdgler.py` will be deprecated in v3.0.0~.
         If you are using `imdgler.py`, please change it to `imgdler.py`.
         There are no changes to the following classes: {}, {}
    """.format(
        Downloadable.__name__,
        ImageDownloader.__name__,
    ))

    logger.warning("`imdgler.py` will be deprecated in version 3. Please change it to `imgdler.py`")

__error()
