
#  from alpha/mathlib import geometry.py
from alpha.mathlib import geometry  #  find geometry.py and run the code
import sys

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module/package search order
# 1. current folder
# 2. folders in PYTHONPATH   "DIR1;DIR2;DIR3" on Windows  "DIR1:DIR2:DIR3" on Mac/Linux
# 3. sys.prefix + "/lib"    current Python installation location
print(sys.prefix, '\n')

for path in sys.path:
    print(path)



