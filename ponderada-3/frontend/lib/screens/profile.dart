import 'package:flutter/material.dart';
import 'package:flutter_application_1/api/image_process.dart';
import 'package:image_picker/image_picker.dart';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'dart:typed_data';

class ProfilePage extends StatefulWidget {
  ProfilePage({super.key});

  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  File? _image;
  Uint8List? _uploadedImageBytes;
  bool processing = false;
  bool uploaded = false;
  Future<void> _pickImage(ImageSource source) async {
    final picker = ImagePicker();
    final pickedFile = await picker.pickImage(source: source);

    if (pickedFile != null) {
      setState(() {
        _image = File(pickedFile.path);
        processing = true;
      });
    }
  }

  Future<void> _uploadImage(BuildContext context) async {
    if (_image != null) {
      uploaded = true;
      Uint8List? responseBytes = await uploadImage(context, _image!);
      if (responseBytes != null) {
        setState(() {
          _uploadedImageBytes = responseBytes;
          processing = false;
          uploaded = false;
        });
      }
    } else {
      processing = false;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Por favor, selecione uma imagem primeiro.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Profile Page'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            _image == null
                ? Text('Nenhuma imagem selecionada.')
                : Image.file(_image!, height: 200),
              if (processing && uploaded)
              const CircularProgressIndicator(),
            SizedBox(height: 20),
            _uploadedImageBytes == null
                ? Text('Nenhuma imagem enviada.')
                : Image.memory(_uploadedImageBytes!, height: 200),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _pickImage(ImageSource.gallery),
              child: Text('Escolher imagem da galeria'),
            ),
            SizedBox(height: 10),
            ElevatedButton(
              onPressed: () => _pickImage(ImageSource.camera),
              child: Text('Tirar uma foto'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => _uploadImage(context),
              child: Text('Enviar imagem'),
            ),
          ],
        ),
      ),
    );
  }
}