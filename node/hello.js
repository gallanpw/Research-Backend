var http = require('http');

http.createServer(function (req, res) {
  res.write('Hello NodeJS\n');
  for(var i=0;i<10000;i++){
	  var number = Math.floor(Math.random() * 1000); 
	  res.write(`Your Number : ${number}\n`);
  }
  res.end();
}).listen(8080); 