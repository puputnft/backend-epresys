from sqlLib import get_main, cek_id_main
import flask
from flask import Flask, jsonify, request
#from waitress import serve
import json
app = Flask(__name__)


@app.route("/user/history", methods=['POST'])
def history():
    json_data = flask.request.json
    if json_data == None:
        result = []
        return json.dumps(result), 504
    else:
        if 'id' not in json_data:
            result = []
            return json.dumps(result), 505
        else:
            id = json_data['id']
            cek_id = cek_id_main(id)
            if cek_id == False:
                result = []
                return json.dumps(result), 506
            else:
                result = get_main(id)
                return result, 201


if __name__ == "__main__":
    # serve(app, host="0.0.0.0", port=9008)
    app.run(port=4008, debug=True)