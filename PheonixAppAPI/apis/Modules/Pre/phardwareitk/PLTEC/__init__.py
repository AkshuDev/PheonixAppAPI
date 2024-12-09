import os
import sys

PHardwareITK = len(sys.path) - 1
PHardwareITK_P = os.path.join(os.path.dirname(__file__), "..", "..", "..")

if not sys.path[PHardwareITK] == PHardwareITK_P:
    sys.path.append(PHardwareITK_P)

from phardwareitk.PLTEC import Checker

Checker.PLTEC_initCheck()