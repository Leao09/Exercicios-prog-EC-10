import "dart:convert";
import "package:flutter_application_1/model/todo.dart";

import "../globals.dart" as globals;
import "package:http/http.dart" as http;

var baseurl = globals.taskURL;

Future<List<ToDo>> getTask() async {
  final response = await http.get(
    Uri.parse("$baseurl/task"),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer ${globals.accessToken}',
    },
  );
  if (response.statusCode == 200) {
    final List<dynamic> data = json.decode(response.body);
    return data.map((d) => ToDo.fromJson(d)).toList();
  } else {
    return ToDo.todoList();
  }
}

Future<bool> addTask(String content) async {
  final response = await http.post(Uri.parse("$baseurl/task"),
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer ${globals.accessToken}',
      },
      body: jsonEncode(<String, dynamic>{
        "Name": content,
      }));
  if (response.statusCode == 200) {
    return true;
  } else {
    return false;
  }
}

Future<bool> removeTask(int id) async {
  final response = await http.delete(
    Uri.parse("$baseurl/task/$id"),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer ${globals.accessToken}',
    },
  );

  if (response.statusCode == 200) {
    return true;
  } else {
    return false;
  }
}

Future<bool> taskDone(int id, bool isDone) async {
  final response = await http.put(
    Uri.parse("$baseurl/task/$id"),
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json',
      'Authorization': 'Bearer ${globals.accessToken}',
    },
    body: jsonEncode({'isDone': !isDone}),
  );
  print(response.body);
  if (response.statusCode == 200) {
    return true;
  } else {
    return false;
  }
}
