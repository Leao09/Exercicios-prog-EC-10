import "dart:convert";
import "dart:developer";
import "dart:io";
import "dart:typed_data";

import "package:flutter/material.dart";
import "notification.dart" as notification;
import "../globals.dart" as globals;
import "package:http/http.dart" as http;

var baseurl = globals.imageURL;


Future<http.Response> sendImage(File imageFile) async {
    final url = Uri.parse('$baseurl/images');
    final request = http.MultipartRequest('POST', url);
    request.files.add(await http.MultipartFile.fromPath('image', imageFile.path));

    final response = await request.send();
    return await http.Response.fromStream(response);
  }

Future<Uint8List?> uploadImage(BuildContext context, File filePath) async {
    try {
      final response = await sendImage(filePath);
      if (response.statusCode == 200) {
        notification.notifyImageProcessed();
        return response.bodyBytes;  // Assumindo que a resposta contém os bytes da imagem processada
      } else {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Falha ao processar imagem')),
        );
        return null;
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Erro: $e')),
      );
      return null;
    }
  }