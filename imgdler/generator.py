from imgdler.generators import BasePathGenerator, PathGenerator, MD5HashedPathGenerator


def __error():
    from imgdler.errors import warning
    from imgdler.logger import logger


    warning("""Warning: `generator.py` will be deprecated in v3.0.0~.
         If you are using `generator.py`, please change it to `generators.py`.
         There are no changes to the following classes: {}, {}, {}
    """.format(
        BasePathGenerator.__name__,
        PathGenerator.__name__,
        MD5HashedPathGenerator.__name__
        )
    )

    logger.warning("`generator.py` will be deprecated in version 3. Please change it to `generators.py`")

__error()
