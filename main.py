from flask import Flask, current_app
from pandas import read_csv

df = read_csv("./data/online_retail.csv")

app = Flask(__name__, static_folder='data', static_url_path='')

@app.route("/<int:year>/<int:month>/<int:day>", methods=['GET'])
def view(year, month, day):
  res = df[df['InvoiceDate'].str.contains(f'{month}/{day}/{year}', case=False, na=False)]
  return res.to_json(orient='records')

