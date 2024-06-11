class ToDo {
  String? id;
  String? todoText;
  bool isDone;

  ToDo({
    required this.id,
    required this.todoText,
    this.isDone = false,
  });

  factory ToDo.fromJson(Map<String, dynamic> json) {
    return ToDo(
      id: json["id"].toString(),
      todoText: json["Name"],
      isDone: json["done"] == 1 ? true : false,
    );
  }

  static List<ToDo> todoList() {
    return [
      ToDo(id: '01', todoText: 'Learn Flutter', isDone: true),
      ToDo(id: '02', todoText: 'Learn Dart', isDone: false),
      ToDo(id: '03', todoText: 'Learn Java', isDone: false),
      ToDo(id: '04', todoText: 'Learn Kotlin', isDone: false),
      ToDo(id: '05', todoText: 'Learn Swift', isDone: false),
    ];
  }
}
