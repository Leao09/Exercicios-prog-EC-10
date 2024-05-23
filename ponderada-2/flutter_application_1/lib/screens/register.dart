import 'package:flutter/material.dart';
import 'package:flutter_application_1/api/login.dart';
import 'package:flutter_application_1/widgets/button.dart';
import 'package:flutter_application_1/widgets/text_field.dart';

class RegisterPage extends StatelessWidget {
  RegisterPage({super.key});

  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  void signUserUp(context,String email, String password) async {
    if (await signUp(email, password)) {
      Navigator.pushNamed(context, '/login');
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Falha no registro!'),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.grey[300],
        body: SafeArea(
            child: Center(
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
            const SizedBox(height: 50),
            const Icon(
              Icons.app_registration,
              size: 100,
            ),
            const SizedBox(height: 50),
            Padding(
                padding: EdgeInsets.symmetric(horizontal: 25.0),
                child: Text(
                  'Não esqueça de conferir os seus dados antes de enviar!.',
                  style: TextStyle(
                    color: Colors.grey[700],
                    fontSize: 16,
                  ),
                )),
            const SizedBox(height: 25),
            MyTextField(
              controller: usernameController,
              hintText: 'Usuário',
              obscureText: false,
            ),
            const SizedBox(height: 10),
            MyTextField(
              controller: passwordController,
              hintText: 'Senha',
              obscureText: true,
            ),
            const SizedBox(height: 10),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 25.0),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.end,
                children: [
                  Text('Esqueceu a senha?',
                      style: TextStyle(color: Colors.grey[600])),
                ],
              ),
            ),
            const SizedBox(height: 25),
            MyButton(onTap: () => signUserUp(context, usernameController.text, passwordController.text), buttonText: 'Cadastre-se'),
            const SizedBox(height: 50),
          ]),
        )));
  }
}
