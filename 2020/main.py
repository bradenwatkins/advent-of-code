import sys
from datetime import date
import runner

today = (date.today() - date(2020, 12, 1)).days + 1
day = sys.argv[1] if len(sys.argv) > 1 else today
runner.run(day=day)