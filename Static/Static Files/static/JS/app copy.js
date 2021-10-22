//APPLE DATA

//#APP --> Apple MACD Data -------------------------------------------------------------------------------->

function buildTable (apple_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.Hist}</td>`;
    
  });

}

d3.json("/api/first_macd_data_apple").then(function(apple_macd_data) 
{console.log(apple_macd_data); 
buildTable (apple_macd_data);
})


// function buildPlot() {

//     var Date = data.dataset.Date;
//     var Close = data.dataset.Close;
//     // var Hist = data.dataset.Hist;
//     // var Volume = data.dataset.Volume;


//     var trace1 = {
//       type: "scatter",
//       mode: "lines",
//       name: n,
//       x: Date,
//       y: Close,
//       line: {
//         color: "#17BECF"
//       }
//     };

//     var data = [trace1];

//     var layout = {
//       title: `${stock} closing prices`,
//       xaxis: {
//         range: [startDate, endDate],
//         type: "date"
//       },
//       yaxis: {
//         autorange: true,
//         type: "linear"
//       }
//     };

//     Plotly.newPlot("plot", data, layout);

//   };


// buildPlot();

// BUILD 2nd APPLE MACD TABLE
//#APP --> Apple MACD Results -------------------------------------------------------------------------------->
function buildTable (apple_second_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_second_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_macd_data_apple").then(function(apple_second_macd_data) 
{console.log(apple_second_macd_data); 
buildTable (apple_second_macd_data);
})


//BUILD first APPLE RSI DATA
//#APP --> Apple RSI Data -------------------------------------------------------------------------------->


function buildTable (apple_first_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_first_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.RSI}</td>`;
  });

}

d3.json("/api/first_rsi_data_apple").then(function(apple_first_rsi_data) 
{console.log(apple_first_rsi_data); 
buildTable (apple_first_rsi_data);
})

//BUILD second_APPLE_RSI-DATA
//#APP --> Apple RSI Results -------------------------------------------------------------------------------->

function buildTable (apple_second_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_second_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_rsi_data_apple").then(function(apple_second_rsi_data) 
{console.log(apple_second_rsi_data); 
buildTable (apple_second_rsi_data);
})

//#APP --> Apple Stoch Data-------------------------------------------------------------------------------->


function buildTable (apple_first_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_first_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.SlowK}</td><td>${d.SlowD}</td>`;
  });

}

d3.json("/api/first_stoch_data_apple").then(function(apple_first_stoch_data) 
{console.log(apple_first_stoch_data); 
buildTable (apple_first_stoch_data);
})

//#APP --> Apple Stoch Results -------------------------------------------------------------------------------->

function buildTable (apple_second_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(apple_second_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Slowk}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
  });

}

d3.json("/api/second_stoch_data_apple").then(function(apple_second_stoch_data) 
{console.log(apple_second_stoch_data); 
buildTable (apple_second_stoch_data);
})

//### GOOGLE ### 


//#APP --> Google MACD Data -------------------------------------------------------------------------------->

function buildTable (google_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.Hist}</td>`;
    
  });

}

d3.json("/api/first_macd_data_google").then(function(google_macd_data) 
{console.log(google_macd_data); 
buildTable (google_macd_data);
})


// BUILD 2nd GOOGLE MACD TABLE
//#APP --> Google MACD Results -------------------------------------------------------------------------------->
function buildTable (google_second_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_second_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_macd_data_google").then(function(google_second_macd_data) 
{console.log(google_second_macd_data); 
buildTable (google_second_macd_data);
})


//BUILD first GOOGLE RSI DATA
//#APP --> GOOGLE RSI Data -------------------------------------------------------------------------------->


function buildTable (google_first_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_first_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.RSI}</td>`;
  });

}

d3.json("/api/first_rsi_data_google").then(function(google_first_rsi_data) 
{console.log(google_first_rsi_data); 
buildTable (google_first_rsi_data);
})


//#APP --> Google RSI Results -------------------------------------------------------------------------------->

function buildTable (google_second_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_second_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_rsi_data_google").then(function(google_second_rsi_data) 
{console.log(google_second_rsi_data); 
buildTable (google_second_rsi_data);
})

//#APP --> Google Stoch Data-------------------------------------------------------------------------------->


function buildTable (google_first_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_first_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.SlowK}</td><td>${d.SlowD}</td>`;
  });

}

d3.json("/api/first_stoch_data").then(function(google_first_stoch_data) 
{console.log(google_first_stoch_data); 
buildTable (google_first_stoch_data);
})

//#APP --> Google Stoch Results -------------------------------------------------------------------------------->

function buildTable (google_second_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(google_second_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Slowk}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
  });

}

d3.json("/api/second_stoch_data_google").then(function(google_second_stoch_data) 
{console.log(google_second_stoch_data); 
buildTable (google_second_stoch_data);
})

// ### TESLA ### 

// #APP --> Tesla MACD Data -------------------------------------------------------------------------------->



function buildTable (tesla_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.Hist}</td>`;
    
  });

}

d3.json("/api/first_macd_data_tesla").then(function(tesla_macd_data) 
{console.log(tesla_macd_data); 
buildTable (tesla_macd_data);
})



//#APP --> Tesla MACD Results -------------------------------------------------------------------------------->
function buildTable (tesla_second_macd_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_second_macd_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_macd_data_tesla").then(function(tesla_second_macd_data) 
{console.log(tesla_second_macd_data); 
buildTable (tesla_second_macd_data);
})


//BUILD first TESLA RSI DATA
//#APP --> TESLA RSI Data -------------------------------------------------------------------------------->


function buildTable (tesla_first_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_first_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.RSI}</td>`;
  });

}

d3.json("/api/first_macd_data_tesla").then(function(tesla_first_rsi_data) 
{console.log(tesla_first_rsi_data); 
buildTable (tesla_first_rsi_data);
})


//#APP --> Google RSI Results -------------------------------------------------------------------------------->

function buildTable (tesla_second_rsi_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_second_rsi_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
  });

}

d3.json("/api/second_rsi_data_tesla").then(function(tesla_second_rsi_data) 
{console.log(tesla_second_rsi_data); 
buildTable (tesla_second_rsi_data);
})

//#APP --> Tesla Stoch Data-------------------------------------------------------------------------------->


function buildTable (tesla_first_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_first_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Volume}</td><td>${d.SlowK}</td><td>${d.SlowD}</td>`;
  });

}

d3.json("/api/first_stoch_data_tesla").then(function(tesla_first_stoch_data) 
{console.log(tesla_first_stoch_data); 
buildTable (tesla_first_stoch_data);
})

//#APP --> Tesla Stoch Results -------------------------------------------------------------------------------->

function buildTable (tesla_second_stoch_data) {


  d3.select("tbody")
  .selectAll("tr")
  .data(tesla_second_stoch_data)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Slowk}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
  });

}

d3.json("/api/second_stoch_data_tesla").then(function(tesla_second_stoch_data) 
{console.log(tesla_second_stoch_data); 
buildTable (tesla_second_stoch_data);
})