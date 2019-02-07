from flask import Flask
import requests

app = Flask(__name__)

url = 'https://www.googleapis.com/bigquery/v2/projects/analytics-sandbox-jf/datasets/analytics-sandbox-jf:weather_data'
r = requests.get(url)
bq_data = r.text


ga_endpoint = 'https://google-analytics.com/collect?v=1&t=event&tid=UA-134072717-1&cid=123456.654321&ec=Weather&ea=' + bq_data
requests.post(ga_endpoint)

@app.route('/')
def home():
    return '<h1>Homepage</h1>'

if __name__ == '__main__':
    app.run(debug=True)