from .generators import BasePathGenerator, PathGenerator, MD5HashedPathGenerator

def __warning():
    from rich.console import Console
    from rich.text import Text
    __generator_duplicated_warn = """Warning: `generator.py` will be deprecated in v3.0.0~.
         If you are using `generator.py`, please change it to `generators.py`.
         There are no changes to the following classes: {}, {}, {}
""".format(
        BasePathGenerator.__name__,
        PathGenerator.__name__,
        MD5HashedPathGenerator.__name__,
    )
    Console().print(Text(__generator_duplicated_warn, "#f0f033"))

__warning()
