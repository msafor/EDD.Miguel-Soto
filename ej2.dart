import 'dart:io';
import 'dart:math';

void main() {
  List<int> lista1 = [14, 2, 5, 3, 9];
  
  List<int> lista2 = [];
  for (int i = 0; i < 5; i++) {
    stdout.write('Ingrese un número entero para la segunda lista: ');
    int entero = int.parse(stdin.readLineSync()!);
    lista2.add(entero);
  }
  List<int> lista3 = [];
  Random listarandom = Random();
  for (int i = 0; i < 5; i++) {
    int numeroAleatorio = listarandom.nextInt(11) - 25;
    lista3.add(numeroAleatorio);
  }
  List<int> resultadofinal = [];
  for (int i = 0; i < 5; i++) {
    resultadofinal.add(lista1[i] - lista2[i] + lista3[i]);
  }
  resultadofinal.insert(0, 17);
  resultadofinal.insert(1, 24);
  resultadofinal.sort((a, b) => b.compareTo(a));
  print('El resultado obtenido es: $resultadofinal');
}


