import 'package:flutter/material.dart';
import 'package:flutter_application_1/widgets/button.dart';
import 'package:flutter_application_1/widgets/square_tile.dart';
import 'package:flutter_application_1/widgets/text_field.dart';

class LoginPage extends StatelessWidget {
  LoginPage({super.key});
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  void signUserIn(){

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        backgroundColor: Colors.grey[300],
        body: SafeArea(
          child:Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                const SizedBox(height: 50),
                const Icon(
                  Icons.lock,
                  size: 100,
                ),
                const SizedBox(height: 50),

                Text(
                  'Bem vindo de volta! Estava a sua espera.',
                  style: TextStyle(
                    color: Colors.grey[700],
                    fontSize: 16,
                    ),
                ),
                const SizedBox(height: 25),
                MyTextField(
                  controller : usernameController,
                  hintText: 'Usuário',
                  obscureText: false,

                ),

                const SizedBox(height: 10),

                MyTextField(
                  controller : passwordController,
                  hintText: 'Senha',
                  obscureText: true,
                ),
                const SizedBox(height: 10),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal:25.0),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      Text('Esqueceu a senha?',
                      style: TextStyle(color: Colors.grey[600])),
                    ],
                  ),
                ),
                const SizedBox(height: 25),

                MyButton(
                  onTap: signUserIn
                  ),

                  const SizedBox(height: 50),

                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 25.0),
                    child: Row(
                      children: [
                        Expanded(
                          child: Divider(
                            thickness: 0.5,
                            color: Colors.grey[400],
                          ),
                        ),
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 10.0),
                          child: Text(
                            'Ou faça login pelo google', 
                            style: TextStyle(color: Colors.grey[700]),
                          ),
                        ),
                        Expanded(
                          child: Divider(
                            thickness: 0.5,
                            color: Colors.grey[400],
                          ),
                        )
                      ],
                      ),
                  ),
                    const SizedBox(height: 50),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children:[
                     SquareTile(imagePath: 'lib/images/googleLogo.png'),
                    ]
                  ),
                  const SizedBox(height: 50),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text('Não tem uma conta?', 
                      style: TextStyle(
                        color: Colors.grey[700],
                      ),
                      ),

                      const SizedBox(width: 4),

                      Text('Registre aqui!', 
                      style: TextStyle(
                        color: Colors.blue,
                        fontWeight: FontWeight.bold
                        
                      ),
                      )
                    ],
                  )
                ]),
          )
        )
      );
  }
}