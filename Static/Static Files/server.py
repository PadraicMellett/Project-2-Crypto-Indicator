import datetime as dt
import numpy as np
import pandas as pd
from flask import render_template

import sqlalchemy
from sqlalchemy import sql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
from sqlalchemy.sql.expression import false

sqlalchemy.types.Numeric(asdecimal=false)

#################################################
# Database Setup
#################################################

#Insert Engines
asset_connection_string = "postgres:dataprojects123@localhost:5432/Apple" 
apple_engine = create_engine(f'postgresql://{asset_connection_string}')

asset_connection_string = "postgres:dataprojects123@localhost:5432/Google" 
google_engine = create_engine(f'postgresql://{asset_connection_string}')

asset_connection_string = "postgres:dataprojects123@localhost:5432/Tesla" 
tesla_engine = create_engine(f'postgresql://{asset_connection_string}')

# reflect an existing database into a new model - convert to python classes
Base_apple = automap_base()
Base_google = automap_base()
Base_tesla = automap_base()

# reflect the tables
Base_apple.prepare(apple_engine, reflect=True)

Base_google.prepare(google_engine, reflect=True)

Base_tesla.prepare(tesla_engine, reflect=True)

#Apple Tables

apple_macd_results = Base_apple.classes.apple_macd_results

apple_rsi_results = Base_apple.classes.apple_rsi_results

apple_stoch_results = Base_apple.classes.apple_stoch_results

#Google Tables

google_macd_results = Base_google.classes.google_macd_results

google_rsi_results = Base_google.classes.google_rsi_results

google_stoch_results = Base_google.classes.google_stoch_results

#Tesla Tables

tesla_macd_results = Base_tesla.classes.tesla_macd_results

tesla_rsi_results = Base_tesla.classes.tesla_rsi_results

tesla_stoch_results = Base_tesla.classes.tesla_stoch_results

#apple_macd_data.Close

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

### APPLE ### 

@app.route("/") 
def homepage():
    return render_template("index.html") 

#APP --> Apple MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data_apple") 
def query_apple_macd_results():

    session = Session(apple_engine)
    
    # Query macd data
    apple_macd_results_final = session.query(apple_macd_results.Date, apple_macd_results.Close, apple_macd_results.Hist, apple_macd_results.Buy, apple_macd_results.Sell, apple_macd_results.capital, apple_macd_results.shares).all()

    session.close()

    apple_macd_table2 = []
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

    return jsonify(apple_macd_table2)


#APP --> Apple RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data_apple") 
def query_apple_rsi_results():

    session = Session(apple_engine)
    
    # Query rsi data
    apple_rsi_results_final = session.query(apple_rsi_results.Date, apple_rsi_results.Close, apple_rsi_results.RSI, apple_rsi_results.Buy, apple_rsi_results.Sell, apple_rsi_results.capital, apple_rsi_results.shares).all()

    session.close()

    apple_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in apple_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["RSI"] = float(RSI)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        apple_rsi_table2.append(table_data)

    return jsonify(apple_rsi_table2)


#APP --> Apple Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data_apple") 
def query_apple_stoch_results():

    session = Session(apple_engine)
    
    # Query stoch data
    apple_stoch_results_final = session.query(apple_stoch_results.Date, apple_stoch_results.Close, apple_stoch_results.SlowK, apple_stoch_results.Buy, apple_stoch_results.Sell, apple_stoch_results.capital, apple_stoch_results.shares).all()

    session.close()

    apple_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in apple_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["SlowK"] = float(SlowK)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        apple_stoch_table2.append(table_data)

    return jsonify(apple_stoch_table2)


### GOOGLE ### 

#APP --> Google MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data_google") 
def query_google_macd_results():

    session = Session(google_engine)
    
    # Query macd data
    google_macd_results_final = session.query(google_macd_results.Date, google_macd_results.Close, google_macd_results.Hist, google_macd_results.Buy, google_macd_results.Sell, google_macd_results.capital, google_macd_results.shares).all()

    session.close()

    google_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in google_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["Hist"] = float(Hist)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        google_macd_table2.append(table_data)

    return jsonify(google_macd_table2)

#APP --> Google RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data_google") 
def query_google_rsi_results():

    session = Session(google_engine)
    
    # Query rsi data
    google_rsi_results_final = session.query(google_rsi_results.Date, google_rsi_results.Close, google_rsi_results.RSI, google_rsi_results.Buy, google_rsi_results.Sell, google_rsi_results.capital, google_rsi_results.shares).all()

    session.close()

    google_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in google_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["RSI"] = float(RSI)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        google_rsi_table2.append(table_data)

    return jsonify(google_rsi_table2)

#APP --> Google Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data_google") 
def query_google_stoch_results():

    session = Session(google_engine)
    
    # Query stoch data
    google_stoch_results_final = session.query(google_stoch_results.Date, google_stoch_results.Close, google_stoch_results.SlowK, google_stoch_results.Buy, google_stoch_results.Sell, google_stoch_results.capital, google_stoch_results.shares).all()

    session.close()

    google_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in google_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["SlowK"] = float(SlowK)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        google_stoch_table2.append(table_data)

    return jsonify(google_stoch_table2)


### TESLA ### 

#APP --> Tesla MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data_tesla") 
def query_tesla_macd_results():

    session = Session(tesla_engine)
    
    # Query macd data
    tesla_macd_results_final = session.query(tesla_macd_results.Date, tesla_macd_results.Close, tesla_macd_results.Hist, tesla_macd_results.Buy, tesla_macd_results.Sell, tesla_macd_results.capital, tesla_macd_results.shares).all()

    session.close()

    tesla_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in tesla_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["Hist"] = float(Hist)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        tesla_macd_table2.append(table_data)

    return jsonify(tesla_macd_table2)

#APP --> Tesla RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data_tesla") 
def query_tesla_rsi_results():

    session = Session(tesla_engine)
    
    # Query rsi data
    tesla_rsi_results_final = session.query(tesla_rsi_results.Date, tesla_rsi_results.Close, tesla_rsi_results.RSI, tesla_rsi_results.Buy, tesla_rsi_results.Sell, tesla_rsi_results.capital, tesla_rsi_results.shares).all()

    session.close()

    tesla_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in tesla_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["RSI"] = float(RSI)
        table_data["Buy"] = Buy
        table_data["Sell"] = float(Sell)
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        tesla_rsi_table2.append(table_data)

    return jsonify(tesla_rsi_table2)

#APP --> Tesla Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data_tesla") 
def query_tesla_stoch_results():

    session = Session(tesla_engine)
    
    # Query stoch data
    tesla_stoch_results_final = session.query(tesla_stoch_results.Date, tesla_stoch_results.Close, tesla_stoch_results.SlowK, tesla_stoch_results.Buy, tesla_stoch_results.Sell, tesla_stoch_results.capital, tesla_stoch_results.shares).all()

    session.close()

    tesla_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in tesla_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = float(Close)
        table_data["SlowK"] = float(SlowK)
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = float(capital)
        table_data["shares"] = float(shares)
        tesla_stoch_table2.append(table_data)

    return jsonify(tesla_stoch_table2)

if __name__ == '__main__':
    app.run()
