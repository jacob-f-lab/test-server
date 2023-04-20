from flask import Flask
from pandas import read_csv

df = read_csv("./data/online_retail.csv")

app = Flask(__name__)

@app.route("/<int:year>/<int:month>/<int:day>", methods=['GET'])
def view(year, month, day):
  res = df[df['InvoiceDate'].str.contains(f'{month}/{day}/{year}', case=False, na=False)]
  return res.to_json(orient='records')
