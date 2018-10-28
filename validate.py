import os
import sys
if not os.geteuid() == 0:
    sys.exit("\n\033[1;31m -- Run as Root -- \n")
