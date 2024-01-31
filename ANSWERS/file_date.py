import sys
import os
from datetime import datetime

for filename in sys.argv[1:]:
    mtime = os.path.getmtime(filename)
    file_date = datetime.fromtimestamp(mtime)
    fmt_date = datetime.strftime(file_date,'%b %d, %Y')
    print("{0:15s} {1}".format(filename, fmt_date))
