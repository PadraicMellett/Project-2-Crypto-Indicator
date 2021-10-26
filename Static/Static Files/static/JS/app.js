//APPLE DATA

//#APP --> Apple MACD Results -------------------------------------------------------------------------------->

d3.json("/api/second_macd_data_apple").then(function (apple_second_macd_data) {
  console.log(apple_second_macd_data);
  d3.select(".apple_macd_results").select("tbody")
    .selectAll("tr")
    .data(apple_second_macd_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
    });

})

//#APP --> Apple RSI Results -------------------------------------------------------------------------------->

d3.json("/api/second_rsi_data_apple").then(function (apple_second_rsi_data) {
  console.log(apple_second_rsi_data);
  d3.select(".apple_rsi_results").select("tbody")
    .selectAll("tr")
    .data(apple_second_rsi_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
    });
})

//#APP --> Apple Stoch Results -------------------------------------------------------------------------------->

d3.json("/api/second_stoch_data_apple").then(function (apple_second_stoch_data) {
  console.log(apple_second_stoch_data);
  d3.select(".apple_stoch_results").select("tbody")
    .selectAll("tr")
    .data(apple_second_stoch_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.SlowK}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
    });
})

//### GOOGLE ### 

//#APP --> Google MACD Results -------------------------------------------------------------------------------->

d3.json("/api/second_macd_data_google").then(function (google_second_macd_data) {
  console.log(google_second_macd_data);
  d3.select(".google_macd_results").select("tbody")
    .selectAll("tr")
    .data(google_second_macd_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
    });
})

//#APP --> Google RSI Results -------------------------------------------------------------------------------->


d3.json("/api/second_rsi_data_google").then(function (google_second_rsi_data) {
  console.log(google_second_rsi_data);
  d3.select(".google_rsi_results").select("tbody")
    .selectAll("tr")
    .data(google_second_rsi_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
    });
})


//#APP --> Google Stoch Results -------------------------------------------------------------------------------->

d3.json("/api/second_stoch_data_google").then(function (google_second_stoch_data) {
  console.log(google_second_stoch_data);
  d3.select(".google_stoch_results").select("tbody")
    .selectAll("tr")
    .data(google_second_stoch_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.SlowK}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
    });
})

// ### TESLA ### 


//#APP --> Tesla MACD Results -------------------------------------------------------------------------------->


d3.json("/api/second_macd_data_tesla").then(function (tesla_second_macd_data) {
  console.log(tesla_second_macd_data);
  d3.select(".tesla_macd_results").select("tbody")
    .selectAll("tr")
    .data(tesla_second_macd_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.Hist}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td>`;
    });
})

//#APP --> Tesla RSI Results -------------------------------------------------------------------------------->


d3.json("/api/second_rsi_data_tesla").then(function (tesla_second_rsi_data) {
  console.log(tesla_second_rsi_data);
  d3.select(".tesla_rsi_results").select("tbody")
    .selectAll("tr")
    .data(tesla_second_rsi_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.RSI}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td></td><td>${d.shares}</td>`;
    });
})

//#APP --> Tesla Stoch Results -------------------------------------------------------------------------------->

d3.json("/api/second_stoch_data_tesla").then(function (tesla_second_stoch_data) {
  console.log(tesla_second_stoch_data);
  d3.select(".tesla_stoch_results").select("tbody")
    .selectAll("tr")
    .data(tesla_second_stoch_data)
    .enter()
    .append("tr")
    .html(function (d) {
      return `<td>${d.Date}</td><td>${d.Close}</td><td>${d.SlowK}</td><td>${d.Buy}</td></td><td>${d.Sell}</td></td><td>${d.capital}</td><td>${d.shares}</td></td>`;
    });
})