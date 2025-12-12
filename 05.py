# import these modules if you need them:
# from datetime import datetime, timezone
# import math
from datetime import datetime
      
def time_until_take_off(from_time: str, take_off_time: str) -> int:
  dt_from_time = datetime.strptime(from_time, '%Y*%m*%d@%H|%M|%S NP')
  dt_take_off_time = datetime.strptime(take_off_time, '%Y*%m*%d@%H|%M|%S NP')
  delta_time = dt_take_off_time - dt_from_time
  delta_time_secs = delta_time.total_seconds()
  
  return delta_time_secs

takeoff = '2025*12*25@00|00|00 NP'

# // desde el 24 diciembre 2025, 23:59:30, 30 segundos antes del despegue
time_until_take_off('2025*12*24@23|59|30 NP', takeoff)
# // 30

# // justo en el momento exacto
time_until_take_off('2025*12*25@00|00|00 NP', takeoff)
# // 0

# // 12 segundos después del despegue
time_until_take_off('2025*12*25@00|00|12 NP', takeoff)
# // -12