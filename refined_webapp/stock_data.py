#!/usr/bin/python
#
# Historical Stock Prices
# with the RPi using Python & Flask
#
# stock_data.py
#
# (c) Dr. Yves J. Hilpisch
# The Python Quants
#

import pandas as pd
import pandas.io.data as web
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, redirect, url_for
from forms import SymbolSearch


app = Flask(__name__)

# Define a route for the default URL, which loads the form   
@app.route('/')
def main():
    return render_template('form_submit.html')

@app.route('/results/', methods=['POST'])
def results():
    symbol=request.form['symbol']
    trend1=request.form['trend1']
    trend2=request.form['trend2']
    print symbol, trend1, trend2
    data = web.DataReader(symbol, data_source='yahoo')
    data['Trend 1'] = pd.rolling_mean(data['Adj Close'], window=int(trend1))
    data['Trend 2'] = pd.rolling_mean(data['Adj Close'], window=int(trend2))
    data[['Adj Close', 'Trend 1', 'Trend 2']].plot()
    output = 'results.png'
    plt.savefig('static/' + output)
    table = data.tail().to_html()
    return render_template('results.html', symbol=symbol,
                            output=output, table=table)

if __name__ == '__main__':
    app.run(debug=True)
