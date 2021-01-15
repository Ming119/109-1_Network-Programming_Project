# app.py
#
# This program runs in Python 3.8
# This is a Web Application for the main.py
#

from flask import Flask, render_template, request, flash
import secrets
import main

app = Flask(__name__);
app.secret_key = secrets.token_urlsafe(32);

stations = main.getStations();
graph = main.constructRoute(stations);

@app.route('/', methods = ['GET', 'POST'])
def index(result = None):
    if request.method == 'POST':
        result = request.form;
        if (result['startStationSelect'] == 'null' or result['endStationSelect'] == 'null'):
            flash('請選擇車站');
            return render_template('./index.html', stations = stations, result = 'error');

        start = main.findStationFromLabel(result['startStationSelect']);
        end = main.findStationFromLabel(result['endStationSelect']);
        path, time = main.dijsktra(graph, start, end);
        price = main.getPrice(start, end);
        mins = time//60;
        seconds = time%60;
        result = (path, price, (mins, seconds))

    return render_template('./index.html', stations = stations, result = result);



if __name__ == "__main__":
    app.run(debug = True);
