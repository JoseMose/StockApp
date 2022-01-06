from flask import Flask, json, render_template
import os
import requests
import finnhub
import content

app = Flask(__name__)

url = "https://data.nasdaq.com/api/v3/datatables/ETFG/FUND.json?ticker=SPY&api_key=AxG8LscgzpqxLLHjrfa4"
url2 = "https://data.nasdaq.com/api/v3/datasets/FRED/NROUST.json?api_key=AxG8LscgzpqxLLHjrfa4"


@app.route("/")
def index():
    finnhub_client = finnhub.Client(api_key="c6qdd2iad3i891nj3ov0")
    response = requests.get(url)
    json_data = response.json()
    important = (json_data)
    covid = finnhub_client.covid19()
    print(covid)
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
        "datasets.html",
        importants = important
    )
app.run(debug=True)
