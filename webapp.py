from flask import Flask, make_response
app = Flask(__name__)
import pytz
from generate_calendar import START_YEAR, END_YEAR, get_calendar 

@app.route('/<path:subpath>')
def calendar(subpath):
    components = subpath.split('/')
    c = []
    res = []
    while len(components):
        e = components.pop(0)
        if e:
            c.append(e)
            t = '/'.join(c)
            if t in pytz.all_timezones:
                res.append(t)
                c = []
    if len(c):
        return make_response("Incorrect value", 404)
    else:
        tzs = []
        for t in res:
            print(t)
            tzs.append(pytz.timezone(t))

        cal = get_calendar(tzs, START_YEAR, END_YEAR)
        response = make_response(str(cal), 200)
        response.headers['Content-Type'] = 'text/calendar'
        return response


@app.route('/')
def index():
    return 'To get the calendar, just append the timezones separated by /, like this: <a href="/Europe/Paris/US/Pacific/">https://thisite/Europe/Paris/US/Pacific/</a>'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
