from flask import Flask, request, jsonify

from algorithms.fcfs import fcfs


app = Flask(__name__)


@app.route("/")
def home():
    return "OS Algorithm Simulator Backend is Running!"


@app.route("/api/cpu/fcfs", methods=["POST"])
def run_fcfs():

    # get data sent by frontend
    data = request.get_json()

    # get processes from the data
    processes = data["processes"]

    # run FCFS algorithm
    result = fcfs(processes)

    # send result back as JSON
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)