import flask
from flask import Flask, jsonify, request
import json
import datetime
from datetime import date
import calendar
# from waitress import serve
from sqlLib import  get_kelas, get_jadwal
app = Flask(__name__)


@app.route('/schedule', methods=['POST'])
def schedule():
    json_data = flask.request.json
    if json_data == None:
        result = []
        resp = json.dumps(result)
        return resp, 402
    else:
        if 'id' not in json_data:
            result = []
            resp = json.dumps(result)
            return resp, 409
        else:
            id = json_data['id']
            kelas = get_kelas(id)
            tgl = date.today()
            tgl = tgl.strftime("%d%m%Y")
            day = datetime.datetime.strptime(tgl, '%d%m%Y').weekday()
            day = calendar.day_name[day]
            day = str(day)
            day = day.lower()
            if kelas == None:
                result = []
                resp = json.dumps(result)
                return resp, 206
            else:
                result = get_jadwal(kelas, day)
                resp = json.dumps(result)
                return resp, 207


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=4002)
    app.run(port=4001, debug=True)