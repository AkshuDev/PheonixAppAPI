import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")

if not BASE_DIR in sys.path:
	sys.path.append(BASE_DIR)
