from datetime import date
import runner

today = (date.today() - date(2020, 12, 1)).days + 1
runner.run(day=today)