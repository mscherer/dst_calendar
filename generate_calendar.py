import pytz
import sys
import datetime
from ics import Calendar, Event
import hashlib 

NB_TZ = len(sys.argv)
NB_CHANGE = 2

if NB_TZ < 2:
    print("error")
    sys.exit(1)
tzs = []
for i in sys.argv[1:]:
    tzs.append(pytz.timezone(i))

def get_tz_transition_time(tz, year):
    return [x for x in tz._utc_transition_times if x.year == year]

START_YEAR = datetime.datetime.today().year - 2
END_YEAR = datetime.datetime.today().year + 5
OUTPUT = 'timezone.ics'

cal = Calendar()

for y in range(START_YEAR, END_YEAR):
    # change_times
    #  - summer
    #  - winter
    change_times = []  
    for c in range(0, NB_CHANGE):
        res = []
        for i in tzs:
            ct = get_tz_transition_time(i, y)
            res.append(ct[c])
        change_times.append(res)
    for c in  range(0, NB_CHANGE):
        begin = change_times[c][0]
        for d in change_times[c]:
            if begin > d:
                begin = d

        end = change_times[c][0]
        for d in change_times[c]:
            if end < d:
                end = d


        uid = hashlib.md5((begin.isoformat()).encode()).hexdigest()
        if c == 0:
            p = "Summer time"
        else:
            p = "Winter time"
        ev = Event(name = "Timezone trouble period - %s %s" % (p, y),
                   uid = uid,
                   begin = begin,
                   end = end)
        ev.make_all_day()
        cal.events.add(ev)


with open(OUTPUT, 'w') as f:
    f.write(str(cal))
    
