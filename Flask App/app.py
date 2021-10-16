import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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

apple_macd_data = Base_apple.classes.apple_macd_data
apple_macd_results = Base_apple.classes.apple_macd_results

apple_rsi_data = Base_apple.classes.apple_rsi_data
apple_rsi_results = Base_apple.classes.apple_rsi_results

apple_stoch_data = Base_apple.classes.apple_stoch_data
apple_stoch_results = Base_apple.classes.apple_stoch_results

#Google Tables

google_macd_data = Base_google.classes.google_macd_data
google_macd_results = Base_google.classes.google_macd_results

google_rsi_data = Base_google.classes.google_rsi_data
google_rsi_results = Base_google.classes.google_rsi_results

google_stoch_data = Base_google.classes.google_stoch_data
google_stoch_results = Base_google.classes.google_stoch_results

#Tesla Tables

tesla_macd_data = Base_tesla.classes.tesla_macd_data
tesla_macd_results = Base_tesla.classes.tesla_macd_results

tesla_rsi_data = Base_tesla.classes.tesla_rsi_data
tesla_rsi_results = Base_tesla.classes.tesla_rsi_results

tesla_stoch_data = Base_tesla.classes.tesla_stoch_data
tesla_stoch_results = Base_tesla.classes.tesla_stoch_results

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

### APPLE ### 

#APP --> Apple MACD Data -------------------------------------------------------------------------------->

@app.route("/api/first_macd_data") 
def apple_macd_data():

    session = Session(apple_engine)
    
    # Query macd data
    apple_macd_data_final = session.query(apple_macd_data.Date, apple_macd_data.Close, apple_macd_data.Volume, apple_macd_data.Hist).all()

    session.close()

    apple_macd_table1 = []
    for Date, Close, Volume, Hist in apple_macd_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["Hist"] = Hist
        apple_macd_table1.append(table_data)

    return jsonify(apple_macd_table1)

#APP --> Apple MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data") 
def apple_macd_results():

    session = Session(apple_engine)
    
    # Query macd data
    apple_macd_results_final = session.query(apple_macd_results.Date, apple_macd_results.Close, apple_macd_results.Hist, apple_macd_results.Buy, apple_macd_results.Sell, apple_macd_results.capital, apple_macd_results.shares).all()

    session.close()

    apple_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in apple_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Hist"] = Hist
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        apple_macd_table2.append(table_data)

    return jsonify(apple_macd_table2)

#APP --> Apple RSI Data -------------------------------------------------------------------------------->

@app.route("/api/first_rsi_data") 
def apple_rsi_data():

    session = Session(apple_engine)
    
    # Query rsi data
    apple_rsi_data_final = session.query(apple_rsi_data.Date, apple_rsi_data.Close, apple_rsi_data.Volume, apple_rsi_data.RSI).all()

    session.close()

    apple_rsi_table1 = []
    for Date, Close, Volume, RSI in apple_rsi_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["RSI"] = RSI
        apple_rsi_table1.append(table_data)

    return jsonify(apple_rsi_table1)

#APP --> Apple RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data") 
def apple_rsi_results():

    session = Session(apple_engine)
    
    # Query rsi data
    apple_rsi_results_final = session.query(apple_rsi_results.Date, apple_rsi_results.Close, apple_rsi_results.RSI, apple_rsi_results.Buy, apple_rsi_results.Sell, apple_rsi_results.capital, apple_rsi_results.shares).all()

    session.close()

    apple_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in apple_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["RSI"] = RSI
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        apple_rsi_table2.append(table_data)

    return jsonify(apple_rsi_table2)

#APP --> Apple Stoch Data -------------------------------------------------------------------------------->

@app.route("/api/first_stoch_data") 
def apple_stoch_data():

    session = Session(apple_engine)
    
    # Query stoch data
    apple_stoch_data_final = session.query(apple_stoch_data.Date, apple_stoch_data.Close, apple_stoch_data.Volume, apple_stoch_data.SlowK, apple_stoch_data.SlowD).all()

    session.close()

    apple_stoch_table1 = []
    for Date, Close, Volume, SlowK, SlowD in apple_stoch_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["SlowK"] = SlowK
        table_data["SlowD"] = SlowD
        apple_stoch_table1.append(table_data)

    return jsonify(apple_stoch_table1)

#APP --> Apple Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data") 
def apple_stoch_results():

    session = Session(apple_engine)
    
    # Query stoch data
    apple_stoch_results_final = session.query(apple_stoch_results.Date, apple_stoch_results.Close, apple_stoch_results.SlowK, apple_stoch_results.Buy, apple_stoch_results.Sell, apple_stoch_results.capital, apple_stoch_results.shares).all()

    session.close()

    apple_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in apple_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["SlowK"] = SlowK
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        apple_stoch_table2.append(table_data)

    return jsonify(apple_stoch_table2)


### GOOGLE ### 


#APP --> Google MACD Data -------------------------------------------------------------------------------->

@app.route("/api/first_macd_data") 
def google_macd_data():

    session = Session(google_engine)
    
    # Query macd data
    google_macd_data_final = session.query(google_macd_data.Date, google_macd_data.Close, google_macd_data.Volume, google_macd_data.Hist).all()

    session.close()

    google_macd_table1 = []
    for Date, Close, Volume, Hist in google_macd_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["Hist"] = Hist
        google_macd_table1.append(table_data)

    return jsonify(google_macd_table1)

#APP --> Google MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data") 
def google_macd_results():

    session = Session(google_engine)
    
    # Query macd data
    google_macd_results_final = session.query(google_macd_results.Date, google_macd_results.Close, google_macd_results.Hist, google_macd_results.Buy, google_macd_results.Sell, google_macd_results.capital, google_macd_results.shares).all()

    session.close()

    google_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in google_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Hist"] = Hist
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        google_macd_table2.append(table_data)

    return jsonify(google_macd_table2)

#APP --> Google RSI Data -------------------------------------------------------------------------------->

@app.route("/api/first_rsi_data") 
def google_rsi_data():

    session = Session(google_engine)
    
    # Query rsi data
    google_rsi_data_final = session.query(google_rsi_data.Date, google_rsi_data.Close, google_rsi_data.Volume, google_rsi_data.RSI).all()

    session.close()

    google_rsi_table1 = []
    for Date, Close, Volume, RSI in google_rsi_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["RSI"] = RSI
        google_rsi_table1.append(table_data)

    return jsonify(google_rsi_table1)

#APP --> Google RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data") 
def google_rsi_results():

    session = Session(google_engine)
    
    # Query rsi data
    google_rsi_results_final = session.query(google_rsi_results.Date, google_rsi_results.Close, google_rsi_results.RSI, google_rsi_results.Buy, google_rsi_results.Sell, google_rsi_results.capital, google_rsi_results.shares).all()

    session.close()

    google_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in google_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["RSI"] = RSI
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        google_rsi_table2.append(table_data)

    return jsonify(google_rsi_table2)

#APP --> Google Stoch Data -------------------------------------------------------------------------------->

@app.route("/api/first_stoch_data") 
def google_stoch_data():

    session = Session(google_engine)
    
    # Query stoch data
    google_stoch_data_final = session.query(google_stoch_data.Date, google_stoch_data.Close, google_stoch_data.Volume, google_stoch_data.SlowK, google_stoch_data.SlowD).all()

    session.close()

    google_stoch_table1 = []
    for Date, Close, Volume, SlowK, SlowD in google_stoch_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["SlowK"] = SlowK
        table_data["SlowD"] = SlowD
        google_stoch_table1.append(table_data)

    return jsonify(google_stoch_table1)

#APP --> Google Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data") 
def google_stoch_results():

    session = Session(google_engine)
    
    # Query stoch data
    google_stoch_results_final = session.query(google_stoch_results.Date, google_stoch_results.Close, google_stoch_results.SlowK, google_stoch_results.Buy, google_stoch_results.Sell, google_stoch_results.capital, google_stoch_results.shares).all()

    session.close()

    google_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in google_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["SlowK"] = SlowK
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        google_stoch_table2.append(table_data)

    return jsonify(google_stoch_table2)


### TESLA ### 


#APP --> Tesla MACD Data -------------------------------------------------------------------------------->

@app.route("/api/first_macd_data") 
def tesla_macd_data():

    session = Session(tesla_engine)
    
    # Query macd data
    tesla_macd_data_final = session.query(tesla_macd_data.Date, tesla_macd_data.Close, tesla_macd_data.Volume, tesla_macd_data.Hist).all()

    session.close()

    tesla_macd_table1 = []
    for Date, Close, Volume, Hist in tesla_macd_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["Hist"] = Hist
        tesla_macd_table1.append(table_data)

    return jsonify(tesla_macd_table1)

#APP --> Tesla MACD Results -------------------------------------------------------------------------------->

@app.route("/api/second_macd_data") 
def tesla_macd_results():

    session = Session(tesla_engine)
    
    # Query macd data
    tesla_macd_results_final = session.query(tesla_macd_results.Date, tesla_macd_results.Close, tesla_macd_results.Hist, tesla_macd_results.Buy, tesla_macd_results.Sell, tesla_macd_results.capital, tesla_macd_results.shares).all()

    session.close()

    tesla_macd_table2 = []
    for Date, Close, Hist, Buy, Sell, capital, shares in tesla_macd_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Hist"] = Hist
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        tesla_macd_table2.append(table_data)

    return jsonify(tesla_macd_table2)

#APP --> Tesla RSI Data -------------------------------------------------------------------------------->

@app.route("/api/first_rsi_data") 
def tesla_rsi_data():

    session = Session(tesla_engine)
    
    # Query rsi data
    tesla_rsi_data_final = session.query(tesla_rsi_data.Date, tesla_rsi_data.Close, tesla_rsi_data.Volume, tesla_rsi_data.RSI).all()

    session.close()

    tesla_rsi_table1 = []
    for Date, Close, Volume, RSI in tesla_rsi_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["RSI"] = RSI
        tesla_rsi_table1.append(table_data)

    return jsonify(tesla_rsi_table1)

#APP --> Tesla RSI Results -------------------------------------------------------------------------------->

@app.route("/api/second_rsi_data") 
def tesla_rsi_results():

    session = Session(tesla_engine)
    
    # Query rsi data
    tesla_rsi_results_final = session.query(tesla_rsi_results.Date, tesla_rsi_results.Close, tesla_rsi_results.RSI, tesla_rsi_results.Buy, tesla_rsi_results.Sell, tesla_rsi_results.capital, tesla_rsi_results.shares).all()

    session.close()

    tesla_rsi_table2 = []
    for Date, Close, RSI, Buy, Sell, capital, shares in tesla_rsi_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["RSI"] = RSI
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        tesla_rsi_table2.append(table_data)

    return jsonify(tesla_rsi_table2)

#APP --> Tesla Stoch Data -------------------------------------------------------------------------------->

@app.route("/api/first_stoch_data") 
def tesla_stoch_data():

    session = Session(tesla_engine)
    
    # Query stoch data
    tesla_stoch_data_final = session.query(tesla_stoch_data.Date, tesla_stoch_data.Close, tesla_stoch_data.Volume, tesla_stoch_data.SlowK, tesla_stoch_data.SlowD).all()

    session.close()

    tesla_stoch_table1 = []
    for Date, Close, Volume, SlowK, SlowD in tesla_stoch_data_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["Volume"] = Volume
        table_data["SlowK"] = SlowK
        table_data["SlowD"] = SlowD
        tesla_stoch_table1.append(table_data)

    return jsonify(tesla_stoch_table1)

#APP --> Tesla Stoch Results -------------------------------------------------------------------------------->

@app.route("/api/second_stoch_data") 
def tesla_stoch_results():

    session = Session(tesla_engine)
    
    # Query stoch data
    tesla_stoch_results_final = session.query(tesla_stoch_results.Date, tesla_stoch_results.Close, tesla_stoch_results.SlowK, tesla_stoch_results.Buy, tesla_stoch_results.Sell, tesla_stoch_results.capital, tesla_stoch_results.shares).all()

    session.close()

    tesla_stoch_table2 = []
    for Date, Close, SlowK, Buy, Sell, capital, shares in tesla_stoch_results_final:
        table_data = {}
        table_data["Date"] = Date
        table_data["Close"] = Close
        table_data["SlowK"] = SlowK
        table_data["Buy"] = Buy
        table_data["Sell"] = Sell
        table_data["capital"] = capital
        table_data["shares"] = shares
        tesla_stoch_table2.append(table_data)

    return jsonify(tesla_stoch_table2)

if __name__ == '__main__':
    app.run()
