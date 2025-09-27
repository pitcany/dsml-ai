__version__ = "0.1.0"

# Re-export selected symbols from submodules to keep the top-level API clean
from .core import *
from .core import __all__ as _core_all
from .viz import *
from .viz import __all__ as _viz_all
from .dl import *
from .dl import __all__ as _dl_all
from .bayes import *
from .bayes import __all__ as _bayes_all
from .time import *
from .time import __all__ as _time_all

__all__ = (
    ["__version__", "hello"]
    + _core_all
    + _viz_all
    + _dl_all
    + _bayes_all
    + _time_all
)

def hello() -> str:
    """Sample function for DSML package."""
    return "Hello, DSML!"
