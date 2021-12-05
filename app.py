from flask import Flask, json, render_template
import os
import requests

app = Flask(__name__)

url = "https://data.nasdaq.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY&api_key=AxG8LscgzpqxLLHjrfa4"
url2 = "https://data.nasdaq.com/api/v3/datasets/FRED/NROUST.json?api_key=AxG8LscgzpqxLLHjrfa4"

@app.route("/")
def index():
    response = requests.get(url)
    json_data = response.json()
    important = (json_data)
    return render_template(
        "index.html",
        importants = important,
    )
@app.route("/datasets")
def datasets():
    response = requests.get(url2)
    json_data = response.json()
    important = (json_data)
    return render_template(
        "index.html",
        importants = important
    )
app.run(debug=True)
