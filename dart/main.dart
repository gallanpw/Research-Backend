import 'dart:io';
import 'dart:async';
import 'dart:math';

Future main() async {
  var server = await HttpServer.bind(
    InternetAddress.loopbackIPv4,
    4040,
  );
  print('Listening on localhost:${server.port}');

  await for (HttpRequest request in server) {
  
	request.response.write("Hello Dart\n");
	for(var i=0;i<10000;i++){
		var number = new Random().nextInt(1000);
		request.response.write("Your Number : ${number}\n");
	}
	request.response.close();
  }
}