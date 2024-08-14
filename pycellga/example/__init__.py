import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import optimizer
from individual import GeneType
from . import example_alpha_cga
from . import example_ccga
from . import example_cga
from . import example_mcccga
from . import example_sync_cga