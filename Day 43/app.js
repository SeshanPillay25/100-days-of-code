fetch(
  "https://api.nasa.gov/neo/rest/v1/feed?start_date=2019-10-16&end_date=2019-10-23&api_key=ENTER_YOUR_API_KEY_HERE"
)
  .then(function(response) {
    console.log(response);
  })
  .catch(function(response) {
    console.log("Error! Please try again");
  });
