const pdf = require('html-pdf');
const request = require('request');

// Make a GET request to the web page you want to generate a PDF for
request('http://127.0.0.1:8000/view/', function (error, response, body) {
  if (!error && response.statusCode === 200) {
    // Use html-pdf to generate a PDF from the response body
    pdf.create(body).toFile('./example.pdf', function(err, res) {
      if (err) return console.log(err);
      console.log(res); // { filename: './example.pdf' }
    });
  }
});