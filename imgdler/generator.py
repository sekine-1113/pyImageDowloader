from .generators import BasePathGenerator, PathGenerator, MD5HashedPathGenerator

def __error():
    from .errors import warning

    warning("""Warning: `generator.py` will be deprecated in v3.0.0~.
         If you are using `generator.py`, please change it to `generators.py`.
         There are no changes to the following classes: {}, {}, {}
    """.format(
        BasePathGenerator.__name__,
        PathGenerator.__name__,
        MD5HashedPathGenerator.__name__
        )
    )

__error()
