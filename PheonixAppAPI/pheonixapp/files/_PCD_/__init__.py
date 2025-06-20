import os
import sys

base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..')
smodule_path = os.path.join(base_path, "pheonixappapi", "files")

if not smodule_path in sys.path:
	sys.path.append(smodule_path)
	
if not base_path in sys.path:
	sys.path.append(base_path)
	
