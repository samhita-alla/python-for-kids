"""
Absolute & Relative Paths
"""

import os

print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.isabs("."))
print(os.path.isabs(os.path.abspath(".")))