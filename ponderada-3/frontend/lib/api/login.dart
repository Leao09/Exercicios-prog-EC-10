import 'dart:convert';
import 'package:http/http.dart' as http;
import '../globals.dart' as globals;

var baseurl = globals.loginURL;

Future<bool> login(String email, String password) async {
  final Map<String, String> data = {
    "Email": email,
    "password": password,
  };

  final jsonData = jsonEncode(data);

  var response = await http.post(Uri.parse("$baseurl/login"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonData);

  if (response.statusCode == 200) {
    final body = jsonDecode(response.body);
    _storeAccessToken(body["acess_token"]);
    return true;
  } else {
    return false;
  }
}

Future<bool> signUp(String email, String password) async {
  final Map<String, String> data = {"Email": email, "password": password};

  var response = await http.post(Uri.parse("$baseurl/signup"),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: jsonEncode(data));

  if (response.statusCode == 200) {
    return true;
  } else {
    return false;
  }
}

void _storeAccessToken(String token) async {
  globals.accessToken = token;
}
