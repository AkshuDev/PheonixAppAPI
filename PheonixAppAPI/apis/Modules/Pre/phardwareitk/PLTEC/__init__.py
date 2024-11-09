import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

from phardwareitk.PLTEC import Checker

Checker.PLTEC_initCheck()