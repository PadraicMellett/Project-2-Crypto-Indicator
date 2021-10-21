import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy import sql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.sql.expression import false
from flask import render_template

sqlalchemy.types.Numeric(asdecimal=false)

#################################################
# Database Setup
#################################################

#Insert Engines
asset_connection_string = "postgres:2021AirushLift8M@localhost:5432/Apple" 
apple_engine = create_engine(f'postgresql://{asset_connection_string}')


# reflect an existing database into a new model - convert to python classes
Base_apple = automap_base()


# reflect the tables
Base_apple.prepare(apple_engine, reflect=True)


#Apple Tables

apple_macd_data = Base_apple.classes.apple_macd_data
apple_macd_results = Base_apple.classes.apple_macd_results



#apple_macd_data.Close

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

### APPLE ### 

#APP --> Apple MACD Data -------------------------------------------------------------------------------->

@app.route("/api/first_macd_data") 
def query_apple_macd_data(): 

    session = Session(apple_engine)

    #Query macd data
    apple_macd_data_final = session.query(apple_macd_data.Date, apple_macd_data.Close, apple_macd_data.Volume, apple_macd_data.Hist).all()

    session.close()

    apple_macd_table1 = []
    for Date, Close, Volume, Hist in apple_macd_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["Volume"] = float(Volume)
        table_data["Hist"] = float(Hist)
        apple_macd_table1.append(table_data)

    return jsonify(apple_macd_table1)

#APP --> Apple MACD Results -------------------------------------------------------------------------------->


@app.route("/") 
def query_apple_macd_results():
    return render_template("index.html")  # flask will look for a file called index.html under the templates folder
    
    # Query macd data
##apple_macd_results_final = session.query(apple_macd_results.Date, apple_macd_results.Close, apple_macd_results.Hist, apple_macd_results.Buy, apple_macd_results.Sell, apple_macd_results.capital, apple_macd_results.shares).all()

#session.close()

#apple_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in apple_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["Hist"] = float(Hist)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        apple_macd_table2.append(table_data)

##return jsonify(apple_macd_table2)


if __name__ == '__main__':
    app.run()
