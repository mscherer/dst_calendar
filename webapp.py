from flask import Flask, make_response
app = Flask(__name__)
import pytz
from generate_calendar import START_YEAR, END_YEAR, get_calendar 

@app.route('/<path:subpath>')
# ‘/’ URL is bound with hello_world() function.
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
            tzs.append(pytz.timezone(t))

        cal = get_calendar(tzs, START_YEAR, END_YEAR)
        response = make_response(str(cal), 200)
        response.headers['Content-Type'] = 'text/calendar'
        return response


@app.route('/')
def index():
    return "Plop"
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()